<template>
  <div class="campaign-card" :style="{ backgroundImage: `url(${localImageUrl})` }">
    <div class="overlay">
      <div class="campaign-info">
        <div class="left-side">
          <h3>{{ campaign.title }}</h3>
          <p>Goal: {{ campaign.goal_amount }}</p>
          <p>Raised: {{ campaign.current_amount }}</p>
        </div>
        <div class="right-side">
          <router-link :to="`/campaigns/${campaign.id}`">View Details</router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    campaign: Object,
  },
  data() {
    return {
      localImageUrl: '',
    };
  },
  created() {
    this.loadImageFromLocalStorage();
  },
  methods: {
    loadImageFromLocalStorage() {
      // Try to get the image from localStorage
      const storedImage = localStorage.getItem(`campaign-image-${this.campaign.id}`);
      
      if (storedImage) {
        // If it's a DataURL (image file uploaded by user), use it
        if (storedImage.startsWith('data:image')) {
          this.localImageUrl = storedImage;
        } else {
          // Otherwise, treat it as a regular URL
          this.localImageUrl = storedImage;
        }
      } else {
        // If no image found in localStorage, use a default image
        this.localImageUrl = 'default-image-path.jpg';
      }
    },
    handleFileUpload(event) {
      const file = event.target.files[0]; // The selected file
      const reader = new FileReader();

      reader.onloadend = () => {
        const imageDataUrl = reader.result; // This is the base64 encoded image
        // Store the image in localStorage
        localStorage.setItem(`campaign-image-${this.campaign.id}`, imageDataUrl);
        // Update the localImageUrl for this component
        this.localImageUrl = imageDataUrl;
      };

      if (file) {
        reader.readAsDataURL(file); // Convert the image file to a DataURL
      }
    },
  },
};
</script>

<style scoped>
.campaign-card {
  position: relative;
  background-size: cover;
  background-position: center;
  height: 200px;
  border-radius: 15px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
  color: rgb(111, 0, 255);
  padding: 20px;
  display: flex;
  align-items: center;
}

.overlay {
  background: rgba(0, 0, 0, 0.5);
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.campaign-info {
  display: flex;
  justify-content: space-between;
  width: 100%;
}

.left-side {
  flex: 1;
}

.right-side {
  flex: 1;
  text-align: right;
}

input[type="file"] {
  margin-top: 10px;
}
</style>
