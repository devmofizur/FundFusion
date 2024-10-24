
<template>
  <div class="campaign-card">
    <h3>{{ campaign.title }}</h3>
    <p>{{ campaign.description }}</p>
    <p>Goal: {{ campaign.goal_amount }}</p>
    <p>Raised: {{ campaign.current_amount }}</p>
    <router-link :to="`/campaigns/${campaign.id}`">View Details</router-link>
  </div>
</template>

<script>
export default {
  props: {
    campaign: Object
  }
}
</script>

<style scoped>
.campaign-card {
  border: 1px solid #ccc;
  padding: 10px;
  margin: 10px;
}
</style>
  