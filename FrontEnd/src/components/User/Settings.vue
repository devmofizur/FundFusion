<template>
  <div class="settings-container">
    <!-- Header Section -->
    <div class="settings-header">
      <h2>Settings</h2>
      <p>Manage your profile, account preferences, and notifications.</p>
    </div>

    <form @submit.prevent="saveSettings" class="settings-form">
      <!-- Profile and Password Settings side by side -->
      <div class="form-row">
        <!-- Profile Settings -->
        <div class="form-section profile-section">
          <h3>Profile Information</h3>
          <label for="name">Name</label>
          <input type="text" id="name" v-model="formData.name" placeholder="Enter your name" />

          <label for="email">Email</label>
          <input type="email" id="email" v-model="formData.email" placeholder="Enter your email" />
          
          <label for="bio">Bio</label>
          <textarea
            id="bio"
            v-model="formData.bio"
            placeholder="Tell us about yourself"
            rows="4"
          ></textarea>
        </div>

        <!-- Change Password Settings -->
        <div class="form-section password-section">
          <h3>Change Password</h3>
          <label for="current-password">Current Password</label>
          <input
            type="password"
            id="current-password"
            v-model="passwordData.currentPassword"
            placeholder="Enter your current password"
          />

          <label for="new-password">New Password</label>
          <input
            type="password"
            id="new-password"
            v-model="passwordData.newPassword"
            placeholder="Enter a new password"
          />

          <label for="confirm-password">Confirm New Password</label>
          <input
            type="password"
            id="confirm-password"
            v-model="passwordData.confirmPassword"
            placeholder="Confirm your new password"
          />
        </div>
      </div>

      <!-- Save and Reset Buttons -->
      <div class="form-actions">
        <button type="submit" class="settings-save-button">Save Changes</button>
        <button type="button" class="settings-reset-button" @click="resetSettings">
          Reset to Default
        </button>
      </div>
    </form>
  </div>
</template>



<script>
export default {
  name: "UserSettings", // Updated component name
  data() {
    return {
      formData: {
        name: "Rahim Ahmed",
        email: "rahim.ahmed@example.com",
        bio: "An active campaigner for change.",
        notifications: {
          email: true,
          sms: false,
          push: true,
        },
      },
      passwordData: {
        currentPassword: "",
        newPassword: "",
        confirmPassword: "",
      },
      defaultData: {},
    };
  },
  mounted() {
    // Save a copy of the default data to reset later
    this.defaultData = JSON.parse(JSON.stringify(this.formData));
  },
  methods: {
    saveSettings() {
      if (this.passwordData.newPassword && this.passwordData.newPassword !== this.passwordData.confirmPassword) {
        alert("New password and confirmation do not match.");
        return;
      }

      if (this.passwordData.currentPassword && this.passwordData.newPassword) {
        alert("Password changed successfully!");
        console.log("Password Changed to:", this.passwordData.newPassword);
      }
      
      alert("Settings saved successfully!");
      console.log("Saved Settings:", this.formData);
    },
    resetSettings() {
      this.formData = JSON.parse(JSON.stringify(this.defaultData));
      this.passwordData = { currentPassword: "", newPassword: "", confirmPassword: "" };
    },
  },
};
</script>
<style scoped>
/* General Styling */
body {
  font-family: 'Inter', Arial, sans-serif;
}

/* Container */
.settings-container {
  padding: 30px;
  max-width: 950px;
  width: 100%;
  margin: 20px auto;
  background: linear-gradient(145deg, #ffffff, #d7f1cb);
  border-radius: 15px;
  box-shadow: 0 8px 15px rgba(0, 0, 0, 0.1);
  
}

.settings-header {
  text-align: center;
  margin-bottom: 30px;
}

.settings-header h2 {
  font-size: 2.4rem;
  color: #333;
  font-weight: 700;
}

.settings-header p {
  font-size: 1rem;
  color: #666;
}

/* Form Styling */
.settings-form {
  display: flex;
  flex-direction: column;
  gap: 25px;
  
}

.form-row {
  display: flex;
  gap: 20px;
  justify-content: space-between;
  
}

.form-section {
  flex: 1;
  padding: 20px;
  background-color: #ffffff;
  border-radius: 12px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
  transition: box-shadow 0.3s;
}


.form-section:hover {
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
}

.form-section h3 {
  font-size: 1.4rem;
  color: #333;
  margin-bottom: 20px;
}

.settings-form label {
  font-size: 1rem;
  color: #555;
  margin-bottom: 8px;
  text-align: left;
  margin-bottom: 5px;
  display: block;
}

.settings-form input,
.settings-form textarea {
  width: 90%;
  padding: 12px 15px;
  border: 1px solid #ccc;
  border-radius: 8px;
  font-size: 1rem;
  color: #333;
  box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.05);
  margin-bottom: 15px;
  transition: border-color 0.3s, box-shadow 0.3s;
}

.settings-form input:focus,
.settings-form textarea:focus {
  border-color: #3498db;
  box-shadow: 0 0 5px rgba(52, 152, 219, 0.5);
  outline: none;
}

.settings-form input[type="checkbox"] {
  margin-right: 10px;
}

.divider {
  height: 1px;
  background-color: #eee;
  border: none;
  margin: 25px 0;
}

/* Actions */
.form-actions {
  display: flex;
  gap: 20px;
}

.settings-save-button,
.settings-reset-button {
  flex: 1;
  padding: 15px;
  font-size: 1.1rem;
  font-weight: bold;
  border: none;
  border-radius: 10px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.settings-save-button {
  background-color: #3498db;
  color: white;
}

.settings-save-button:hover {
  background-color: #2980b9;
  transform: translateY(-2px);
}

.settings-reset-button {
  background-color: #e74c3c;
  color: white;
}

.settings-reset-button:hover {
  background-color: #c0392b;
  transform: translateY(-2px);
}

/* Responsive Styling */
@media (max-width: 768px) {
  .form-row {
    flex-direction: column;
  }
}
</style>
