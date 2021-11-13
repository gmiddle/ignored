const LOAD = "channels/LOAD";
const LOAD_ONE = "channels/LOAD_ONE"
const ADD_ONE = "channels/ADD_ONE";

const load = (channels) => ({
    type: LOAD,
    payload: channels,
});

const addOneChannel = (channel) => ({
  type: ADD_ONE,
  channel,
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
    const allChannelsList = await response.json();

    dispatch(load(allChannelsList));
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

const channelsReducer = (state = initialState, action) => {
  let newState;
  let newChannel;
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
export default channelsReducer;
