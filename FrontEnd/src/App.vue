
<template>
  <div id="app">
    <AppHeader />
    <router-view />
    <AppFooter />
  </div>
</template>

<script>
import AppHeader from './components/Layout/AppHeader.vue';
import AppFooter from './components/Layout/AppFooter.vue';


export default {
  components: {
    AppHeader,
    AppFooter
  }
};
</script>

<!-- [Do not touch. Scrollbar always] -->
<style>
#app {
  display: flex;
  flex-direction: column;
  min-height: 100vh; /* Ensure the app takes full viewport height */
}

.main-content {
  flex: 1; /* Allow this to grow and fill the space */
  display: flex;
  justify-content: center; /* Center the content horizontally */
  align-items: flex-start; /* Align content to the top */
}

footer {
  flex-shrink: 0; /* Prevent footer from shrinking */
}
</style>
<!-- [Do not touch. Scrollbar always]  -->