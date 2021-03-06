import React from 'react';
import { NavLink } from 'react-router-dom';
import './navBar.css';
import {useSelector} from 'react-redux'



const NavBar = () => {
  const sessionUser = useSelector(state => state.session.user);

  return (
    <nav>
      <div >
        <NavLink to="/">
        <img alt="Logo" className="logo" src="https://res.cloudinary.com/dxo7djnid/image/upload/v1636220158/ignored/WHITE_Chat_Communication_Logo_1500_x_500_px_190_x_40_px_1_etunj2.svg"/>
        </NavLink>
      </div>
     {!sessionUser?  <button className="loginBtn">
          <NavLink to='/login' exact={true} activeClassName='active' >
            Login
          </NavLink>
        </button>: null}


    </nav>
  );
}

export default NavBar;
