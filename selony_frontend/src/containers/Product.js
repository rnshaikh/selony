import React from "react";

import ProductDetail from "../components/ProductDetail";
import Footer from "../components/Footer";
import Header from "../components/Header";


const Product = ()=>{

    return (
        <div className="main-container">
            <Header></Header>
            <ProductDetail></ProductDetail>
            <Footer></Footer>
        </div>
    )

}

export default Product;
