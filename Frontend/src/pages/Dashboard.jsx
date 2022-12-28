import React from "react";
import "../App.css";
import { useHistory } from "react-router-dom";
import Footer from "../components/Footer";
import Navbar from "../components/Header";
import axios from "axios";

const Dashboard = () => {
    const history = useHistory();
    const [logout, setLogout] = React.useState(false);

    React.useEffect(() => {
        if (!localStorage.getItem("auth")) history.push("/login");
    }, [logout]);

    const logoutHandler = (e) => {
        e.preventDefault();
        localStorage.removeItem("auth");
        setLogout(true);
    };

    // TODO: Create modal instead of alert boxes for showing values
    const balanceHandler = (e) => {
        axios.get('http://localhost:5000/balance').then(res => {
            if (res.data.status === "Success") {
                alert("Credit balance is " + res.data.balance)
            } else {
                alert("Failed, Please check error log")
            }
        });
    };

    // TODO: Need to modify code
    const registerHandler = (e) => {
        axios.get('http://localhost:5000/register').then(res => {
            if (res.data.status === "Success") {
                alert(res.data.no_of_regs + " new vessels have been registered ! \n" + res.data.cost + " credits reduced")
            } else {
                alert("Failed")
            }
        });
    };

    // TODO: Need to modify code
    const vfcHandler = (e) => {
        axios.get('http://localhost:5000/vfc').then(res => {
            if (res.data.status === "Success") {
                alert("Number of vessels tracked : " + res.data.tracked)
            } else {
                alert("Failed, Please check error log")
            }
        });
    };

    // TODO: Need to modify code
    const svpHandler = (e) => {
        axios.get('http://localhost:5000/svp').then(res => {
            if (res.data.status === "Success") {
                alert("Number of vessels tracked before MBL generated : " + res.data.vessel_position + "\n" + res.data.cost + " credits reduced")
            } else {
                alert("Failed, Please check error log")
            }
        });
    };

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
                <br /><br />
                <button id="btnRegister" onClick={registerHandler} className='btn bg2' type="submit">
                    Vessel Registration
                </button>
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
