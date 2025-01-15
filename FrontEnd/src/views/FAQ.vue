<template>
  <div class="faq-page" @mousemove="updateBackground" :style="{ background: backgroundStyle }">
    <h1 class="faq-title">Frequently Asked Questions</h1>

    <div v-for="(faq, index) in faqs" :key="index" class="faq-item">
      <!-- Question Section -->
      <div
        class="faq-question"
        :class="{ active: isAnswerVisible(index) }"
        @click="toggleAnswer(index)"
      >
        <div class="question-text">
          <h3>{{ faq.question }}</h3>
        </div>
        <div class="icon-container">
          <span v-if="isAnswerVisible(index)" class="toggle-icon">&#x2191;</span> <!-- Up arrow -->
          <span v-else class="toggle-icon">&#x2193;</span> <!-- Down arrow -->
        </div>
      </div>

      <!-- Answer Section -->
      <transition name="fade">
        <div v-if="isAnswerVisible(index)" class="faq-answer">
          <p>{{ faq.answer }}</p>
        </div>
      </transition>
    </div>
  </div>
</template>

<script>
export default {
  name: 'FAQ',
  data() {
    return {
      faqs: [
        { question: 'What is FundFusion?', answer: 'FundFusion is a crowdfunding platform that helps people raise money for various causes.' },
        { question: 'How can I create a campaign?', answer: 'To create a campaign, sign up for an account and fill out the campaign details.' },
        { question: 'Can I donate anonymously?', answer: 'Yes, you can choose to donate anonymously on FundFusion.' },
        { question: 'Are my donations secure?', answer: 'Yes, all transactions are encrypted and secure.' },
        { question: 'What types of campaigns can I create?', answer: 'You can create campaigns for charity, personal projects, or community initiatives.' },
        { question: 'How can I share my campaign?', answer: 'You can share your campaign link via social media or email.' },
        { question: 'Can I update my campaign?', answer: 'Yes, you can edit your campaign details at any time.' },
        { question: 'How do I track donations?', answer: 'You can track donations through the campaign dashboard.' },
        { question: 'Can I refund a donation?', answer: 'Donations are generally non-refundable, but you can contact support for exceptions.' }
      ],
      visibleAnswers: [],
      mouseX: 0,
      mouseY: 0,
      backgroundStyle: 'none'
    };
  },
  methods: {
    toggleAnswer(index) {
      const isVisible = this.visibleAnswers.includes(index);
      if (isVisible) {
        this.visibleAnswers = this.visibleAnswers.filter(i => i !== index);
      } else {
        this.visibleAnswers.push(index);
      }
    },
    isAnswerVisible(index) {
      return this.visibleAnswers.includes(index);
    },
    updateBackground(event) {
      this.mouseX = event.clientX;
      this.mouseY = event.clientY;
      this.backgroundStyle = `radial-gradient(circle at ${this.mouseX}px ${this.mouseY}px, rgba(255, 255, 255, 0.2), transparent 50%)`;
    }
  }
};
</script>

<style scoped>
.faq-page {
  padding: 40px;
  background-color: #f4f7fa;
  color: #333;
  font-family: 'Roboto', sans-serif;
  transition: background 0.2s ease-in-out;
}

.faq-title {
  font-size: 2.5em;
  color: #2c3e50;
  text-align: center;
  margin-bottom: 40px;
  font-weight: 600;
  letter-spacing: 2px;
  text-transform: uppercase;
  animation: fadeIn 1s ease-out;
}

.faq-item {
  margin-bottom: 20px;
  border-radius: 12px;
  background-color: #ffffff;
  padding: 20px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease-in-out;
  opacity: 0;
  animation: fadeInUp 0.5s forwards;
}

.faq-item:hover {
  transform: scale(1.02);
}

.faq-question {
  font-size: 1.1em;
  color: #34495e;
  cursor: pointer;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 12px;
  background-color: #f1f1f1;
  border-radius: 8px;
  transition: background-color 0.3s ease-in-out;
}

.faq-question:hover {
  background-color: #e0e0e0;
}

.faq-question.active {
  background-color: #3498db;
  color: #fff;
}

.faq-question.active .toggle-icon {
  color: #fff;
}

.icon-container {
  font-size: 1.5em;
}

.toggle-icon {
  transition: transform 0.3s ease;
}

.faq-answer {
  padding: 10px 20px;
  background-color: #ecf0f1;
  margin-top: 10px;
  border-radius: 5px;
  font-size: 1.1em;
  color: #34495e;
  line-height: 1.6;
  opacity: 1;
  transition: opacity 0.3s ease-in-out;
}

/* Fade animations */
.faq-answer-enter-active, .faq-answer-leave-active {
  transition: opacity 0.3s;
}

.faq-answer-enter, .faq-answer-leave-to {
  opacity: 0;
}

/* Keyframe Animations */
@keyframes fadeIn {
  0% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }
}

@keyframes fadeInUp {
  0% {
    opacity: 0;
    transform: translateY(20px);
  }
  100% {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>
