import React from 'react'
import './Chat.css'
import Messages from '../Messages/Index'
import ChatHeader from '../ChatHeader/Index'

const Chat = () => {
    return (
        <div className='chat'>
            <ChatHeader />
            <div className='chatMessages'>
                {/* ADD MESSAGES */}
                <Messages />
                <Messages />
                <Messages />
                <Messages />
                <Messages />
                <Messages />
                <Messages />
                <Messages />
                <Messages />
                <Messages />
                <Messages />
                </div>

                <div className='chatArea'>
                    <form>
                        <input type='text' placeholder={`Message #ChannelName `}  />
                    {/* ADD CHANNEL NAME */}
                        <button type='submit'className="chatSubmitBtn">
                            Send Message
                        </button>
                        </form>

                </div>
        </div>
    )
}

export default Chat
