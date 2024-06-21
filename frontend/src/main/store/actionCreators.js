import * as constants from './constants';
import axios from 'axios';

export const setcategorypage = (page) => ({
  type: constants.SET_CATEGORY_PAGE,
  page
});

export const trainersendinfo = (type, t_id, t_name, email_id, phone, gender, hire_date, salary) => {
  return (dispatch) => {
    axios./*測試api時把get換成post*/get('/api/trainer.json', { type, t_id, t_name, email_id, phone, gender, hire_date, salary }).then((res) => {
      if (type === 2) {
        const result = res.data.trainers;
        dispatch(trainerdata(result));
      }
    }).catch(() => {
      alert('fail')
    });
  }
}

const trainerdata = (result) => ({
  type:constants.TRAINER_DATA,
  result
})

export const membersendinfo = (type, mem_id, m_name, phone, start_date, gender, subs, height, weight, age, email_id, trainer_id) => {
  return (dispatch) => {
    axios./*測試api時把get換成post*/get('/api/member.json', { type, mem_id, m_name, phone, start_date, gender, subs, height, weight, age, email_id, trainer_id }).then((res) => {
      if (type === 2) {
        const result = res.data.members;
        dispatch(memberdata(result));
      }
    }).catch(() => {
      alert('fail')
    });
  }
}

const memberdata = (result) => ({
  type:constants.MEMBER_DATA,
  result
})

export const subscriptionssendinfo = (type, sub_ID, price, duration, sub_num) => {
  return (dispatch) => {
    axios./*測試api時把get換成post*/get('/api/subscription.json', { type, sub_ID, price, duration, sub_num }).then((res) => {
      if (type === 2) {
        const result = res.data.subscriptions;
        dispatch(subscriptiondata(result));
      }
    }).catch(() => {
      alert('fail')
    });
  }
}

const subscriptiondata = (result) => ({
  type:constants.SUBSCRIPTION_DATA,
  result
})

export const consistsendinfo = (type, sub_pack, exercise_ID) => {
  return (dispatch) => {
    axios./*測試api時把get換成post*/get('/api/consist.json', { type, sub_pack, exercise_ID }).then((res) => {
      if (type === 2) {
        const result = res.data.consist;
        dispatch(consistdata(result));
      }
    }).catch(() => {
      alert('fail')
    });
  }
}

const consistdata = (result) => ({
  type:constants.CONSIST_DATA,
  result
})

export const equipmentsendinfo = (type, eq_ID, name, quantity, cost) => {
  return (dispatch) => {
    axios./*測試api時把get換成post*/get('/api/equipment.json', { type, eq_ID, name, quantity, cost }).then((res) => {
      if (type === 2) {
        const result = res.data.equipments;
        dispatch(equipmentdata(result));
      }
    }).catch(() => {
      alert('fail')
    });
  }
}

const equipmentdata = (result) => ({
  type:constants.EQUIPMENT_DATA,
  result
})

export const usesendinfo = (type, member_ID, equipment_ID) => {
  return (dispatch) => {
    axios./*測試api時把get換成post*/get('/api/use.json', { type, member_ID, equipment_ID }).then((res) => {
      if (type === 2) {
        const result = res.data.uses;
        dispatch(usedata(result));
      }
    }).catch(() => {
      alert('fail')
    });
  }
}

const usedata = (result) => ({
  type:constants.USE_DATA,
  result
})

export const exercisesendinfo = (type, ex_ID, ex_name, types, time_slot, frequency) => {
  return (dispatch) => {
    axios./*測試api時把get換成post*/get('/api/exercise.json', { type, ex_ID, ex_name, types, time_slot, frequency }).then((res) => {
      if (type === 2) {
        const result = res.data.exercises;
        dispatch(exercisedata(result));
      }
    }).catch(() => {
      alert('fail')
    });
  }
}

const exercisedata = (result) => ({
  type:constants.EXERCISE_DATA,
  result
})

export const dosendinfo = (type, member_ID, exercise_ID) => {
  return (dispatch) => {
    axios./*測試api時把get換成post*/get('/api/do.json', { type, member_ID, exercise_ID }).then((res) => {
      if (type === 2) {
        const result = res.data.do;
        dispatch(dodata(result));
      }
    }).catch(() => {
      alert('fail')
    });
  }
}

const dodata = (result) => ({
  type:constants.DO_DATA,
  result
})