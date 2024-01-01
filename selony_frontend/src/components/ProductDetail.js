import React, { Fragment } from "react";

import { Link } from "react-router-dom";
import { AiFillStar, AiOutlineStar, AiOutlineMinus, AiOutlinePlus } from "react-icons/ai";


const ProductDetail = ()=>{


    return (
        <Fragment>
            <div className="product-detail-container">
            <div>
            <div className="image-container">
                <img src="" className="product-detail-image" />
            </div>
            <div className="small-images-container">
                <img 
                    key=""
                    src=""
                    className='small-image selected-image'
                    onMouseEnter=""
                />
            </div>
            </div>

            <div className="product-detail-desc">
            <h1>Boat Immortal 1000D</h1>
            <div className="reviews">
                <div>
                <AiFillStar />
                <AiFillStar />
                <AiFillStar />
                <AiFillStar />
                <AiOutlineStar />
                </div>
                <p>
                (20)
                </p>
            </div>
            <h4>Details: </h4>
            <p>Headphones are a pair of small loudspeaker drivers worn on or around the head over a user's ears. They are electroacoustic transducers, which convert an electrical signal to a corresponding sound.</p>
            <p className="price">$50</p>
            <div className="quantity">
                <h3>Quantity:</h3>
                <p className="quantity-desc">
                <span className="minus" onClick=""><AiOutlineMinus /></span>
                <span className="num">1</span>
                <span className="plus" onClick=""><AiOutlinePlus /></span>
                </p>
            </div>
            <div className="buttons">
                <button type="button" className="add-to-cart" onClick="">Add to Cart</button>
                <button type="button" className="buy-now" onClick="">Buy Now</button>
            </div>
            </div>
            </div>
            <div class="maylike-products-wrapper">
                <h2>You may also like</h2>
                <div className="marquee">
                    <div className="maylike-products-container track">       
                    <div>
                        <Link href="">
                            <div className="product-card">
                            <img 
                                src=""
                                width={250}
                                height={250}
                                className="product-image"
                            />
                            <p className="product-name">boat party pal 50</p>
                            <p className="product-price">$36</p>
                            </div>
                        </Link>
                    </div>
                    <div>
                        <Link href="">
                            <div className="product-card">
                            <img 
                                src=""
                                width={250}
                                height={250}
                                className="product-image"
                            />
                            <p className="product-name">boat party pal 50</p>
                            <p className="product-price">$36</p>
                            </div>
                        </Link>
                    </div>
                    </div>
                </div>
            </div>
        </Fragment>

    )


}

export default ProductDetail;