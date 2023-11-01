import React, { useState } from 'react';
import '../index.css';

const Header = () => {
    return (
    <div className="header">
        <div className="header-img-container">
            <img className="header-image" src="/header_image.PNG" alt="App Logo" />
        </div>

        <div className="header-title-nav-container">
            <div className="header-title">
                <h2 >ModL</h2>
            </div>
            <div className="header-nav-list">
                <nav>
                    <ul >
                        <li><a href="/">Home</a></li>
                        <li><a href="/about">About</a></li>
                        <li><a href="/contact">Contact</a></li>
                    </ul>
                </nav>
            </div>

        </div>


    </div>
);

};

export default Header;