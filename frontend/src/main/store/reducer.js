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
            return { ...state, categorypage: action.page }
        case constants.TRAINER_DATA:
            return { trainerdata: action.result }
        case constants.MEMBER_DATA:
            return { memberdata: action.result }
        case constants.SUBSCRIPTION_DATA:
            return { subscriptiondata: action.result }
        case constants.CONSIST_DATA:
            return { consistdata: action.result }
        case constants.EQUIPMENT_DATA:
            return { equipmentdata: action.result }
        case constants.USE_DATA:
            return { usedata: action.result }
        case constants.EXERCISE_DATA:
            return { exercisedata: action.result }
        case constants.DO_DATA:
            return { dodata: action.result }
        default:
            return state;
    };
}

export default reducer;
