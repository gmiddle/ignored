import { useState } from "react";
import { useDispatch } from "react-redux";
import { updateUser } from "../../store/session";
import { editMessage } from "../../store/message";

import "./EditMessageForm.css";

const EditMessageForm = ({ userId, showModal,messageToEdit }) => {
  const dispatch = useDispatch();

  const [content, setContent] = useState(messageToEdit.content);
  const [user_id] = useState(userId);


  const handleSubmit = async (e) => {
    e.preventDefault();
    messageToEdit.content = content


    let editedMessage = await dispatch(editMessage(messageToEdit));

    if (editedMessage) {
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
        id="ContentInput"
        type="text"
        value={content}
        required
        placeholder="Message"
        onChange={(e) => setContent(e.target.value)}
      />
      <button id="channelSubmit" type="submit">Submit Change</button>
      <button onClick={handleCancelClick}>Cancel</button>
    </form>
  );
};

export default EditMessageForm;
