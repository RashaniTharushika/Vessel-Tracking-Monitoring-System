import React from "react";
import "../App.css";

const Page1 = () => {

  return (
    <>
    <h3 className="topic" style={{marginLeft:'500px' , marginTop: '100px'}}>Vessel Tracking & Monitoring Platform</h3><br/><br/>
    <div className="set" style={{marginLeft: '250px'}}>

    <form>
        <div class="form-group row">
            <label for="FileUpdatedDate" class="col-4 col-form-label">File Updated Date by Logistic Team</label> 
            <div class="col-8">
            <input id="FileUpdatedDate" name="FileUpdatedDate" placeholder="File Updated Date by Logistic Team" type="text" required="required" class="form-control"></input>
            </div>
        </div>
        <div class="form-group row">
            <label for="RecordUpdatedDate" class="col-4 col-form-label">Record Updated Date by Logistic Team</label> 
            <div class="col-8">
            <input id="RecordUpdatedDate" name="RecordUpdatedDate" placeholder="Record Updated Date by Logistic Team" type="text" class="form-control" required="required"></input>
            </div>
        </div>
        <div class="form-group row">
            <label for="MBL" class="col-4 col-form-label">MBL NO</label> 
            <div class="col-8">
            <input id="MBL" name="MBL" placeholder="Master Bill of Lading Number" type="text" class="form-control" required="required"></input>
            </div>
        </div>
        <div class="form-group row">
            <label for="VESSEL" class="col-4 col-form-label">Vessel Name</label> 
            <div class="col-8">
            <input id="VESSEL" name="VESSEL" placeholder="Vessel Name" type="text" class="form-control" required="required"></input>
            </div>
        </div>
        <div class="form-group row">
            <label for="Carrier" class="col-4 col-form-label">Carrier</label> 
            <div class="col-8">
            <select id="Carrier" name="Carrier" required="required" class="custom-select" aria-describedby="CarrierHelpBlock">
                <option value="notfound">Not Found</option>
                <option value="duck">OOCL</option>
                <option value="fish">ZIM</option>
                <option value="wanhai">Wan Hai</option>
                <option value="maersk">Maersk</option>
                <option value="cnc">CNC</option>
                <option value="dongjin">Dongjin</option>
                <option value="heung">Heung-A</option>
                <option value="jinjiang">Jin Jiang</option>
                <option value="interasis">Interasia</option>
                <option value="haihua">Hai Hua</option>
                <option value="sinotrans">Sinotrans</option>
                <option value="sitc">SITC</option>
                <option value="misheng">Misheng</option>
                <option value="ts">T.S.</option>
                <option value="pancontinental">Pan Continental</option>
                <option value="nirint">Nirint</option>
                <option value="acl">ACL</option>
                <option value="admiralcontainer">Admiral Container</option>
                <option value="accontainer">AC Container</option>
            </select> 
            <span id="CarrierHelpBlock" class="form-text text-muted">Select Carrier Name from the List</span>
            </div>
        </div>
        <div class="form-group row">
            <label for="pol" class="col-4 col-form-label">POL</label> 
            <div class="col-8">
            <input id="pol" name="pol" placeholder="Loading Port" type="text" class="form-control" required="required"></input>
            </div>
        </div>
        <div class="form-group row">
            <label for="etd" class="col-4 col-form-label">ETD</label> 
            <div class="col-8">
            <input id="etd" name="etd" placeholder="ETD " type="text" class="form-control" required="required"></input>
            </div>
        </div>
        <div class="form-group row">
            <label for="etaToCMB" class="col-4 col-form-label">ETA to CMB</label> 
            <div class="col-8">
            <input id="etaToCMB" name="etaToCMB" placeholder="ETA to CMB" type="text" class="form-control" required="required"></input>
            </div>
        </div>
        <div class="form-group row">
            <label for="NeedRegistering" class="col-4 col-form-label">Need Registering Yes/No?</label> 
            <div class="col-8">
            <select id="NeedRegistering" name="NeedRegistering" class="custom-select" aria-describedby="NeedRegisteringHelpBlock" required="required">
                <option value="yes">Yes</option>
                <option value="no">No</option>
            </select> 
            <span id="NeedRegisteringHelpBlock" class="form-text text-muted">Need Registering?</span>
            </div>
        </div>
        <div class="form-group row">
            <label for="TrackingCommonMBL " class="col-4 col-form-label">Tracking Common MBL</label> 
            <div class="col-8">
            <input id="TrackingCommonMBL " name="TrackingCommonMBL " placeholder="Tracking Common MBL " type="text" class="form-control" required="required"></input>
            </div>
        </div>
        <div class="form-group row">
            <label for="MMSI" class="col-4 col-form-label">MMSI</label> 
            <div class="col-8">
            <input id="MMSI" name="MMSI" placeholder="MMSI" type="text" class="form-control" required="required"></input>
            </div>
        </div>
        <div class="form-group row">
            <label for="Voyage" class="col-4 col-form-label">Voyage</label> 
            <div class="col-8">
            <input id="Voyage" name="Voyage" placeholder="Voyage No" type="text" class="form-control" required="required"></input>
            </div>
        </div>
        <div class="form-group row">
            <label for="HBL" class="col-4 col-form-label">HBL</label> 
            <div class="col-8">
            <input id="HBL" name="HBL" placeholder="HBL" type="text" class="form-control" required="required"></input>
            </div>
        </div>
        <div class="form-group row">
            <label for="ShipmentType" class="col-4 col-form-label">Shipment Type</label> 
            <div class="col-8">
            <input id="ShipmentType" name="ShipmentType" placeholder="Shipment Type" type="text" class="form-control" required="required"></input>
            </div>
        </div> 
        <div class="form-group row">
            <div class="offset-4 col-8">
            <button name="submit" type="submit" class="btn btn-primary">Submit</button>
            </div>
        </div>
        </form>   

      </div>
    </>
  );
};

export default Page1;

