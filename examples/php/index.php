<?php

// Database connection configuration
$host = 'localhost';
$dbname = '';
$username = 'root';
$password = '';

try {
    $pdo = new PDO("mysql:host=$host;dbname=$dbname;charset=utf8", $username, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    http_response_code(500);
    echo json_encode(['error' => 'Database connection failed: ' . $e->getMessage()]);
    exit;
}

// Set headers for JSON response
header('Content-Type: application/json');

// Route handling with query parameter
$query = isset($_GET['api']) ? $_GET['api'] : '';

switch ($query) {
    case 'products':
        handleProducts($pdo);
        break;
    case 'categories':
        handleCategories($pdo);
        break;
    case 'subcategories':
        handleSubcategories($pdo);
        break;
    default:
        http_response_code(400);
        echo json_encode(['error' => 'Invalid API endpoint']);
        break;
}

// Function to handle products
function handleProducts($pdo) {
    try {
        $stmt = $pdo->query('SELECT p.*, c.name AS category_name, s.name AS subcategory_name 
                             FROM products p
                             LEFT JOIN categories c ON p.category_id = c.id
                             LEFT JOIN subcategories s ON p.subcategory_id = s.id');
        $products = $stmt->fetchAll(PDO::FETCH_ASSOC);
        
        // Filter out null image fields and ensure valid URLs
        $products = array_map(function($product) {
            $images = ['image1', 'image2', 'image3', 'image4', 'image5'];
            foreach ($images as $image) {
                if (empty($product[$image])) {
                    unset($product[$image]);
                } else {
                    // Normalize the URL
                    $product[$image] = normalizeUrl($product[$image]);
                }
            }
            return $product;
        }, $products);
        
        echo json_encode($products, JSON_UNESCAPED_SLASHES);
    } catch (PDOException $e) {
        http_response_code(500);
        echo json_encode(['error' => $e->getMessage()]);
    }
}

// Function to handle categories
function handleCategories($pdo) {
    try {
        $stmt = $pdo->query('SELECT * FROM categories');
        $categories = $stmt->fetchAll(PDO::FETCH_ASSOC);
        echo json_encode($categories, JSON_UNESCAPED_SLASHES);
    } catch (PDOException $e) {
        http_response_code(500);
        echo json_encode(['error' => $e->getMessage()]);
    }
}

// Function to handle subcategories
function handleSubcategories($pdo) {
    try {
        $stmt = $pdo->query('SELECT * FROM subcategories');
        $subcategories = $stmt->fetchAll(PDO::FETCH_ASSOC);
        echo json_encode($subcategories, JSON_UNESCAPED_SLASHES);
    } catch (PDOException $e) {
        http_response_code(500);
        echo json_encode(['error' => $e->getMessage()]);
    }
}

// Function to normalize URL
function normalizeUrl($url) {
    // Remove potential extra slashes or spaces
    $url = trim($url);
    $url = preg_replace('#/+#', '/', $url);

    // Optionally, you can add additional URL validation here

    return $url;
}
