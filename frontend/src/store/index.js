import { configureStore, compose } from '@reduxjs/toolkit'
import reducer from './reducer'

const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;
const store = configureStore({reducer,composeEnhancers});

export default store;