import React from "react";
import "../App.css";
import { useHistory } from "react-router-dom";
import Footer from "../components/Footer";
import Navbar from "../components/Header";
import axios from "axios";
import { NavLink } from "react-router-dom";

const Dashboard = () => {
    const history = useHistory();
    const [logout, setLogout] = React.useState(false);
    const plant = localStorage.getItem('plant')

    console.log(plant)

    React.useEffect(() => {
        if (!localStorage.getItem("auth")) history.push("/login");
    }, [logout]);

    const logoutHandler = (e) => {
        e.preventDefault();
        localStorage.removeItem("auth");
        localStorage.removeItem("plant");
        setLogout(true);
    };

    // TODO: Create modal instead of alert boxes for showing values
    const balanceHandler = (e) => {
        axios.post('http://localhost:5000/balance', {
            plant
        }).then(res => {
            if (res.data.status === "Success") {
                alert("Credit balance is " + res.data.balance)
            } else {
                alert("Failed, Please check error log")
            }
        });
    };

    // // TODO: Need to modify code
    // const registerHandler = (e) => {
    //     axios.post('http://localhost:5000/register', {
    //         plant
    //     }).then(res => {
    //         if (res.data.status === "Success") {
    //             alert(res.data.no_of_regs + " new vessels have been registered ! \n" + res.data.cost + " credits reduced")
    //         } else {
    //             alert("Failed")
    //         }
    //     });
    // };

    // TODO: Need to modify code
    const vfcHandler = (e) => {
        axios.post('http://localhost:5000/vfc', {
            plant
        }).then(res => {
            if (res.data.status === "Success") {
                alert("Number of vessels tracked : " + res.data.tracked)
            } else {
                alert("Failed, Please check error log")
            }
        });
    };

    // TODO: Need to modify code
    const svpHandler = (e) => {
        axios.post('http://localhost:5000/svp', {
            plant
        }).then(res => {
            if (res.data.status === "Success") {
                alert("Number of vessels tracked before MBL generated : " + res.data.vessel_position + "\n" + res.data.cost + " credits reduced")
            } else {
                alert("Failed, Please check error log")
            }
        });
    };

        // // TODO: Need to modify code
        // const inputHandler = (e) => {
        //     axios.get('http://localhost:5000/input').then(res => {
        //         if (res.data.status === "Success") {
        //             alert(res.data.no_of_regs + " new vessels have been entered !")
        //         } else {
        //             alert("Failed")
        //         }
        //     });
        // };

    return (<>
    <div className="main-content">
        <Navbar />
        
            <h3 className="topic" style={{ marginLeft: '500px', marginTop: '100px', color: '#eee', fontWeight:'bold' }}>Vessel Tracking & Monitoring
                Platform</h3><br /><br />
            <div className="set" style={{ marginLeft: '550px' }}>
                <button id="btnShipmentTracking" onClick={vfcHandler} className='btn bg2 px-5' type="submit">
                    Shipment Tracking
                </button>
                <br /><br />
                <button id="btnSVP" onClick={svpHandler} className='btn bg2' type="submit">
                    Single Vessel Position
                </button>
                {/* <br /><br />
                <button id="btnInput" onClick={inputHandler} className='btn bg2' type="submit">
                    Input Vessel Details
                </button> */}
                <br /><br />
                {/* <button id="btnRegister" onClick={registerHandler} className='btn bg2' type="submit">
                    Vessel Registration
                </button> */}
                <NavLink to="/page4" className='btn bg2'>Register</NavLink>
                <br /><br />
                <button id="btnBalance" onClick={balanceHandler} className='btn bg2' type="button">
                    Credit Balance
                </button>
                <br /><br />
                <button onClick={logoutHandler} className="btn btn-primary text-center">Logout</button>
            </div>
            <hr />
       
        <Footer />
        </div>
    </>);
};

export default Dashboard;
