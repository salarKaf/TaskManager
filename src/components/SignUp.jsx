import React from "react";
import Bootstrap from "bootstrap";
import { Link } from 'react-router-dom';

const SignUp = () => { 
    return ( 
    <div style={{ backgroundColor: 'rgb(209, 247, 255)', height: 100% }}>
        <div id="nav" className="container" style={{ height: '150px' }}></div> 
        <div className="row"> 
            <div className="col-lg-4"></div> 
            <div className="col-lg-4"> 
                <div className="ps-2" style={{ height: '50px' }}> 
                    Let's get your account ready now! 
                </div> 
                <div style={{ height: '50px' }}> 
                    <input type="text" className="form-control" placeholder="First name" />
                </div> 
                <div style={{ height: '50px' }}> 
                    <input type="text" className="form-control" placeholder="Last name" /> 
                </div> 
                <div style={{ height: '50px' }}> 
                    <input type="text" className="form-control" placeholder="Username" /> 
                </div> 
                <div style={{ height: '50px' }}> 
                    <input type="text" className="form-control" placeholder="Email" /> 
                </div> 
                <div style={{ height: '50px' }}> 
                    <input type="text" className="form-control" placeholder="Password" /> 
                </div> 
                <div style={{ height: '50px' }}> 
                    <input type="text" className="form-control" placeholder="Confirm Password" /> 
                </div> 
                <div className="row"> 
                    <div className="col-lg-5"></div> 
                    <div className="col-lg-4"> 
                        <button type="button" className="btn btn-success" style={{ width: '100px' }}> 
                            submit 
                        </button> 
                    </div> 
                </div> 
            </div> 
        </div> 
    </div> ); }

export default SignUp;