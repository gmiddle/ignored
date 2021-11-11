const LOAD = "users/LOAD";


const load = (users) => ({
    type: LOAD,
    payload: users,
});

export const getUsers = () => async (dispatch) => {
    const response = await fetch('api/users/')
    if (response.ok) {
      const allUsersList = await response.json();
      console.log(allUsersList, 'allUserList')
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
          list:action.list,
        };
    }
    default:
      return state;
  }
};

export default usersReducer;