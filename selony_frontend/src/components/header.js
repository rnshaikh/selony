import React from 'react';
import { Link } from 'react-router-dom';
import { AiOutlineShopping } from 'react-icons/ai';


const Header = ()=>{


    return (

        <header>
        <div class="navbar-container">
            <p class="logo">
                <Link href="/">Selony</Link>
            </p>

            <button type="button" class="cart-icon">
                <AiOutlineShopping />
                <span clas="cart-item-qty">10</span>
            </button>
        </div>
        </header>
    )
}


export default Header;

