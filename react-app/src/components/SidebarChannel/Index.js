import React from 'react'
// import { useSelector} from 'react-redux'
// import { useEffect } from 'react'
import './SidebarChannel.css'



const SidebarChannel = ({channel, handleChannelClick, setCurrentChannelId}) => {
    console.log('--------------------SideBarChannel-channel.id',channel.id)

    return (
        <div className="sidebarChannel" value={channel.id} onClick={()=>handleChannelClick(setCurrentChannelId(channel.id))}>
            <h4><span className='sidebarChannelHash'>#</span> {channel.name}  </h4>
        </div>
    )
}

export default SidebarChannel
