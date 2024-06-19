import { combineReducers } from 'redux';
import { reducer as mainReducer } from '../main/store';

const reducer = combineReducers({
  main: mainReducer
})

export default reducer;