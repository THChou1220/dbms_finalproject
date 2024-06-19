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

class Exercises extends PureComponent {
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
                    <Componentindex>ex ID</Componentindex>
                    <Componentinput ref={(input) => { this.ex_ID = input }} />
                </ComponentoptionWapper>
                <ComponentoptionWapper>
                    <Componentindex>ex name</Componentindex>
                    <Componentinput ref={(input) => { this.ex_name = input }} />
                </ComponentoptionWapper>
                <ComponentoptionWapper>
                    <Componentindex>type</Componentindex>
                    <Componentinput ref={(input) => { this.types = input }} />
                </ComponentoptionWapper>
                <ComponentoptionWapper>
                    <Componentindex>time slot</Componentindex>
                    <Componentinput ref={(input) => { this.time_slot = input }} />
                </ComponentoptionWapper>
                <ComponentoptionWapper>
                    <Componentindex>frequency</Componentindex>
                    <Componentinput ref={(input) => { this.frequency = input }} />
                </ComponentoptionWapper>
                <Componentbutton onClick={() => this.props.exercisesendinfo(
                    type,
                    this.ex_ID,
                    this.ex_name,
                    this.types,
                    this.time_slot,
                    this.frequency
                )}>comfirm</Componentbutton>
            </ComponentWapper>
        )
    }
}

const mapStateToProps = (state) => ({

})

const mapDisptchToProps = (dispatch) => {
    return {
        exercisesendinfo(type, ex_ID, ex_name, types, time_slot, frequency) {
            dispatch(actionCreators.exercisesendinfo(type, ex_ID.value, ex_name.value, types.value, time_slot.value, frequency.value));
        }
    }
}

export default connect(mapStateToProps, mapDisptchToProps)(Exercises);