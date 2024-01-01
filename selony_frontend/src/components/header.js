import React from 'react';
import { Link } from 'react-router-dom';
import { AiOutlineShopping } from 'react-icons/ai';


const Header = ()=>{


    return (

        <header>
        <div className="navbar-container">
            <p className="logo">
                <Link href="/">Selony</Link>
            </p>

            <button type="button" className="cart-icon">
                <AiOutlineShopping />
                <span className="cart-item-qty">10</span>
            </button>
        </div>
        </header>
    )
}


export default Header;

