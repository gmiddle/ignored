import React from 'react';
import { NavLink } from 'react-router-dom';
import './navBar.css';


const NavBar = () => {
  return (
    <nav>

        <button className="loginBtn">
          <NavLink to='/login' exact={true} activeClassName='active' >
            Login
          </NavLink>
        </button>

    </nav>
  );
}

export default NavBar;
