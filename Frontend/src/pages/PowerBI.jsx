import React from "react";
import "../App.css";
import Navbar from "../components/Header";

const PowerBI = () => {
    <Navbar />
    const plant = localStorage.getItem('plant')

    if (plant === "INTIMATES") {
        return (
            <>
                <iframe title="Logistic Vessel Tracking and Monitoring System" width="1700" height="700" src="https://app.powerbi.com/reportEmbed?reportId=7b1f5ed2-1e43-40f1-8818-be3678adc495&autoAuth=true&ctid=852c5799-8134-4f15-9d38-eba4296cc76f" frameborder="0" allowFullScreen="true"></iframe>     
            </>);
    }

    if (plant === "ACTIVE") {
        return (
            <>
                <iframe title="Logistic Vessel Tracking and Monitoring System- MAS Active" width="1700" height="700" src="https://app.powerbi.com/reportEmbed?reportId=c673bf2c-7645-4467-9593-99f62aa2962d&autoAuth=true&ctid=852c5799-8134-4f15-9d38-eba4296cc76f" frameborder="0" allowFullScreen="true"></iframe>
            </>);
    }

    if (plant === "BODYLINE") {
        return (
            <>
                <iframe title="Logistic Vessel Tracking and Monitoring System-BODYLINE" width="1700" height="700" src="https://app.powerbi.com/reportEmbed?reportId=04ce11c2-2a2e-4950-a878-fab198e6748b&autoAuth=true&ctid=852c5799-8134-4f15-9d38-eba4296cc76f" frameborder="0" allowFullScreen="true"></iframe>
            </>);
    }

    if (plant === "KREEDA") {
        return (
            <>
                <iframe title="Logistic Vessel Tracking and Monitoring System- KREEDA" width="1700" height="700" src="https://app.powerbi.com/reportEmbed?reportId=0cc54949-ef49-4d6d-b266-f5cd779ecd61&autoAuth=true&ctid=852c5799-8134-4f15-9d38-eba4296cc76f" frameborder="0" allowFullScreen="true"></iframe>
            </>);
    }


    return (<>
        <h3>There is nothing to show! Please Log in</h3>
    </>);
};

export default PowerBI;

