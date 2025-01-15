<template>
  <div class="about-us-page">
    <!-- Hero Section -->
    <section class="hero">
      <h1 class="hero-title">About FundFusion</h1>
      <p class="hero-description">
        We're on a mission to bring people together to support meaningful causes and make the world a better place.
      </p>
    </section>

    <!-- Our Story Section -->
    <section class="our-story" v-scroll-reveal>
      <h2 class="section-title">Our Story</h2>
      <div class="story-content">
        <p>
          FundFusion was created with the goal of connecting individuals with causes they care about. Our platform
          enables users to both discover and contribute to campaigns that are changing the world, one donation at a time.
        </p>
      </div>
    </section>

    <!-- Our Mission Section -->
    <section class="our-mission" v-scroll-reveal>
      <h2 class="section-title">Our Mission</h2>
      <div class="mission-content">
        <p class="mission-text">
          At FundFusion, our mission is simple: to empower individuals to make a difference. We believe that by coming
          together, we can create lasting change. Every campaign is an opportunity for people to contribute to the greater good.
        </p>
      </div>
    </section>

    <!-- Our Values Section -->
    <section class="our-values" v-scroll-reveal>
      <h2 class="section-title">Our Values</h2>
      <div class="values-content">
        <div class="value-item">
          <h3 class="value-title">Integrity</h3>
          <p>We believe in transparency and honesty in everything we do.</p>
        </div>
        <div class="value-item">
          <h3 class="value-title">Community</h3>
          <p>We value the power of collaboration and the strength of community.</p>
        </div>
        <div class="value-item">
          <h3 class="value-title">Impact</h3>
          <p>We are driven by the desire to make a meaningful difference in the world.</p>
        </div>
      </div>
    </section>

    <!-- Call to Action Section -->
    <section class="call-to-action" v-scroll-reveal>
      <h2 class="cta-title">Join Us in Making a Difference</h2>
      <p class="cta-description">
        Ready to be part of something bigger? Join FundFusion today and start supporting the causes that matter most to you.
      </p>
      <button class="cta-button" @click="joinUs">
        Get Started
      </button>
    </section>
  </div>
</template>

<script>
export default {
  name: 'AboutUs',
  methods: {
    joinUs() {
      // Navigate to the sign-up or campaign discovery page
      this.$router.push({ name: 'Home' });
    },
  },
};
</script>

<style scoped>
/* Main Styles */
.about-us-page {
  padding: 20px;
  background: linear-gradient(to bottom, #f8f9fa, #e1f3f1);
}

/* Hero Section */
.hero {
  text-align: center;
  margin-bottom: 40px;
  padding: 50px 20px;
  background-color: #34495e;
  color: white;
  border-radius: 10px;
  opacity: 0;
  animation: fadeInUp 1s forwards;
}

.hero-title {
  font-size: 3em;
  margin-bottom: 10px;
}

.hero-description {
  font-size: 1.2em;
  max-width: 600px;
  margin: 0 auto;
}

/* Fade-in animation */
@keyframes fadeInUp {
  0% {
    opacity: 0;
    transform: translateY(50px);
  }
  100% {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Section Titles */
.section-title {
  font-size: 2.5em;
  color: #34495e;
  margin-bottom: 20px;
  text-align: center;
}

/* Our Story Section */
.our-story {
  margin-bottom: 40px;
  text-align: center;
  opacity: 0;
  animation: fadeInUp 1s forwards;
}

.story-content p {
  width: 60%;
  font-size: 1.1em;
  color: #7f8c8d;
  line-height: 1.6;
  margin: 0 auto;
}

/* Our Mission Section */
.our-mission {
  margin-bottom: 40px;
  background: #ffffff;
  padding: 40px 20px;
  border-radius: 10px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
  opacity: 0;
  animation: fadeInUp 1s forwards;
}

.mission-content {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 20px;
}

.mission-text {
  width: 60%;
  font-size: 1.1em;
  color: #7f8c8d;
  line-height: 1.6;
  margin: 0 auto;
}

/* Our Values Section */
.our-values {
  margin-bottom: 40px;
  text-align: center;
  opacity: 0;
  animation: fadeInUp 1s forwards;
}

.values-content {
  display: flex;
  justify-content: space-around;
  gap: 30px;
}

.value-item {
  width: 30%;
  background: #ffffff;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
  opacity: 0;
  animation: fadeInUp 1s forwards;
}

.value-title {
  font-size: 1.5em;
  color: #34495e;
  margin-bottom: 10px;
}

/* Call to Action Section */
.call-to-action {
  text-align: center;
  padding: 40px 20px;
  background-color: #76c7c0;
  color: white;
  border-radius: 10px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
  opacity: 0;
  animation: fadeInUp 1s forwards;
}

.cta-title {
  font-size: 2.5em;
  margin-bottom: 15px;
}

.cta-description {
  font-size: 1.2em;
  margin-bottom: 30px;
}

.cta-button {
  background-color: #34495e;
  border: none;
  color: white;
  padding: 15px 30px;
  font-size: 1.2em;
  cursor: pointer;
  border-radius: 5px;
  transition: background-color 0.3s;
}

.cta-button:hover {
  background-color: #2c3e50;
}
</style>
