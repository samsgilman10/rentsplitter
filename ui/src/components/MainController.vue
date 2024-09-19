<template>
  <div class="controller-box">
    <WelcomeScreen
      v-if="showScreen(ControllerValue.WELCOME_SCREEN)"
      @start-session="screenController = ControllerValue.START_SCREEN"
      @join-session="screenController = ControllerValue.JOIN_SCREEN"
    />
    <StartScreen
      v-if="showScreen(ControllerValue.START_SCREEN)"
      @back="screenController = ControllerValue.WELCOME_SCREEN"
      @submit="createSession"
    />
  </div>
</template>
  
<script setup lang="ts">
import { ref, Ref } from 'vue';
import { postNewSession } from '../apiConnect';
import { ControllerValue, nameStorageKey } from '../constants'

import StartScreen from './StartScreen.vue';
import WelcomeScreen from './WelcomeScreen.vue';

const screenController : Ref<ControllerValue> = ref(ControllerValue.WELCOME_SCREEN)

const showScreen = (value : ControllerValue) => screenController.value === value;

async function createSession(roomLabels: string[]) {
  const response = await postNewSession(
    localStorage.getItem(nameStorageKey) ?? '',
    roomLabels
  );
}
</script>

<style lang="css">
.controller-box {
  margin: 16px;
}
</style>