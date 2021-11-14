import { useState } from "react";
import { useDispatch } from "react-redux";
import { useHistory } from "react-router";
import { createServer } from "../../store/server";
import { updateUser } from "../../store/session";
import { getServerbyId } from "../../store/server";
import "./AddServerForm.css";

const ServerForm = ({ userId, showModal, setCurrentServerId }) => {
  const dispatch = useDispatch();
  const [name, setName] = useState("");
  const [description, setDescription] = useState("");
  


  const handleSubmit = async (e) => {
    e.preventDefault();
    const newServer = {
      ownerId: userId,
      name: name,
      description: description,
    };

    const createdServer = await dispatch(createServer(newServer));
    if (createdServer) {
      localStorage.setItem('currentServerId',createdServer.id)
      await dispatch(getServerbyId(localStorage.currentServerId))
      showModal(false)
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
        onChange={(e) => setName(e.target.value)}
      />
      <input
        id="descriptionInput"
        type="text"
        value={description}
        required
        placeholder="Server Description"
        onChange={(e) => setDescription(e.target.value)}
      />
      <button id="serverSubmit" type="submit">
        Create New Server
      </button>
      <button onClick={handleCancelClick}>Cancel</button>
    </form>
  );
};

export default ServerForm;
