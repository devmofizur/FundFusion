<template>
  <footer class="app-footer">
    <div class="footer-content">
      <router-link to="/privacy-policy" class="privacy-policy-link">Privacy Policy</router-link>
      <p>Page Views: {{ pageViewCount }}</p> <!-- Display page view count -->
    </div>
    <p>© 2024 FundFusion. All rights reserved.</p>
  </footer>
</template>

<script>
export default {
  name: 'AppFooter',
  data() {
    return {
      pageViewCount: 0, // Initialize page view count
    };
  },
  mounted() {
    this.incrementPageView(); // Increment view count when component is mounted
  },
  methods: {
    incrementPageView() {
      // Fetch existing view count from local storage or start at 0
      const count = localStorage.getItem('pageViewCount') || 0;
      this.pageViewCount = parseInt(count) + 1; // Increment count
      localStorage.setItem('pageViewCount', this.pageViewCount); // Store updated count
    },
  },
};
</script>

