<template>
  <div class="create-campaign-container">
    <div class="create-campaign-box">
      <h1>Create a New Campaign</h1>

      <form @submit.prevent="submitCampaign" class="campaign-form">
        <div class="form-group">
          <label for="title">Campaign Title</label>
          <input
            type="text"
            id="title"
            v-model="campaign.title"
            placeholder="Enter campaign title"
            required
          />
        </div>

        <div class="form-group">
          <label for="goalAmount">Goal Amount</label>
          <input
            type="number"
            id="goal_amount"
            v-model="campaign.goal_amount"
            placeholder="Enter goal amount"
            required
            min="10"
          />
        </div>

        <div class="form-group">
          <label for="location">Location</label>
          <input
            type="text"
            id="location"
            v-model="campaign.location"
            placeholder="Enter campaign location"
            required
          />
        </div>

        <div class="form-group">
          <label for="bannerImage">Upload Banner Image</label>
          <input type="file" id="bannerImage" @change="handleFileUpload" />
          <div v-if="bannerPreview" class="banner-preview">
            <img :src="bannerPreview" alt="Banner Preview" />
          </div>
        </div>

        <div class="form-group">
          <label for="description">Campaign Description</label>
          <textarea
            id="description"
            v-model="campaign.description"
            placeholder="Describe your campaign"
            required
          ></textarea>
        </div>

        <div class="form-group">
          <label for="endDate">End Date</label>
          <input
            type="date"
            id="endDate"
            v-model="campaign.end_date"
            required
          />
        </div>

        <div class="form-group">
          <label for="category">Category</label>
          <select id="category" v-model="campaign.category" required>
            <option disabled value="">Select a category</option>
            <option value="Medical">Medical</option>
            <option value="Education">Education</option>
            <option value="Disaster Relief">Disaster Relief</option>
            <option value="Environmental Conservation">
              Environmental Conservation
            </option>
            <option value="Social Justice">Social Justice</option>
            <option value="Animal Welfare">Animal Welfare</option>
            <option value="Community Development">Community Development</option>
            <option value="Non-profit Support">Non-profit Support</option>
            <option value="Arts and Culture">Arts and Culture</option>
            <option value="Other">Other</option>
          </select>
        </div>

        <div class="form-group">
          <label for="contactInfo">Contact Information</label>
          <input
            type="email"
            id="contactInfo"
            v-model="campaign.contact_info"
            placeholder="Enter your contact email"
            required
          />
        </div>

        <button type="submit" class="submit-btn">Create Campaign</button>
      </form>

      <div v-if="successMessage" class="success-message">
        <p>{{ successMessage }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'CreateCampaign',
  data() {
    return {
      campaign: {
        title: '',
        goal_amount: '',
        location: '',
        bannerImage: null,
        description: '',
        endDate: '12/11/2024',
        category: '',
        contactInfo: 'result@cgpa.com',
        story: '', // Added optional story field
        documents: [], // Added optional documents upload
      },
      bannerPreview: null,
      successMessage: '',
      categories: [
        'Medical',
        'Education',
        'Disaster Relief',
        'Environmental Conservation',
        'Social Justice',
        'Animal Welfare',
        'Community Development',
        'Non-profit Support',
        'Arts and Culture',
        'Other',
      ],
    }
  },
  methods: {
    handleFileUpload(event) {
      const file = event.target.files[0]
      if (file) {
        // Validate file size (10MB limit)
        if (file.size > 10 * 1024 * 1024) {
          alert('File size must be less than 10MB')
          return
        }

        const reader = new FileReader()
        reader.onloadend = () => {
          this.bannerPreview = reader.result
          this.campaign.bannerImage = file
        }
        reader.readAsDataURL(file)
      }
    },
    handleDocumentUpload(event) {
      const files = Array.from(event.target.files)
      // Validate total file size and number of files
      const totalSize = files.reduce((acc, file) => acc + file.size, 0)
      if (totalSize > 50 * 1024 * 1024) {
        // 50MB total limit
        alert('Total document size must be less than 50MB')
        return
      }
      if (files.length > 5) {
        alert('Maximum 5 documents allowed')
        return
      }
      this.campaign.documents = files
    },
    async submitCampaign() {
      // Validate required fields
      const requiredFields = [
        'title',
        'goal_amount',
        'location',
        'endDate',
        'category',
        'contactInfo',
      ]
      for (const field of requiredFields) {
        if (!this.campaign[field]) {
          alert(`Please fill in the ${field} field.`)
          return
        }
      }
      
      try {
        // const accessToken = localStorage.getItem('accessToken')
        // const formData = new FormData()

        // // Append all campaign data to FormData
        // for (const key in this.campaign) {
        //   if (key === 'bannerImage' && this.campaign.bannerImage) {
        //     formData.append('bannerImage', this.campaign.bannerImage)
        //   } else if (key === 'documents' && this.campaign.documents.length) {
        //     this.campaign.documents.forEach(doc => {
        //       formData.append('documents', doc)
        //     })
        //   } else if (
        //     this.campaign[key] !== null &&
        //     this.campaign[key] !== undefined
        //   ) {
        //     formData.append(key, this.campaign[key])
        //   }
        // }

        // // const response = await axios.post("http://localhost:8080/api/campaigns/", formData, {
        // //   headers: {
        // //     Authorization: `Bearer ${accessToken}`,
        // //     "Content-Type": "multipart/form-data",
        // //   },
        // // });
        alert('Campaign created successfully!')
        this.successMessage = 'Campaign created successfully!'
        this.resetForm()
        // Optionally, navigate to campaign list or detail page
        this.$router.push('/campaigns')
      } catch (error) {
        console.error(
          'Error creating campaign:',
          error.response?.data || error.message,
        )
        // More detailed error handling
        if (error.response && error.response.data) {
          const errors = error.response.data
          let errorMessage = 'Error creating campaign:\n'
          Object.keys(errors).forEach(key => {
            errorMessage += `${key}: ${errors[key]}\n`
          })
          alert(errorMessage)
        } else {
          alert('Error creating campaign. Please try again later.')
        }
      }
    },
    resetForm() {
      this.campaign = {
        title: '',
        goal_amount: '',
        location: '',
        bannerImage: null,
        description: '',
        endDate: '',
        category: '',
        contactInfo: '',
        story: '',
        documents: [],
      }
      this.bannerPreview = null
    },
  },
}
</script>

<style scoped>
/* Styling (unchanged from the previous version) */
.create-campaign-container {
  width: 100%;
  height: 100vh;
  background: linear-gradient(to bottom, #f0fffe, #83cfcb);
  display: flex;
  justify-content: center;
  align-items: center;
}

.create-campaign-box {
  background-color: white;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  padding: 20px 30px; /* Adjust padding for better spacing */
  width: 100%;
  max-width: 700px; /* Control the maximum width of the form box */
  border-radius: 10px;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: stretch;
  max-height: 90vh; /* Set maximum height for the box */
  overflow-y: auto; /* Allow scrolling if content overflows */
}

h1 {
  text-align: center;
  margin-bottom: 20px;
}

.form-group {
  margin-bottom: 15px;
}

label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

input,
select,
textarea {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 14px;
}

textarea {
  resize: none;
}

.image-preview img {
  max-width: 100%;
  margin-top: 10px;
}

.submit-btn {
  background-color: #007bff;
  color: white;
  padding: 10px 15px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  width: 100%;
}

.submit-btn:hover {
  background-color: #0056b3;
}

.success-message {
  color: green;
  text-align: center;
  margin-top: 15px;
}
</style>
