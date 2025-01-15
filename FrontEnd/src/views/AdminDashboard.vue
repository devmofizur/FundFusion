<template>
  <div class="admin-dashboard">
    <!-- Dashboard Header -->
    <header class="dashboard-header">
      <h1>Admin Dashboard</h1>
    </header>

    <!-- Navigation Panel -->
    <nav class="dashboard-nav">
      <ul>
        <li><a href="#campaign-approval" class="nav-item">Campaign Approval</a></li>
        <li><a href="#user-management" class="nav-item">User Management</a></li>
        <li><a href="#canceled-campaigns" class="nav-item">Canceled Campaigns</a></li>
      </ul>
    </nav>

    <!-- Main Content -->
    <main class="dashboard-content">
      <!-- Campaign Approval Section -->
      <section id="campaign-approval">
        <h2>Campaign Approval</h2>
        <p>Review and manage campaigns pending approval.</p>
        <div class="pending-campaigns-table">
          <table>
            <thead>
              <tr>
                <th>Campaign Title</th>
                <th>Owner</th>
                <th>Amount Raised</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="campaign in pendingCampaigns" :key="campaign.id">
                <td>{{ campaign.title }}</td>
                <td>{{ campaign.owner }}</td>
                <td>{{ campaign.amountRaised }}</td>
                <td>
                  <button @click="viewCampaignDetails(campaign)" class="view-btn">View</button>
                  <button @click="approveCampaign(campaign.id)" class="approve-btn">Approve</button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>

      <!-- User Management Section -->
      <section id="user-management">
        <h2>User Management</h2>
        <p>Manage registered users of the platform.</p>
        <div class="user-management-table">
          <table>
            <thead>
              <tr>
                <th>User ID</th>
                <th>Username</th>
                <th>Email</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="user in users" :key="user.id">
                <td>{{ user.id }}</td>
                <td>{{ user.username }}</td>
                <td>{{ user.email }}</td>
                <td>
                  <button @click="viewUserDetails(user)" class="view-btn">View</button>
                  <button @click="deleteUser(user.id)" class="delete-btn">Delete</button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>

      <!-- Canceled Campaigns Section -->
      <section id="canceled-campaigns">
        <h2>Canceled Campaigns Log</h2>
        <p>View the log of canceled campaigns.</p>
        <div class="canceled-campaigns-table">
          <table>
            <thead>
              <tr>
                <th>Campaign Title</th>
                <th>Owner</th>
                <th>Reason</th>
                <th>Date Canceled</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="campaign in canceledCampaigns" :key="campaign.id">
                <td>{{ campaign.title }}</td>
                <td>{{ campaign.owner }}</td>
                <td>{{ campaign.reason }}</td>
                <td>{{ campaign.date }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>
    </main>

    <!-- Campaign Details Modal -->
    <div v-if="selectedCampaign" class="modal-overlay">
      <div class="modal-content">
        <h3>Campaign Details</h3>
        <p><strong>Title:</strong> {{ selectedCampaign.title }}</p>
        <p><strong>Owner:</strong> {{ selectedCampaign.owner }}</p>
        <p><strong>Amount Raised:</strong> {{ selectedCampaign.amountRaised }}</p>
        <p><strong>Description:</strong> {{ selectedCampaign.description }}</p>
        <p><strong>Goal:</strong> {{ selectedCampaign.goalAmount }}</p>
        <button @click="closeModal" class="close-modal-btn">Close</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      pendingCampaigns: [
        { id: 1, title: 'Plant Trees in Dhaka', owner: 'tanvir_ahmed', amountRaised: 20000, goalAmount: 50000, description: 'Plant trees to improve air quality in Dhaka.' },
        { id: 2, title: 'Flood Relief in Sylhet', owner: 'rahima_khatun', amountRaised: 15000, goalAmount: 40000, description: 'Provide relief materials to flood-affected areas.' },
      ],
      canceledCampaigns: [
        { id: 1, title: 'Support for Rohingya Refugees', owner: 'kabir_hasan', reason: 'Insufficient donations', date: '2024-12-10' },
        { id: 2, title: 'Clean Cox’s Bazar Beach', owner: 'sharmin_akter', reason: 'Campaigner withdrawal', date: '2024-11-25' },
      ],
      users: [
        { id: 1, username: 'tanvir_ahmed', email: 'tanvir@gmail.com' },
        { id: 2, username: 'rahima_khatun', email: 'rahima@gmail.com' },
        { id: 3, username: 'kabir_hasan', email: 'kabir@gmail.com' },
        { id: 4, username: 'sharmin_akter', email: 'sharmin@gmail.com' },
      ],
      selectedCampaign: null, // Stores the campaign selected for viewing
    };
  },
  methods: {
    // Approve a campaign
    approveCampaign(campaignId) {
      this.pendingCampaigns = this.pendingCampaigns.filter(campaign => campaign.id !== campaignId);
      alert(`Campaign ID ${campaignId} approved!`);
    },
    // View campaign details
    viewCampaignDetails(campaign) {
      this.selectedCampaign = campaign;
    },
    // Delete a user
    deleteUser(userId) {
      this.users = this.users.filter(user => user.id !== userId);
      alert(`User ID ${userId} deleted!`);
    },
    // Close the modal
    closeModal() {
      this.selectedCampaign = null;
    },
  },
};
</script>

<style scoped>
/* General Styles */
.dashboard-content section {
  margin-bottom: 30px;
}

/* Navigation Panel Styles */
.dashboard-nav {
  background-color: #3c84d6;
  padding: 15px;
  border-radius: 8px;
  margin-bottom: 20px;
}

.dashboard-nav ul {
  display: flex;
  list-style-type: none;
  justify-content: space-around;
  padding: 0;
}

.dashboard-nav ul li {
  margin: 0;
}

.dashboard-nav .nav-item {
  color: white;
  text-decoration: none;
  font-weight: bold;
  padding: 10px 15px;
  border-radius: 5px;
  transition: background-color 0.3s ease;
}

.dashboard-nav .nav-item:hover {
  background-color: #2b6ea3;
}

/* Modal Styles */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal-content {
  background: white;
  padding: 20px;
  border-radius: 8px;
  width: 400px;
  text-align: center;
}

.close-modal-btn {
  background-color: #3c84d6;
  color: white;
  padding: 10px 15px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.close-modal-btn:hover {
  background-color: #2b6ea3;
}

/* Table Styles */
table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 15px;
}

table th, table td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: left;
}

table th {
  background-color: #3c84d6;
  color: white;
}

.view-btn, .approve-btn, .delete-btn {
  background-color: #3c84d6;
  color: white;
  padding: 5px 10px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.view-btn:hover, .approve-btn:hover, .delete-btn:hover {
  background-color: #2b6ea3;
}
</style>
