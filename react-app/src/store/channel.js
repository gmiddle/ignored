const LOAD = "channels/LOAD";
const LOAD_ONE = "channels/LOAD_ONE"
const ADD_ONE = "channels/ADD_ONE";
const DELETE_ONE = "channels/DELETE_ONE";

const load = (channels) => ({
    type: LOAD,
    payload: channels,
});

const loadOne = (channel) => ({
  type: LOAD_ONE,
  payload: channel
})

const removeChannel = (channel) => ({
  type: DELETE_ONE,
  payload: channel
})

const addOneChannel = (channel) => ({
  type: ADD_ONE,
  payload: channel,
});

export const getChannels = () => async (dispatch) => {
  const response = await fetch('api/channels/')
  if (response.ok) {
    const allChannelsList = await response.json();
    console.log(allChannelsList, 'allChannelList')
    dispatch(load(allChannelsList));
  }
}

export const getChannelbyId = (id) => async (dispatch) => {
  const response = await fetch(`/api/channels/${id}`);
  if (response.ok) {
    const channel = await response.json();

    dispatch(loadOne(channel));
  }
};

export const createChannel = (payload) => async (dispatch) => {
  console.log(JSON.stringify(payload))
  const response = await fetch(`/api/channels/server/${payload.server_id}/new`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  });
  if (response.ok) {
    const newChannel = await response.json();
    dispatch(addOneChannel(newChannel));
    return newChannel;
  }
};

export const deleteChannel = (id) => async (dispatch) => {
  const response = await fetch(`/api/channels/delete/${id}`, {
    method: "DELETE",
  });

  if (response.ok) {
    const deletedChannel = await response.json();
    dispatch(removeChannel(deletedChannel))
    return deletedChannel;
  }
};

export const editChannel = (updatedChannel) => async (dispatch) => {

  const channel_id = updatedChannel.id;
  const response = await fetch(`/api/channels/edit/${channel_id}`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(updatedChannel),
  });
  if (response.ok) {
    const newChannel = await response.json();
    dispatch(addOneChannel(newChannel));
    return newChannel
  }
};

const initialState = {};

const ChannelsReducer = (state = initialState, action) => {
  let newState;
  let newChannel;
  switch (action.type) {
    case LOAD: {
      return {
        ...state,
        allChannels:action.payload
      }
    }
    case LOAD_ONE: {
      return  {
        ...state,
        currentChannel:action.payload
      }
    }
    case ADD_ONE: {
      newState = Object.assign({}, state)
      newState.allChannels.channels.push(action.payload)
      console.log(newState, 'adding channel')
      return  newState
    }
    default:
      return state;
  }
};
export default ChannelsReducer;
