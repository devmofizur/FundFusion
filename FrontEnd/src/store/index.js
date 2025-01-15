
import { createStore } from 'vuex';
import api from '../services/api';

const store = createStore({
  state: {
    user: null,
    campaigns: [],
    loading: false,
    error: null,
    
  },
  mutations: {
    setUser(state, user) {
      state.user = user;
    },
    setCampaigns(state, campaigns) {
      state.campaigns = campaigns;
    },
    setLoading(state, status) {
      state.loading = status;
    },
    setError(state, error) {
      state.error = error;
    }
  },
  actions: {
    async login({ commit }, credentials) {
      try {
        const response = await api.post('/auth/login/', credentials);
        localStorage.setItem('token', response.data.access);
        commit('setUser', response.data.user);
      } catch (error) {
        commit('setError', error.response.data.detail);
      }
    },
    async fetchCampaigns({ commit }) {
      commit('setLoading', true);
      try {
        const response = await api.get('/campaigns/');
        commit('setCampaigns', response.data);
      } catch (error) {
        commit('setError', error.response.data.detail);
      } finally {
        commit('setLoading', false);
      }
    }
  }
});

export default store;
  