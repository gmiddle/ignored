import React, { useEffect } from 'react'
import './Messages.css'
import { useSelector, useDispatch } from "react-redux";
import { getUsers } from '../../store/users';


const Messages = ({message, setCurrentChannelId}) => {
    const users = useSelector((state) => state.users.list)
    const user = users.find((user) => user.id === message.user_id)
    const dispatch = useDispatch();

    useEffect(() => {
        console.log("inside dispatch for messages---------")
        dispatch(getUsers())
    }, [setCurrentChannelId])

    console.log("---------this is the users that got dispatched here", users)

    return (
        <div className='messages'>
            {/* maybe an avatar? */}
            <div className="messageInfo">
                <h4>
                {user.name}
                <span className='timeStamp'>
                    {message.createdAt.toDateString()}
                </span>
                </h4>
                <div className="actualMessage">
                     {message.content}
                </div>
            </div>
        </div>
    )
}

export default Messages
