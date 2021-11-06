import React from 'react';
import { NavLink } from 'react-router-dom';
import './navBar.css';
import Logo from '../../public/Logo.svg'


const NavBar = () => {
  return (
    <nav>
      <img alt="Logo" src={Logo}/>

        <button className="loginBtn">
          <NavLink to='/login' exact={true} activeClassName='active' >
            Login
          </NavLink>
        </button>

    </nav>
  );
}

export default NavBar;
