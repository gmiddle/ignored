import { Modal } from "../../context/Modal";
import React, { useState, useEffect } from "react";
import EditMessageForm from "./EditMessageForm";

function EditMessageModal({userId,  messageToEdit}) {
  useEffect(() => {

  }, [])
  const [showModal, setShowModal] = useState(false);

  return (
    <div>
      <button onClick={() => setShowModal(true)}><i class="far fa-edit"></i></button>
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
