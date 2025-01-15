<template>
  <div class="auth-page">
    <div class="auth-container">
      <h2>Forgot Password</h2>

      <div v-if="step === 1" class="forgot-password-step">
        <form @submit.prevent="sendOTP">
          <input type="email" v-model="email" placeholder="Enter your email" required />
          <button type="submit">Send OTP</button>
        </form>
      </div>

      <div v-if="step === 2" class="forgot-password-step">
        <form @submit.prevent="verifyOTP">
          <input type="text" v-model="otp" placeholder="Enter OTP" required />
          <button type="submit">Verify OTP</button>
        </form>
        <p v-if="otpError" style="color: red;">{{ otpError }}</p>
      </div>

      <div v-if="step === 3" class="forgot-password-step">
        <form @submit.prevent="resetPassword">
          <input type="password" v-model="newPassword" placeholder="Enter new password" required />
          <input type="password" v-model="confirmPassword" placeholder="Confirm new password" required />
          <button type="submit">Reset Password</button>
        </form>
        <p v-if="passwordError" style="color: red;">{{ passwordError }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      email: '',
      otp: '',
      newPassword: '',
      confirmPassword: '',
      step: 1, // 1 = Enter email, 2 = Verify OTP, 3 = Reset Password
      otpError: '',
      passwordError: '',
    };
  },
  methods: {
    // Step 1: Send OTP
    sendOTP() {
      this.otpError = '';
      this.passwordError = '';

      // Simulate sending OTP (this would usually be an API call)
      console.log(`Sending OTP to ${this.email}`);
      setTimeout(() => {
        this.step = 2; // Move to OTP verification step
      }, 1000);
    },

    // Step 2: Verify OTP
    verifyOTP() {
      this.otpError = '';
      this.passwordError = '';

      if (!this.otp) {
        this.otpError = 'OTP is required.';
        return;
      }

      // Simulate OTP verification (this would usually be an API call)
      if (this.otp === '123456') { // Example OTP, you would compare this to the server's OTP
        this.step = 3; // Move to password reset step
      } else {
        this.otpError = 'Invalid OTP.';
      }
    },

    // Step 3: Reset Password
    resetPassword() {
      this.passwordError = '';

      if (this.newPassword !== this.confirmPassword) {
        this.passwordError = 'Passwords do not match.';
        return;
      }

      // Simulate password reset (this would usually be an API call)
      console.log(`Resetting password to ${this.newPassword}`);
      setTimeout(() => {
        alert('Password reset successfully!');
        this.$router.push('/login'); // Redirect to login page
      }, 1000);
    }
  }
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
  text-align: center;
}

.auth-container h2 {
  margin-bottom: 20px;
  font-size: 24px;
}

.auth-container form {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.auth-container form input {
  padding: 10px;
  margin-bottom: 15px;
  border: 1px solid #ccc;
  border-radius: 5px;
  width: 100%;
  box-sizing: border-box;
}

.auth-container form button {
  padding: 10px;
  background: linear-gradient(to right, #83CFCB, #83CFCB);
  color: #fff;
  border: none;
  border-radius: 5px;
  font-weight: bold;
  cursor: pointer;
  transition: transform 0.3s, background-color 0.3s;
  width: 100%;
  box-sizing: border-box;
}

.auth-container form button:hover {
  transform: scale(1.05);
  background: linear-gradient(to right, #83CFCB, #83CFCB);
}

.forgot-password-step {
  margin-bottom: 20px;
}

/* Error message */
p {
  color: red;
  font-size: 14px;
  margin-top: 10px;
}
</style>
