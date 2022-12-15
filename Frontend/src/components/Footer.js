import React from "react";
import "./style.css";

function Footer() {
  return (
    <div className="main-footer">
      <div className="container">
        <div className="row">
          {/* Column1 */}
          <div className="col">
            <h4>XXXXXXXXX</h4>
            <h1 className="list-unstyled">
              <li>342-420-6969</li>
              <li>XXXXX, XXX</li>
              <li>123 XXXXX XXX XXXXX XXX</li>
            </h1>
          </div>
          {/* Column2 */}
          <div className="col">
            <h4>XXXXX</h4>
            <ui className="list-unstyled">
              <li>XXXXX XXX</li>
              <li>XXXXX XXX</li>
              <li>XXXXX XXX</li>
            </ui>
          </div>
          {/* Column3 */}
          <div className="col">
            <h4>XXXXX XXXXXX</h4>
            <ui className="list-unstyled">
              <li>XXXXX XXX</li>
              <li>XXXXX XXX</li>
              <li>XXXXX XXX</li>
            </ui>
          </div>
        </div>
        <hr />
        <div className="row">
          <p className="col-sm">
            &copy;{new Date().getFullYear()} XXXXX XXX | All rights reserved |
            Terms Of Service | Privacy
          </p>
        </div>
      </div>
    </div>
  );
}

export default Footer;
