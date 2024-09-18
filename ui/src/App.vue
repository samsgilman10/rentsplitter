<template>
  <div>
    <div class="menu-bar">
      <div class="left-menu">
        <img src="/vite.svg" class="logo" alt="Vite logo" />
        <span> RentSplitter </span>
      </div>
      <Button @click="showAbout = true" label="About" severity="contrast" class='about-button' />
    </div>
    <div>
      <MainController />
    </div>
    <Dialog v-model:visible="showAbout" modal header="About" class="dialog-box">
      <AboutSection />
    </Dialog>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import Button from 'primevue/button';
import AboutSection from './components/AboutSection.vue'
import MainController from './components/MainController.vue';

const showAbout = ref(false);
</script>

<style lang="css">
.menu-bar {
  position: sticky;
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 40px;
  border-bottom: 1px solid black;
}

.left-menu {
  display: flex;
  margin: 8px;
  gap: 8px;
  align-items: center;
}

.logo {
  max-height: 90%;
}

.about-button {
  margin-right: 8px;
}

.dialog-box {
  max-width: 668px;
  margin: 0 16px;
}
</style>
