const LOAD = "Messages/LOAD";
const LOAD_ONE = "Messages/LOAD_ONE"
const ADD_ONE = "Messages/ADD_ONE";
const EDIT_MESSAGE = "Messages/EDIT_MESSAGE"
const REMOVE_ONE = "Messages/REMOVE_ONE"

const load = (Channel) => ({
    type: LOAD,
    payload: Channel,
});

const removeOneMessage = (deletedMessage) => ({
  type: REMOVE_ONE,
  deletedMessage
});

const addOneMessage = (message) => ({
  type: ADD_ONE,
  message,
});

const changeMessage = (message) => ({
  type: EDIT_MESSAGE,
  message,
});

export const getMessages = (channel_id) => async (dispatch) => {
  const response = await fetch(`api/channels/${channel_id}`);
  if (response.ok) {
    const allMessagesList = await response.json();
    dispatch(load(allMessagesList));
  }
}

export const getMessagebyId = (id) => async (dispatch) => {
  const response = await fetch(`/api/messages/${id}`);
  if (response.ok) {
    const allMessagesList = await response.json();
    return allMessagesList
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
    dispatch(removeOneMessage(deletedMessage));
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
    dispatch(changeMessage(newMessage));
    return newMessage
  }
};

const initialState = {};

const MessagesReducer = (state = initialState, action) => {
  let newState;
  let newMessage;
  switch (action.type) {
    case LOAD: {
      return {
        ...state,
        existingMessages: action.payload.messages,
      };
    }
    case ADD_ONE: {
      newState = newState=Object.assign({}, state)
      console.log("newState===========>",newState)
      newState['existingMessages'].push(action.message)
      return newState
    }
    case LOAD_ONE: {
    }
    case REMOVE_ONE: {
      newState=Object.assign({}, state)

      const res = newState['existingMessages'].filter(
        (message) => message.id !== action.deletedMessage.id
      );
      return {existingMessages:res}
      };
    case EDIT_MESSAGE:{
      newState=Object.assign({}, state)

      const res = newState['existingMessages'].filter(
        (message) => message.id !== action.message.id
      );
      res.push(action.message)
      return {existingMessages:res}
      };

    default:
      return state;
  }
};
export default MessagesReducer;
