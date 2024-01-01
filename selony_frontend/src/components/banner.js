import React from "react";
import { Link } from "react-router-dom";

import bannerLogo from '../assets/headphones_a_1.webp';

const Banner = ()=>{

    return(

        <div className="hero-banner-container">
            <div>
                <p className="beats-solo">Beats Solo Wireless</p>
                <h3>Wireless</h3>
                <h1>Headphones</h1>
                <img src={bannerLogo} alt="headphones" className="hero-banner-image" />

                <div>
                <div className="desc">
                    <h5>Description</h5>
                    <p>Headphones are a pair of small loudspeaker drivers worn on or around the head over a user's ears. They are electroacoustic transducers, which convert an electrical signal to a corresponding sound</p>
                </div>
                </div>
                <Link href="">
                    <button type="button">Shop Wireless Headphone</button>
                </Link>
            </div>
        </div>
    )

}

export default Banner;
