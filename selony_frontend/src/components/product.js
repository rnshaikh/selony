import React from "react";

import { Link } from 'react-router-dom';


const Product = ()=>{


    return (
        <div>
          <Link href={`/product/`}>
            <div className="product-card">
              <img 
                src=""
                width={250}
                height={250}
                className="product-image"
              />
              <p className="product-name">headphones</p>
              <p className="product-price">100</p>
            </div>
          </Link>
        </div>
      )

}

export default Product;