import * as constants from './constants';

const defaultState = {
    categorypage: 1
};

const reducer = (state = defaultState, action) => {
    switch (action.type) {
        case constants.SET_CATEGORY_PAGE:
            return{...state,categorypage:action.page}
        default:
            return state;
    };
}

export default reducer;
