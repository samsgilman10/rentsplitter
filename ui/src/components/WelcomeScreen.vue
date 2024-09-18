<template>
  <div>
    Welcome to RentSplitter! This is an applet that you can
    use to decide on a fair division of rent between roommates so that
    everyone is happy.
    What you like to do?
    <div class='button-wrapper'>
        <Button 
          @click="$emit('start-session')"
          label="Start a New Session"
          severity="contrast"
        />
        <Button
          @click="$emit('join-session')"
          label="Join an Existing Session"
          severity="contrast" 
        />
    </div>
  </div>
</template>

<script setup lang="ts">
import Button from 'primevue/button';

defineEmits(['start-session', 'join-session'])
</script>

<style lang="css">
.button-wrapper {
  margin: 16px auto;
  display: flex;
  gap: 16px;
  flex-direction: column;
  width: 50%;
}
</style>