<template>
  <footer class="app-footer">
    <div class="footer-content">
      <router-link to="/privacy-policy" class="privacy-policy-link">Privacy Policy</router-link>
      <p>Page Views: {{ pageViewCount }}</p>
    </div>
    <p>© 2024 FundFusion. All rights reserved.</p>
  </footer>
</template>

<script>
export default {
  name: 'AppFooter',
  data() {
    return {
      pageViewCount: 0,
    };
  },
  mounted() {
    this.incrementPageView();
  },
  methods: {
    incrementPageView() {
      const count = localStorage.getItem('pageViewCount') || 0;
      this.pageViewCount = parseInt(count) + 1;
      localStorage.setItem('pageViewCount', this.pageViewCount);
    }
  }
};
</script>

<style scoped>
.app-footer {
  background: linear-gradient(to bottom,rgb(127, 200, 196), rgba(97, 175, 169, 0.8));
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1); /* Outer shadow only */
  text-align: center;
  color: #ffffff;
  border-radius: 0 0 20px 20px; /* Rounded bottom corners */
}

.footer-content {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 20px;
}

.privacy-policy-link {
  color: #000000;
  text-decoration: none;
  font-weight: 500;
  padding: 8px 16px;
  border-radius: 15px;
  transition: color 0.3s, transform 0.3s;
}

.privacy-policy-link:hover {
  color: #302c26;
  transform: scale(1.02);
}

.app-footer p {
  margin: 0;
  font-weight: 500;
  color: #000000; 
}
</style>
