const LOAD = "users/LOAD";


const load = (users) => ({
    type: LOAD,
    payload: users,
});

export const getUsers = () => async (dispatch) => {
    const response = await fetch('api/users/')
    if (response.ok) {
      const allUsersList = await response.json();
      dispatch(load(allUsersList));
    }
}

const initialState = {};

const usersReducer = (state = initialState, action) => {
  switch (action.type) {
    case LOAD: {
        return {
          ...state,
          list:action.payload.users,
        };
    }
    default:
      return state;
  }
};

export default usersReducer;
