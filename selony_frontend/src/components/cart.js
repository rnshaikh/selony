import React from "react";

import {Link} from 'react-router-dom';
import { AiOutlineShopping, AiOutlineLeft, AiOutlineMinus, AiOutlinePlus} from 'react-icons/ai';
import { TiDeleteOutline } from 'react-icons/ti';



const Cart = () =>{

    return(

        <div className="cart-wrapper">
            <div className="cart-container">
                <button
                type="button"
                className="cart-heading">
                <AiOutlineLeft />
                <span class="heading">Your Cart</span>
                <span class="cart-num-items">(10 items)</span>
                </button>
                <div className="empty-cart">
                    <AiOutlineShopping size={150} />
                    <h3>Your shopping bag is empty</h3>
                    <Link href="/">
                    <button
                        type="button"
                        className="btn"
                    >
                        Continue Shopping
                    </button>
                    </Link>
                </div>
            <div className="product-container">
                <div className="product" key="">
                <img src="" className="cart-product-image" />
                <div className="item-desc">
                    <div className="flex top">
                    <h5>HeadPhone</h5>
                    <h4>11000</h4>
                    </div>
                    <div className="flex bottom">
                    <div>
                    <p className="quantity-desc">
                        <span class="minus">
                        <AiOutlineMinus />
                        </span>
                        <span className="num">10</span>
                        <span className="plus"><AiOutlinePlus /></span>
                    </p>
                    </div>
                    <button
                        type="button"
                        className="remove-item"
                    >
                        <TiDeleteOutline />
                    </button>
                    </div>
                </div>
                </div>
            </div>
        <div class="cart-bottom">
            <div class="total">
            <h3>Subtotal:</h3>
            <h3>11000</h3>
            </div>
            <div class="btn-container">
            <button type="button" class="btn">
                Pay with Stripe
            </button>
            </div>
        </div>
    </div>
        </div>
    )


}

export default Cart;