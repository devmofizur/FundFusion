<template>
  <div class="home-view">
    <!-- Full Background Image -->
    <div class="full-background">
      <div class="content-overlay">
        <p class="quote">A Little Care Can Change the World</p>
        <p class="quote secondary">Designed to Do Good</p>
        <p class="hero-description">
          FundFusion connects individuals with meaningful causes. Join us to support campaigns that make a real difference in the world!
        </p>
        <button class="start-fusion-btn" @click="scrollToCampaigns">Start Fusion</button>
      </div>
    </div>

    <!-- Section for How It Works -->
    <div class="how-it-works">
      <p class="section-description">
        Whether you're looking to support a cause or launch your own campaign, FundFusion makes it easy to make an impact.
      </p>
      <div class="how-it-works-steps">
        <div class="step">
          <h3>1. Discover</h3>
          <p>Browse through various campaigns and find one that aligns with your passions.</p>
        </div>
        <div class="step">
          <h3>2. Support</h3>
          <p>Contribute to the cause, whether through donations or spreading awareness.</p>
        </div>
        <div class="step">
          <h3>3. Make a Difference</h3>
          <p>Your support helps bring about real change and creates a lasting impact.</p>
        </div>
      </div>
    </div>

    <!-- Campaigns Section -->
    <CampaignList :campaigns="topCampaigns" />
  </div>
</template>

<script>
import CampaignList from '../components/Campaign/CampaignList.vue';

export default {
  name: 'HomeView',
  components: {
    CampaignList,
  },
  data() {
    return {
      campaigns: [], // Will be populated from CampaignList
    };
  },
  computed: {
    // Get the top 4 campaigns sorted by the highest views, excluding fully funded campaigns
    topCampaigns() {
      // Make sure campaigns data is not empty or undefined
      if (!Array.isArray(this.campaigns) || this.campaigns.length === 0) {
        return [];
      }

      return this.campaigns
        .filter(campaign => {
          // Only include campaigns that are not fully funded (current_amount < goal_amount)
          return campaign.current_amount < campaign.goal_amount && campaign.current_amount >= 0 && campaign.goal_amount > 0;
        })
        .map(campaign => ({
          ...campaign,
          progress: (campaign.current_amount / campaign.goal_amount) * 100, // Calculate progress
        }))
        .sort((a, b) => b.views - a.views) // Sort by views in descending order
        .slice(0, 4); // Get top 4 based on views
    },
  },
  methods: {
    // Scroll to the Campaigns section when the button is clicked
    scrollToCampaigns() {
      const campaignsSection = document.querySelector('.campaign-container');
      if (campaignsSection) {
        campaignsSection.scrollIntoView({ behavior: 'smooth' });
      }
    },
  },
};
</script>



<style scoped>
/* Home View General Styles */
.home-view {
  background: linear-gradient(to bottom, #f0fffe, #83cfcb); /* Gradient Background */
}

/* Full Background Image Section */
.full-background {
  background-image: url('@/assets/HomeBack.jpg'); /* Path to your image */
  background-size: cover; /* Ensures the full image is displayed */
  background-position: center;
  width: 100%;
  height: 100vh; /* Full screen height */
  position: relative;
  opacity: 0.89; /* Slight transparency */
}

.content-overlay {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%); /* Center content */
  text-align: center;
  width: 80%;
}

/* Quotes Styles */
.quote {
  font-size: 2em;
  color: white;
  font-weight: bold;
  margin: 10px 0;
  text-shadow: 0 4px 6px rgba(0, 0, 0, 0.5);
}

.quote.secondary {
  font-size: 1.5em;
  font-weight: normal;
  font-style: italic;
  color: #f0f0f0;
}

.hero-description {
  font-size: 1.2em;
  color: white;
  margin-top: 30px;
  text-shadow: 0 4px 6px rgba(0, 0, 0, 0.5);
}

.start-fusion-btn {
  margin-top: 20px;
  padding: 15px 30px;
  background-color: #00bfae;
  color: white;
  font-size: 1.2em;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
  transition: background-color 0.3s ease, transform 0.3s ease;
}

.start-fusion-btn:hover {
  background-color: #009f8b;
  transform: scale(1.05);
}

/* How It Works Section */
.how-it-works {
  margin: 60px auto;
  padding: 40px;
  background-color: #f8f9fa;
  border-radius: 15px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  width: 90%;
}

.section-description {
  font-size: 1.5em;
  text-align: center;
  color: #34495e;
  margin-bottom: 30px;
}

.how-it-works-steps {
  display: flex;
  justify-content: space-between;
  gap: 20px;
}

.step {
  flex: 1;
  padding: 20px;
  background-color: #ffffff;
  border-radius: 10px;
  text-align: center;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}

.step h3 {
  font-size: 1.8em;
  color: #2c3e50;
  margin-bottom: 15px;
}

.step p {
  font-size: 1.1em;
  color: #7f8c8d;
}

/* Campaign List Section */
.campaign-container {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  justify-content: center;
}
</style>
