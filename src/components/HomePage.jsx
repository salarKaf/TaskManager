import React from 'react';
import taskIcon from '../assets/img/task.png';
import noteBookIcon from '../assets/img.notebook.png';
import { Link } from 'react-router-dom';

const HomePage = () => {
  return (
    <div className="home-page" style={{backgroundColor: rgb(218, 240, 245)}}>
      <header className="fixed-top" style={{ height: "50px", backgroundColor: "white", width: "101%" }}>
        <div className="row">
          <div className="col-lg-2">
            <p style={{ marginLeft: "50px", marginTop: "6px", fontSize: "25px", fontWeight: "600" }}>TaskManager</p>
          </div>
          <div className="col-lg-4">
            <div className="input-group" style={{ marginTop: "12px" }}>
              <input className="form-control" type="text" placeholder="Search" style={{ height: "30px" }} />
              <div className="input-group-append">
                  {/* <button className="btn btn-secondery">
                        <i className="fa fa-search">
                            ::before
                        </i>
                  </button> */}
              </div>
            </div>
          </div>
          <div className="col-lg-6">
            <div className="row" style={{ marginTop: "7px", height: "30px" }}>
                <div className="col-lg-6"></div>
                <a className="col-lg-2 pe-3 nav-link text-center mt-2" href="" id="sign_in" style={{ width: "90px", fontWeight: "600" }}> Sign in </a>
                <button className="col-lg-2 btn" id="sign_up" type="button" style={{ marginLeft: "10px", width: "90px", fontWeight: "600", backgroundColor: "rgb(93, 163, 214)", color: "white" }}>Sign up</button>
            </div>
          </div>
        </div>
      </header>
      <div className="container" style={{ height: "100px" }}></div>
      <div className="row">
        <div className="col-lg-1"></div>
        <div className="col-lg-3">
          <img src={taskIcon} alt="task-img" style={{ height: "400px" }} />
        </div>
        <div className="col-lg-7 me-3 mt-4" style={{ height: "200px", marginLeft: "45px" }}>
          <p style={{ fontWeight: "bold", fontSize: "55px", marginTop: "90px" }}> Manager </p>
        <div id="line" style={{ backgroundColor: "rgb(93, 163, 214)", height: "7px" }}></div>
          <div className="row">
            <div id="motto" className="col-lg-6 mt-2" style={{ fontSize: "30px", fontWeight: "600", marginLeft: "120px" }}>
                <p> Manage All Of Your Work </p>
                <p style={{ marginLeft: "80px" }}> In One Place </p>
                <p style={{ marginLeft: "100px" }}> Efficiently </p>
            </div>
            <div className="col-lg-4">
                <img src={noteBookIcon.png} style={{ height: "120px", marginLeft: "100px", marginTop: "50px" }} />
            </div>
          </div>
        </div>
      </div>
    </div>

    // <div className="home-page">
    //   <h1>Welcome to My Website</h1>
    //   <nav>
    //     <ul>
    //       <li>
    //         <Link to="/">Home</Link>
    //       </li>
    //       <li>
    //         <Link to="/about">About</Link>
    //       </li>
    //       <li>
    //         <Link to="/services">Services</Link>
    //       </li>
    //       <li>
    //         <Link to="/contact">Contact</Link>
    //       </li>
    //     </ul>
    //   </nav>
    //   <div className="content">
    //     <h2>About Us</h2>
    //     <p>
    //       Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam
    //       semper faucibus mauris, id luctus neque rhoncus quis. Aliquam
    //       maximus risus ac metus tempor, et dictum erat convallis. Pellentesque
    //       habitant morbi tristique senectus et netus et malesuada fames ac
    //       turpis egestas.
    //     </p>
    //   </div>
    // </div>
  );
};

export default HomePage;