<template>
  <div>
    <div class="campaign-container">
      <div
        class="campaign-card"
        v-for="(campaign, index) in topCampaigns"
        :key="index"
        :style="{ backgroundImage: `url(${campaign.bannerImage})` }"
      >
        <div class="overlay">
          <h3 class="campaign-title">{{ campaign.title }}</h3>

          <!-- Campaign Location -->
          <p class="campaign-location">{{ campaign.location }}</p>

          <!-- Progress Bar -->
          <div class="progress-container">
            <div
              class="progress-bar"
              :style="{
                width: `${calculateProgress(campaign.current_amount, campaign.goal_amount)}%`,
              }"
            ></div>
          </div>
          <div class="progress-text">
            <span>Raised: ${{ campaign.current_amount }}</span>
            <span>Goal: ${{ campaign.goal_amount }}</span>
          </div>

          <!-- Donate Button -->
          <button class="donate-btn" @click="donate(campaign.id)">
            View
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CampaignList',
  data() {
    return {
      campaigns: [
        // Sample campaigns, update with real data if needed
        {
          id: 1,
          title: 'Help Build a School in Rural Area',
          goal_amount: 5000,
          current_amount: 1200,
          description: 'This campaign aims to address the urgent need for educational infrastructure in remote and underserved communities. Many rural areas lack proper school buildings, leaving children without a safe and conducive environment to learn. This campaign seeks to raise funds and gather resources to construct schools equipped with classrooms, libraries, and basic amenities such as clean water and sanitation facilities. By building schools in these areas, we aim to provide children with access to education, improve literacy rates, and empower local communities for a brighter and more sustainable future.',
          location: 'Rural Village, India',
          bannerImage: new URL('@/assets/campaign_banner/school.jpg', import.meta.url).href,
          views: 150,
        },
        {
  id: 2,
  title: 'Provide Clean Drinking Water',
  goal_amount: 3000,
  current_amount: 800,
  description: 'Millions lack access to clean drinking water, leading to preventable diseases and suffering. Our campaign focuses on bringing safe, potable water to underprivileged communities in Sub-Saharan Africa. With your help, we can build sustainable water sources like wells and filtration systems. Every contribution brings us closer to a future where children and families no longer endure waterborne illnesses. Your support not only provides water but also transforms lives by improving health, education, and livelihoods in these communities. Together, let’s ensure clean drinking water for all.',
  location: 'Sub-Saharan Africa',
  bannerImage: new URL('@/assets/campaign_banner/water.jpg', import.meta.url).href,
  views: 200,
},
{
  id: 3,
  title: 'Support Homeless Shelters',
  goal_amount: 7000,
  current_amount: 2500,
  description: 'Homelessness affects countless individuals and families worldwide. This campaign provides critical resources such as shelter, meals, hygiene products, and counseling services to those in need. In New York, USA, we’re partnering with local organizations to enhance facilities and expand outreach programs. Your donation offers warmth and hope to people who have nowhere else to turn. Join us in our mission to give homeless individuals the opportunity for a stable and dignified life.',
  location: 'New York, USA',
  bannerImage: new URL('@/assets/campaign_banner/homeless.jpg', import.meta.url).href,
  views: 120,
},
{
  id: 4,
  title: 'Disaster Relief Fund',
  goal_amount: 10000,
  current_amount: 3500,
  description: 'Natural disasters strike without warning, leaving countless lives in peril and communities devastated. Our Disaster Relief Fund supports immediate rescue operations, medical aid, food, and shelter for those affected. From hurricanes to earthquakes, your contributions enable us to respond swiftly and effectively. Together, we can restore hope and rebuild lives for disaster-stricken families across the globe. Be a beacon of light during the darkest times—your generosity makes a world of difference.',
  location: 'Global',
  bannerImage: new URL('@/assets/campaign_banner/DisasterReliefFund.png', import.meta.url).href,
  views: 180,
},
{
  id: 5,
  title: 'Tree Planting Initiative',
  goal_amount: 2000,
  current_amount: 1500,
  description: 'Deforestation contributes significantly to climate change and biodiversity loss. Help us combat this crisis by supporting our tree-planting campaign in the Amazon Rainforest, Brazil. Your donation enables us to plant trees, restore habitats, and protect wildlife. Reforesting these areas not only improves air quality but also empowers local communities through sustainable practices. Every tree planted is a step toward healing our planet. Together, we can create a greener and more sustainable future for generations to come.',
  location: 'Amazon Rainforest, Brazil',
  bannerImage: new URL('@/assets/campaign_banner/Planting-Trees.jpg', import.meta.url).href,
  views: 250,
},
{
  id: 6,
  title: 'Animal Rescue and Adoption',
  goal_amount: 4000,
  current_amount: 1800,
  description: 'Thousands of animals face abandonment and neglect daily. Our campaign focuses on rescuing, rehabilitating, and rehoming these vulnerable animals in Los Angeles, USA. We provide medical care, shelter, and adoption services, ensuring each animal finds a loving family. By contributing, you support their recovery and the fight against animal cruelty. Every donation saves lives and gives these animals a chance at happiness. Join us in being their voice and making a difference.',
  location: 'Los Angeles, USA',
  bannerImage: new URL('@/assets/campaign_banner/rescue.webp', import.meta.url).href,
  views: 300,
},
{
  id: 8,
  title: 'Clean Energy Project',
  goal_amount: 15000,
  current_amount: 5400,
  description: 'Climate change demands immediate action. This project funds the development of renewable energy solutions like solar and wind power in California, USA. Your support helps us reduce greenhouse gas emissions, create sustainable jobs, and ensure cleaner energy for future generations. Every dollar brings us closer to a more sustainable and eco-friendly world. Together, we can lead the fight against climate change and transition to a cleaner, greener future.',
  location: 'California, USA',
  bannerImage: new URL('@/assets/campaign_banner/clean_energy.jpg', import.meta.url).href,
  views: 400,
},
{
  id: 9,
  title: 'Support for Refugees',
  goal_amount: 12000,
  current_amount: 4000,
  description: 'Millions of refugees worldwide are displaced due to war and persecution. This campaign provides critical aid, including food, shelter, medical care, and education, to refugees in Syria. Your support gives hope to families striving to rebuild their lives. Together, we can help them overcome immense challenges and start anew. Join us in offering safety and dignity to those who need it most.',
  location: 'Syria',
  bannerImage: new URL('@/assets/campaign_banner/rohingya-refugsupport_refugees.png', import.meta.url).href,
  views: 220,
},
{
  id: 10,
  title: 'Mental Health Awareness',
  goal_amount: 8000,
  current_amount: 3300,
  description: 'Mental health is an essential yet often overlooked aspect of overall well-being. This campaign promotes awareness, education, and resources for mental health on a global scale. By supporting this initiative, you help provide access to counseling, hotlines, and mental health programs for those in need. Together, we can reduce stigma and ensure that no one has to face their struggles alone. Your donation changes lives and strengthens communities worldwide.',
  location: 'Global',
  bannerImage: new URL('@/assets/campaign_banner/mental_health.jpg', import.meta.url).href,
  views: 130,
},

      ],
    };
  },
  computed: {
    topCampaigns() {
      // Filter out fully funded campaigns
      return this.campaigns
        .filter(campaign => campaign.current_amount < campaign.goal_amount)
        .sort((a, b) => b.views - a.views) // Sort by views in descending order
        .slice(0, 3); // Get the top 4 campaigns
    },
  },
  methods: {
    // Calculate progress as a percentage
    calculateProgress(current, goal) {
      return Math.min((current / goal) * 100, 100); // Ensure progress does not exceed 100%
    },
    
    // Handle the donation button click
    donate(campaignId) {
      // Pass the campaignId to DonatePage.vue using router params
      this.$router.push({ name: 'Donate', params: { campaignId: campaignId } });
    },
  },
};
</script>

