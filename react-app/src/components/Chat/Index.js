import React from 'react'
import './Chat.css'
import Messages from '../Messages/Index'
import ChatHeader from '../ChatHeader/Index'
import { useSelector, useDispatch,useState,useEffect } from "react-redux";
import { useDispatch } from 'react';
// import { getUsers } from '../../store/users';
// import the socket
import { io } from 'socket.io-client';

// outside of your component, initialize the socket variable
let socket;

const Chat = ({ currentServerId, setCurrentServerId, currentChannelId, setCurrentChannelId, currUser}) => {
    const {serverList} = useSelector((state) => state.session.user)
    const currentServer = serverList.find(server=>`${server.id}` === localStorage.currentServerId)
    const channelList = currentServer ? currentServer.channels : []
    const currentChannel = channelList.find(channel=>`${channel.id}` === localStorage.currentChannelId)
    const [messages, setMessages] = useState([])
    const [chatInput, updateChatInput] = useState("");

    const user = useSelector(state => state.session.user)



    const dispatch = useDispatch();

    useEffect(() => {
        // create websocket
        socket = io();
        // listen for chat events
        socket.on("chat", (chat) => {
            // when we recieve a chat, add it into our messages array in state
            setMessages(messages => [...messages, chat])
        })
        // when component unmounts, disconnect
        return (() => {
            socket.disconnect()
        })
    }, [])

    const sendChat = (e) => {
        e.preventDefault()
        // emit a message
        socket.emit("chat", { user_id: user.id, content: chatInput });
        // clear the input field after the message is sent
        setChatInput("")
    }


    return (
        <div className='chat'>
            <ChatHeader />
            <div className='chatMessages'>
                {currentChannel && currentChannel.messages.map((message) => (
                    <Messages message={message} />
                ))}
            <div>
                {messages.map((message, ind) => (
                <Messages key={ind} message={message}/>
                ))}
                </div>
            </div>

                <div className='chatArea'>
                    <form onSubmit={sendChat}>
                        <input type='text' placeholder={"Send a Message"} value={chatInput} onChange={updateChatInput} />
                        <button type='submit'className="chatSubmitBtn">
                        </button>
                    </form>
                </div>
        </div>
    )
}

export default Chat
