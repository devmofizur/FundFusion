<template>
  <div class="user-profile">
    <!-- User Info with Create Campaign Button on the same line -->
    <div class="user-info">
      <div class="user-name">
        <h2>Dashboard</h2>
      </div>
    </div>

    <!-- Date Joined and Motivation -->

    <div class="motivation">
      <em>{{ randomMotivation }}</em>
    </div>

    <!-- Create Campaign Button -->
    <div class="create-campaign">
      <p><button @click="createCampaign">Create Campaign</button></p>
    </div>

    <!-- Profile Content Section (Donations, Activity, Created Campaigns) -->
    <div class="profile-content">
      <!-- Donations Section -->
      <div class="donations">
        <h3>Donations ({{ totalDonations }})</h3>
        <div v-if="sortedDonations.length > 0" class="scrollable-content">
          <div
            v-for="(donation, index) in sortedDonations"
            :key="index"
            class="donation-item"
          >
            <p><strong>Campaign:</strong> {{ donation.campaignTitle }}</p>
            <p><strong>Amount Donated:</strong> ${{ donation.amount }}</p>
            <p><strong>Date:</strong> {{ formatDate(donation.date) }}</p>
          </div>
        </div>
        <div v-else>
          <p>You have not made any donations yet.</p>
        </div>
      </div>

      <!-- Activity Graph Section with Time Range Selection -->
      <div class="activity-graph-container">
        <h3>Activity</h3>

        <!-- Time Range Selection (Weekly, Monthly, Yearly) -->
        <div class="time-range-selector">
          <label>
            <input type="radio" value="weekly" v-model="selectedRange" /> Weekly
          </label>
          <label>
            <input type="radio" value="monthly" v-model="selectedRange" />
            Monthly
          </label>
          <label>
            <input type="radio" value="yearly" v-model="selectedRange" /> Yearly
          </label>
        </div>

        <div class="activity-graph">
          <apexchart
            type="heatmap"
            :options="chartOptions"
            :series="chartData"
          ></apexchart>
        </div>
      </div>

      <!-- Created Campaigns Section -->
      <div class="created-campaigns">
        <h3>Created Campaigns ({{ totalCreatedCampaigns }})</h3>
        <p>
          <strong :class="'approved-text'">Approved:</strong>
          {{ approvedCampaigns }}
          <strong :class="'rejected-text'"> Rejected:</strong>
          {{ rejectedCampaigns }}
        </p>
        <div
          v-if="sortedCreatedCampaigns.length > 0"
          class="scrollable-content"
        >
          <div
            v-for="(campaign, index) in sortedCreatedCampaigns"
            :key="index"
            class="campaign-item"
          >
            <h4>{{ campaign.title }}</h4>
            <p>
              <strong>Created on:</strong>
              {{ formatDate(campaign.creationDate) }}
            </p>
            <p><strong>Views:</strong> {{ campaign.views }}</p>
            <p>
              <strong>Status:</strong>
              <span :class="`status ${campaign.status.toLowerCase()}`">{{
                campaign.status
              }}</span>
            </p>
            <p v-if="campaign.status === 'Rejected'" class="notice-box">
              <strong>Reason:</strong> {{ campaign.feedback }}
            </p>
          </div>
        </div>
        <div v-else>
          <p>You have not created any campaigns yet.</p>
        </div>
      </div>
    </div>

    <!-- Profile Settings Modal -->
    <ProfileSettingsModal
      v-if="showSettingsModal"
      :user="user"
      @close="toggleSettingsModal"
      @save="updateProfile"
    />
  </div>
</template>

<script>
import axios from 'axios'
import ProfileSettingsModal from '@/components/User/Settings.vue'
import ApexCharts from 'vue3-apexcharts'

