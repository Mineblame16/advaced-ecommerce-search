# Advanced E-commerce Search

## Description

Advanced E-commerce Search is a powerful web application designed to enhance the search functionality of e-commerce platforms. This tool leverages advanced features like translation, query correction, synonym expansion, and anti-spamming measures to provide a more robust and user-friendly search experience.

## Features

- **Translation:** Automatically detects and translates non-English search queries into English.
- **Correction:** Corrects spelling and grammatical errors in search queries.
- **Synonyms:** Expands search queries with synonyms from custom lists and WordNet.
- **Pagination:** Supports pagination to efficiently manage large sets of search results.
- **Anti-Spamming:** Implements measures to temporarily ban users who exceed request limits, preventing abuse.

## Example Backends

The tool is designed to integrate seamlessly with various backend systems. Below are examples of how you can set it up with different backends:

- **PHP:** Integrate with PHP-based e-commerce systems by connecting to the appropriate APIs and endpoints.
- **Node.js:** Use with Node.js servers by sending HTTP requests to the search tool.

## Installation

### Prerequisites

Ensure you have the following installed:

- [Python 3+](https://www.python.org/downloads/)
- [Flask](https://flask.palletsprojects.com/)
- [MySQL](https://www.mysql.com/) or any other database you are using
- [Node.js](https://nodejs.org/) or PHP (if integrating with a backend)

### Setup

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Mineblame16/advanced-ecommerce-search.git
   cd advanced-ecommerce-search
   ```
2. **Install the required Python packages**:

    ```
    python -m pip install -r requirements.txt
    ```
3. **Setup Your Database**:

    A complete SQL script to setup the db is on `examples/db.sql`

4. **Setup an API** :

    Recommendation for Node.js: For a straightforward and efficient setup, we highly recommend using Node.js as your backend for this tool. Node.js offers a simple and flexible environment for building APIs, with a rich ecosystem of packages and robust performance for handling high traffic. Its asynchronous nature makes it well-suited for managing multiple search requests concurrently, ensuring smooth operation of the Advanced E-commerce Search tool.

    1. Setup Node.js API:

    Navigate to the `examples/nodejs/` directory. It contains a complete example of how to set up the API using Node.js.

    ```bash
    cd examples/nodejs
    ```

    2. Setup PHP API:

   Navigate to the `examples/php/` directory. It contains a complete example of how to set up the API using Node.js.

   ```bash
   cd examples/nodejs
   ```
    
## That's it 🎉

Now you can run the search app without any errors. Enjoy your enhanced search functionality and have a great time exploring the features!

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For any questions or support, please contact abderrahmaneouadi2012@gmail.com.