import React from "react";
import { FaEnvelope, FaFacebook, FaInstagram, FaLocationArrow, FaPhone, FaTwitter, FaYoutube } from "react-icons/fa";
import "./style.css";

function Footer() {
  return (
    <div className="main-footer">
      <div className="container">
        <div className="left box">
          <h2>About us</h2>
          <div className="content">
            <p>MAS Holdings is a global apparel tech conglomerate providing concept-to-delivery solutions for the world’s leading apparel brands.</p>
          </div>
        </div>

        <div className="center box">
          <h2>Address</h2>
          <div className="content">
            <div className="place">
              <FaLocationArrow />
              <span className="text">199,Kaduwela Road,Battaramulla    Colombo,Sri Lanka</span>
            </div>
            <div className="email">
              <FaEnvelope />
              <span className="text">info@masholdings.com</span>
            </div>
          </div>
        </div>

        <div className="right box">
          <h2>Contact us</h2>
          <div className="content">
            <div className="phone">
              <FaPhone />
              <span className="text">  0114 796 444</span>
            </div>
            <div className="social">
              <a href="https://www.facebook.com/MASHoldingsSL"><FaFacebook  color="#3b5998" size={20}/></a>
              <a href="https://twitter.com/masholdings?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor"><FaTwitter color="#00acee" size={20}/></a>
              <a href="https://www.instagram.com/mas_holdings/"><FaInstagram color="#8a3ab9" size={20}/></a>
              <a href="https://www.youtube.com/channel/UCENNIATRP-VeRFRydvwZsXA"><FaYoutube color="#FF0000" size={20}/></a>
            </div>
          </div>
        </div>
      </div>
      <div className="bottom">
        <center>
          <span className="credit">Created By <a href="#">Rashani</a> | </span>
          <span className="far fa-copyright"></span><span> 2022 All rights reserved.</span>
        </center>
      </div>

    </div>
  );
}

export default Footer;
