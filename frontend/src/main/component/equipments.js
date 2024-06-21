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
        const { equipmentdata } = this.props;
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
                    <Componentindex>Eq_ID</Componentindex>
                    <Componentinput ref={(input) => { this.eq_ID = input }} />
                </ComponentoptionWapper>
                <ComponentoptionWapper>
                    <Componentindex>Name</Componentindex>
                    <Componentinput ref={(input) => { this.name = input }} />
                </ComponentoptionWapper>
                <ComponentoptionWapper>
                    <Componentindex>Quantity</Componentindex>
                    <Componentinput ref={(input) => { this.quantity = input }} />
                </ComponentoptionWapper>
                <ComponentoptionWapper>
                    <Componentindex>Cost</Componentindex>
                    <Componentinput ref={(input) => { this.cost = input }} />
                </ComponentoptionWapper>
                <Componentbutton onClick={() => this.props.equipmentsendinfo(
                    type,
                    this.eq_ID,
                    this.name,
                    this.quantity,
                    this.cost,
                )}>comfirm</Componentbutton>
                <ComponentWapper>
                    <ComponentoptionWapper>
                        <Componentindex>Eq_ID</Componentindex>
                        <Componentindex>Name</Componentindex>
                        <Componentindex>Quantity</Componentindex>
                        <Componentindex>Cost</Componentindex>
                    </ComponentoptionWapper>
                    {type === 2 && equipmentdata && equipmentdata.length > 0 && equipmentdata.map((item, index) => (
                        <ComponentoptionWapper key={index}>
                            <Componentindex>{item.Eq_ID}</Componentindex>
                            <Componentindex>{item.Name}</Componentindex>
                            <Componentindex>{item.Quantity}</Componentindex>
                            <Componentindex>{item.Cost}</Componentindex>

                        </ComponentoptionWapper>
                    ))}
                </ComponentWapper>
            </ComponentWapper>
        )
    }
}

const mapStateToProps = (state) => ({
    equipmentdata: state.main.equipmentdata
})

const mapDisptchToProps = (dispatch) => {
    return {
        equipmentsendinfo(type, eq_ID, name, quantity, cost) {
            dispatch(actionCreators.equipmentsendinfo(type, eq_ID.value, name.value, quantity.value, cost.value));
        }
    }
}

export default connect(mapStateToProps, mapDisptchToProps)(Equipments);