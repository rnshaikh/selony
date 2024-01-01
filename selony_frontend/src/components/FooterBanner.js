import React from "react";
import { Link } from "react-router-dom";

const FooterBanner = () =>{

    return (

        <div className="footer-banner-container">
            <div className="banner-desc">
                <div className="left">
                <p>20% OFF</p>
                <h3>FINE</h3>
                <h3>SMILE</h3>
                <p>15 nov to 7 dec</p>
                </div>
                <div className="right">
                <p>beats Solo Air</p>
                <h3>Summer Sale</h3>
                <p>company that grow from 240 t0 999 emplyoees in last 12 month</p>
                <Link href="">
                    <button type="button">Shop Now</button>
                </Link>
                </div>

                <img 
                src="" className="footer-banner-image"
                />
            </div>
        </div>
    )

}

export default FooterBanner;