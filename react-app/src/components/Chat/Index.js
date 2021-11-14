import React, {useEffect,useState} from 'react'
import './Chat.css'
import Messages from '../Messages/Index'
import ChatHeader from '../ChatHeader/Index'
import { useSelector, useDispatch } from "react-redux";
import { createMessage, deleteMessage, getMessages } from '../../store/message';  //removed getMessagebyId
import  { Redirect } from 'react-router-dom'
// import { getUsers } from '../../store/users';
// import the socket
import { io } from 'socket.io-client';
import EditMessageModal from '../EditMessageForm/index'
// import {updateUser} from '../../store/session'
// outside of your component, initialize the socket variable
let socket;

const Chat = () => {  // old props: { currUser, currentChannelId,messageToEdit}
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.6.3/css/all.css" integrity="sha384-UHRtZLI+pbxtHCWp1t77Bi1L4ZtiqrqD80Kn4Z8NTSRyMA2Fd33n5dQ8lWUE00s/" crossOrigin="anonymous" />

    // const {serverList} = useSelector((state) => state.session.user)

    const {existingMessages} = useSelector((state) => state.messages)
    // const [currentServer, setCurrentServer] = useState()
    // const [channelList, setChannelList] = useState()
    const currentChannel = useSelector((state) => state.channels.currentChannel)


    const [messages, setMessages] = useState([])
    const [chatInput, updateChatInput] = useState("");
    const combinedMessages = new Set(existingMessages, messages)
    console.log(combinedMessages)
    const user = useSelector(state => state.session.user)

    const dispatch = useDispatch();

    useEffect(()=> {

    },[currentChannel])

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
    }, [existingMessages])

    const sendChat = async (e) => {
        e.preventDefault()

        const newMessage = {
            content: chatInput,
            user_id: user.id,
            channel_id: localStorage.currentChannelId,
        }

        const uploadedMessage = await dispatch(createMessage(newMessage))
        // emit a message
        socket.emit("chat", {id:uploadedMessage.id, user_id: user.id, content: chatInput });
        // clear the input field after the message is sent

        updateChatInput("")
    }

    // const deleteChat = async (e) => {
    //     e.preventDefault()
    //     const existingMessage = await dispatch(getMessagebyId(e.target.value))
    //     const uploadedMessage = await dispatch(deleteMessage(existingMessage.id))
    //     // emit a message
    //     socket.emit("delete", {id:existingMessage.id, user_id: user.id, content: chatInput });
    //     // clear the input field after the message is sent
    // }


    const onChange = (event) => {
        updateChatInput(event.target.value);
      };

    //  delete message
    const deleteMessages = async (e) => {
        await dispatch(deleteMessage(e.target.value))
        // await dispatch(getMessages(localStorage.currentChannelId));
    }


    const displayMessages= Array.from(combinedMessages)
    useEffect( async () => {
      await dispatch(getMessages(localStorage.currentChannelId))
      console.log('hit-----------------------------', currentChannel)
    }, [currentChannel])
   return existingMessages? (

        <div className='chat'>
            <ChatHeader />
            <div className='chatMessages'>
                {displayMessages && displayMessages.map((message) => (
                    <div className="messageCard">
                    <Messages message={message} />
                    {message.user_id === user.id && <EditMessageModal messageToEdit={message} />}
                    {message.user_id === user.id && <button value={message.id} onClick={deleteMessages}>Delete</button>}
                    </div>
                ))}
           <div>
                </div>
            </div>

                <div className='chatArea'>
                    <form onSubmit={sendChat}>
                        <input type='text' placeholder={"send a message"} value={chatInput} onChange={onChange} />
                        <button type='submit'className="chatSubmitBtn">
                        </button>
                    </form>
                </div>
        </div>
    ): (<div>
        <Redirect to='/dashboard' />

      </div>)
}

export default Chat
