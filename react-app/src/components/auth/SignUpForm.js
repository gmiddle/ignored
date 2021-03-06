import React, { useState } from 'react';
// import { Link } from 'react-router-dom'
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


  const user = useSelector(state => state.session.user);
  const dispatch = useDispatch();


  if (user) return <Redirect to="/dashboard" />;

  const onSignUp = async (e) => {
    e.preventDefault();
    if (password) {
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


  if (user) {
    return <Redirect to='/' />;
  }


  const demoLogin = async () => {
    setEmail('demo@aa.io');
    setPassword('password');
    setUsername('demo');
    return dispatch(
      sessionActions.login({username: 'demo',email: 'demo@aa.io', password: 'password'})
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
        <button type='submit' className="signed">Sign Up</button>
        {!user?
        <button className="demoBtn" onClick={demoLogin}>Demo Login</button>
        : null}
        <a className="register" href="/login">Already have an account?</a>
      </form>
      <Footer />
    </div>
  );
};

export default SignUpForm;
