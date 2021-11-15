import { useState } from "react";
import { useDispatch } from "react-redux";
// import { useHistory } from "react-router";
import { createChannel } from "../../store/channel";
// import { updateUser } from "../../store/session";
import {  getChannelbyId } from "../../store/channel";
import "./AddChannelForm.css";

const ChannelForm = ({ userId, showModal, }) => {
  const dispatch = useDispatch();
  const [name, setName] = useState("");
  const [topic, setTopic] = useState("");



  const handleSubmit = async (e) => {
    e.preventDefault();
    const newChannel = {
      name: name,
      topic: topic,
      server_id:localStorage.getItem('currentServerId')
    };

    const createdChannel = await dispatch(createChannel(newChannel))
    // .then
    // dispatch(getChannelbyId(localStorage.currentChannelId))
    // console.log(createChannel, 'createdChannel')
    if (createdChannel) {
      localStorage.setItem('currentChannelId', createdChannel.id)
      await dispatch(getChannelbyId(localStorage.currentChannelId))
      showModal(false)
    }
  };

  const handleCancelClick = (e) => {
    e.preventDefault();
    showModal(false);
  };
  return (
    <form id="channel-form" onSubmit={handleSubmit}>
      <input
        id="nameInput"
        type="text"
        value={name}
        required
        placeholder="Server Name"
        onChange={(e) => setName(e.target.value)}
      />
      <input
        id="topicInput"
        type="text"
        value={topic}
        required
        placeholder="Channel Topic"
        onChange={(e) => setTopic(e.target.value)}
      />
      <button id="serverSubmit" type="submit">
        Create New Channel
      </button>
      <button onClick={handleCancelClick}>Cancel</button>
    </form>
  );
};

export default ChannelForm;
