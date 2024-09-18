<template>
  <div class="controller-box">
    <WelcomeScreen
      v-if="showScreen(ControllerValue.WELCOME_SCREEN)"
      @start-session="startSession"
      @join-session="joinSession"
    />
    <StartScreen
      v-if="showScreen(ControllerValue.START_SCREEN)"
    />
  </div>
</template>
  
<script setup lang="ts">
import { ref, Ref } from 'vue';
import { ControllerValue } from '../constants'

import StartScreen from './StartScreen.vue';
import WelcomeScreen from './WelcomeScreen.vue';

const screenController : Ref<ControllerValue> = ref(ControllerValue.WELCOME_SCREEN)

const showScreen = (value : ControllerValue) => screenController.value === value;

function startSession() {
  screenController.value = ControllerValue.START_SCREEN;
}

function joinSession() {
  console.log('join session');
}
</script>

<style lang="css">
.controller-box {
  margin: 16px;
}
</style>