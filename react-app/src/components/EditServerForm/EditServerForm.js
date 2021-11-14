import { useState } from "react";
import { useDispatch } from "react-redux";
// import { useHistory } from "react-router";
import { editServer, getServers } from "../../store/server";
// import { updateUser } from "../../store/session";
import "./EditServerForm.css";

const EditServerForm = ({ userId, showModal, serverToEdit }) => {
  const dispatch = useDispatch();
  // const history = useHistory();
  const [name, setName] = useState(serverToEdit.name);
  const [description, setDescription] = useState(serverToEdit.description);
  const [user_id] = useState(userId);


  const handleSubmit = async (e) => {
    e.preventDefault();
    serverToEdit.name = name
    serverToEdit.description = description

    let editedServer = await dispatch(editServer(serverToEdit));
    if (editedServer) {
      await dispatch(getServers())
      localStorage.setItem('currentServerId', editedServer.id)
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
      <button id="serverSubmit" type="submit">Submit Change</button>
      <button id="serverCancel"onClick={handleCancelClick}>Cancel</button>
    </form>
  );
};

export default EditServerForm;
