import { Modal } from "../../context/Modal";
import React, { useState, useEffect } from "react";
import ServerForm from "./AddServerForm"

function AddServerModal({userId, setCurrentServerId}) {
  useEffect(() => {

  }, [])
  const [showModal, setShowModal] = useState(false);
  
  return (
    <div>
      <button onClick={() => setShowModal(true)}><i className="fas fa-plus" id="addServer"></i></button>
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
