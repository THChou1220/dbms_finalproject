import * as constants from './constants';
import axios from 'axios';

const API_URL = 'http://localhost:5000/';

export const setcategorypage = (page) => ({
  type: constants.SET_CATEGORY_PAGE,
  page
});

export const trainersendinfo = (type, T_id, T_Name, Email_ID, Phone, Gender, Hire_Date, Salary) => {
  return (dispatch) => {
    if (type === 1) {
      axios.post(`${API_URL}/trainers`, { T_id, T_Name, Email_ID, Phone, Gender, Hire_Date, Salary }).then(() => { }).catch(() => { alert('fail') });
    }
    else if (type === 2) {
      axios.get(`${API_URL}/trainers`).then((res) => {
        const result = res.data;
        dispatch(trainerdata(result));
      }).catch(() => { alert('fail') });
    }
    else if (type === 3) {
      axios.patch(`${API_URL}/trainers/${T_id}`, { T_Name, Email_ID, Phone, Gender, Hire_Date, Salary }).then(() => { }).catch(() => { alert('fail') });
    }
    else {
      axios.delete(`${API_URL}/trainers/${T_id}`).then(() => { }).catch(() => { alert('fail') });
    }
  }
}

const trainerdata = (result) => ({
  type: constants.TRAINER_DATA,
  result
})

export const membersendinfo = (type, Mem_ID, M_Name, Phone, Start_Date, Gender, Subs, Height, Weight, Age, Email_ID, Trainer_ID) => {
  return (dispatch) => {
    if (type === 1) {
      axios.post(`${API_URL}/members`, { Mem_ID, M_Name, Phone, Start_Date, Gender, Subs, Height, Weight, Age, Email_ID, Trainer_ID }).then(() => { }).catch(() => { alert('fail') });
    }
    else if (type === 2) {
      axios.get(`${API_URL}/members`).then((res) => {
        const result = res.data;
        dispatch(memberdata(result));
      }).catch(() => { alert('fail') });
    }
    else if (type === 3) {
      axios.patch(`${API_URL}/members/${Mem_ID}`, { M_Name, Phone, Start_Date, Gender, Subs, Height, Weight, Age, Email_ID, Trainer_ID }).then(() => { }).catch(() => { alert('fail') });
    }
    else {
      axios.delete(`${API_URL}/members/${Mem_ID}`).then(() => { }).catch(() => { alert('fail') });
    }
  }
}

const memberdata = (result) => ({
  type: constants.MEMBER_DATA,
  result
})

export const subscriptionssendinfo = (type, Sub_ID, Price, Duration, Sub_Num) => {
  return (dispatch) => {
    if (type === 1) {
      axios.post(`${API_URL}/subscriptions`, { Sub_ID, Price, Duration, Sub_Num }).then(() => { }).catch(() => { alert('fail') });
    }
    else if (type === 2) {
      axios.get(`${API_URL}/subscriptions`).then((res) => {
        const result = res.data;
        dispatch(subscriptiondata(result));
      }).catch(() => { alert('fail') });
    }
    else if (type === 3) {
      axios.patch(`${API_URL}/subscriptions/${Sub_ID}`, { Price, Duration, Sub_Num }).then(() => { }).catch(() => { alert('fail') });
    }
    else {
      axios.delete(`${API_URL}/subscriptions/${Sub_ID}`).then(() => { }).catch(() => { alert('fail') });
    }
  }
}

const subscriptiondata = (result) => ({
  type: constants.SUBSCRIPTION_DATA,
  result
})

export const consistsendinfo = (type, Sub_Pack, Exercise_ID) => {
  return (dispatch) => {
    if (type === 1) {
      axios.post(`${API_URL}/consist`, { Sub_Pack, Exercise_ID }).then(() => { }).catch(() => { alert('fail') });
    }
    else if (type === 2) {
      axios.get(`${API_URL}/consist`).then((res) => {
        const result = res.data;
        dispatch(consistdata(result));
      }).catch(() => { alert('fail') });
    }
    else if (type === 3) {
      axios.patch(`${API_URL}/consist/${Sub_Pack}`, { Exercise_ID }).then(() => { }).catch(() => { alert('fail') });
    }
    else {
      axios.delete(`${API_URL}/consist/${Sub_Pack}`).then(() => { }).catch(() => { alert('fail') });
    }
  }
}