export default {
  components: {
    ProfileSettingsModal,
    apexchart: ApexCharts,
  },
  data() {
    return {
      user: {
        username: '',
        dateJoined: '',
        donations: [
          {
            campaignTitle: 'Save the Forest',
            amount: 50,
            date: '2024-05-10T14:00:00Z',
          },
          {
            campaignTitle: 'Water for All',
            amount: 100,
            date: '2024-06-15T10:30:00Z',
          },
          {
            campaignTitle: 'Help Educate',
            amount: 200,
            date: '2024-07-05T11:45:00Z',
          },
          {
            campaignTitle: 'Support Local Farmers',
            amount: 75,
            date: '2024-08-20T13:00:00Z',
          },
          {
            campaignTitle: 'Clean Rivers',
            amount: 150,
            date: '2024-09-10T09:00:00Z',
          },
          {
            campaignTitle: 'Medical Aid for Rural Areas',
            amount: 250,
            date: '2024-10-25T16:30:00Z',
          },
          {
            campaignTitle: 'Fight Hunger',
            amount: 300,
            date: '2024-11-15T08:00:00Z',
          },
          {
            campaignTitle: 'Flood Relief Fund',
            amount: 500,
            date: '2024-11-22T14:15:00Z',
          },
        ],
      },
      createdCampaigns: [
        {
          title: 'Save the Oceans',
          creationDate: '2024-02-20T08:00:00Z',
          views: 320,
          status: 'Approved',
        },
        {
          title: 'Fight Hunger',
          creationDate: '2024-03-15T09:00:00Z',
          views: 150,
          status: 'Rejected',
          feedback: 'Insufficient details provided',
        },
        {
          title: 'Flood Relief Campaign',
          creationDate: '2024-06-01T10:30:00Z',
          views: 500,
          status: 'Approved',
        },
        {
          title: 'Help Educate',
          creationDate: '2024-07-15T12:00:00Z',
          views: 200,
          status: 'Approved',
        },
        {
          title: 'Support Local Farmers',
          creationDate: '2024-08-05T14:30:00Z',
          views: 180,
          status: 'Approved',
        },
        {
          title: 'Clean Rivers',
          creationDate: '2024-09-15T09:00:00Z',
          views: 300,
          status: 'Approved',
        },
        {
          title: 'Medical Aid for Rural Areas',
          creationDate: '2024-10-05T15:45:00Z',
          views: 250,
          status: 'Approved',
        },
        {
          title: 'Green Bangladesh',
          creationDate: '2024-11-10T11:15:00Z',
          views: 120,
          status: 'Rejected',
          feedback: 'Lack of volunteers',
        },
      ],
      randomMotivation: '',
      selectedRange: 'weekly',
      chartOptions: {
        chart: {
          type: 'heatmap',
        },
        plotOptions: {
          heatmap: {
            colorScale: {
              ranges: [
                { from: 0, to: 5, color: '#f3b7a1', name: 'Low' },
                { from: 6, to: 15, color: '#feb019', name: 'Medium' },
                { from: 16, to: 30, color: '#00e396', name: 'High' },
              ],
            },
          },
        },
        xaxis: {
          categories: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
        },
        title: {
          text: 'Activity Heatmap',
        },
      },
      chartData: [
        {
          name: 'Donations',
          data: [0, 5, 10, 15, 20, 25, 30],
        },
        {
          name: 'Campaigns',
          data: [3, 10, 15, 0, 20, 10, 5],
        },
      ],
      showSettingsModal: false,
    }
  },
  computed: {
    sortedDonations() {
      return [...this.user.donations].sort(
        (a, b) => new Date(b.date) - new Date(a.date),
      )
    },
    sortedCreatedCampaigns() {
      return [...this.createdCampaigns].sort(
        (a, b) => new Date(b.creationDate) - new Date(a.creationDate),
      )
    },
    totalDonations() {
      return this.user.donations.length
    },
    totalCreatedCampaigns() {
      return this.createdCampaigns.length
    },
    approvedCampaigns() {
      return this.createdCampaigns.filter(
        campaign => campaign.status === 'Approved',
      ).length
    },
    rejectedCampaigns() {
      return this.createdCampaigns.filter(
        campaign => campaign.status === 'Rejected',
      ).length
    },
  },
  watch: {
    selectedRange(newRange) {
      this.updateChartData(newRange)
    },
  },
  created() {
    this.generateMotivation()
    this.updateChartData(this.selectedRange)
    this.fetchUserProfile()
  },
  methods: {
    async fetchUserProfile() {
      try {
        const token = localStorage.getItem('access_token')
        const response = await axios.get(
          'http://localhost:8080/api/users/profile/',
          {
            headers: {
              Authorization: `Bearer ${token}`,
            },
          },
        )

        console.log('Full response data:', response.data)

        this.user.username = response.data.username
        this.user.dateJoined = this.formatDate(response.data.date_joined)
      } catch (error) {
        console.error(
          'Error fetching user profile:',
          error.response ? error.response.data : error,
        )
      }
    },
    formatDate(dateString) {
      if (!dateString) return 'N/A'
      try {
        return new Date(dateString).toLocaleDateString()
      } catch {
        return 'Invalid Date'
      }
    },
    generateRandomData(length, min, max) {
      return Array.from(
        { length },
        () => Math.floor(Math.random() * (max - min + 1)) + min,
      )
    },
    createCampaign() {
      this.$router.push({ name: 'CreateCampaign' })
    },
    toggleSettingsModal() {
      this.showSettingsModal = !this.showSettingsModal
    },
    updateProfile(updatedUser) {
      this.user = updatedUser
      this.showSettingsModal = false
    },
    generateMotivation() {
      const motivations = [
        'Every donation counts!',
        'Your generosity changes lives.',
        'Together, we make a difference.',
        'Giving is the greatest act of grace.',
      ]
      this.randomMotivation =
        motivations[Math.floor(Math.random() * motivations.length)]
    },
    updateChartData(range) {
      let newCategories = []
      let newData = []
      if (range === 'weekly') {
        newCategories = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        newData = [
          { name: 'Donations', data: this.generateRandomData(7, 0, 30) },
          { name: 'Campaigns', data: this.generateRandomData(7, 0, 25) },
        ]
      } else if (range === 'monthly') {
        newCategories = ['Week 1', 'Week 2', 'Week 3', 'Week 4']
        newData = [
          { name: 'Donations', data: this.generateRandomData(4, 50, 200) },
          { name: 'Campaigns', data: this.generateRandomData(4, 30, 150) },
        ]
      } else if (range === 'yearly') {
        newCategories = [
          'Jan',
          'Feb',
          'Mar',
          'Apr',
          'May',
          'Jun',
          'Jul',
          'Aug',
          'Sep',
          'Oct',
          'Nov',
          'Dec',
        ]
        newData = [
          { name: 'Donations', data: this.generateRandomData(12, 500, 2000) },
          { name: 'Campaigns', data: this.generateRandomData(12, 300, 1500) },
        ]
      }
      const updatedOptions = {
        ...this.chartOptions,
        xaxis: { ...this.chartOptions.xaxis, categories: newCategories },
      }
      this.chartData = newData
      this.chartOptions = updatedOptions
      this.$nextTick(() => {
        if (this.$refs.chart) {
          this.$refs.chart.updateOptions(updatedOptions, true)
        }
      })
    },
  },
}
</script>

