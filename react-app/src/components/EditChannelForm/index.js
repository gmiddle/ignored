import { Modal } from "../../context/Modal";
import React, { useState, useEffect } from "react";
import EditChannelForm from "./EditChannelForm"

function EditChannelModal({userId, setCurrentChannelId, channelToEdit}) {
  useEffect(() => {

  }, [])
  const [showModal, setShowModal] = useState(false);

  return (
    <div>
      <div className="channelEdit">
      <button onClick={() => setShowModal(true)}><i class="fas fa-edit" id="editChannel"></i></button>
      </div>
      {showModal && (
        <Modal onClose={() => setShowModal(false)}>
          <EditChannelForm
            setCurrentChannelId={setCurrentChannelId}
            showModal={setShowModal}
            userId={userId}
            channelToEdit={channelToEdit}
          />
        </Modal>
      )}

    </div>
  );
}

export default EditChannelModal;

{/* <i class="fas fa-plus" id="addChannel" ></i>  */}
