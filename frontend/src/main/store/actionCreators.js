import * as constants from './constants';
import axios from 'axios';

const API_URL = 'http://localhost:5000/';

export const setcategorypage = (page) => ({
  type: constants.SET_CATEGORY_PAGE,
  page
});

export const trainersendinfo = (type, t_id, t_name, email_id, phone, gender, hire_date, salary) => {
  return (dispatch) => {
    if (type === 1) {
      axios.post(`${API_URL}/trainers`, { t_id, t_name, email_id, phone, gender, hire_date, salary }).then(() => { }).catch(() => { alert('fail') });
    }
    else if (type === 2) {
      axios.get(`${API_URL}/trainers`).then((res) => {
        const result = res.data;
        dispatch(trainerdata(result));
      }).catch(() => { alert('fail') });
    }
    else if (type === 3) {
      axios.patch(`${API_URL}/trainers/${t_id}`, { t_name, email_id, phone, gender, hire_date, salary }).then(() => { }).catch(() => { alert('fail') });
    }
    else {
      axios.delete(`${API_URL}/trainers/${t_id}`).then(() => { }).catch(() => { alert('fail') });
    }
  }
}

const trainerdata = (result) => ({
  type: constants.TRAINER_DATA,
  result
})

export const membersendinfo = (type, mem_id, m_name, phone, start_date, gender, subs, height, weight, age, email_id, trainer_id) => {
  return (dispatch) => {
    if (type === 1) {
      axios.post(`${API_URL}/members`, { mem_id, m_name, phone, start_date, gender, subs, height, weight, age, email_id, trainer_id }).then(() => { }).catch(() => { alert('fail') });
    }
    else if (type === 2) {
      axios.get(`${API_URL}/members`).then((res) => {
        const result = res.data;
        dispatch(memberdata(result));
      }).catch(() => { alert('fail') });
    }
    else if (type === 3) {
      axios.patch(`${API_URL}/members/${mem_id}`, { m_name, phone, start_date, gender, subs, height, weight, age, email_id, trainer_id }).then(() => { }).catch(() => { alert('fail') });
    }
    else {
      axios.delete(`${API_URL}/members/${mem_id}`).then(() => { }).catch(() => { alert('fail') });
    }
  }
}

const memberdata = (result) => ({
  type: constants.MEMBER_DATA,
  result
})

export const subscriptionssendinfo = (type, sub_ID, price, duration, sub_num) => {
  return (dispatch) => {
    if (type === 1) {
      axios.post(`${API_URL}/subscriptions`, { sub_ID, price, duration, sub_num }).then(() => { }).catch(() => { alert('fail') });
    }
    else if (type === 2) {
      axios.get(`${API_URL}/subscriptions`).then((res) => {
        const result = res.data;
        dispatch(subscriptiondata(result));
      }).catch(() => { alert('fail') });
    }
    else if (type === 3) {
      axios.patch(`${API_URL}/subscriptions/${sub_ID}`, { price, duration, sub_num }).then(() => { }).catch(() => { alert('fail') });
    }
    else {
      axios.delete(`${API_URL}/subscriptions/${sub_ID}`).then(() => { }).catch(() => { alert('fail') });
    }
  }
}

const subscriptiondata = (result) => ({
  type: constants.SUBSCRIPTION_DATA,
  result
})

export const consistsendinfo = (type, sub_pack, exercise_ID) => {
  return (dispatch) => {
    if (type === 1) {
      axios.post(`${API_URL}/consist`, { sub_pack, exercise_ID }).then(() => { }).catch(() => { alert('fail') });
    }
    else if (type === 2) {
      axios.get(`${API_URL}/consist`).then((res) => {
        const result = res.data;
        dispatch(consistdata(result));
      }).catch(() => { alert('fail') });
    }
    else if (type === 3) {
      axios.patch(`${API_URL}/consist/${sub_pack}`, { exercise_ID }).then(() => { }).catch(() => { alert('fail') });
    }
    else {
      axios.delete(`${API_URL}/consist/${sub_pack}`).then(() => { }).catch(() => { alert('fail') });
    }
  }
}

