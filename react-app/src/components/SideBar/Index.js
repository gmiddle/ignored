import React, { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import AddServerModal from "../AddServerForm";
import AddChannelModal from "../AddChannelForm";
// import dcordicon from "../../public/dcordicon.png";
import "./Sidebar.css";
// import { updateUser } from "../../store/session";
import EditServerModal from "../EditServerForm";
import EditChannelModal from "../EditChannelForm";
import { deleteServer, getServers, getServerbyId } from "../../store/server";
import { deleteChannel, getChannelbyId, getChannels } from "../../store/channel";
import {logout} from '../../store/session'
import { getMessages } from "../../store/message";


const Sidebar = ({ setCurrentServerId, setCurrentChannelId, currUser, }) => {

  const serverList = useSelector((state) => state.server.allServers?.servers);
  const currentServer = useSelector((state) => state.server.currentServer)
  // const channelList = useSelector((state) => state.channels.allChannels?.channels)
  const currentChannel = useSelector((state) => state.channels.currentChannel)
  const allChannels = useSelector((state) => state.channels.allChannels)



  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(getServers())
    if(localStorage.currentServerId) dispatch(getServerbyId(localStorage.currentServerId))
    dispatch(getChannels())
    if(localStorage.currentChannelId) dispatch(getChannelbyId(localStorage.currentChannelId))
  }, []);

  useEffect(() => {
    dispatch(getServers())
    dispatch(getChannels())
    dispatch(getMessages(localStorage.currentChannelId))
  }, [currentServer, currentChannel]);


  const handleServerDeleteClick = async (e) => {
    e.preventDefault();
    let serverId = e.target.value;
    await dispatch(deleteServer(serverId));
  };

  const handleServerClick = async (e) => {
    let serverId = e.target.value;
    await localStorage.setItem("currentServerId", serverId);
    await dispatch(getServerbyId(serverId))
  };



  const handleChannelClick = async (e) => {
    let channelId = e.target.value
    await localStorage.setItem("currentChannelId", e.target.value);
    await dispatch(getChannelbyId(channelId))
  };

  const handleChannelDeleteClick = async (e) => {
    e.preventDefault();
    let channelId = e.target.value;
    await dispatch(deleteChannel(channelId));
    localStorage.setItem("currentChannelId", "");
    await getChannels()
  };

  const handleLogout = async () => {
    await dispatch(logout())
  }

  // const userChannelMap = allChannels.allChannels?.channels?.map((channel) => {
            
  //   if (channel.ownerId == currUser.id) {
  //     return (
  //       <div className="channelCard" key={channel.id}>
  //           <span  className='sidebarChannelHash'>#</span>
  //           <button value={channel.id} onClick={handleChannelClick} className="sidebarChannel" >
  //             {channel.name}
  //           </button>
  //         <EditChannelModal
  //         setCurrentChannelId= {setCurrentChannelId}
  //         userId= {currUser.id}
  //         channelToEdit= {channel}
  //         />
  //         <button value={channel.id} onClick={handleChannelDeleteClick} id="channelDelete">Delete</button>
  //       </div>
  //     )
  //   }
  // })


  return (
    <div className="sideBar">
      <link
        rel="stylesheet"
        href="https://use.fontawesome.com/releases/v5.6.3/css/all.css"
        integrity="sha384-UHRtZLI+pbxtHCWp1t77Bi1L4ZtiqrqD80Kn4Z8NTSRyMA2Fd33n5dQ8lWUE00s/"
        crossOrigin="anonymous"
      />
      <div className="sideBarTop">
        <div id="serversHeader">
          <h3>{"servers"}</h3>
          <AddServerModal
            setCurrentServerId={setCurrentServerId}
            userId={currUser.id}
          />
        </div>
        {serverList?.filter(server => server.ownerId == currUser.id).map((server) => (
          <div className="serverCard" key={server.id}>
            <div className="server-icon" value={server.serverImg}>
              <button
              //  onClick={() => handleServerClick(setCurrentServerId(server.id))}
                  onClick={handleServerClick}
                  className="serverCard-clickable-button"
                  value={server.id}
              ></button>
            </div>
            <div><h3 className="h3-server-name">{server.name}</h3></div>
            <button className="server-delete-button" value={server.id} onClick={handleServerDeleteClick}>
            Delete
            </button>
            <EditServerModal
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
            userId={currUser.id}
          />
        </div>
        <div className="sideBarChannelList">
          {/* {currentServer && currentServer.channels.map((channel) => ( */}
          {/* {console.log("allChannels-----------", allChannels)} */}
          {allChannels?.channels?.filter((channel) => channel.server_id == localStorage.currentServerId).map((channel) => (
            <div className="channelCard" key={channel.id}>
                {/* {console.log(channel)} */}
                  <span  className='sidebarChannelHash'>#</span>
                  <button value={channel.id} onClick={handleChannelClick} className="sidebarChannel" >
                    {channel.name}
                  </button>
                <EditChannelModal
                setCurrentChannelId= {setCurrentChannelId}
                userId= {currUser.id}
                channelToEdit= {channel}
                />
                <button value={channel.id} onClick={handleChannelDeleteClick} id="channelDelete">Delete</button>
              </div>
          ))}
          {/* <userChannelMap/> */}

        </div>
      </div>
      <div className="sideBarUser">
        <div className="sideBarUserName">
          <h3> {currUser.username}</h3>
        </div>
        <div className="logoutIcon">
          <button onClick={handleLogout}>
          <i className="fas fa-sign-out-alt"></i>
          </button>
        </div>
      </div>
    </div>
  );
};

export default Sidebar;
