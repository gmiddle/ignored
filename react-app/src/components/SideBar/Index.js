import React, { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import SidebarChannel from "../SidebarChannel/Index";
import AddServerModal from "../AddServerForm";
import AddChannelModal from "../AddChannelForm";
import dcordicon from "../../public/dcordicon.png";
import "./Sidebar.css";
import { updateUser } from "../../store/session";
import EditServerModal from "../EditServerForm";
import EditChannelModal from "../EditChannelForm";
import { deleteServer, getServers } from "../../store/server";
import { deleteChannel, editChannel } from "../../store/channel";
import {logout} from '../../store/session'

const Sidebar = ({
  currentServerId,
  setCurrentServerId,
  currentChannelId,
  setCurrentChannelId,
  currUser,
}) => {
  // const user = useSelector((state) => state.session.user.id)
  const { serverList } = useSelector((state) => state.session.user);
  const currentServer = serverList.find(
    (server) => `${server.id}` === localStorage.currentServerId
  );
  // const channelList = currentServer.channels
  // const currentChannel = channelList.find(channel=>`${channel.id}` === localStorage.currentChannelId)
  const dispatch = useDispatch();

  useEffect(() => {}, [serverList]);

  const handleServerDeleteClick = async (e) => {
    e.preventDefault();
    let serverId = e.target.value;
    await dispatch(deleteServer(serverId));
    await dispatch(updateUser(currUser.id));
  };

  const handleServerClick = async (e) => {
    let serverId = e.target.value;

    setCurrentServerId(serverId)
    await localStorage.setItem("currentServerId", currentServerId);
  };


  const handleChannelClick = async () => {

    await localStorage.setItem("currentChannelId", currentChannelId);
  };

  const handleChannelDeleteClick = async (e) => {
    e.preventDefault();
    let channelId = e.target.value;
    await dispatch(deleteChannel(channelId));
    await dispatch(updateUser(currUser.id));
  };

  const handleLogout = async () => {
    await dispatch(logout())
  }


  return (
    <div className="sideBar">
      <link
        rel="stylesheet"
        href="https://use.fontawesome.com/releases/v5.6.3/css/all.css"
        integrity="sha384-UHRtZLI+pbxtHCWp1t77Bi1L4ZtiqrqD80Kn4Z8NTSRyMA2Fd33n5dQ8lWUE00s/"
        crossorigin="anonymous"
      />
      <div className="sideBarTop">
        <div id="serversHeader">
          <h3>{"servers"}</h3>
          <AddServerModal
            setCurrentServerId={setCurrentServerId}
            userId={currUser.id}
          />
        </div>
        {serverList.map((server) => (
          <div className="serverCard">
            <div className="server-icon">
              <button
              //  onClick={() => handleServerClick(setCurrentServerId(server.id))}
                  onClick={handleServerClick}
                  className="serverCard-clickable-button"
                  value={server.id}
              ></button>
            </div>
            <div><h3 className="h3-server-name">{server.name}</h3></div>
            <button value={server.id} onClick={handleServerDeleteClick}>
              Delete
            </button>
            <EditServerModal
              setCurrentServerId={setCurrentServerId}
              userId={currUser.id}
              serverToEdit={server}
            />
          </div>
        ))}
      </div>
      <div className="sideBarChannels">
        <div className="sideBarChannelName">
          <div className="sideBarChannelNameText">
            <h3>{"channels"}</h3>
          </div>
          <AddChannelModal
            setCurrentChannelId={setCurrentChannelId}
            userId={currUser.id}
          />
        </div>
        <div className="sideBarChannelList">
          {currentServer &&
            currentServer.channels.map((channel) => (
            <div className="channelCard">
              <SidebarChannel
                channel={channel}
                handleChannelClick={handleChannelClick}
                setCurrentChannelId={setCurrentChannelId}
                currentChannelId={currentChannelId}
              />
              <EditChannelModal
              setCurrentChannelId= {setCurrentChannelId}
              userId= {currUser.id}
              channelToEdit= {channel}
              />
              <button value={channel.id} onClick={handleChannelDeleteClick}>Delete</button>
            </div>
            ))}
        </div>
      </div>
      <div className="sideBarUser">
        <div className="sideBarUserName">
          <h3> {currUser.username}</h3>
        </div>
        <div className="logoutIcon">
          <button onClick={handleLogout}>
          <i class="fas fa-sign-out-alt"></i>
          </button>
        </div>
      </div>
    </div>
  );
};

export default Sidebar;
