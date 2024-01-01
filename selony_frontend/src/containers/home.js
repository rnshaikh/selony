import React from 'react';
import Header from '../components/Header';
import Banner from '../components/Banner';
import Product from '../components/Product';
import Footer from '../components/Footer';
import FooterBanner from '../components/FooterBanner';


const Home = ()=>{

    return (

        <div>
            <Header/>
            <div className="main-container">
                <Banner></Banner>
                <div className="products-heading">
                    <h2>Best Seller Products</h2>
                    <p>speaker There are many variations passages</p>
                </div>
                <div className="products-container">
                    <Product></Product>
                    <Product></Product>
                    <Product></Product>
                </div>
                <FooterBanner></FooterBanner>
                <div className="footer-container">
                    <Footer></Footer>
                </div>
            </div>
        </div>
    )

}

export default Home;