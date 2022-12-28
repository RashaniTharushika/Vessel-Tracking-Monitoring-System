import React, {useEffect, useState} from 'react';
import {Select, Button, TextInput} from "@mantine/core";
import {DatePicker} from "@mantine/dates";
import "../App.css";
import axios from "axios";

const Page3 = () => {

    const [FileUpdatedDate, setFileUpdatedDate] = useState();
    const [RecordUpdatedDate, setRecordUpdatedDate] = useState();
    const [MBL, setMBL] = useState();
    const [VESSEL, setVESSEL] = useState();
    const [Carrier, setCarrier] = useState();
    const [pol, setPol] = useState();
    const [etd, setEtd] = useState();
    const [etaToCMB, setEtaToCMB] = useState();
    const [NeedRegistering, setNeedRegistering] = useState();
    const [TrackingCommonMBL, setTrackingCommonMBL] = useState();
    const [MMSI, setMMSI] = useState();
    const [Voyage, setVoyage] = useState();
    const [HBL, setHBL] = useState();
    const [ShipmentType, setShipmentType] = useState();


    const submitForm = (e) => {
        e.preventDefault()

        if (!FileUpdatedDate || !RecordUpdatedDate || !MBL || !VESSEL || !Carrier || !pol || !etd || !etaToCMB || !NeedRegistering || !TrackingCommonMBL || !MMSI || !Voyage || !HBL || !ShipmentType) {
            alert("Please fill all the fields");
            return;
        }

        axios.post('http://localhost:5000/form', {
            FileUpdatedDate: FileUpdatedDate.toISOString().split('T')[0],
            RecordUpdatedDate: RecordUpdatedDate.toISOString().split('T')[0],
            MBL,
            VESSEL,
            Carrier,
            pol,
            etd: etd.toISOString().split('T')[0],
            etaToCMB: etaToCMB.toISOString().split('T')[0],
            NeedRegistering,
            TrackingCommonMBL,
            MMSI,
            Voyage,
            HBL,
            ShipmentType
        }).then(res => {
            if (res.data.status === "Success") {
                alert(res.data.rows + " rows added \n")
                window.location.reload()
            } else {
                alert("Failed")
            }
        }).catch( (e) => {
            console.log(e)
        });

    };

    return (<>
        <div>
            <h3 className="topic text-center" style={{marginTop: '50px', fontWeight: 'bold'}}>Vessel Tracking &
                Monitoring
                Platform</h3><br/><br/>
        </div>

        <div className="row">
            <div className="col-3"></div>
            <div className="col-6">
                <form onSubmit={submitForm}>
                    <div class="form-group row">
                        <label for="FileUpdatedDate" class="col-4 col-form-label">File Updated Date by Logistic
                            Team</label>
                        <div class="col-8">
                            <DatePicker id="FileUpdatedDate" name="FileUpdatedDate" value={FileUpdatedDate}
                                        onChange={setFileUpdatedDate}
                                        placeholder="File Updated Date by Logistic Team" type="date" required={true}
                                        class="form-control" />
                        </div>
                    </div>
                    <div class="form-group row">
                        <label for="RecordUpdatedDate" class="col-4 col-form-label">Record Updated Date by Logistic
                            Team</label>
                        <div class="col-8">
                            <DatePicker id="RecordUpdatedDate" name="RecordUpdatedDate" value={RecordUpdatedDate}
                                        onChange={setRecordUpdatedDate}
                                        placeholder="Record Updated Date by Logistic Team" type="date"
                                        class="form-control"
                                        required={true}/>
                        </div>
                    </div>
                    <div class="form-group row">
                        <label for="MBL" class="col-4 col-form-label">MBL NO</label>
                        <div class="col-8">
                            <TextInput id="MBL" name="MBL" placeholder="Master Bill of Lading Number" value={MBL}
                                       onChange={(e) => {
                                           setMBL(e.target.value)
                                       }}
                                       class="form-control" required={true}/>
                        </div>
                    </div>
                    <div class="form-group row">
                        <label for="VESSEL" class="col-4 col-form-label">Vessel Name</label>
                        <div class="col-8">
                            <TextInput id="VESSEL" name="VESSEL" placeholder="Vessel Name" type="text"
                                       class="form-control" value={VESSEL} onChange={(e) => {
                                setVESSEL(e.target.value)
                            }}
                                       required="required"/>
                        </div>
                    </div>
                    <div class="form-group row">
                        <label for="Carrier" class="col-4 col-form-label">Carrier</label>
                        <div class="col-8">
                            <Select id="Carrier" name="Carrier" required="required" class="form-control"
                                    value={Carrier} onChange={setCarrier}
                                    aria-describedby="CarrierHelpBlock"
                                    data={[
                                        {value: 'notfound', label: 'Not Found'},
                                        {value: 'duck', label: 'OOCL'},
                                        {value: 'fish', label: 'ZIM'},
                                        {value: 'wanhai', label: 'Wan Hai'},
                                        {value: 'maersk', label: 'Maersk'},
                                        {value: 'cnc', label: 'CNC'},
                                        {value: 'dongjin', label: 'Dongjin'},
                                        {value: 'heung', label: 'Heung-A'},
                                        {value: 'jinjiang', label: 'Jin Jiang'},
                                        {value: 'interasia', label: 'Interasia'},
                                        {value: 'haihua', label: 'Hai Hua'},
                                        {value: 'sinotrans', label: 'Sinotrans'},
                                        {value: 'sitc', label: 'SITC'},
                                        {value: 'misheng', label: 'Misheng'},
                                        {value: 'ts', label: 'T.S.'},
                                        {value: 'pancontinental', label: 'Pan Continental'},
                                        {value: 'nirint', label: 'Nirint'},
                                        {value: 'acl', label: 'ACL'},
                                        {value: 'admiralcontainer', label: 'Admiral Container'},
                                        {value: 'accontainer', label: 'AC Container'}
                                    ]}
                            />
                            <span id="CarrierHelpBlock"
                                  class="form-text text-muted small">Select Carrier Name from the List</span>
                        </div>
                    </div>
                    <div class="form-group row">
                        <label for="pol" class="col-4 col-form-label">POL</label>
                        <div class="col-8">
                            <TextInput id="pol" name="pol" placeholder="Loading Port" type="text" class="form-control"
                                       value={pol} onChange={(e) => {
                                setPol(e.target.value)
                            }}
                                       required="required"/>
                        </div>
                    </div>
                    <div class="form-group row">
                        <label for="etd" class="col-4 col-form-label">ETD</label>
                        <div class="col-8">
                            <DatePicker id="etd" name="etd" placeholder="ETD " type="date" class="form-control"
                                        value={etd} onChange={setEtd}
                                        required="required"/>
                        </div>
                    </div>
                    <div class="form-group row">
                        <label for="etaToCMB" class="col-4 col-form-label">ETA to CMB</label>
                        <div class="col-8">
                            <DatePicker id="etaToCMB" name="etaToCMB" placeholder="ETA to CMB" type="date"
                                        value={etaToCMB} onChange={setEtaToCMB}
                                        class="form-control" required="required"/>
                        </div>
                    </div>
                    <div class="form-group row">
                        <label for="NeedRegistering" class="col-4 col-form-label">Need Registering Yes/No?</label>
                        <div class="col-8">
                            <Select id="NeedRegistering" name="NeedRegistering" class="form-control"
                                    value={NeedRegistering} onChange={setNeedRegistering}
                                    aria-describedby="NeedRegisteringHelpBlock" required="required"
                                    data={[{value: 'Yes', label: 'Yes'}, {value: 'No', label: 'No'}]}/>
                            <span id="NeedRegisteringHelpBlock"
                                  class="form-text text-muted small">Need Registering?</span>
                        </div>
                    </div>
                    <div class="form-group row">
                        <label for="TrackingCommonMBL " class="col-4 col-form-label">Tracking Common MBL</label>
                        <div class="col-8">
                            <TextInput id="TrackingCommonMBL " name="TrackingCommonMBL "
                                       placeholder="Tracking Common MBL " value={TrackingCommonMBL} onChange={(e) => {
                                setTrackingCommonMBL(e.target.value)
                            }}
                                       type="text" class="form-control" required="required"/>
                        </div>
                    </div>
                    <div class="form-group row">
                        <label for="MMSI" class="col-4 col-form-label">MMSI</label>
                        <div class="col-8">
                            <TextInput id="MMSI" name="MMSI" placeholder="MMSI" type="text" class="form-control"
                                       value={MMSI} onChange={(e) => {
                                setMMSI(e.target.value)
                            }}
                                       required="required"/>
                        </div>
                    </div>
                    <div class="form-group row">
                        <label for="Voyage" class="col-4 col-form-label">Voyage</label>
                        <div class="col-8">
                            <TextInput id="Voyage" name="Voyage" placeholder="Voyage No" type="text"
                                       class="form-control" value={Voyage} onChange={(e) => {
                                setVoyage(e.target.value)
                            }}
                                       required="required"/>
                        </div>
                    </div>
                    <div class="form-group row">
                        <label for="HBL" class="col-4 col-form-label">HBL</label>
                        <div class="col-8">
                            <TextInput id="HBL" name="HBL" placeholder="HBL" type="text" class="form-control"
                                       value={HBL} onChange={(e) => {
                                setHBL(e.target.value)
                            }}
                                       required="required"/>
                        </div>
                    </div>
                    <div class="form-group row">
                        <label for="ShipmentType" class="col-4 col-form-label">Shipment Type</label>
                        <div class="col-8">
                            <TextInput id="ShipmentType" name="ShipmentType" placeholder="Shipment Type" type="text"
                                       value={ShipmentType} onChange={(e) => {
                                setShipmentType(e.target.value)
                            }}
                                       class="form-control" required="required"/>
                        </div>
                    </div>
                    <div class="form-group row justify-content-center p-4">
                        <div>
                            <button name="submit" type="submit" class="btn btn-primary">Submit</button>
                        </div>
                    </div>
                </form>
            </div>
            <div className="col-3"></div>
        </div>
    </>);
};

export default Page3;

