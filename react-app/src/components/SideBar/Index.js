import React from 'react'
import { useDispatch, useSelector } from "react-redux";
import SidebarChannel from '../SidebarChannel/Index'
import './Sidebar.css'


const Sidebar = () => {
    const {serverList} = useSelector((state) => state.session.user)
    return (

        <div className="sideBar">
             <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.6.3/css/all.css" integrity="sha384-UHRtZLI+pbxtHCWp1t77Bi1L4ZtiqrqD80Kn4Z8NTSRyMA2Fd33n5dQ8lWUE00s/" crossorigin="anonymous" />
          <div className="sideBarTop">
                {/* <h3>{servers}</h3>  render servers in h3*/}
                <h3>{'servers'}</h3>
                {console.log(serverList)}
                {serverList.map((server)=>(
                    <p>{server.name}</p>
                ))}
                <i class="fas fa-chevron-circle-down"></i> {/* drop down for servers list */}
            </div>
            <div className="sideBarChannels">
                <div className="sideBarChannelName">
                    <div className="sideBarChannelNameText">
                    <i class="fas fa-chevron-circle-down"></i> {/* drop down for channels list */}
                        <h3>{'channels'}</h3>
                        </div>
                        <i class="fas fa-plus"></i> {/* add channel button */}
                    </div>
            <div className="sideBarChannelList">
                <SidebarChannel />
                <SidebarChannel />
                <SidebarChannel />
                <SidebarChannel />
                <SidebarChannel />
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
