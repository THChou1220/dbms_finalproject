import * as constants from './constants';
import axios from 'axios';

export const setcategorypage = (page) => ({
  type: constants.SET_CATEGORY_PAGE,
  page
});

export const trainersendinfo = (type, t_id, t_name, email_id, phone, gender, hire_date, salary) => {
  return () => {
    axios./*正是對接時用post*/get('/api/CUinfo.json', { type, t_id, t_name, email_id, phone, gender, hire_date, salary }).then((res) => {
      /*接收*/
    }).catch(() => {
      alert('fail')
    });
  }
}

export const membersendinfo = (type, mem_id, m_name, phone, start_date, gender, subs, height, weight, age, email_id, trainer_id) => {
  return () => {
    axios./*正是對接時用post*/get('/api/CUinfo.json', { type, mem_id, m_name, phone, start_date, gender, subs, height, weight, age, email_id, trainer_id }).then((res) => {
      /*接收*/
    }).catch(() => {
      alert('fail')
    });
  }
}

export const subscriptionssendinfo = (type, sub_ID, price, duration, sub_num) => {
  return () => {
    axios./*正是對接時用post*/get('/api/CUinfo.json', { type, sub_ID, price, duration, sub_num }).then((res) => {
      /*接收*/
    }).catch(() => {
      alert('fail')
    });
  }
}

export const consistsendinfo = (type, sub_pack, exercise_ID) => {
  return () => {
    axios./*正是對接時用post*/get('/api/CUinfo.json', { type, sub_pack, exercise_ID }).then((res) => {
      /*接收*/
    }).catch(() => {
      alert('fail')
    });
  }
}

export const equipmentsendinfo = (type, eq_ID, name, quantity, cost) => {
  return () => {
    axios./*正是對接時用post*/get('/api/CUinfo.json', { type, eq_ID, name, quantity, cost }).then((res) => {
      /*接收*/
    }).catch(() => {
      alert('fail')
    });
  }
}

export const usesendinfo = (type, member_ID, equipment_ID) => {
  return () => {
    axios./*正是對接時用post*/get('/api/CUinfo.json', { type, member_ID, equipment_ID }).then((res) => {
      /*接收*/
    }).catch(() => {
      alert('fail')
    });
  }
}

export const exercisesendinfo = (type, ex_ID, ex_name, types, time_slot, frequency) => {
  return () => {
    axios./*正是對接時用post*/get('/api/CUinfo.json', { type, ex_ID, ex_name, types, time_slot, frequency }).then((res) => {
      /*接收*/
    }).catch(() => {
      alert('fail')
    });
  }
}

export const dosendinfo = (type, member_ID, exercise_ID) => {
  return () => {
    axios./*正是對接時用post*/get('/api/CUinfo.json', { type, member_ID, exercise_ID }).then((res) => {
      /*接收*/
    }).catch(() => {
      alert('fail')
    });
  }
}