import { Modal } from "../../context/Modal";
import React, { useState, useEffect } from "react";
import EditServerForm from "./EditServerForm"

function EditServerModal({userId, setCurrentServerId, serverToEdit}) {
  useEffect(() => {

  }, [])
  const [showModal, setShowModal] = useState(false);
  
  return (
    <div>
      <button onClick={() => setShowModal(true)}>Edit</button>
      {showModal && (
        <Modal onClose={() => setShowModal(false)}>
          <EditServerForm
            setCurrentServerId={setCurrentServerId}
            showModal={setShowModal}
            userId={userId}
            serverToEdit={serverToEdit} 
          />
        </Modal>
      )}
      
    </div>
  );
}

export default EditServerModal;

{/* <i class="fas fa-plus" id="addChannel" ></i>  */}