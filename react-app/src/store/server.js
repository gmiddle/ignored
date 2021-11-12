
const LOAD = "servers/LOAD";
const LOAD_ONE = "servers/LOAD_ONE"
const ADD_ONE = "servers/ADD_ONE";

const load = (servers) => ({
    type: LOAD,
    payload: servers,
});

const addOneServer = (server) => ({
  type: ADD_ONE,
  server,
});

export const getServers = () => async (dispatch) => {
  const response = await fetch('api/servers/')
  if (response.ok) {
    const allServersList = await response.json();
    console.log(allServersList, 'allServerList')
    dispatch(load(allServersList));
  }
}

export const getServerbyId = (id) => async (dispatch) => {
  const response = await fetch(`/api/servers/${id}`);
  if (response.ok) {
    const allServersList = await response.json();

    dispatch(load(allServersList));
  }
};

export const createServer = (payload) => async (dispatch) => {
  const response = await fetch(`/api/servers/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  });
  console.log(response, '----------------------')
  if (response.ok) {
    const newServer = await response.json();
    console.log(newServer, 'uiopsjDfhjikolSdfHKJASDFG')
    dispatch(addOneServer(newServer));
    return newServer;
  }
};

export const deleteServer = (id) => async (dispatch) => {
  const response = await fetch(`/api/servers/delete/${id}`, {
    method: "DELETE",
  });

  if (response.ok) {
    const deletedServer = await response.json();
    return deletedServer;
  }
};

export const editServer = (updatedServer) => async (dispatch) => {

  const server_id = updatedServer.id;
  const response = await fetch(`/api/servers/edit/${server_id}`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(updatedServer),
  });
  if (response.ok) {
    const newServer = await response.json();
    dispatch(addOneServer(newServer));
    return newServer
  }
};

const initialState = {};

const serversReducer = (state = initialState, action) => {
  let newState;
  let newServer;
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
export default serversReducer;
