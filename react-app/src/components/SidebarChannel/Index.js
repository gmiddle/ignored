import React from 'react'
// import { useSelector} from 'react-redux'
// import { useEffect } from 'react'
import './SidebarChannel.css'



const SidebarChannel = ({channel, handleChannelClick, setCurrentChannelId, currentChannelId}) => {
    console.log('--------------------SideBarChannel-channel.id',channel.id)

    const channelClickAndIdHandler = () => {
        // handleChannelClick(channel.id)
        localStorage.setItem("currentChannelId", channel.id)
        setCurrentChannelId(channel.id)
        console.log('-----------SidebarChannel - currentChannelId', currentChannelId)
    }

    return (
        <div className="sidebarChannel" value={channel.id} onClick={()=>channelClickAndIdHandler()}>
            <h4><span className='sidebarChannelHash'>#</span> {channel.name}  </h4>
        </div>
    )
}

export default SidebarChannel