<style scoped>
/* Add the styles for the time range selector */
.time-range-selector {
  margin-bottom: 20px;
  display: flex;
  gap: 15px;
}

.time-range-selector label {
  font-size: 1.1em;
  cursor: pointer;
}

.time-range-selector input {
  margin-right: 5px;
}

.user-profile {
  padding: 30px;
  background-color: #f4f6f9;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  max-width: 100%;
  width: 100%;
  margin: 0 auto;
  box-sizing: border-box;
}

.user-info {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 15px;
}

.user-name h2 {
  font-size: 2.2em;
  color: #333;
  font-weight: 600;
}

.date-joined {
  font-size: 1.1em;
  color: #555;
  margin-top: 10px;
}

.motivation {
  font-size: 1.2em;
  color: #4caf50;
  margin-top: 10px;
  font-style: italic;
}

.create-campaign {
  margin-top: 20px;
  text-align: center;
}

.create-campaign button {
  padding: 12px 25px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 1.2em;
  transition: background-color 0.3s;
}

.create-campaign button:hover {
  background-color: #0056b3;
}

.profile-content {
  display: flex;
  justify-content: space-between;
  gap: 20px;
  flex-wrap: wrap;
}

.donations,
.created-campaigns {
  flex: 1;
  background-color: #fff;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.donations h3,
.created-campaigns h3 {
  font-size: 1.5em;
  margin-bottom: 15px;
  color: #333;
}

.donation-item,
.campaign-item {
  background-color: #f9f9f9;
  padding: 15px;
  margin-bottom: 10px;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.campaign-item h4 {
  font-size: 1.3em;
  color: #333;
}

.notice-box {
  background-color: #f8d7da;
  padding: 10px;
  margin-top: 10px;
  border-radius: 5px;
  color: #721c24;
}

.status {
  font-weight: bold;
}

.status.approved,
.approved-text {
  color: #28a745;
}

.status.rejected,
.rejected-text {
  color: #dc3545;
}

.activity-graph-container {
  flex: 1;
  background-color: #fff;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.activity-graph {
  height: 350px;
}
/* Scrollable container for Donations and Created Campaigns */
.scrollable-content {
  max-height: 300px; /* Set a fixed height for the scrollable area */
  overflow-y: auto; /* Enable vertical scrolling */
  padding-right: 10px; /* Avoid content clipping near the scrollbar */
}

/* Optional: Customize scrollbar appearance for better UX */
.scrollable-content::-webkit-scrollbar {
  width: 8px;
}

.scrollable-content::-webkit-scrollbar-thumb {
  background-color: #ccc; /* Color of the scrollbar thumb */
  border-radius: 10px;
}

.scrollable-content::-webkit-scrollbar-thumb:hover {
  background-color: #aaa; /* Darker color on hover */
}

.scrollable-content::-webkit-scrollbar-track {
  background-color: #f9f9f9; /* Track background */
}

@media (max-width: 768px) {
  .profile-content {
    flex-direction: column;
    gap: 15px;
  }

  .user-name h2 {
    font-size: 1.8em;
  }
}
</style>