const consistdata = (result) => ({
  type: constants.CONSIST_DATA,
  result
})

export const equipmentsendinfo = (type, eq_ID, name, quantity, cost) => {
  return (dispatch) => {
    if (type === 1) {
      axios.post(`${API_URL}/equipments`, { eq_ID, name, quantity, cost }).then(() => { }).catch(() => { alert('fail') });
    }
    else if (type === 2) {
      axios.get(`${API_URL}/equipments`).then((res) => {
        const result = res.data;
        dispatch(equipmentdata(result));
      }).catch(() => { alert('fail') });
    }
    else if (type === 3) {
      axios.patch(`${API_URL}/equipments/${eq_ID}`, { name, quantity, cost }).then(() => { }).catch(() => { alert('fail') });
    }
    else {
      axios.delete(`${API_URL}/equipments/${eq_ID}`).then(() => { }).catch(() => { alert('fail') });
    }
  }
}

const equipmentdata = (result) => ({
  type: constants.EQUIPMENT_DATA,
  result
})

export const usesendinfo = (type, member_ID, equipment_ID) => {
  return (dispatch) => {
    if (type === 1) {
      axios.post(`${API_URL}/use`, { member_ID, equipment_ID }).then(() => { }).catch(() => { alert('fail') });
    }
    else if (type === 2) {
      axios.get(`${API_URL}/use`).then((res) => {
        const result = res.data;
        dispatch(usedata(result));
      }).catch(() => { alert('fail') });
    }
    else if (type === 3) {
      axios.patch(`${API_URL}/use/${member_ID}`, { equipment_ID }).then(() => { }).catch(() => { alert('fail') });
    }
    else {
      axios.delete(`${API_URL}/use/${member_ID}`).then(() => { }).catch(() => { alert('fail') });
    }
  }
}

const usedata = (result) => ({
  type: constants.USE_DATA,
  result
})

export const exercisesendinfo = (type, ex_ID, ex_name, types, time_slot, frequency) => {
  return (dispatch) => {
    if (type === 1) {
      axios.post(`${API_URL}/exercises`, { ex_ID, ex_name, types, time_slot, frequency }).then(() => { }).catch(() => { alert('fail') });
    }
    else if (type === 2) {
      axios.get(`${API_URL}/exercises`).then((res) => {
        const result = res.data;
        dispatch(exercisedata(result));
      }).catch(() => { alert('fail') });
    }
    else if (type === 3) {
      axios.patch(`${API_URL}/exercises/${ex_ID}`, { ex_name, types, time_slot, frequency }).then(() => { }).catch(() => { alert('fail') });
    }
    else {
      axios.delete(`${API_URL}/exercises/${ex_ID}`).then(() => { }).catch(() => { alert('fail') });
    }
  }
}

const exercisedata = (result) => ({
  type: constants.EXERCISE_DATA,
  result
})

export const dosendinfo = (type, member_ID, exercise_ID) => {
  return (dispatch) => {
    if (type === 1) {
      axios.post(`${API_URL}/do`, { member_ID, exercise_ID }).then(() => { }).catch(() => { alert('fail') });
    }
    else if (type === 2) {
      axios.get(`${API_URL}/do`).then((res) => {
        const result = res.data;
        dispatch(dodata(result));
      }).catch(() => { alert('fail') });
    }
    else if (type === 3) {
      axios.patch(`${API_URL}/do/${member_ID}`, { exercise_ID }).then(() => { }).catch(() => { alert('fail') });
    }
    else {
      axios.delete(`${API_URL}/do/${member_ID}`).then(() => { }).catch(() => { alert('fail') });
    }
  }
}

const dodata = (result) => ({
  type: constants.DO_DATA,
  result
})