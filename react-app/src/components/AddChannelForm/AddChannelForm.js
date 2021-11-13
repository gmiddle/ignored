import { useState } from "react";
import { useDispatch } from "react-redux";
import { useHistory } from "react-router";
import { createChannel } from "../../store/channel";
import { updateUser } from "../../store/session";
import "./AddChannelForm.css";

const ChannelForm = ({ userId, showModal, setCurrentChannelId }) => {
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

    const createdChannel = await dispatch(createChannel(newChannel));
    if (createdChannel) {
      dispatch(updateUser(userId))
      setCurrentChannelId(createdChannel.id)
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
