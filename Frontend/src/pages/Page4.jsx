import React, {useState, useEffect, useContext} from 'react'
import Footer from "../components/Footer";
import Navbar from "../components/Header";
import "../components/style.css";
import {Link, NavLink} from "react-router-dom";
import axios from "axios";


const Page4 = () => {

    const plant = localStorage.getItem('plant')
    const [getVesselData, setVesselData] = useState([{}])
    const getData = async (e) => {
        await axios.post('http://localhost:5000/view', {
            plant
        }).then(res => {
            if (res.data.status === "Success") {
                setVesselData(JSON.parse(res.data.data.replace(/\bNaN\b/g, "null")))
            } else {
                alert("Failed")
                console.log(res)
            }
        });
    };

    useEffect(() => {
        getData();
        console.log(getVesselData)
    }, [])

    //Delete part


    // TODO: Need to modify code
    const registerHandler = (e) => {
        axios.post('http://localhost:5000/register', {
            plant
        }).then(res => {
            if (res.data.status === "Success") {
                alert(res.data.no_of_regs + " new vessels have been registered ! \n" + res.data.cost + " credits reduced")
            } else {
                alert("Failed")
            }
        });
    };

    // const deleteHandler = (event, param) => {
    //
    //     axios.post('http://localhost:5000/delete', {
    //         plant,
    //         HBL: param
    //     }).then(res => {
    //         if (res.data.status === "Success") {
    //             alert("Vessel detail removed")
    //             window.location.reload()
    //         } else {
    //             alert("Failed")
    //         }
    //     });
    // };

    console.log(getVesselData)
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
                {/*<NavLink to="/#" className='btn4r bg2'>Register</NavLink>*/}
                <button id="btnRegister" onClick={registerHandler} className='btn4r bg2' type="submit">
                    Register
                </button>
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
                    <th scope="col">Need Registering Yes/No?</th>
                    <th scope="col">Tracking Common MBL</th>
                    <th scope="col">Refered CN no</th>
                    <th scope="col">MMSI</th>
                    <th scope="col">Voyage</th>
                    <th scope="col">HBL</th>
                    <th scope="col">Shipment Type</th>
                    {/*<th scope="col">Action</th>*/}
                </tr>
                </thead>
                <tbody>
                {
                    getVesselData.map((element, id) => (

                            <>
                                <tr class="table-light">
                                    {/*<th scope='row'>{id + 1}</th>*/}
                                    <td>{element['File Updated Date by Logistic Team']}</td>
                                    <td>{element['Record Updated Date by Logistic Team']}</td>
                                    <td>{element['MBL NO']}</td>
                                    <td>{element.VESSEL}</td>
                                    <td>{element.Carrier}</td>
                                    <td>{element.POL}</td>
                                    <td>{element['ETD ']}</td>
                                    <td>{element['ETA to CMB']}</td>
                                    <td>{element['Need Registering Yes/No?']}</td>
                                    <td>{element['Tracking Common MBL ']}</td>
                                    <td>{element['Refered CN no']}</td>
                                    <td>{element.MMSI}</td>
                                    <td>{element.Voyage}</td>
                                    <td>{element.HBL}</td>
                                    <td>{element['Shipment Type']}</td>
                                    {/*<td><button onClick={event => deleteHandler(event, element.HBL)}>Delete</button></td>*/}
                                    <td className="d-flex justify-content-between">

                                    </td>
                                </tr>
                            </>
                        )
                    )
                }
                </tbody>
            </table>
            <br/>
            <Footer/>
        </div>
    </>);
};

export default Page4;
