import { useState } from "react";
import { useDispatch } from "react-redux";
import { useHistory } from "react-router";
import { createServer } from "../../store/server";
import "./AddServerForm.css";

const ServerForm = ({ userId, showModal }) => {
  const dispatch = useDispatch();
  const history = useHistory();
  const [name, setName] = useState("");
  const [description, setDescription] = useState("");
  const [user_id] = useState(userId);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const newServer = {
      ownerId: user_id,
      name: name,
      description: description,
    };

    const createdServer = dispatch(createServer(newServer));
    if (createdServer) {
      history.push(`/dashboard/`);
    }
  };

  const handleCancelClick = (e) => {
    e.preventDefault();
    showModal(false);
  };
  return (
    <form id="server-form" onSubmit={handleSubmit}>
      <input
        id="nameInput"
        type="text"
        value={name}
        required
        placeholder="Server Name"
        onChange={setName}
      />
      <input
        id="descriptionInput"
        type="text"
        value={description}
        required
        placeholder="Server Description"
        onChange={setDescription}
      />
      <button id="serverSubmit" type="submit">
        Create New Server
      </button>
      <button onClick={handleCancelClick}>Cancel</button>
    </form>
  );
};

export default ServerForm;
