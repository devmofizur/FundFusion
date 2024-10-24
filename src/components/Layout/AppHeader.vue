<template>
  <header>
    <nav>
      <ul class="nav-list">
        <li><router-link to="/">Home</router-link></li>
        <li><router-link to="/campaigns">Campaigns</router-link></li>
        <li><router-link to="/about">About Us</router-link></li>
        <li><router-link to="/faq">FAQ</router-link></li>
      </ul>
    </nav>
  </header>
</template>

<script>
export default {
  name: 'AppHeader'
}
</script>