<style scoped>
/* Campaign Card Styles */
.campaign-card {
  background-size: cover;
  background-position: center;
  height: 180px; /* Increased height to fit the progress bar and button */
  width: 100%;
  max-width: 300px; /* Limit the width of the card */
  border-radius: 15px;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #fff;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.5);
  overflow: hidden;
}

.overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.6); /* Dark overlay for better text visibility */
  padding: 20px;
  text-align: center;
  z-index: 1;
}

.campaign-title {
  margin: 0;
  font-size: 1.5em;
  font-weight: bold;
  text-transform: uppercase;
  margin-bottom: 15px;
}

.campaign-location {
  font-size: 1em;
  color: #fff;
  margin-bottom: 10px;
  font-style: italic;
}

/* Progress Bar Styles */
.progress-container {
  background: #e0e0e0;
  border-radius: 10px;
  height: 10px;
  overflow: hidden;
  margin: 10px 0;
}

.progress-bar {
  background: #4caf50;
  height: 100%;
  transition: width 0.4s ease;
}

.progress-text {
  display: flex;
  justify-content: space-between;
  font-size: 0.9em;
  margin-top: 5px;
}

/* Donate Button */
.donate-btn {
  margin-top: 10px;
  padding: 10px 20px;
  background-color: #00bfae;
  color: white;
  font-size: 1em;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
  transition:
    background-color 0.3s ease,
    transform 0.3s ease;
}

.donate-btn:hover {
  background-color: #009f8b;
  transform: scale(1.05);
}
</style>
