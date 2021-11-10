import React, { useEffect } from 'react'
import { useDispatch, useSelector } from "react-redux";
import SidebarChannel from '../SidebarChannel/Index'
import dcordicon from '../../public/dcordicon.png'
import './Sidebar.css'


const Sidebar = ({currentServerId, setCurrentServerId}) => {
    const {serverList} = useSelector((state) => state.session.user)
    const currentServer = serverList.find(server=>server.id === currentServerId)

    useEffect(()=>{

    },[currentServerId])

    return (

        <div className="sideBar">
             <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.6.3/css/all.css" integrity="sha384-UHRtZLI+pbxtHCWp1t77Bi1L4ZtiqrqD80Kn4Z8NTSRyMA2Fd33n5dQ8lWUE00s/" crossorigin="anonymous" />
            <div className="sideBarTop">
                <div id="serversHeader">
                    <i class="fas fa-chevron-circle-down"></i> {/* drop down for servers list */}
                    <h3>{'servers'}</h3>
                </div>
                {serverList.map((server)=>(
                <div className="serverCard">
                   <div onClick={()=>setCurrentServerId(server.id)} className="serverIcon"></div>
                </div>
                ))}
            </div>
            <div className="sideBarChannels">
                <div className="sideBarChannelName">
                    <div className="sideBarChannelNameText">
                        <h3>{'channels'}</h3>
                        </div>
                        <i class="fas fa-plus" id="addChannel"></i> {/* add channel button */}
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
                <i class="fas fa-cog"></i>
                </div>
            </div>
        </div>

    )
}

export default Sidebar
