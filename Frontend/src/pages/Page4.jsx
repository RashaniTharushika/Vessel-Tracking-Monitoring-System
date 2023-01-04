import React, {useState, useEffect, useContext} from 'react'
import Footer from "../components/Footer";
import Navbar from "../components/Header";
import "../components/style.css";
import {Link, NavLink} from "react-router-dom";
import axios from "axios";

const Page4 = () => {

    const plant = localStorage.getItem('plant')
    const [getVesselData, setVesselData] = useState([])
    const getData = async (e) => {
        await axios.post('http://localhost:5000/view', {
            plant
        }).then(res => {
            if (res.data.status === "Success") {
                setVesselData(res.data.data)
            } else {
                alert("Failed")
            }
        });
    };

    useEffect(() => {
        getData();
        console.log(getVesselData)
    }, [])

    return (<>
        <div className="main-content">
            <Navbar/>
            <br/>
            <div className="set1" style={{marginLeft: '550px'}}>
                <Link to="/Page3">
                    <button id="btninputdetails" className='btn4 bg2 px-5'>
                        Input Vessel Details
                    </button>
                </Link>
                <NavLink to="/#" className='btn4r bg2'>Register</NavLink>
                <br/><br/>


            </div>
            <hr/>

            <table className="table table-striped">
                <thead>
                <tr className="table-primary">
                    <th scope="col">File Updated Date by Logistic Team</th>
                    <th scope="col">Record Updated Date by Logistic Team</th>
                    <th scope="col">MBL NO</th>
                    <th scope="col">VESSEL</th>
                    <th scope="col">Carrier</th>
                    <th scope="col">POL</th>
                    <th scope="col">ETD</th>
                    <th scope="col">ETA to CMB</th>
                    <th scope="col">Need Registering Yes\/No?</th>
                    <th scope="col">Tracking Common MBL</th>
                    <th scope="col">Refered CN no</th>
                    <th scope="col">MMSI</th>
                    <th scope="col">Voyage</th>
                    <th scope="col">HBL</th>
                    <th scope="col">Shipment Type</th>
                </tr>
                </thead>
                <tbody>
                </tbody>
            </table>
<br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br>
            <Footer/>
        </div>
    </>);
};

export default Page4;
    