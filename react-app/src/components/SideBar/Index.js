import React, { useEffect } from 'react'
import { useSelector, useDispatch } from "react-redux";
import SidebarChannel from '../SidebarChannel/Index'
import dcordicon from '../../public/dcordicon.png'
import './Sidebar.css'
import AddServerModal from '../AddServerForm';
import { deleteServer } from '../../store/server';

const Sidebar = ({currentServerId, setCurrentServerId}) => {
    const userId = useSelector((state) => state.session.user.id)
    const {serverList} = useSelector((state) => state.session.user)
    const currentServer = serverList.find(server=>`${server.id}` === localStorage.currentServerId)
    
    const dispatch = useDispatch();

    useEffect(() => {
      console.log('here')
    }, [serverList])

    const handleDeleteClick = (e) => {
      e.preventDefault()
      let serverId = e.target.value
      console.log(serverId, 'serverId')
      dispatch(deleteServer(serverId))
    }

    const handleClick = () => {
        localStorage.setItem('currentServerId', currentServerId)
    }
    
    return (

        <div className="sideBar">
             <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.6.3/css/all.css" integrity="sha384-UHRtZLI+pbxtHCWp1t77Bi1L4ZtiqrqD80Kn4Z8NTSRyMA2Fd33n5dQ8lWUE00s/" crossorigin="anonymous" />
            <div className="sideBarTop">
                <div id="serversHeader">
                    <i className="fas fa-chevron-circle-down"></i> {/* drop down for servers list */}                   
                    <h3>{'servers'}</h3>
                    <AddServerModal 
                      setCurrentServerId={setCurrentServerId}
                      userId={userId} />
                </div>
                {serverList.map((server)=>(
                <div className="serverCard">
                   <div onClick={()=>handleClick(setCurrentServerId(server.id))} className="serverIcon"></div>
                   <button value={server.id} onClick={handleDeleteClick}>Delete</button>
                </div>
                ))}
            </div>
            <div className="sideBarChannels">
                <div className="sideBarChannelName">
                    <div className="sideBarChannelNameText">
                        <h3>{'channels'}</h3>
                        </div>
                        <i className="fas fa-plus" id="addChannel"></i> {/* add channel button */}
                    </div>
            <div className="sideBarChannelList">
            {currentServer && currentServer.channels.map((channel)=>(
                <SidebarChannel channelName={channel.name} />
            ))}


            </div>
        </div>
        <div className="sideBarUser">
            <div className="sideBarUserName">
                <h3> user name</h3>
                {/* {userName} */}
                </div>
                <div className="logoutIcon">
                <i className="fas fa-cog"></i>
                </div>
            </div>
        </div>

    )
}

export default Sidebar
