import React, { PureComponent } from 'react';
import { connect } from 'react-redux';
import { actionCreators } from '../store';
import {
    ComponentWapper,
    Componentindex,
    Componentinput,
    Componentbutton,
    ComponentoptionWapper,
    Categoryoption
} from '../style';

class Consist extends PureComponent {
    state = {
        hoveredBox: null,
        type: null,
        pages: [
            { id: 1, text: 'creat' },
            { id: 2, text: 'read' },
            { id: 3, text: 'update' },
            { id: 4, text: 'delete' }
        ]
    };

    handleMouseEnter = (index) => {
        this.setState({ hoveredBox: index });
    };

    handleMouseLeave = () => {
        this.setState({ hoveredBox: null });
    };

    setcategorypage = (id) => {
        this.setState({ type: id })
    }

    render() {
        const { hoveredBox, pages, type } = this.state;
        return (
            <ComponentWapper>
                <ComponentoptionWapper>
                    {pages.map(({ id, text }) => (
                        <Categoryoption
                            key={id}
                            onClick={() => this.setcategorypage(id)}
                            onMouseEnter={() => this.handleMouseEnter(id)}
                            onMouseLeave={this.handleMouseLeave}
                            className={type === id || hoveredBox === id ? 'mousein' : ''}
                        >
                            {text}
                        </Categoryoption>
                    ))}</ComponentoptionWapper>
                <ComponentoptionWapper>
                    <Componentindex>sub pack</Componentindex>
                    <Componentinput ref={(input) => { this.sub_pack = input }} />
                </ComponentoptionWapper>
                <ComponentoptionWapper>
                    <Componentindex>exercise ID</Componentindex>
                    <Componentinput ref={(input) => { this.exercise_ID = input }} />
                </ComponentoptionWapper>
                <Componentbutton onClick={() => this.props.consistsendinfo(
                    type,
                    this.sub_pack,
                    this.exercise_ID,
                )}>comfirm</Componentbutton>
            </ComponentWapper>
        )
    }
}

const mapStateToProps = (state) => ({

})

const mapDisptchToProps = (dispatch) => {
    return {
        consistsendinfo(type, sub_pack, exercise_ID) {
            dispatch(actionCreators.consistsendinfo(type, sub_pack.value, exercise_ID.value));
        }
    }
}

export default connect(mapStateToProps, mapDisptchToProps)(Consist);