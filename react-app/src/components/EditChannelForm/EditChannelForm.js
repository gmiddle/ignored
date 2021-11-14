import { useState } from "react";
import { useDispatch } from "react-redux";
import { editChannel } from "../../store/channel";
import { updateUser } from "../../store/session";
import "./EditChannelForm.css";

const EditChannelForm = ({ userId, showModal, setCurrentChannelId, channelToEdit }) => {
  const dispatch = useDispatch();
  const [name, setName] = useState(channelToEdit.name);
  const [topic, setTopic] = useState(channelToEdit.topic);



  const handleSubmit = async (e) => {
    e.preventDefault();
    channelToEdit.name = name
    channelToEdit.topic = topic

    let editedChannel = await dispatch(editChannel(channelToEdit));
    if (editedChannel) {
      await dispatch(updateUser(userId))
      setCurrentChannelId(editedChannel.id)
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
      <button id="channelSubmit" type="submit">Submit Change</button>
      <button id="channelCancel" onClick={handleCancelClick}>Cancel</button>
    </form>
  );
};

export default EditChannelForm;
