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
        const { exercisedata } = this.props;
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
                    <Componentindex>EX_ID</Componentindex>
                    <Componentinput ref={(input) => { this.ex_ID = input }} />
                </ComponentoptionWapper>
                <ComponentoptionWapper>
                    <Componentindex>EX_Name</Componentindex>
                    <Componentinput ref={(input) => { this.ex_name = input }} />
                </ComponentoptionWapper>
                <ComponentoptionWapper>
                    <Componentindex>Type</Componentindex>
                    <Componentinput ref={(input) => { this.types = input }} />
                </ComponentoptionWapper>
                <ComponentoptionWapper>
                    <Componentindex>Time_Slot</Componentindex>
                    <Componentinput ref={(input) => { this.time_slot = input }} />
                </ComponentoptionWapper>
                <ComponentoptionWapper>
                    <Componentindex>Frequency</Componentindex>
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
                <ComponentWapper>
                    <ComponentoptionWapper>
                        <Componentindex>EX_Name</Componentindex>
                        <Componentindex>Type</Componentindex>
                        <Componentindex>Time_Slot</Componentindex>
                        <Componentindex>Frequency</Componentindex>
                    </ComponentoptionWapper>
                    {type === 2 && exercisedata && exercisedata.length > 0 && exercisedata.map((item, index) => (
                        <ComponentoptionWapper key={index}>
                            <Componentindex>{item.EX_Name}</Componentindex>
                            <Componentindex>{item.Type}</Componentindex>
                            <Componentindex>{item.Time_Slot}</Componentindex>
                            <Componentindex>{item.Frequency}</Componentindex>
                        </ComponentoptionWapper>
                    ))}
                </ComponentWapper>
            </ComponentWapper>
        )
    }
}

const mapStateToProps = (state) => ({
    exercisedata: state.main.exercisedata
})

const mapDisptchToProps = (dispatch) => {
    return {
        exercisesendinfo(type, ex_ID, ex_name, types, time_slot, frequency) {
            dispatch(actionCreators.exercisesendinfo(type, ex_ID.value, ex_name.value, types.value, time_slot.value, frequency.value));
        }
    }
}

export default connect(mapStateToProps, mapDisptchToProps)(Exercises);