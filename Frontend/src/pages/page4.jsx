import React from "react";
import Footer from "../components/Footer";
import Navbar from "../components/Header";
import "../components/style.css";
import { NavLink } from "react-router-dom";

const page4 = () => {
    return (<>
        <div className="main-content">
            <Navbar />
            <br/>
                <div className="set1" style={{ marginLeft: '550px' }}>
                    <button id="btninputdetails"  className='btn4 bg2 px-5' type="submit">
                        Input Vessel Details
                    </button>
                    <NavLink to="/#" className='btn4r bg2'>Register</NavLink>
                    <br /><br />
                    
                    
                    
                </div>
                <hr />
           
            <Footer />
            </div>
        </>);
    };
    
    export default page4;
    