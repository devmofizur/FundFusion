<template>
  <div>
    <h1 class="heading">All Campaigns</h1>

    <!-- Search Bar -->
    <div class="search-bar">
      <input
        v-model="searchQuery"
        type="text"
        placeholder="Search campaigns..."
        class="search-input"
      />
    </div>

    <!-- Display the list view -->
    <div class="campaign-container list-view">
      <div
        class="campaign-card list-item"
        v-for="(campaign, index) in filteredCampaigns"
        :key="index"
      >
        <div class="left-side">
          <img :src="campaign.bannerImage" alt="Campaign Image" class="campaign-image" />
        </div>
        <div class="divider"></div>
        <div class="right-side">
          <h3 class="campaign-title">{{ campaign.title }}</h3>
          <div class="campaign-stats">
            <span class="raised-amount">Raised: ${{ campaign.current_amount }}</span>
            <button class="donate-button" @click="donate(campaign.id)">View</button>
            <span class="target-amount">Goal: ${{ campaign.goal_amount }}</span>
          </div>
          
          <!-- Display the campaign location -->
          <p class="campaign-location"><strong>Location:</strong> {{ campaign.location }}</p>
          <div class="progress-container">
            <div
              class="progress-bar"
              :style="{
                width: `${calculateProgress(campaign.current_amount, campaign.goal_amount)}%` 
              }"
            ></div>
          </div>
          <p class="campaign-description">{{ campaign.description }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// Import CampaignList which contains the campaign data
import CampaignList from '../components/Campaign/CampaignList.vue';

export default {
  name: 'AllCampaigns',
  data() {
    return {
      campaigns: [], // Will hold the campaigns imported from CampaignList
      searchQuery: '', // Holds the query for search
    };
  },
  created() {
    // Initialize campaigns from CampaignList
    this.campaigns = CampaignList.data().campaigns;
  },
  
  computed: {
    // Computed property to filter campaigns based on search query
    filteredCampaigns() {
      const query = this.searchQuery.toLowerCase();
      return this.campaigns.filter((campaign) =>
        campaign.title.toLowerCase().includes(query) ||
        campaign.description.toLowerCase().includes(query) ||
        campaign.location.toLowerCase().includes(query)
      );
    },
  },
  methods: {
    // Calculate progress as a percentage
    calculateProgress(current, goal) {
      return Math.min((current / goal) * 100, 100); // Ensure progress does not exceed 100%
    },
    // Method for handling donations (e.g., redirect to donation page)
    donate(campaignId) {
      // Redirect to a donation page with campaignId
      this.$router.push({ name: 'Donate', params: { campaignId: campaignId } });
    },
  },
};
</script>

<style scoped>
.heading {
  padding: 20px;
  background-color: rgba(232, 240, 250, 1);  /* Light grayish blue */
}

/* Search Bar */
.search-bar {
  padding: 10px;
  text-align: center;
  background-color: rgba(240, 240, 240, 1);  /* Light gray */
  margin-bottom: 20px;
}

.search-input {
  width: 80%;
  padding: 10px;
  font-size: 1.1em;
  border-radius: 5px;
  border: 1px solid #ccc;
  outline: none;
}

.search-input:focus {
  border-color: #4caf50;
}

/* Campaign Container */
.campaign-container {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

/* List View Styles */
.list-view {
  flex-direction: column;
}

.list-item {
  display: flex;
  align-items: center;
  height: 260px;
  padding: 15px;
  border-radius: 2px;
  background-color: rgba(131, 151, 147, 0.705);
  margin-bottom: 20px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
}

.left-side {
  flex: 1;
  padding-right: 10px;
}

.campaign-image {
  width: 100%;
  height: 240px; /* Fixed height */
  object-fit: cover; /* Crop and maintain aspect ratio */
  border-radius: 2px;
}

.divider {
  border-left: 3px solid #000000;
  margin: 0 20px;
  height: 100%;
}

.right-side {
  flex: 2;
}

.campaign-title {
  font-size: 1.5em;
  font-weight: bold;
  color: #000000;
  margin-bottom: 10px;
}

.campaign-stats {
  font-size: 1em;
  margin-bottom: 10px;
  color: #34495e;
}

.campaign-location {
  font-size: 1em;
  color: #ffffff;
  margin-bottom: 10px;
  align-content: center;
}

.campaign-description {
  font-size: 1em;
  color: #474747;
  margin-top: 10px;
  padding: 10px;
  background-color: #f8f8f8;
  border-radius: 2px;
  text-align: justify; /* Justified text */
}

/* Progress Bar Styles */
.progress-container {
  background: #e0e0e0;
  border-radius: 10px;
  height: 10px;
  margin-top: 10px;
}

.progress-bar {
  background: #60e464;
  height: 100%;
  transition: width 0.4s ease;
}

/* Donate Button Styles */
.donate-button {
  padding: 10px 20px;
  font-size: 1.1em;
  background-color: #4caf50;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.donate-button:hover {
  background-color: #45a082;
}
</style>
