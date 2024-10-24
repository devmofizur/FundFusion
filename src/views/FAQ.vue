<template>
  <div class="faq-container">
    <h1>Frequently Asked Questions</h1>
    <div class="faq-item" v-for="(faq, index) in faqs" :key="index">
      <div class="faq-question" @click="toggleAnswer(index)">
        <h3>{{ faq.question }}</h3>
        <span class="toggle-icon">{{ isOpen[index] ? '-' : '+' }}</span>
      </div>
      <div v-if="isOpen[index]" class="faq-answer">
        <p>{{ faq.answer }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isOpen: [], // Array to track which answers are open
      faqs: [
        {
          question: 'What is FundFusion?',
          answer:
            'FundFusion is a platform designed to help users support various causes through donations.',
        },
        {
          question: 'How can I create a campaign?',
          answer:
            'You can create a campaign by registering on our website and following the prompts in your dashboard.',
        },
        {
          question: 'How do I make a donation?',
          answer:
            'Simply choose a campaign, enter the amount you wish to donate, and follow the checkout process.',
        },
        {
          question: 'Is my donation tax-deductible?',
          answer:
            'Please check with your local tax laws or consult a tax professional regarding the deductibility of your donations.',
        },
        {
          question: 'Can I track my donations?',
          answer:
            'Yes, you can track all your donations through your profile dashboard.',
        },
      ],
    }
  },
  methods: {
    toggleAnswer(index) {
      this.$set(this.isOpen, index, !this.isOpen[index]) // Toggle the answer visibility
    },
  },
}
</script>

<style scoped>
.faq-container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

h1 {
  text-align: center;
  margin-bottom: 20px;
}

.faq-item {
  border: 1px solid #ccc;
  border-radius: 8px;
  margin-bottom: 10px;
  padding: 15px;
  background-color: #f9f9f9;
}

.faq-question {
  display: flex;
  justify-content: space-between;
  cursor: pointer;
  font-weight: bold;
}

.toggle-icon {
  margin-left: 10px;
}

.faq-answer {
  padding-top: 10px;
  font-size: 0.95em;
}
</style>
