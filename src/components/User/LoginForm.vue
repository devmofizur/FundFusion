
<template>
  <form @submit.prevent="login">
    <div>
      <label for="username">Username:</label>
      <input v-model="username" type="text" id="username" required />
    </div>
    <div>
      <label for="password">Password:</label>
      <input v-model="password" type="password" id="password" required />
    </div>
    <button type="submit">Login</button>
    <p v-if="error" class="error">{{ error }}</p>
  </form>
</template>

<script>
export default {
  data() {
    return {
      username: '',
      password: '',
      error: null
    };
  },
  methods: {
    async login() {
      try {
        await this.$store.dispatch('login', { username: this.username, password: this.password });
        this.$router.push({ name: 'Home' });
      } catch (e) {
        this.error = 'Invalid credentials';
      }
    }
  }
}
</script>

<style scoped>
.error {
  color: red;
}
</style>
  