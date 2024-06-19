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

class Subscriptions extends PureComponent {
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
                    <Componentindex>sub ID</Componentindex>
                    <Componentinput ref={(input) => { this.sub_ID = input }} />
                </ComponentoptionWapper>
                <ComponentoptionWapper>
                    <Componentindex>price</Componentindex>
                    <Componentinput ref={(input) => { this.price = input }} />
                </ComponentoptionWapper>
                <ComponentoptionWapper>
                    <Componentindex>duration</Componentindex>
                    <Componentinput ref={(input) => { this.duration = input }} />
                </ComponentoptionWapper>
                <ComponentoptionWapper>
                    <Componentindex>sub num</Componentindex>
                    <Componentinput ref={(input) => { this.sub_num = input }} />
                </ComponentoptionWapper>
                <Componentbutton onClick={() => this.props.subscriptionssendinfo(
                    type,
                    this.sub_ID,
                    this.price,
                    this.duration,
                    this.sub_num,
                )}>comfirm</Componentbutton>
            </ComponentWapper>
        )
    }
}

const mapStateToProps = (state) => ({

})

const mapDisptchToProps = (dispatch) => {
    return {
        subscriptionssendinfo(type, sub_ID, price, duration, sub_num) {
            dispatch(actionCreators.subscriptionssendinfo(type, sub_ID.value, price.value, duration.value, sub_num.value));
        }
    }
}

export default connect(mapStateToProps, mapDisptchToProps)(Subscriptions);