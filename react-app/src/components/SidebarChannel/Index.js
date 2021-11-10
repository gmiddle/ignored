import React from 'react'
import { useSelector} from 'react-redux'
import { useEffect } from 'react'
import './SidebarChannel.css'


const SidebarChannel = ({channelName}) => {




   

    return (
        <div className="sidebarChannel">
            <h4><span className='sidebarChannelHash'>#</span>  {channelName}  </h4>
        </div>
    )
}

export default SidebarChannel
