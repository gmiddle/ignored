import React from 'react'
import './Chat.css'
import ChatHeader from '../ChatHeader/Index'

const Chat = () => {
    return (
        <div className='chat'>
            <ChatHeader />
            <div className='chatMessages'>
                </div>

                <div className='chatArea'>
                    <form>
                        <input type='text' placeholder={`Message #ChannelName `} />
                        <button type='submit'className="chatSubmitBtn">
                            Send Message
                        </button>
                        </form>

                </div>
        </div>
    )
}

export default Chat
