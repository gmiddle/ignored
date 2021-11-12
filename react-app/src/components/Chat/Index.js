import React from 'react'
import './Chat.css'
import Messages from '../Messages/Index'
import ChatHeader from '../ChatHeader/Index'
import { useSelector, useDispatch } from "react-redux";
// import { getUsers } from '../../store/users';


const Chat = ({ currentServerId, setCurrentServerId, currentChannelId, setCurrentChannelId, currUser}) => {
    const {serverList} = useSelector((state) => state.session.user)
    const currentServer = serverList.find(server=>`${server.id}` === localStorage.currentServerId)
    const channelList = currentServer ? currentServer.channels : []
    const currentChannel = channelList.find(channel=>`${channel.id}` === localStorage.currentChannelId)
    const dispatch = useDispatch();

    return (
        <div className='chat'>
            <ChatHeader />
            <div className='chatMessages'>
                {currentChannel && currentChannel.messages.map((message) => (
                    <Messages message={message} />

                ))}

            </div>

                <div className='chatArea'>
                    <form>
                        <input type='text' placeholder={currentChannel.name}  />
                        <button type='submit'className="chatSubmitBtn">
                            Send Message
                        </button>
                    </form>

                </div>
        </div>
    )
}

export default Chat
