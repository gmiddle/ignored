import { Modal } from "../../context/Modal";
import React, { useState, useEffect } from "react";
import ChannelForm from "./AddChannelForm"

function AddChannelModal({userId, setCurrentChannelId}) {
  useEffect(() => {

  }, [])
  const [showModal, setShowModal] = useState(false);

  return (
    <div>
      <button onClick={() => setShowModal(true)}><i className="fas fa-plus" id="addChannel"></i></button>
      {showModal && (
        <Modal onClose={() => setShowModal(false)}>
          <ChannelForm
            setCurrentChannelId={setCurrentChannelId}
            showModal={setShowModal}
            userId={userId}
            />
        </Modal>
      )}

    </div>
  );
}

export default AddChannelModal;
