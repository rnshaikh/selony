import React from 'react';

import {Link} from 'react-router-dom';

import Header from '../components/header';

import Banner from '../components/banner';
import Product from '../components/product';
import Footer from '../components/footer';



const Home = ()=>{

    return (

        <div>
            <Header/>
            <Banner></Banner>
            <div class="products-heading">
                <h2>Best Seller Products</h2>
                <p>speaker There are many variations passages</p>
            </div>
            <div class="products-container">
                <Product></Product>
                <Product></Product>
                <Product></Product>
            </div>
            <div class="footer-banner-container">
                <div class="banner-desc">
                    <div class="left">
                    <p>20% OFF</p>
                    <h3>FINE</h3>
                    <h3>SMILE</h3>
                    <p>15 nov to 7 dec</p>
                    </div>
                    <div class="right">
                    <p>beats Solo Air</p>
                    <h3>Summer Sale</h3>
                    <p>company that grow from 240 t0 999 emplyoees in last 12 month</p>
                    <Link href="">
                        <button type="button">Shop Now</button>
                    </Link>
                    </div>

                    <img 
                    src="" class="footer-banner-image"
                    />
                </div>
            </div>
            <Footer></Footer>
        </div>
    )

}

export default Home;