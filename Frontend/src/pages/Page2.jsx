import React from "react";
import "../App.css";

const Page2 = () => {

  return (
    <>
    <h3 className="topic" style={{marginLeft:'500px' , marginTop: '100px'}}>Vessel Tracking & Monitoring Platform</h3><br/><br/>
    <div className="set" style={{marginLeft: '550px'}}>
                <button className='btn bg2' type="submit">
                    Shipment Tracking
                </button><br /><br/>
                <button className='btn bg2' type="submit">
                    Credit Balance
                </button><br/>
            </div>    
	  <hr/>
      
    </>
  );
};

export default Page2;
