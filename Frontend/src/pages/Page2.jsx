import React from "react";
import "../App.css";

const Page2 = () => {

  return (
    <>
    <h3 className="topic" style={{marginLeft:'500px' , marginTop: '100px'}}>Vessel Tracking & Monitoring Platform</h3><br/><br/>
    <div className="set" style={{marginLeft: '550px'}}>
              <form action="http://127.0.0.1:5000/vfc" method="get">
                <button className='btn bg2' type="submit">
                    Shipment Tracking
                </button>
                </form>
                <br /><br/>
                <form action="http://127.0.0.1:5000/balance" method="get">
                <button className='btn bg2' type="submit">
                    Credit Balance
                </button></form><br/>
            </div>    

      
    </>
  );
};

export default Page2;
