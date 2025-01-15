<template>
  <div class="background-box">
    <div class="donate-container">
      <div class="donate-page">
        <!-- Introduction Section -->
        <div class="intro-section">
          <h1>Make a Difference Today</h1>
          <p>
            Your support can change lives. Select a campaign, choose your preferred
            payment method, enter the donation amount, and help bring about a
            lasting impact.
          </p>
        </div>

        <!-- Campaign Information -->
        <div class="campaign-info" v-if="campaign">
          <h2>{{ campaign.title }}</h2>
          <p class="campaign-location"><strong>Location:</strong> {{ campaign.location }}</p>
          <p class="campaign-description">{{ campaign.description }}</p>

          <div class="progress-container">
            <div
              class="progress-bar"
              :style="{ width: `${calculateProgress(campaign.current_amount, campaign.goal_amount)}%` }"
            ></div>
          </div>
          <div class="progress-text">
            <span>Raised: ${{ campaign.current_amount }}</span>
            <span>Goal: ${{ campaign.goal_amount }}</span>
          </div>
        </div>

        <!-- Donation Form -->
        <form @submit.prevent="handleSubmit" class="donation-form">
          <!-- Donation Amount -->
          <div class="form-group">
            <label for="amount" class="form-label">Donation Amount</label>
            <input
              v-model="donationAmount"
              type="number"
              id="amount"
              class="form-control"
              placeholder="Enter amount"
              required
              min="1"
            />
          </div>

          <!-- Payment Method Selection -->
          <div class="form-group">
            <label for="paymentMethod" class="form-label">Select Payment Method</label>
            <select
              v-model="selectedPaymentMethod"
              id="paymentMethod"
              class="form-control"
              required
            >
              <option value="" disabled>Select Payment Method</option>
              <option value="bkash">bKash</option>
              <option value="rocket">Rocket</option>
              <option value="bankTransfer">Bank Transfer</option>
            </select>
          </div>

          <!-- Conditional Payment Details -->
          <div v-if="selectedPaymentMethod === 'bkash'" class="payment-details">
            <div class="form-group">
              <label for="bkashNumber" class="form-label">bKash Number</label>
              <input
                v-model="bkashNumber"
                type="text"
                id="bkashNumber"
                class="form-control"
                placeholder="Enter bKash Number"
                required
              />
            </div>
          </div>

          <div v-if="selectedPaymentMethod === 'rocket'" class="payment-details">
            <div class="form-group">
              <label for="rocketNumber" class="form-label">Rocket Number</label>
              <input
                v-model="rocketNumber"
                type="text"
                id="rocketNumber"
                class="form-control"
                placeholder="Enter Rocket Number"
                required
              />
            </div>
          </div>

          <div v-if="selectedPaymentMethod === 'bankTransfer'" class="payment-details">
            <div class="form-group">
              <label for="bankAccountNumber" class="form-label">Bank Account Number</label>
              <input
                v-model="bankAccountNumber"
                type="text"
                id="bankAccountNumber"
                class="form-control"
                placeholder="Enter Bank Account Number"
                required
              />
            </div>
            <div class="form-group">
              <label for="bankName" class="form-label">Bank Name</label>
              <input
                v-model="bankName"
                type="text"
                id="bankName"
                class="form-control"
                placeholder="Enter Bank Name"
                required
              />
            </div>
          </div>

          <!-- Submit Button -->
          <button type="submit" class="donate-button">Donate Now</button>
        </form>
      </div>
    </div>
  </div>
</template>



<script>
import CampaignList from '../components/Campaign/CampaignList.vue';

