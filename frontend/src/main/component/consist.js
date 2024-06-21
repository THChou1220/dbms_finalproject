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
        const { consistdata } = this.props;
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
                    <Componentindex>Sub_Pack</Componentindex>
                    <Componentinput ref={(input) => { this.sub_pack = input }} />
                </ComponentoptionWapper>
                <ComponentoptionWapper>
                    <Componentindex>Exercise_ID</Componentindex>
                    <Componentinput ref={(input) => { this.exercise_ID = input }} />
                </ComponentoptionWapper>
                <Componentbutton onClick={() => this.props.consistsendinfo(
                    type,
                    this.sub_pack,
                    this.exercise_ID,
                )}>comfirm</Componentbutton>
                <ComponentWapper>
                    <ComponentoptionWapper>
                        <Componentindex>Sub_Pack</Componentindex>
                        <Componentindex>Exercise_ID</Componentindex>
                    </ComponentoptionWapper>
                    {type === 2 && consistdata && consistdata.length > 0 && consistdata.map((item, index) => (
                        <ComponentoptionWapper key={index}>
                            <Componentindex>{item.Sub_Pack}</Componentindex>
                            <Componentindex>{item.Exercise_ID}</Componentindex>
                        </ComponentoptionWapper>
                    ))}
                </ComponentWapper>
            </ComponentWapper>
        )
    }
}

const mapStateToProps = (state) => ({
    consistdata: state.main.consistdata
})

const mapDisptchToProps = (dispatch) => {
    return {
        consistsendinfo(type, sub_pack, exercise_ID) {
            dispatch(actionCreators.consistsendinfo(type, sub_pack.value, exercise_ID.value));
        }
    }
}

export default connect(mapStateToProps, mapDisptchToProps)(Consist);