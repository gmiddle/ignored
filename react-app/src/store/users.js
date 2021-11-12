const LOAD = "users/LOAD";


const load = (users) => ({
    type: LOAD,
    payload: users,
});

export const getUsers = () => async (dispatch) => {
    const response = await fetch('api/users/')
    if (response.ok) {
      const allUsersList = await response.json();
      console.log('--------------store-users-allUsersList', allUsersList)
      dispatch(load(allUsersList));
    }
}

const initialState = {};

const usersReducer = (state = initialState, action) => {
  let newState;
  let newUser;
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