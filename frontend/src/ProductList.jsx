// ProductList.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';


const ProductList = () => {
  const [products, setProducts] = useState([]);

 
  useEffect(() => {

    fetchData();

  }, []);


  const fetchData = async () => {
    const result = await axios.get('http://127.0.0.1:8000/products/');
    setProducts(result.data);

  }

  return (
    <div>
      <h1>Products</h1>
      <ul>
        {products.map((product) => (
          <li key={product.id}>
            <a href={`/product/${product.id}`}>{product.name}</a>
            <p>{product.body}</p>
            <img src={ product.image } alt="" />
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ProductList;