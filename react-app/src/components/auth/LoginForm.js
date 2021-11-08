import React, { useState } from 'react';
import { Link } from 'react-router-dom'
import { useSelector, useDispatch } from 'react-redux';
import { Redirect } from 'react-router-dom';
import { login } from '../../store/session';
import * as sessionActions from '../../store/session';
import Footer from '../Footer/Index.js';
import './LoginForm.css'

const LoginForm = () => {
  const [errors, setErrors] = useState([]);
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  // const [credential, setCredential] = useState('');
  const user = useSelector(state => state.session.user);
  const dispatch = useDispatch();

  const onLogin = async (e) => {
    e.preventDefault();
    const data = await dispatch(login(email, password));
    if (data) {
      setErrors(data);
    }
  };

  const updateEmail = (e) => {
    setEmail(e.target.value);
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  };

  if (user) {
    return <Redirect to='/' />;
  }


  const demoLogin = async () => {
    setEmail('demo@aa.io');
    setPassword('password');
    return dispatch(
      sessionActions.login({email: 'demo@aa.io', password: 'password'})
    );
  }

  return (
    <div className='loginFormContainer'>
      <form onSubmit={onLogin} className='loginForm'>
        <div className="headerContainer">
        <h2 className="welcomeBack">Welcome back!</h2>
        <h3 className="loginAccount">We're so excited to see you again!</h3>
        </div>
        <div>
          {errors.map((error, ind) => (
            <div key={ind}>{error}</div>
          ))}
        </div>
        <div>
          <label htmlFor='email'></label>
          <input
            name='email'
            type='text'
            placeholder='Email'
            value={email}
            onChange={updateEmail}
          />
        </div>
        <div>
          <label htmlFor='password'></label>
          <input
            name='password'
            type='password'
            placeholder='Password'
            value={password}
            onChange={updatePassword}
          />
        </div>
          <button type='submit' className="logged">Login</button>
          {!user?
        <button className="demoBtn" onClick={demoLogin}>Demo Login</button>
        : null}
        <div>
          <p className="dontAccount">Dont have an account?</p>
          <a className="register" href="/sign-up">Register</a>
          </div>

      </form>
      <Footer/>
    </div>
  );
};

export default LoginForm;
