import React from 'react'
import './Messages.css'
const Messages = () => {


    return (
        <div className='messages'>
            <div className="messageInfo">
                <h4>{/* {UserName} */}
                UserName
                <span className='timeStamp'>
                Time Stamp
                </span>
                </h4>
                <p>ACTUAL MESSAGE</p>
                {/* {generate messages} */}
            </div>
        </div>
    )
}

export default Messages
