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
  const response = await fetch(`/api/channels/server/${payload.server_id}/new`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  });
  if (response.ok) {
    // console.log('asdasdafgsdgadfgh')
    const newChannel = await response.json();
    // console.log(newChannel,'storerchane')
    dispatch(addOneChannel(newChannel));
    return newChannel;
  }
};

export const deleteChannel = (id) => async (dispatch) => {
  const response = await fetch(`/api/channels/delete/${id}`, {
    method: "DELETE",
  });
  // console.log('here', id)
  if (response.ok) {
    // console.log('ok')
    const deletedChannel = await response.json();
    // console.log('ok')

    // console.log(deleteChannel,'dedededed')
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
  // let newChannel;
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
      // console.log(newState, 'addingl')
      // newState.allChannels.channels[action.payload.id] = action.payload 
      newState.allChannels.channels.push(action.payload)
      // console.log(newState, 'adding channel') 
      // console.log(newState, "newState")
      return  newState
    }
    case DELETE_ONE: {
      newState=Object.assign({}, state)
      const res = newState.allChannels.channels.filter(
        (channel) => channel.id !== action.payload.id
      );
      return {allChannels:{channels:res}}
    };
    default:
      return state;
  }
};
export default ChannelsReducer;
