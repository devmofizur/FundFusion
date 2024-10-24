import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/Home.vue';
import CampaignDetail from '../views/CampaignDetail.vue';
import LoginView from '../views/Login.vue';
import RegisterView from '../views/Register.vue';
import UserProfileView from '../views/UserProfile.vue';
import AdminDashboardView from '../views/AdminDashboard.vue';
import AboutUsView from '../views/AboutUs.vue';  // Import About Us
import FAQView from '../views/FAQ.vue';           // Import FAQ
import store from '../store';

const routes = [
  { path: '/', name: 'Home', component: HomeView },
  { path: '/campaigns/:id', name: 'CampaignDetail', component: CampaignDetail },
  { path: '/login', name: 'Login', component: LoginView },
  { path: '/register', name: 'Register', component: RegisterView },
  { path: '/profile', name: 'UserProfile', component: UserProfileView, meta: { requiresAuth: true } },
  { path: '/admin', name: 'AdminDashboard', component: AdminDashboardView, meta: { requiresAdmin: true } },
  { path: '/about', name: 'AboutUs', component: AboutUsView },  // Add About Us route
  { path: '/faq', name: 'FAQ', component: FAQView },            // Add FAQ route
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

// Route guards
router.beforeEach((to, from, next) => {
  const isAuthenticated = store.state.user;
  const isAdmin = isAuthenticated && store.state.user.isAdmin;

  if (to.meta.requiresAuth && !isAuthenticated) {
    next({ name: 'Login' });
  } else if (to.meta.requiresAdmin && !isAdmin) {
    next({ name: 'Home' });
  } else {
    next();
  }
});

export default router;
