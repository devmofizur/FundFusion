<template>
  <div class="auth-page">
    <div class="auth-container">
      <div class="auth-tabs">
        <button
          :class="{ active: activeTab === 'login' }"
          @click="activeTab = 'login'">
          Login
        </button>
        <button
          :class="{ active: activeTab === 'register' }"
          @click="activeTab = 'register'">
          Register
        </button>
      </div>

      <div class="auth-content">
        <!-- Login Form -->
        <div v-if="activeTab === 'login'" class="login-form">
          <form @submit.prevent="login">
            <input type="email" v-model="loginForm.email" placeholder="Email" required />
            <input type="password" v-model="loginForm.password" placeholder="Password" required />
            <button type="submit">Login</button>
          </form>
          <p><router-link to="/forgot-password">Forgot your password?</router-link></p>
        </div>

        <!-- Register Form -->
        <div v-if="activeTab === 'register'" class="register-form">
          <form @submit.prevent="register">
            <input type="text" v-model="registerForm.username" placeholder="Username" required />
            <input type="email" v-model="registerForm.email" placeholder="Email" required />
            <input type="password" v-model="registerForm.password" placeholder="Password" required />
            <input type="password" v-model="registerForm.confirmPassword" placeholder="Confirm Password" required />
            <button type="submit">Register</button>
          </form>

          <!-- Success Message After Registration -->
          <div v-if="registrationSuccess" class="success-message">
            <p>Registration successful! Redirecting to login...</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import api from '@/services/api'; // Import the configured Axios instance

export default {
  name: 'AuthPage',
  data() {
    return {
      activeTab: 'login',
      loginForm: {
        email: '',
        password: '',
      },
      registerForm: {
        username: '',
        email: '',
        password: '',
        confirmPassword: '',
      },
      registrationSuccess: false,
      errorMessage: '',
    };
  },
  methods: {
    async login() {
      try {
        // Use api instance instead of axios directly
        const response = await api.post('/auth/login/', {
          email: this.loginForm.email,
          password: this.loginForm.password,
        });

        // Destructure response data
        const { access, refresh, user } = response.data;

        // Store tokens securely
        localStorage.setItem('accessToken', access);
        localStorage.setItem('refreshToken', refresh);

        // Optional: Store user info in localStorage or Vuex store
        localStorage.setItem('userInfo', JSON.stringify(user));

        // Redirect based on user role with more robust routing
        this.$router.push(user.is_admin ? '/admin' : '/dashboard');
        this.$store.state.isLoggedIn = true;
        
      } catch (error) {
        // Centralized error handling
        this.handleAuthError(error, 'Login');
      }
    },
    async register() {
      // Validate passwords match
      if (this.registerForm.password !== this.registerForm.confirmPassword) {
        this.showError('Passwords do not match');
        return;
      }

      try {
        const response = await api.post('/auth/register/', {
          username: this.registerForm.username,
          email: this.registerForm.email,
          password: this.registerForm.password,
          confirm_password: this.registerForm.confirmPassword,
        });

        this.showSuccess('Registration successful');

        // Reset form and switch to login
        this.resetRegistrationForm();
        this.activeTab = 'login';
      } catch (error) {
        this.handleAuthError(error, 'Registration');
      }
    },
    handleAuthError(error, context) {
      let errorMessage = 'Unexpected error occurred';

      if (error.response) {
        // Server responded with an error
        errorMessage = error.response.data.detail ||
                       error.response.data.error ||
                       `${context} failed. Please try again.`;
      } else if (error.request) {
        // Request made but no response received
        errorMessage = 'Network error. Please check your connection.';
      }

      // Display error
      this.showError(errorMessage);
    },
    showError(message) {
      this.errorMessage = message;
      alert(message); // Or use a more sophisticated error display method
    },
    showSuccess(message) {
      alert(message); // Replace with your preferred success notification
    },
    resetRegistrationForm() {
      this.registerForm = {
        username: '',
        email: '',
        password: '',
        confirmPassword: '',
      };
    },
  },
};
</script>


<style scoped>
.auth-page {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background: linear-gradient(to bottom, #f0fffe, #83CFCB);
  overflow: hidden;
  position: relative;
}

.auth-container {
  width: 400px;
  background: #fff;
  border-radius: 10px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
  padding: 20px;
}

.auth-tabs {
  display: flex;
  justify-content: space-evenly;
  margin-bottom: 20px;
}

.auth-tabs button {
  flex: 1;
  padding: 10px 0;
  background: #f1f1f1;
  border: none;
  border-radius: 5px;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.3s, transform 0.3s;
}

.auth-tabs button.active {
  background: linear-gradient(to right, #83CFCB, #83CFCB);
  color: #fff;
  transform: scale(1.05);
}

.auth-content {
  text-align: center;
}

.auth-content h2 {
  margin-bottom: 20px;
}

.auth-content form {
  display: flex;
  flex-direction: column;
}

.auth-content form input {
  padding: 10px;
  margin-bottom: 15px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.auth-content form button {
  padding: 10px;
  background: linear-gradient(to right, #83CFCB , #83CFCB);
  color: #fff;
  border: none;
  border-radius: 5px;
  font-weight: bold;
  cursor: pointer;
  transition: transform 0.3s, background-color 0.3s;
}

.auth-content form button:hover {
  transform: scale(1.05);
}

.password-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.password-container input {
  flex: 1;
  margin-right: 2px;
}

.admin-checkbox {
  display: flex;
  align-items: baseline;
}

.admin-label {
  font-size: 1em;
  color: #8b8a8a;
  margin-left: 8px;
}

p {
  margin-top: 10px;
}

router-link {
  color: #83CFCB;
  text-decoration: none;
}

router-link:hover {
  text-decoration: underline;
}


.success-message {
  margin-top: 20px;
  padding: 10px;
  background-color: #d4edda;
  color: #155724;
  border-radius: 5px;
  border: 1px solid #c3e6cb;
}
</style>
