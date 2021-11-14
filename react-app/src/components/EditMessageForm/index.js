import { Modal } from "../../context/Modal";
import React, { useState, useEffect } from "react";
import EditMessageForm from "./EditMessageForm";
import "./EditMessageForm.css";

function EditMessageModal({userId,  messageToEdit}) {
  useEffect(() => {

  }, [])
  const [showModal, setShowModal] = useState(false);

  return (
    <div>
      <button onClick={() => setShowModal(true)}><i className="far fa-edit" id="messageEdit"></i></button>
      {showModal && (
        <Modal onClose={() => setShowModal(false)}>
          <EditMessageForm
            showModal={setShowModal}
            userId={userId}
            messageToEdit={messageToEdit}
          />
        </Modal>
      )}

    </div>
  );
}

export default EditMessageModal;
