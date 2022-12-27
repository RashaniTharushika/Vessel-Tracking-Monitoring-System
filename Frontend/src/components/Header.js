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
				<a href="https://app.powerbi.com/reportEmbed?reportId=7b1f5ed2-1e43-40f1-8818-be3678adc495&autoAuth=true&ctid=852c5799-8134-4f15-9d38-eba4296cc76f">Power BI dashboard</a>
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
