import React, { useState, useEffect,  } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import LoginForm from './components/auth/LoginForm';
import SignUpForm from './components/auth/SignUpForm';
import ProtectedRoute from './components/auth/ProtectedRoute';
import UsersList from './components/UsersList';
import User from './components/User';
import Splash from './components/Splash/Index';
import Sidebar from './components/SideBar/Index';
import Chat from './components/Chat/Index';
import { authenticate } from './store/session';
import './index.css'
// import SidebarChannel from './components/SidebarChannel/Index';

function App() {
  const user = useSelector((state) => state.session.user)
  const [loaded, setLoaded] = useState(false);
  const [currentServerId, setCurrentServerId] = useState();
  // const [currentServerId, setCurrentServerId] = useState(localStorage.getItem("currentServerId") ? localStorage.getItem("currentServerId") : user.servers[0].id);
  const [currentChannelId, setCurrentChannelId] = useState();
  const [currUser, setCurrUser] = useState(user)
  const dispatch = useDispatch();

  useEffect(()=>{
    setCurrUser(user);
  }, [user]);

  useEffect(() => {
    (async() => {
      await dispatch(authenticate());
      setLoaded(true);
    })();
  }, [dispatch]);

  if (!loaded) {
    return null;
  }

  return (
    <BrowserRouter>
      <Switch>
      <Route exact path="/">
            <Splash />
          </Route>
        <Route path='/login' exact={true}>
          <LoginForm />
        </Route>
        <Route path='/sign-up' exact={true}>
          <SignUpForm />
        </Route>
        <ProtectedRoute path='/users' exact={true} >
          <UsersList/>
        </ProtectedRoute>
        <ProtectedRoute path='/users/:userId' exact={true} >
          <User />
        </ProtectedRoute>
        <ProtectedRoute path='/' exact={true} >
          <h1>My Home Page</h1>
        </ProtectedRoute>
        <ProtectedRoute exact path='/dashboard' exact={true} >
          <div className="app">
          <Sidebar
            currUser={currUser}
            currentServerId={currentServerId}
            setCurrentServerId={setCurrentServerId}
            currentChannelId={currentChannelId}
            setCurrentChannelId={setCurrentServerId}
          />
          <Chat
            currUser={currUser}
            currentServerId={currentServerId}
            setCurrentServerId={setCurrentServerId}
            currentChannelId={currentChannelId}
            setCurrentChannelId={setCurrentChannelId}
          />
          </div>
        </ProtectedRoute>

      </Switch>
    </BrowserRouter>
  );
}

export default App;
