import React, { useState } from 'react';
import { Link } from 'react-router-dom'
import { useSelector, useDispatch } from 'react-redux'
import { Redirect } from 'react-router-dom';
import { signUp } from '../../store/session';
import * as sessionActions from '../../store/session';
import "./SignUpForm.css"
import Footer from '../Footer/Index.js';

const SignUpForm = () => {
  const [errors, setErrors] = useState([]);
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [repeatPassword, setRepeatPassword] = useState('');
  const [credential, setCredential] = useState('');
  const user = useSelector(state => state.session.user);
  const dispatch = useDispatch();

  const onSignUp = async (e) => {
    e.preventDefault();
    if (password === repeatPassword) {
      const data = await dispatch(signUp(username, email, password));
      if (data) {
        setErrors(data)
      }
    }
  };

  const updateUsername = (e) => {
    setUsername(e.target.value);
  };

  const updateEmail = (e) => {
    setEmail(e.target.value);
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  };

  const updateRepeatPassword = (e) => {
    setRepeatPassword(e.target.value);
  };

  if (user) {
    return <Redirect to='/' />;
  }


  const demoLogin = async () => {
    setCredential('demo@aa.io');
    setPassword('password');
    return dispatch(
      sessionActions.login({credential: 'demo@aa.io', password: 'password'})
    );
  }

  return (
    <div className='signUpFormContainer'>
      <form onSubmit={onSignUp} className='signUpForm'>
        <h3 className="registerAccount">Create an Account</h3>
        <div>
          {errors.map((error, ind) => (
            <div key={ind}>{error}</div>
          ))}
        </div>
        <div>
          <input
          placeholder="User Name"
            type='text'
            name='username'
            onChange={updateUsername}
            value={username}
          ></input>
        </div>
        <div>
          <input
          placeholder="Email"
            type='text'
            name='email'
            onChange={updateEmail}
            value={email}
          ></input>
        </div>
        <div>
          <input
          placeholder="Password"
            type='password'
            name='password'
            onChange={updatePassword}
            value={password}
          ></input>
        </div>
        <div>
          <input
          placeholder="Confirm Password"
            type='password'
            name='repeat_password'
            onChange={updateRepeatPassword}
            value={repeatPassword}
            required={true}
          ></input>
        </div>
        <button type='submit' className="signed">Sign Up</button>
        {!user?
        <button className="demoBtn" onClick={demoLogin}>Demo Login</button>
        : null}
        <a className="register" href="/sign-up">Already have an account?</a>
      </form>
      <Footer />
    </div>
  );
};

export default SignUpForm;
