const LOAD = "Messages/LOAD";
const LOAD_ONE = "Messages/LOAD_ONE"
const ADD_ONE = "Messages/ADD_ONE";

const load = (Messages) => ({
    type: LOAD,
    payload: Messages,
});

const addOneMessage = (getMessages) => ({
  type: ADD_ONE,
  getMessages,
});

export const getMessages = () => async (dispatch) => {
  const response = await fetch('api/messages/')
  if (response.ok) {
    const allMessagesList = await response.json();
    dispatch(load(allMessagesList));
  }
}

export const getMessagebyId = (id) => async (dispatch) => {
  const response = await fetch(`/api/messages/${id}`);
  if (response.ok) {
    const allMessagesList = await response.json();
    dispatch(load(allMessagesList));
  }
};

export const createMessage = (payload) => async (dispatch) => {
  const response = await fetch(`/api/messages/channel/${payload.channel_id}/new`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  });
  if (response.ok) {
    const newMessage = await response.json();
    dispatch(addOneMessage(newMessage));
    return newMessage;
  }
};

export const deleteMessage = (id) => async (dispatch) => {
  const response = await fetch(`/api/messages/delete/${id}`, {
    method: "DELETE",
  });

  if (response.ok) {
    const deletedMessage = await response.json();
    return deletedMessage;
  }
};

export const editMessage = (updatedMessage) => async (dispatch) => {

  const message_id = updatedMessage.id;
  const response = await fetch(`/api/messages/edit/${message_id}`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(updatedMessage),
  });
  if (response.ok) {
    const newMessage = await response.json();
    dispatch(addOneMessage(newMessage));
    return newMessage
  }
};

const initialState = {};

const MessagesReducer = (state = initialState, action) => {
  let newState;
  let newMessage;
  switch (action.type) {
    case LOAD: {
      newState = Object.assign({}, state);
    }
    case LOAD_ONE: {
    }
    default:
      return state;
  }
};
export default MessagesReducer;
