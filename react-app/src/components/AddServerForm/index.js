import React, { useState } from "react";
import { useSelector } from "react-redux";
import { Modal } from "../../context/Modal";
import AddServerForm from "./AddServerForm";

function AddServerModal() {
  const [showModal, setShowModal] = useState(false);
  
  return (
    <>
      <button onClick={() => setShowModal(true)}>Edit Comment</button>
      {showModal && (
        <Modal onClose={() => setShowModal(false)}>
          <AddServerForm
            showModal={setShowModal}
            userId={userId}
          />
        </Modal>
      )}
    </>
  );
}

export default AddServerModal;
