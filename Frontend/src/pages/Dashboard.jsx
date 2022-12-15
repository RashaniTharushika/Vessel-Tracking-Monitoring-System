import React from "react";
import "../App.css";
import { useHistory } from "react-router-dom";
import Footer from "../components/Footer";
import Navbar from "../components/Header";

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

  return (
    <>
    <Navbar />
    <h3 className="topic" style={{marginLeft:'500px' , marginTop: '100px'}}>Vessel Tracking & Monitoring Platform</h3><br/><br/>
    <div className="set" style={{marginLeft: '550px'}}>
              <form action="http://127.0.0.1:5000/vfc" method="get">
                <button className='btn bg2' type="submit">
                    Shipment Tracking
                </button></form><br /><br/>
                <button className='btn bg2' type="submit">
                    Single Vessel Position
                </button><br /><br/>
                <button className='btn bg2' type="submit">
                    Vessel Registration
                </button><br /><br/>
                <form action="http://127.0.0.1:5000/balance" method="get">
                <button className='btn bg2' type="submit">
                    Credit Balance
                </button></form><br/><br/>
                <button onClick={logoutHandler} className="btn btn-primary text-left">Logout</button>
            </div>    
	  <hr/>
    <Footer /> 
    </>
  );
};

export default Dashboard;
