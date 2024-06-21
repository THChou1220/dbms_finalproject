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

class Trainers extends PureComponent {
    state = {
        hoveredBox: null,
        type: null,
        pages: [
            { id: 1, text: 'create' },
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
        const { trainerdata } = this.props;
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
                    <Componentindex>T_ID</Componentindex>
                    <Componentinput ref={(input) => { this.t_id = input }} />
                </ComponentoptionWapper>
                <ComponentoptionWapper>
                    <Componentindex>T_Name</Componentindex>
                    <Componentinput ref={(input) => { this.t_name = input }} />
                </ComponentoptionWapper>
                <ComponentoptionWapper>
                    <Componentindex>Email_ID</Componentindex>
                    <Componentinput ref={(input) => { this.email_id = input }} />
                </ComponentoptionWapper>
                <ComponentoptionWapper>
                    <Componentindex>Phone</Componentindex>
                    <Componentinput ref={(input) => { this.phone = input }} />
                </ComponentoptionWapper>
                <ComponentoptionWapper>
                    <Componentindex>Gender</Componentindex>
                    <Componentinput ref={(input) => { this.gender = input }} />
                </ComponentoptionWapper>
                <ComponentoptionWapper>
                    <Componentindex>Hire_Date</Componentindex>
                    <Componentinput ref={(input) => { this.hire_date = input }} />
                </ComponentoptionWapper>
                <ComponentoptionWapper>
                    <Componentindex>Salary</Componentindex>
                    <Componentinput ref={(input) => { this.salary = input }} />
                </ComponentoptionWapper>
                <Componentbutton onClick={() => this.props.trainersendinfo(
                    type,
                    this.t_id,
                    this.t_name,
                    this.email_id,
                    this.phone,
                    this.gender,
                    this.hire_date,
                    this.salary
                )}>comfirm</Componentbutton>
                <ComponentWapper>
                    <ComponentoptionWapper>
                        <Componentindex>T_ID</Componentindex>
                        <Componentindex>T_Name</Componentindex>
                        <Componentindex>Email_ID</Componentindex>
                        <Componentindex>Phone</Componentindex>
                        <Componentindex>Gender</Componentindex>
                        <Componentindex>Hire_Date</Componentindex>
                        <Componentindex>Salary</Componentindex>
                    </ComponentoptionWapper>
                    {type === 2 && trainerdata && trainerdata.length > 0 && trainerdata.map((item, index) => (
                        <ComponentoptionWapper key={index}>
                            <Componentindex>{item.T_id}</Componentindex>
                            <Componentindex>{item.T_Name}</Componentindex>
                            <Componentindex>{item.Email_ID}</Componentindex>
                            <Componentindex>{item.Phone}</Componentindex>
                            <Componentindex>{item.Gender}</Componentindex>
                            <Componentindex>{item.Hire_Date}</Componentindex>
                            <Componentindex>{item.Salary}</Componentindex>
                        </ComponentoptionWapper>
                    ))}
                </ComponentWapper>
            </ComponentWapper>
        )
    }
}

const mapStateToProps = (state) => ({
    trainerdata: state.main.trainerdata
})

const mapDisptchToProps = (dispatch) => {
    return {
        trainersendinfo(type, t_id, t_name, email_id, phone, gender, hire_date, salary) {
            dispatch(actionCreators.trainersendinfo(type, t_id.value, t_name.value, email_id.value, phone.value, gender.value, hire_date.value, salary.value));
        }
    }
}

export default connect(mapStateToProps, mapDisptchToProps)(Trainers);
