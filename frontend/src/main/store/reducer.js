import * as constants from './constants';

const defaultState = {
    categorypage: 1,
    trainerdata: [],
    memberdata: [],
    subscriptiondata: [],
    consistdata: [],
    equipmentdata: [],
    usedata: [],
    exercisedata: [],
    dodata: []
};

const reducer = (state = defaultState, action) => {
    switch (action.type) {
        case constants.SET_CATEGORY_PAGE:
            return { categorypage: action.page }
        case constants.TRAINER_DATA:
            return { ...state, trainerdata: action.result }
        case constants.MEMBER_DATA:
            return { ...state, memberdata: action.result }
        case constants.SUBSCRIPTION_DATA:
            return { ...state, subscriptiondata: action.result }
        case constants.CONSIST_DATA:
            return { ...state, consistdata: action.result }
        case constants.EQUIPMENT_DATA:
            return { ...state, equipmentdata: action.result }
        case constants.USE_DATA:
            return { ...state, usedata: action.result }
        case constants.EXERCISE_DATA:
            return { ...state, exercisedata: action.result }
        case constants.DO_DATA:
            return { ...state, dodata: action.result }
        default:
            return state;
    };
}

export default reducer;
