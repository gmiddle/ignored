import { Modal } from "../../context/Modal";
import React, { useState } from "react";
import ServerForm from "./AddServerForm"

function AddServerModal({userId, setCurrentServerId}) {
  
  const [showModal, setShowModal] = useState(false);
  
  return (
    <div>
      <button onClick={() => setShowModal(true)}>butto</button>
      {showModal && (
        <Modal onClose={() => setShowModal(false)}>
          <ServerForm
            setCurrentServerId={setCurrentServerId}
            showModal={setShowModal}
            userId={userId}
            />
        </Modal>
      )}
    </div>
  );
}

export default AddServerModal;

{/* <i class="fas fa-plus" id="addChannel" ></i>  */}
