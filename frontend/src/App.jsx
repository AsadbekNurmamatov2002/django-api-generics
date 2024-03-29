// App.js
import React from 'react';
import ProductList from './ProductList';
import ProductDetail from './ProductDetail';
// import { BrowserRouter as Router, Route, Link } from 'react-router-dom';

function App() {
  return (
    // <Router>
      <div>
        <nav>
          {/* <ProductDetail /> */}
          <ProductList />
          {/* <Link to="/">Products</Link> */}
        </nav>
        {/* <Route path="/" exact component={ProductList} /> */}
        {/* <Route path="/product/:id" component={ProductDetail} /> */}
      </div>
    // </Router>
  );
}

export default App;