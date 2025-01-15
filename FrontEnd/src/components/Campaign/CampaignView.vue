<template>
  <div>
    <h1>Campaigns</h1>
    
    <!-- View toggle for List/Grid -->
    <div class="view-toggle">
      <span v-if="!isGridView" @click="setGridView" class="view-icon">
        <img src="@/assets/grid-icon.svg" alt="Grid View" />
      </span>
      <span v-if="isGridView" @click="setListView" class="view-icon">
        <img src="@/assets/list-icon.svg" alt="List View" />
      </span>
    </div>
    
    <!-- Use the CampaignList component and pass the event to set campaigns -->
    <CampaignList @campaigns-loaded="setCampaigns" />
    
    <!-- Display the grid view -->
    <div v-if="isGridView" class="campaign-container">
      <div
        class="campaign-card grid-item"
        v-for="(campaign, index) in campaigns"
        :key="index"
        :style="{ backgroundImage: `url(${campaign.bannerImage})` }"
      >
        <div class="overlay">
          <h3 class="campaign-title">{{ campaign.title }}</h3>
          <div class="campaign-stats">
            <span class="raised-amount">{{ campaign.current_amount }}</span> |
            <span class="target-amount">{{ campaign.goal_amount }}</span>
          </div>
        </div>
      </div>
    </div>
    
    <!-- Display the list view -->
    <div v-else class="campaign-container list-view">
      <div
        class="campaign-card list-item"
        v-for="(campaign, index) in campaigns"
        :key="index"
      >
        <div class="left-side">
          <img :src="campaign.bannerImage" alt="Campaign Image" class="campaign-image" />
        </div>
        <div class="divider"></div>
        <div class="right-side">
          <h3 class="campaign-title">{{ campaign.title }}</h3>
          <div class="campaign-stats">
            <span class="raised-amount">{{ campaign.current_amount }}</span> 
            <span class="target-amount">{{ campaign.goal_amount }}</span>
          </div>
          <p class="campaign-description">{{ campaign.description }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import CampaignList from './CampaignList.vue';

export default {
  components: {
    CampaignList,
  },
  data() {
    return {
      isGridView: true, // Default view mode is Grid View
      campaigns: [], // Campaign data will be populated from CampaignList
    };
  },
  methods: {
    setGridView() {
      this.isGridView = true;
    },
    setListView() {
      this.isGridView = false;
    },
    setCampaigns(campaigns) {
      this.campaigns = campaigns;
    },
  },
};
</script>


<style scoped>
.view-toggle {
  margin-bottom: 20px;
  display: flex;
  justify-content: flex-end;
}

.view-icon {
  cursor: pointer;
  margin-left: 15px;
}

.view-icon img {
  width: 30px;
  height: 30px;
  transition: transform 0.3s;
}

.view-icon:hover img {
  transform: scale(1.05);
}

.campaign-container {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}

/* Grid View Styles */
.grid-item {
  background-size: cover;
  background-position: center;
  height: 100px; /* Adjust as needed */
  border-radius: 15px;
  position: relative;
  display: flex;
  align-items: center; /* Vertically center the content */
  justify-content: center; /* Horizontally center the content */
  color: rgb(255, 255, 255);
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.5);
  overflow: hidden;
}

.overlay {
  position: absolute; /* Position the overlay absolutely within the parent */
  top: 0; /* Align it to the top */
  left: 0; /* Align it to the left */
  right: 0; /* Align it to the right */
  bottom: 0; /* Stretch it to the bottom */
  background: rgba(0, 0, 0, 0.5); /* Dark overlay for better text visibility */
  padding: 20px; /* Maintain padding around the content */
  text-align: center; /* Justify the text */
  z-index: 1; /* Ensure it's above other content */
}

.campaign-title,
.campaign-stats {
  margin: 0; /* Remove any default margin that might push text upwards */
}

/* List View Styles */
.list-view {
  flex-direction: column;
}

.list-item {
  display: flex;
  align-items: center;
  height: 240px;
  padding: 15px;
  border-radius: 8px;
  background-color: rgb(128, 158, 187);
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
  border-radius: 8px;
}

.divider {
  border-left: 3px solid #34495e;
  margin: 0 20px;
  height: 100%;
}

.right-side {
  flex: 2;
}

.campaign-description {
  font-size: 1em;
  color: #474747;
  margin-top: 10px;
  padding: 10px;
  background-color: #f8f8f8;
  border-radius: 8px;
  text-align: justify; /* Justified text */
}
</style>
