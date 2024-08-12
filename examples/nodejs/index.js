const express = require('express');
const path = require('path');
const mysql = require('mysql2');
const cors = require('cors'); // Import the cors package
require('dotenv').config();

// Create a connection pool for MySQL
const pool = mysql.createPool({
  host: process.env.DB_HOST,
  user: process.env.DB_USER,
  password: process.env.DB_PASSWORD,
  database: process.env.DB_NAME
});
const db = pool.promise();

const app = express();
const port = 3000;

// Middleware to parse JSON bodies
app.use(express.json());

// Middleware to handle CORS
app.use(cors({
  origin: 'http://localhost:5173', // Update this to your frontend's origin
  credentials: true
}));

// Helper function to filter out null image fields
const filterImages = (product) => {
  const images = ['image1', 'image2', 'image3', 'image4', 'image5'];
  images.forEach((image) => {
    if (!product[image]) {
      delete product[image];
    }
  });
  return product;
};

// Routes

// Get all products with category and subcategory names
app.get('/api/products', async (req, res) => {
  try {
    const [rows] = await db.query(`
      SELECT p.*, c.name as category_name, s.name as subcategory_name 
      FROM products p
      LEFT JOIN categories c ON p.category_id = c.id
      LEFT JOIN subcategories s ON p.subcategory_id = s.id
    `);
    const filteredRows = rows.map(filterImages);
    res.json(filteredRows);
  } catch (err) {
    console.error(err);
    res.status(500).send('Server error');
  }
});

// Get all categories
app.get('/api/categories', async (req, res) => {
  try {
    const [categories] = await db.query('SELECT * FROM categories');
    res.json(categories);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// Get all subcategories
app.get('/api/subcategories', async (req, res) => {
  try {
    const [subcategories] = await db.query('SELECT * FROM subcategories');
    res.json(subcategories);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});
