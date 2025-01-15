import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/Home.vue';
import CampaignDetail from '../views/CampaignsDetail.vue';
import LoginView from '../views/LoginForm.vue';
import UserProfileView from '../views/UserProfile.vue';
import AdminDashboardView from '../views/AdminDashboard.vue';
import AboutUsView from '../views/AboutUs.vue';
import FAQView from '../views/FAQ.vue';
import ForgotPassword from '../views/ForgotPassword.vue';
import CreateCampaign from '../views/CreateCampaign.vue';
import DonatePage from '../views/ViewSingleCampaign.vue'; 
import PrivacyPolicy from '../views/PrivacyPolicy.vue';
import SettingsPage from '../components/User/Settings.vue';
import store from '../store';

const routes = [
  { path: '/', name: 'Home', component: HomeView },
  { path: '/campaigns', name: 'CampaignDetail', component: CampaignDetail },
  { path: '/auth', name: 'Login', component: LoginView },
  { path: '/dashboard', name: 'Dashboard', component: UserProfileView, meta: { requiresAuth: false } },
  { path: '/admin', name: 'AdminDashboard', component: AdminDashboardView, meta: { requiresAdmin: false } },
  { path: '/about', name: 'AboutUs', component: AboutUsView },
  { path: '/faq', name: 'FAQ', component: FAQView },
  { path: '/forgot-password', name: 'ForgotPassword', component: ForgotPassword },
  { path: '/create-campaign', name: 'CreateCampaign', component: CreateCampaign, meta: { requiresAuth: false } },
  { path: '/view/:campaignId', name: 'Donate', component: DonatePage, props: false },
  { path: '/privacy-policy', name: 'PrivacyPolicy', component: PrivacyPolicy }, 
  { path: '/settings', name: 'Settings', component: SettingsPage, meta: { requiresAuth: false } },
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
