<template>
  <div class="welcome-screen">
    <div>
      Welcome to RentSplitter! This is an applet that you can
      use to decide on a fair division of rent between roommates so that
      everyone is happy. To start, enter your name:
    </div>
    <InputText type="text" v-model="name" placeholder="Name" />
    <div>
      What you like to do?
    </div>
    <Button 
        @click="$emit('start-session')"
        :disabled="!name"
        label="Start a New Session"
        severity="contrast"
        class='button'
    />
    <Button
        @click="$emit('join-session')"
        :disabled="!name"
        label="Join an Existing Session"
        severity="contrast" 
        class='button'
    />
  </div>
</template>

<script setup lang="ts">
import { useSessionStorage } from '@vueuse/core';
import { nameStorageKey } from '../constants';

import Button from 'primevue/button';

defineEmits(['start-session', 'join-session'])

const name = useSessionStorage(nameStorageKey, '');
</script>

<style lang="css">
.welcome-screen {
  display: flex;
  flex-direction: column;
  gap: 16px;
  align-items: center;
}
.button {
  width: 50%;
}
</style>