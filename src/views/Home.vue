<template>
  <div class="home-view">
    <h1 class="home-title">Welcome to Fund Fusion</h1>
    <p class="home-introduction">
      Discover various campaigns that are making a difference. Join us in supporting causes that matter to you!
    </p>
    <CampaignList />
  </div>
</template>

<script>
import CampaignList from '../components/Campaign/CampaignView.vue'

export default {
  name: 'HomeView',
  components: {
    CampaignList,
  },
}
</script>

<style scoped>
.home-view {
  padding: 20px; /* Add some padding */
  background-color: #f9f9f9; /* Light background for a clean look */
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1); /* Subtle shadow for depth */
}

.home-title {
  font-size: 2.5em; /* Larger title */
  color: #2c3e50; /* Dark color for contrast */
  margin-bottom: 10px; /* Space below title */
  text-align: center; /* Center title */
}

.home-introduction {
  font-size: 1.2em; /* Slightly larger text for introduction */
  color: #34495e; /* A softer dark color */
  margin-bottom: 20px; /* Space below introduction */
  text-align: center; /* Center introduction text */
}
</style>
