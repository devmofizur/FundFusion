<template>
  <header class="app-header">
    <h1 class="site-title">Fund Fusion</h1>
    <nav>
      <ul class="nav-list">
        <li><router-link to="/">Home</router-link></li>
        <li><router-link to="/campaigns">Campaigns</router-link></li>
        <li><router-link to="/about">About Us</router-link></li>
        <li><router-link to="/faq">FAQ</router-link></li>
      </ul>
    </nav>

    <!-- Show the 'My Account' button or user circle based on login status -->
    <div class="auth-button-container">
      <router-link v-if="!isLoggedIn" to="/auth" class="auth-button">My Account</router-link>

      <!-- User Circle for logged in users -->
      <div v-if="isLoggedIn" class="user-circle" @click="toggleMenu">
        {{ userInitials }}
      </div>
      
      <!-- Dropdown menu for Settings and Logout -->
      <div v-if="menuVisible" class="dropdown-menu">
        <button @click="goToDashboard">Dashboard</button>
        <button @click="goToSettings">Settings</button>
        <button @click="logout">Logout</button>
      </div>
    </div>
  </header>
</template>

<script>
import { mapState, mapMutations } from 'vuex';

export default {
  name: 'AppHeader',
  computed: {
    ...mapState(['isLoggedIn', 'user']), // Access Vuex state for login status and user data
    userInitials() {
      return this.user?.username?.charAt(0).toUpperCase() || 'R'; // Extract initials from Vuex user state
    },
  },
  methods: {
    ...mapMutations(['logoutUser']), // Map Vuex mutation for logout
    toggleMenu() {
      this.menuVisible = !this.menuVisible;
    },
    goToDashboard() {
      this.$router.push({ name: 'Dashboard' });
      this.menuVisible = false;
    },
    goToSettings() {
      this.$router.push({ name: 'Settings' });
      this.menuVisible = false;
    },
    logout() {
      this.logoutUser(); // Call Vuex mutation to clear user data and logout
      this.menuVisible = false;
      this.$router.push({ name: 'Login' });
      this.$store.state.isLoggedIn = false;
    },
  },
  data() {
    return {
      menuVisible: false, // Track dropdown visibility
    };
  },
};
</script>


<style scoped>
.app-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 10px 20px;
  background-color: #f8f9fa;
  box-shadow: inset 0 4px 10px rgba(0, 0, 0, 0.1); /* Inner shadow for depth */
}

.site-title {
  font-size: 1.8em;
  font-weight: bold;
  margin: 0;
  background: linear-gradient(to right, #a70ace, #25e3fc); /* Gradient colors */
  background-clip: text;
  color: transparent; /* Text becomes transparent to show the gradient */
  text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2); /* Add text shadow for punchiness */
}

.nav-list {
  display: flex;
  list-style: none;
  gap: 20px; /* Spacing between navigation items */
  margin: 0;
  padding: 0;
}

.nav-list li {
  font-size: 1em;
}

.nav-list a {
  color: #333; /* Color for links */
  text-decoration: none;
  font-weight: 500;
  padding: 5px 10px;
  border-radius: 5px;
  transition: background-color 0.3s, box-shadow 0.3s;
  text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.2); /* Inner shadow for links */
}

.nav-list a:hover {
  background-color: rgba(0, 0, 0, 0.1); /* Background effect on hover */
  box-shadow: inset 0 4px 10px rgba(0, 0, 0, 0.2); /* Inner shadow on hover */
}

.auth-button-container {
  display: flex;
  align-items: center;
  gap: 10px;
}

.auth-button {
  font-size: 1em;
  font-weight: 600;
  color: #fff;
  text-decoration: none;
  padding: 8px 16px;
  border-radius: 5px;
  background: linear-gradient(to right, #83CFCB, #83CFCB);
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
  transition: transform 0.3s, box-shadow 0.3s;
}

.auth-button:hover {
  transform: scale(1.01);
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
}

/* User Circle Styles */
.user-circle {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background-color: #3498db; /* Circle color */
  color: #fff;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 1.2em;
  font-weight: bold;
  cursor: pointer;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.user-circle:hover {
  transform: scale(1.1); /* Slight scale effect on hover */
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3);
}

/* Dropdown Menu */
.dropdown-menu {
  position: absolute;
  top: 50px;
  right: 10px;
  background-color: #fff;
  color: #000;
  border-radius: 8px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
  display: flex;
  flex-direction: column;
  padding: 10px;
  z-index: 100;
}

.dropdown-menu button {
  background-color: transparent;
  border: none;
  padding: 8px 16px;
  font-size: 1em;
  cursor: pointer;
  text-align: left;
}

.dropdown-menu button:hover {
  background-color: #f1f1f1;
}
</style>
