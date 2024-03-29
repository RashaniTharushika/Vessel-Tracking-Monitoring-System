import React from 'react';
import {emailValidator, passwordValidator} from '../components/regexValidator';
import {useHistory} from "react-router-dom"
import Logo from "./../images/logo.png";
import "../components/login.css";

const Login = () => {
    const history = useHistory()

    const [input, setInput] = React.useState({email: '', password: ''});

    const [errorMessage, seterrorMessage] = React.useState('');
    const [successMessage, setsuccessMessage] = React.useState('');

    const handleChange = e => {
        setInput({...input, [e.target.name]: e.target.value});
    };

    React.useEffect(() => {
        if (localStorage.getItem('auth')) history.push('/')
    }, [])

    const formSubmitter = e => {
        e.preventDefault();
        setsuccessMessage('');
        if (!emailValidator(input.email)) return seterrorMessage('Please enter valid email id');

        if (!passwordValidator(input.password))
            return seterrorMessage(
                'Password should have minimum 8 character with the combination of uppercase, lowercase, numbers and specialcharaters'
            );
        // setsuccessMessage('Successfully Validated');
        // if (input.email !== 'admin@gmail.com' || input.password !== 'Password@1') return seterrorMessage('Invalid email or password');

        if (input.email === 'intimates@gmail.com' && input.password === 'Password@1') {
            localStorage.setItem('plant', 'INTIMATES')
        } else if (input.email === 'masactive@gmail.com' && input.password === 'Active@1') {
            localStorage.setItem('plant', 'ACTIVE')
        } else if (input.email === 'bodyline@gmail.com' && input.password === 'Bodyline@1') {
            localStorage.setItem('plant', 'BODYLINE')
        } else if (input.email === 'maskreeda@gmail.com' && input.password === 'Kreeda@1') {
            localStorage.setItem('plant', 'KREEDA')
        } else {
            return seterrorMessage('Invalid email or password')
        }

        history.push('/')
        localStorage.setItem('auth', true)

    };

    return (
        <div>
            <div className="limiter">
                <div className="container-login100">
                    <div className="wrap-login100 p-l-55 p-r-55 p-t-65 p-b-54">
                        <form className="login100-form validate-form" onSubmit={formSubmitter}>
                            <span className="login100-form-title p-b-49"> <img src={Logo} alt="logo" className="Logo"/></span>
                            {errorMessage.length > 0 &&
                                <div style={{marginBottom: '10px', color: 'red'}}>{errorMessage}</div>}
                            {successMessage.length > 0 && (
                                <div style={{marginBottom: '10px', color: 'green'}}>{successMessage}</div>
                            )}
                            <div className="wrap-input100 validate-input m-b-23" data-validate="email is required">
                                <span className="label-input100">Email</span>
                                <input
                                    className="input100"
                                    type="text"
                                    name="email"
                                    placeholder="Type your username"
                                    onChange={handleChange}
                                />
                                <span className="focus-input100" data-symbol=""/>
                            </div>
                            <div className="wrap-input100 validate-input" data-validate="Password is required">
                                <span className="label-input100">Password</span>
                                <input
                                    className="input100"
                                    type="password"
                                    name="password"
                                    placeholder="Type your password"
                                    onChange={handleChange}
                                />
                                <span className="focus-input100" data-symbol=""/>
                            </div>
                            <div className="text-right p-t-8 p-b-31">
                                <a href="#">Forgot password?</a>
                            </div>
                            <div className="container-login100-form-btn">
                                <div className="wrap-login100-form-btn">
                                    <div className="login100-form-bgbtn"/>
                                    <button className="login100-form-btn">LOGIN AS ADMIN</button>
                                </div>
                            </div>
                            {/*<div className="txt1">*/}
                            {/*    <span>OR</span>*/}
                            {/*</div>*/}
                            {/*<div className="flex-c">*/}
                            {/*    <a href='/Dashboard2' className="btn"> CONTINUE WITHOUT LOGIN</a>*/}
                            {/*</div>*/}
                            {/* <div className="flex-col-c p-t-155">
                <span className="txt1 p-b-17">Or Sign Up Using</span>
                <a href="#" className="txt2">
                  Sign Up
                </a>
              </div> */}
                        </form>
                    </div>
                </div>
            </div>
            <div id="dropDownSelect1"/>
        </div>
    );
};

export default Login;
