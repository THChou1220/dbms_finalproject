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

class Do extends PureComponent {
    state = {
        hoveredBox: null,
        type: null,
        pages: [
            { id: 1, text: 'creat' },
            { id: 2, text: 'read' },
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
        const { dodata } = this.props;
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
                    <Componentindex>Member_ID</Componentindex>
                    <Componentinput ref={(input) => { this.member_ID = input }} />
                </ComponentoptionWapper>
                <ComponentoptionWapper>
                    <Componentindex>Exercise_ID</Componentindex>
                    <Componentinput ref={(input) => { this.exercise_ID = input }} />
                </ComponentoptionWapper>
                <Componentbutton onClick={() => this.props.dosendinfo(
                    type,
                    this.member_ID,
                    this.exercise_ID,
                )}>comfirm</Componentbutton>
                <ComponentWapper>
                    <ComponentoptionWapper>
                        <Componentindex>Member_ID</Componentindex>
                        <Componentindex>Exercise_ID</Componentindex>
                    </ComponentoptionWapper>
                    {type === 2 && dodata && dodata.length > 0 && dodata.map((item, index) => (
                        <ComponentoptionWapper key={index}>
                            <Componentindex>{item.Member_ID}</Componentindex>
                            <Componentindex>{item.Exercise_ID}</Componentindex>
                        </ComponentoptionWapper>
                    ))}
                </ComponentWapper>
            </ComponentWapper>
        )
    }
}

const mapStateToProps = (state) => ({
    dodata: state.main.dodata
})

const mapDisptchToProps = (dispatch) => {
    return {
        dosendinfo(type, member_ID, exercise_ID) {
            dispatch(actionCreators.dosendinfo(type, member_ID.value, exercise_ID.value));
        }
    }
}

export default connect(mapStateToProps, mapDisptchToProps)(Do);