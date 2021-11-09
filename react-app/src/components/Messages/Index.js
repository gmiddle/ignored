import React from 'react'
import './Messages.css'




const Messages = () => {


    return (
        <div className='messages'>
            {/* maybe an avatar? */}
            <div className="messageInfo">
                <h4>{/* {UserName} */}
                UserName
                <span className='timeStamp'>
                Time Stamp
                </span>
                </h4>
                <div className="actualMessage">
                    Actual Message
                     {/* {generate messages} */}
                    </div>

            </div>
        </div>
    )
}

export default Messages
