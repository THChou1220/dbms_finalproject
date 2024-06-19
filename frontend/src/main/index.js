import React, { Component } from "react";
import { connect } from "react-redux";
import { actionCreators } from './store';

import Trainers from './component/trainers';
import Members from './component/members'
import Subscrptions from './component/subscriptions'
import Consist from './component/consist'
import Equipments from "./component/equipments";
import Use from "./component/use";
import Exercises from './component/exercise'
import Do from './component/do'


//import { Link } from 'react-router-dom'
import {
  MainWapper,
  CategoryWapper,
  Categoryoption,
  ComponentWapper
} from './style';


class Main extends Component {
  state = {
    hoveredBox: null,
    pages: [
      { id: 1, text: 'Trainers' },
      { id: 2, text: 'Members' },
      { id: 3, text: 'Subscriptions' },
      { id: 4, text: 'Consist' },
      { id: 5, text: 'Equipments' },
      { id: 6, text: 'Use' },
      { id: 7, text: 'Exercises' },
      { id: 8, text: 'Do' }
    ]
  };

  handleMouseEnter = (index) => {
    this.setState({ hoveredBox: index });
  };

  handleMouseLeave = () => {
    this.setState({ hoveredBox: null });
  };

  whichpage(categorypage) {
    switch (categorypage) {
      case 2:
        return <Members />;
      case 3:
        return <Subscrptions />;
      case 4:
        return <Consist />;
      case 5:
        return <Equipments />;
      case 6:
        return <Use />;
      case 7:
        return <Exercises />;
      case 8:
        return <Do />;
      default:
        return <Trainers />;
    }
  }

  render() {
    const { setcategorypage, categorypage } = this.props;
    const { hoveredBox, pages } = this.state;
    return (
      <MainWapper>
        <CategoryWapper>
          {pages.map(({ id, text }) => (
            <Categoryoption
              key={id}
              onClick={() => setcategorypage(id)}
              onMouseEnter={() => this.handleMouseEnter(id)}
              onMouseLeave={this.handleMouseLeave}
              className={categorypage === id || hoveredBox === id ? 'mousein' : ''}
            >
              {text}
            </Categoryoption>
          ))}
        </CategoryWapper>
        <ComponentWapper>
          {this.whichpage(categorypage)}
        </ComponentWapper>
      </MainWapper>
    )
  }
}

const mapStateToProps = (state) => {
  return {
    categorypage: state.main.categorypage,
  }
}

const mapDisptchToProps = (dispatch) => {
  return {
    setcategorypage(page) {
      dispatch(actionCreators.setcategorypage(page));
    }
  }
}

export default connect(mapStateToProps, mapDisptchToProps)(Main);