import { useRef } from "react";
import { FaBars, FaTimes } from "react-icons/fa";
import "./style.css";

function Navbar() {
	const navRef = useRef();

	const showNavbar = () => {
		navRef.current.classList.toggle("responsive_nav");
	};

	return (
		<header>
			<img src="https://seeklogo.com/images/M/mas-holdings-logo-2ACA338CD6-seeklogo.com.png" className="Logo" style={{width: '10%'}}/>
			<nav ref={navRef}>
				<a href="../Dashboard.jsx">Home</a>
				<a href="/#">Operation team</a>
				<a href="/PowerBI.jsx">Power BI dashboard</a>
				<a href="/#">About</a>
				<button
					className="nav-btn nav-close-btn"
					onClick={showNavbar}>
					<FaTimes />
				</button>
			</nav>
			<button className="nav-btn" onClick={showNavbar}>
				<FaBars />
			</button>
		</header>
	);
}

export default Navbar;
