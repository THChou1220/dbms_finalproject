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

class Members extends PureComponent {
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
        const { memberdata } = this.props;
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
                    <Componentindex>Mem_ID</Componentindex>
                    <Componentinput ref={(input) => { this.mem_id = input }} />
                </ComponentoptionWapper>
                <ComponentoptionWapper>
                    <Componentindex>M_Name</Componentindex>
                    <Componentinput ref={(input) => { this.m_name = input }} />
                </ComponentoptionWapper>
                <ComponentoptionWapper>
                    <Componentindex>Phone</Componentindex>
                    <Componentinput ref={(input) => { this.phone = input }} />
                </ComponentoptionWapper>
                <ComponentoptionWapper>
                    <Componentindex>Start_Date</Componentindex>
                    <Componentinput ref={(input) => { this.start_date = input }} />
                </ComponentoptionWapper>
                <ComponentoptionWapper>
                    <Componentindex>Gender</Componentindex>
                    <Componentinput ref={(input) => { this.gender = input }} />
                </ComponentoptionWapper>
                <ComponentoptionWapper>
                    <Componentindex>Subs</Componentindex>
                    <Componentinput ref={(input) => { this.subs = input }} />
                </ComponentoptionWapper>
                <ComponentoptionWapper>
                    <Componentindex>Height</Componentindex>
                    <Componentinput ref={(input) => { this.height = input }} />
                </ComponentoptionWapper>
                <ComponentoptionWapper>
                    <Componentindex>Weight</Componentindex>
                    <Componentinput ref={(input) => { this.weight = input }} />
                </ComponentoptionWapper>
                <ComponentoptionWapper>
                    <Componentindex>Age</Componentindex>
                    <Componentinput ref={(input) => { this.age = input }} />
                </ComponentoptionWapper>
                <ComponentoptionWapper>
                    <Componentindex>Email_ID</Componentindex>
                    <Componentinput ref={(input) => { this.email_id = input }} />
                </ComponentoptionWapper>
                <ComponentoptionWapper>
                    <Componentindex>Trainer_ID</Componentindex>
                    <Componentinput ref={(input) => { this.trainer_id = input }} />
                </ComponentoptionWapper>
                <Componentbutton onClick={() => this.props.membersendinfo(
                    type,
                    this.mem_id,
                    this.m_name,
                    this.phone,
                    this.start_date,
                    this.gender,
                    this.subs,
                    this.height,
                    this.weight,
                    this.age,
                    this.email_id,
                    this.trainer_id
                )}>comfirm</Componentbutton>
                <ComponentWapper>
                    <ComponentoptionWapper>
                        <Componentindex>Mem_ID</Componentindex>
                        <Componentindex>M_Name</Componentindex>
                        <Componentindex>Phone</Componentindex>
                        <Componentindex>Start_Date</Componentindex>
                        <Componentindex>Gender</Componentindex>
                        <Componentindex>Subs</Componentindex>
                        <Componentindex>Height</Componentindex>
                        <Componentindex>Weight</Componentindex>
                        <Componentindex>Age</Componentindex>
                        <Componentindex>Email_ID</Componentindex>
                        <Componentindex>Trainer_ID</Componentindex>
                    </ComponentoptionWapper>
                    {type === 2 && memberdata && memberdata.length > 0 && memberdata.map((item,index) => (
                        <ComponentoptionWapper key={index}>
                            <Componentindex>{item.Mem_ID}</Componentindex>
                            <Componentindex>{item.M_Name}</Componentindex>
                            <Componentindex>{item.Phone}</Componentindex>
                            <Componentindex>{item.Start_Date}</Componentindex>
                            <Componentindex>{item.Gender}</Componentindex>
                            <Componentindex>{item.Subs}</Componentindex>
                            <Componentindex>{item.Height}</Componentindex>
                            <Componentindex>{item.Weight}</Componentindex>
                            <Componentindex>{item.Age}</Componentindex>
                            <Componentindex>{item.Email_ID}</Componentindex>
                            <Componentindex>{item.Trainer_ID}</Componentindex>
                        </ComponentoptionWapper>
                    ))}
                </ComponentWapper>
            </ComponentWapper>
        )
    }
}

const mapStateToProps = (state) => ({
    memberdata: state.main.memberdata
})

const mapDisptchToProps = (dispatch) => {
    return {
        membersendinfo(type, mem_id, m_name, phone, start_date, gender, subs, height, weight, age, email_id, trainer_id) {
            dispatch(actionCreators.membersendinfo(type, mem_id.value, m_name.value, phone.value, start_date.value, gender.value, subs.value, height.value, weight.value, age.value, email_id.value, trainer_id.value));
        }
    }
}

export default connect(mapStateToProps, mapDisptchToProps)(Members);