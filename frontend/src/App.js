import { Component } from 'react'
import store from './store';
import { Provider } from 'react-redux';
import { BrowserRouter, Route, Routes } from 'react-router-dom';

import Main from './main';


class App extends Component {
  render() {
    return (
      <Provider store={store}>
        <BrowserRouter>
          <Routes>
            <Route path='/' element={<Main />}></Route>
          </Routes>
        </BrowserRouter>
      </Provider >
    )
  }
}

export default App;