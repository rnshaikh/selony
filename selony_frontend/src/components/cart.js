import React from "react";

import {Link} from 'react-router-dom';
import { AiOutlineShopping, AiOutlineLeft, AiOutlineMinus, AiOutlinePlus} from 'react-icons/ai';
import { TiDeleteOutline } from 'react-icons/ti';



const Cart = () =>{

    return(

        <div class="cart-wrapper">
            <div class="cart-container">
                <button
                type="button"
                class="cart-heading">
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
                        class="btn"
                    >
                        Continue Shopping
                    </button>
                    </Link>
                </div>
            <div class="product-container">
                <div class="product" key="">
                <img src="" class="cart-product-image" />
                <div class="item-desc">
                    <div className="flex top">
                    <h5>HeadPhone</h5>
                    <h4>11000</h4>
                    </div>
                    <div class="flex bottom">
                    <div>
                    <p class="quantity-desc">
                        <span class="minus">
                        <AiOutlineMinus />
                        </span>
                        <span class="num">10</span>
                        <span class="plus"><AiOutlinePlus /></span>
                    </p>
                    </div>
                    <button
                        type="button"
                        class="remove-item"
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