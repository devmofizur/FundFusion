<template>
    <div>
      <h1>Campaigns</h1>
      <div class="view-toggle">
        <!-- Show Grid View button only if in List View -->
        <span
          v-if="!isGridView"
          @click="setGridView"
          class="view-icon"
        >
          <img src="@/assets/grid-icon.svg" alt="Grid View" />
        </span>
        <!-- Show List View button only if in Grid View -->
        <span
          v-if="isGridView"
          @click="setListView"
          class="view-icon"
        >
          <img src="@/assets/list-icon.svg" alt="List View" />
        </span>
      </div>
      <!-- Display the grid view -->
      <div v-if="isGridView" class="campaign-container">
        <div
          class="campaign-card"
          v-for="(campaign, index) in campaigns"
          :key="index"
          @mouseover="showDescription[index] = true"
          @mouseleave="showDescription[index] = false"
        >
          <h3 class="campaign-title">{{ campaign.title }}</h3>
          <div class="campaign-stats">
            <span class="raised-amount">{{ campaign.raisedAmount }}</span> /
            <span class="target-amount">{{ campaign.targetAmount }}</span>
          </div>
        </div>
      </div>
      <!-- Display the list view -->
      <div v-else class="campaign-container list-view">
        <div
          class="campaign-card"
          v-for="(campaign, index) in campaigns"
          :key="index"
          @mouseover="showDescription[index] = true"
          @mouseleave="showDescription[index] = false"
        >
          <h3 class="campaign-title">{{ campaign.title }}</h3>
          <div class="campaign-stats">
            <span class="raised-amount">{{ campaign.raisedAmount }}</span> /
            <span class="target-amount">{{ campaign.targetAmount }}</span>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        isGridView: true,
        showDescription: [],
        campaigns: [
          { title: 'Campaign 1', raisedAmount: 300, targetAmount: 1000 },
          { title: 'Campaign 2', raisedAmount: 500, targetAmount: 1500 },
          { title: 'Campaign 3', raisedAmount: 200, targetAmount: 800 },
          { title: 'Campaign 4', raisedAmount: 700, targetAmount: 1200 },
        ],
      }
    },
    methods: {
      setGridView() {
        this.isGridView = true
      },
      setListView() {
        this.isGridView = false
      },
    },
  }
  </script>
  
  <style scoped>
  .view-toggle {
    margin-bottom: 20px;
    display: flex;
    justify-content: flex-end; /* Align icons to the right */
  }
  
  .view-icon {
    cursor: pointer;
    margin-left: 15px; /* Space between icons */
  }
  
  .view-icon img {
    width: 30px; /* Adjust the size of the icons */
    height: 30px;
    transition: transform 0.3s; /* Transition for hover effect */
  }
  
  .view-icon:hover img {
    transform: scale(1.1); /* Slightly enlarge the icon on hover */
  }
  
  .campaign-container {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
  }
  
  .campaign-card {
    background-color: rgb(231, 243, 212);
    border-radius: 25px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    padding: 20px;
    transition: transform 0.3s;
    position: relative; /* Required for positioning the description box */
  }
  
  .campaign-card:hover {
    transform: scale(1.05);
  }
  
  .campaign-title {
    font-size: 1.5em;
    margin-bottom: 10px;
    color: #2c3e50;
  }
  
  .campaign-stats {
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 1.2em;
    color: #34495e;
    margin-bottom: 10px;
  }
  
  .raised-amount {
    font-weight: bold;
    color: #2c3e50;
  }
  
  .target-amount {
    color: #e74c3c;
    font-weight: bold;
  }
  
  /* List view specific styles */
  .list-view {
    flex-direction: column; /* Stack items vertically */
  }
  
  .campaign-card.list-view {
    width: 100%; /* Full width for list view */
  }
  </style>
  