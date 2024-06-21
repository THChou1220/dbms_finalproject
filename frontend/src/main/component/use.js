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

class Use extends PureComponent {
    state = {
        hoveredBox: null,
        type: null,
        pages: [
            { id: 1, text: 'create' },
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
        const { usedata } = this.props;
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
                    <Componentindex>Equipment_ID</Componentindex>
                    <Componentinput ref={(input) => { this.equipment_ID = input }} />
                </ComponentoptionWapper>
                <Componentbutton onClick={() => this.props.usesendinfo(
                    type,
                    this.member_ID,
                    this.equipment_ID,
                )}>comfirm</Componentbutton>
                <ComponentWapper>
                    <ComponentoptionWapper>
                        <Componentindex>Member_ID</Componentindex>
                        <Componentindex>Equipment_ID</Componentindex>
                    </ComponentoptionWapper>
                    {type === 2 && usedata && usedata.length > 0 && usedata.map((item, index) => (
                        <ComponentoptionWapper key={index}>
                            <Componentindex>{item.Member_ID}</Componentindex>
                            <Componentindex>{item.Equipment_ID}</Componentindex>
                        </ComponentoptionWapper>
                    ))}
                </ComponentWapper>
            </ComponentWapper>
        )
    }
}

const mapStateToProps = (state) => ({
    usedata: state.main.usedata
})

const mapDisptchToProps = (dispatch) => {
    return {
        usesendinfo(type, member_ID, equipment_ID) {
            dispatch(actionCreators.usesendinfo(type, member_ID.value, equipment_ID.value));
        }
    }
}

export default connect(mapStateToProps, mapDisptchToProps)(Use);