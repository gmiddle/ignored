
const LOAD = "servers/LOAD";
const LOAD_ONE = "servers/LOAD_ONE"
const ADD_ONE = "servers/ADD_ONE";
const REMOVE_ONE = "servers/REMOVE_ONE"

const load = (servers) => ({
  type: LOAD,
  payload: servers,
});

const removeOneServer = (deletedServer) => ({
  type: REMOVE_ONE,
  deletedServer
});

const addOneServer = (server) => ({
  type: ADD_ONE,
  payload: server,
});

const loadOne = (server) => ({
  type: LOAD_ONE,
  payload: server,
});

export const getServers = () => async (dispatch) => {
  const response = await fetch('api/servers/')
  if (response.ok) {
    const allServersList = await response.json();
    dispatch(load(allServersList));
  }
}

export const getServerbyId = (id) => async (dispatch) => {
  const response = await fetch(`/api/servers/${id}`);
  if (response.ok) {
    const server = await response.json();

    dispatch(loadOne(server));
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

  if (response.ok) {
    const newServer = await response.json();
    console.log(newServer, 'stoernererwer')
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
    dispatch(removeOneServer(deletedServer))
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
      return {
        ...state,
        allServers:action.payload
      }
    }
    case LOAD_ONE: {
      return  {
        ...state,
        currentServer:action.payload
      }
    }
    case ADD_ONE: {
      newState = Object.assign({}, state)
      newState.allServers.servers.push(action.payload)
      return  newState
    }
    case REMOVE_ONE: {
      newState=Object.assign({}, state)
      const res = newState.allServers.servers.filter(
        (server) => server.id !== action.deletedServer.id
      );
      return {allServers:{servers:res}}
      };
    default:
      return state;
  }
};
export default serversReducer;
