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

class Equipments extends PureComponent {
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
                    <Componentindex>eq ID</Componentindex>
                    <Componentinput ref={(input) => { this.eq_ID = input }} />
                </ComponentoptionWapper>
                <ComponentoptionWapper>
                    <Componentindex>name</Componentindex>
                    <Componentinput ref={(input) => { this.name = input }} />
                </ComponentoptionWapper>
                <ComponentoptionWapper>
                    <Componentindex>quantity</Componentindex>
                    <Componentinput ref={(input) => { this.quantity = input }} />
                </ComponentoptionWapper>
                <ComponentoptionWapper>
                    <Componentindex>cost</Componentindex>
                    <Componentinput ref={(input) => { this.cost = input }} />
                </ComponentoptionWapper>
                <Componentbutton onClick={() => this.props.equipmentsendinfo(
                    type,
                    this.eq_ID,
                    this.name,
                    this.quantity,
                    this.cost,
                )}>comfirm</Componentbutton>
            </ComponentWapper>
        )
    }
}

const mapStateToProps = (state) => ({

})

const mapDisptchToProps = (dispatch) => {
    return {
        equipmentsendinfo(type, eq_ID, name, quantity, cost) {
            dispatch(actionCreators.equipmentsendinfo(type, eq_ID.value, name.value, quantity.value, cost.value));
        }
    }
}

export default connect(mapStateToProps, mapDisptchToProps)(Equipments);