export default {
  name: 'DonatePage',
  data() {
    return {
      donationAmount: '',
      selectedPaymentMethod: '',
      bkashNumber: '',
      rocketNumber: '',
      bankAccountNumber: '',
      bankName: '',
      campaignId: this.$route.params.campaignId, // Get campaign ID from route params
      campaign: {}, // Selected campaign details
      campaigns: [], // All campaigns passed from CampaignList.vue
    };
  },
  created() {
    this.campaigns = CampaignList.data().campaigns; // Get campaigns from CampaignList
    this.fetchCampaignDetails();
  },
  mounted() {
    window.scrollTo(0, 0);
  },
  methods: {
    fetchCampaignDetails() {
      const foundCampaign = this.campaigns.find(
        (campaign) => campaign.id === Number(this.campaignId)
      );
      if (foundCampaign) {
        this.campaign = foundCampaign;
      } else {
        console.error('Campaign not found');
      }
    },
    calculateProgress(current, goal) {
      return Math.min((current / goal) * 100, 100); // Ensure progress is capped at 100%
    },
    handleSubmit() {
      if (!this.donationAmount || this.donationAmount <= 0) {
        alert('Please enter a valid donation amount');
        return;
      }

      console.log('Donation submitted:', {
        campaignId: this.campaignId,
        donationAmount: this.donationAmount,
        selectedPaymentMethod: this.selectedPaymentMethod,
        paymentDetails: {
          bkashNumber: this.bkashNumber,
          rocketNumber: this.rocketNumber,
          bankAccountNumber: this.bankAccountNumber,
          bankName: this.bankName,
        },
      });

      // Add donation amount to campaign's current amount
      const donation = parseFloat(this.donationAmount);
      this.campaign.current_amount += donation; // Dynamically add donation to current amount

      // Clear the form
      this.donationAmount = '';
      this.selectedPaymentMethod = '';
      this.bkashNumber = '';
      this.rocketNumber = '';
      this.bankAccountNumber = '';
      this.bankName = '';

      alert('Thank you for your donation!');
    },
  },
};
</script>


<style scoped>
/* General Styling */
.background-box {
  background: linear-gradient(to bottom, #f0fffe, #83cfcb); /* Light gradient for the background */
  padding: 50px 0; /* Space around the container */
  min-height: 100vh; /* Full-page height */
  display: flex;
  justify-content: center;
  align-items: center;
}


.donate-container {
  width: 100%;
  max-width: 1200px; /* Limit the maximum width */
  margin: 0 auto;
  padding: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
}

/* Content Styling */
.donate-page {
  width: 100%;
  max-width: 900px;
  background: white;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2); /* Optional shadow for contrast */
}


.intro-section {
  text-align: center;
  margin-bottom: 40px;
}

.intro-section h1 {
  font-size: 2.5em;
  margin-bottom: 15px;
  color: #2b2b2b;
}

.intro-section p {
  color: #555;
  font-size: 1.1em;
  max-width: 700px;
  margin: 0 auto;
}

.campaign-info {
  background: #ffffff;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  margin-bottom: 30px;
}

.campaign-info h2 {
  font-size: 2em;
  color: #00bfae;
  margin-bottom: 10px;
}

.campaign-location,
.campaign-description {
  font-size: 1.1em;
  margin-bottom: 15px;
}

.progress-container {
  background: #e0e0e0;
  height: 10px;
  border-radius: 5px;
  margin: 10px 0;
  overflow: hidden;
}

.progress-bar {
  background: #4caf50;
  height: 100%;
  transition: width 0.5s ease-in-out;
}

.progress-text {
  display: flex;
  justify-content: space-between;
  font-size: 0.95em;
  color: #555;
}

.donation-form {
  background: #ffffff;
  padding: 25px;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.form-group {
  margin-bottom: 20px;
}

.form-label {
  display: block;
  font-weight: bold;
  margin-bottom: 8px;
  font-size: 1.1em;
  color: #333;
}

.form-control {
  width: 96%;
  padding: 12px;
  border: 1px solid #ddd;
  border-radius: 6px;
  font-size: 1em;
  color: #333;
  background-color: #f9f9f9;
  transition: border-color 0.3s ease;
}

.form-control:focus {
  border-color: #00bfae;
  outline: none;
}

.donate-button {
  background-color: #00bfae;
  color: white;
  padding: 15px 25px;
  border: none;
  border-radius: 5px;
  font-size: 1.2em;
  cursor: pointer;
  width: 100%;
  transition: background-color 0.3s, transform 0.3s;
}

.donate-button:hover {
  background-color: #009f8b;
  transform: scale(1.05);
}

.payment-details {
  margin-top: 20px;
}

.payment-details .form-group {
  margin-bottom: 15px;
}
</style>
