import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8080/api', // Use full base URL
  headers: {
    'Content-Type': 'application/json'
  }
});

// Request interceptor for adding token to requests
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('accessToken');
    if (token) {
      config.headers['Authorization'] = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

// Response interceptor for handling token refresh and errors
api.interceptors.response.use(
  (response) => response,
  async (error) => {
    const originalRequest = error.config;

    // If unauthorized and not already retried
    if (error.response.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;

      try {
        const refreshToken = localStorage.getItem('refreshToken');

        // Token refresh request
        const response = await axios.post('http://localhost:8080/api/auth/token/refresh/',
          { refresh: refreshToken }
        );

        const { access } = response.data;

        // Update tokens
        localStorage.setItem('accessToken', access);

        // Retry original request with new token
        originalRequest.headers['Authorization'] = `Bearer ${access}`;
        return axios(originalRequest);
      } catch (refreshError) {
        // Refresh failed - force logout
        localStorage.removeItem('accessToken');
        localStorage.removeItem('refreshToken');

        // Redirect to login or dispatch logout action
        window.location.href = '/login';

        return Promise.reject(refreshError);
      }
    }

    return Promise.reject(error);
  }
);

export default api;
