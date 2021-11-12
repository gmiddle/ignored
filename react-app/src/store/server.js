const LOAD = "servers/LOAD";
const LOAD_ONE = "servers/LOAD_ONE"
const ADD_ONE = "servers/ADD_ONE";

const load = (server) => ({
    type: LOAD,
    server,
  });

  const addOneServer = (server) => ({
    type: ADD_ONE,
    server,
  });

  export const getServers = (id) => async (dispatch) => {
    const response = await fetch(`/api/servers/${id}`);
    if (response.ok) {
      const allServersList = await response.json();

      dispatch(load(allServersList));
    }
  };

  export const createServer = (newServer) => async (dispatch) => {
    const response = await fetch(`/api/servers/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(newServer),
    });

    if (response.ok) {
      const newServer = await response.json();
      dispatch(addOneServer(newServer));
      return newServer;
    }
  };

  export const deleteServer = (id) => async (dispatch) => {
    let deleteId = id.serverId;
    const response = await fetch(`/api/servers/${deleteId}`, {
      method: "DELETE",
    });

    if (response.ok) {
      const deletedServer = await response.json();
      return deletedServer;
    }
  };

  export const editComment = ({updatedServer}) => async (dispatch) => {

    const server_id = updatedServer.server_id;
    const response = await fetch(`/api/comments/${server_id}`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(response),
    });
    if (response.ok) {
      const newServer = await response.json();
      dispatch(addOneServer(newServer));
      return newServer
    }
  };

  const initialState = {
    comments: [],
  };

  const serversReducer = (state = initialState, action) => {
    switch (action.type) {
      case LOAD: {
        return {
          ...state,
        };
      }

      default:
        return state;
    }
  };
  export default serversReducer;