const consistdata = (result) => ({
  type: constants.CONSIST_DATA,
  result
})

export const equipmentsendinfo = (type, Eq_ID, Name, Quantity, Cost) => {
  return (dispatch) => {
    if (type === 1) {
      axios.post(`${API_URL}/equipments`, { Eq_ID, Name, Quantity, Cost }).then(() => { }).catch(() => { alert('fail') });
    }
    else if (type === 2) {
      axios.get(`${API_URL}/equipments`).then((res) => {
        const result = res.data;
        dispatch(equipmentdata(result));
      }).catch(() => { alert('fail') });
    }
    else if (type === 3) {
      axios.patch(`${API_URL}/equipments/${Eq_ID}`, { Name, Quantity, Cost }).then(() => { }).catch(() => { alert('fail') });
    }
    else {
      axios.delete(`${API_URL}/equipments/${Eq_ID}`).then(() => { }).catch(() => { alert('fail') });
    }
  }
}

const equipmentdata = (result) => ({
  type: constants.EQUIPMENT_DATA,
  result
})

export const usesendinfo = (type, Member_ID, Equipment_ID) => {
  return (dispatch) => {
    if (type === 1) {
      axios.post(`${API_URL}/use`, { Member_ID, Equipment_ID }).then(() => { }).catch(() => { alert('fail') });
    }
    else if (type === 2) {
      axios.get(`${API_URL}/use`).then((res) => {
        const result = res.data;
        dispatch(usedata(result));
      }).catch(() => { alert('fail') });
    }
    else if (type === 3) {
      axios.patch(`${API_URL}/use/${Member_ID}`, { Equipment_ID }).then(() => { }).catch(() => { alert('fail') });
    }
    else {
      axios.delete(`${API_URL}/use/${Member_ID}`).then(() => { }).catch(() => { alert('fail') });
    }
  }
}

const usedata = (result) => ({
  type: constants.USE_DATA,
  result
})

export const exercisesendinfo = (type, EX_id, EX_Name, Type, Time_Slot, Frequency) => {
  return (dispatch) => {
    if (type === 1) {
      axios.post(`${API_URL}/exercises`, { EX_id, EX_Name, Type, Time_Slot, Frequency }).then(() => { }).catch(() => { alert('fail') });
    }
    else if (type === 2) {
      axios.get(`${API_URL}/exercises`).then((res) => {
        const result = res.data;
        dispatch(exercisedata(result));
      }).catch(() => { alert('fail') });
    }
    else if (type === 3) {
      axios.patch(`${API_URL}/exercises/${EX_id}`, { EX_Name, Type, Time_Slot, Frequency }).then(() => { }).catch(() => { alert('fail') });
    }
    else {
      axios.delete(`${API_URL}/exercises/${EX_id}`).then(() => { }).catch(() => { alert('fail') });
    }
  }
}

const exercisedata = (result) => ({
  type: constants.EXERCISE_DATA,
  result
})

export const dosendinfo = (type, Member_ID, Exercise_ID) => {
  return (dispatch) => {
    if (type === 1) {
      axios.post(`${API_URL}/do`, { Member_ID, Exercise_ID }).then(() => { }).catch(() => { alert('fail') });
    }
    else if (type === 2) {
      axios.get(`${API_URL}/do`).then((res) => {
        const result = res.data;
        dispatch(dodata(result));
      }).catch(() => { alert('fail') });
    }
    else if (type === 3) {
      axios.patch(`${API_URL}/do/${Member_ID}`, { Exercise_ID }).then(() => { }).catch(() => { alert('fail') });
    }
    else {
      axios.delete(`${API_URL}/do/${Member_ID}`).then(() => { }).catch(() => { alert('fail') });
    }
  }
}

const dodata = (result) => ({
  type: constants.DO_DATA,
  result
})