from flask import Flask, request, jsonify
import requests
from nltk.corpus import wordnet
from langdetect import detect
from deep_translator import GoogleTranslator
from textblob import TextBlob
import time

app = Flask(__name__)

# Custom synonyms dictionary
custom_synonyms = {
    "phone": ["telephone", "mobile", "cellphone"],
    "laptop": ["notebook", "macbook", "computer"],
    "camera": ["photocamera", "dslr", "mirrorless"],
    "book": ["novel", "volume", "publication"],
    "dress": ["gown", "attire", "garment"]
}

# Global variables for rate limiting and banning
rate_limit = 5  # Max requests per second
ban_duration = 10  # Ban duration in seconds
banned_ips = {}  # {ip: (ban_end_time, attempts)}
ip_attempts = {}  # {ip: attempts_count}

def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {'error': f'Unable to fetch data from {url}'}

def fetch_all_data():
    products_url = 'http://localhost:3000/api/products'
    categories_url = 'http://localhost:3000/api/categories'
    subcategories_url = 'http://localhost:3000/api/subcategories'
    
    products = fetch_data(products_url)
    categories = fetch_data(categories_url)
    subcategories = fetch_data(subcategories_url)
    
    return products, categories, subcategories

def get_wordnet_synonyms(word):
    synonyms = set()
    for synset in wordnet.synsets(word):
        for lemma in synset.lemmas():
            synonyms.add(lemma.name().lower().replace('_', ' '))
    return list(synonyms)

def detect_and_translate(query):
    detected_language = detect(query)
    if detected_language != 'en':
        translation = GoogleTranslator(source=detected_language, target='en').translate(query)
        return translation
    return query

def correct_query(query):
    corrected_query = str(TextBlob(query).correct())
    return corrected_query

def generate_search_terms(query):
    search_terms = set([query.lower()])

    if query.lower() in custom_synonyms:
        search_terms.update(custom_synonyms[query.lower()])

    search_terms.update(get_wordnet_synonyms(query.lower()))

    if query.lower().endswith('s'):
        search_terms.add(query.lower()[:-1])
    else:
        search_terms.add(query.lower() + 's')
        search_terms.add(query.lower() + 'yet')

    return list(search_terms)

def search_products(products, queries):
    results = []
    seen_product_ids = set()  # To keep track of added product IDs
    
    for query in queries:
        search_terms = generate_search_terms(query)
        for product in products:
            if product['id'] in seen_product_ids:
                continue  # Skip the product if it's already been added
            
            title = product.get('title', '').lower()
            description = product.get('description', '').lower()
            category_name = product.get('category_name', '').lower()
            subcategory_name = product.get('subcategory_name', '').lower()
            
            if any(
                term in title or 
                term in description or 
                term in category_name or 
                term in subcategory_name
                for term in search_terms
            ):
                results.append(product)
                seen_product_ids.add(product['id'])  # Mark this product as added
    
    return results

def is_banned(ip):
    if ip in banned_ips:
        ban_end_time, _ = banned_ips[ip]
        if time.time() < ban_end_time:
            return True
        else:
            del banned_ips[ip]
    return False

def handle_request(ip):
    current_time = time.time()
    if ip not in ip_attempts:
        ip_attempts[ip] = []

    ip_attempts[ip] = [timestamp for timestamp in ip_attempts[ip] if current_time - timestamp < 1]
    
    if len(ip_attempts[ip]) >= rate_limit:
        banned_ips[ip] = (current_time + ban_duration, len(ip_attempts[ip]))
        ip_attempts[ip] = []  # Clear attempts
        log_ban(ip, ban_duration)  # Log the ban
        return True  # Banned
    else:
        ip_attempts[ip].append(current_time)
        return False  # Not banned

def log_ban(ip, duration):
    with open('./ban.log', 'a') as f:
        ban_end_time = time.time() + duration
        f.write(f'{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())} - Banned IP: {ip}, Ban End Time: {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ban_end_time))}\n')

@app.route('/search', methods=['GET'])
def search():
    ip = request.remote_addr
    if is_banned(ip):
        return jsonify({"error": "Banned from service for 10 seconds"}), 429
    
    if handle_request(ip):
        return jsonify({"error": "Banned from service for 10 seconds"}), 429
    
    query = request.args.get('q')
    page = int(request.args.get('page', 1))
    
    if not query:
        return jsonify({"error": "Query parameter 'q' is required"}), 400
    
    products, categories, subcategories = fetch_all_data()
    
    if 'error' in products:
        return jsonify({"error": products['error']}), 500
    
    # Pagination
    page_size = 10
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    
    if start_index >= len(products):
        return jsonify({"error": "No results found"}), 404
    
    paginated_products = products[start_index:end_index]
    
    translated_query = detect_and_translate(query)
    corrected_translated_query = correct_query(translated_query)
    
    search_terms = [query, translated_query, corrected_translated_query]
    search_results = search_products(paginated_products, search_terms)
    
    return jsonify(search_results)

if __name__ == "__main__":
    app.run(debug=True)
