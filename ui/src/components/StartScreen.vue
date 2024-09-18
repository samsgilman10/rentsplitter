<template>
  <div class="start-screen">
    <div>
        <InputText type="text" v-model="name" placeholder="Your Name" />
    </div>
    <div>
        <SelectButton v-model="numRooms" :options optionLabel="name" />
    </div>
    <div>
        <Button 
          @click="$emit('back')"
          label="Go Back"
          severity="contrast"
        />
        <Button 
          @click="$emit('submit')"
          label="Submit"
          severity="contrast"
        />
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import Button from 'primevue/button';
import InputText from 'primevue/inputtext';
import SelectButton from 'primevue/selectbutton';

const options = [2, 3, 4, 5, 6, 7, 8, 9, 10].map(num => ({
    name: num.toString(),
    value: num,
}));

const name = ref('');
const numRooms = ref(2);

</script>

<style lang="css">
.start-screen {
  min-width: 50%;
  display: flex;
  gap: 16px;
}
</style>