<template>
  <div class="start-screen">
    <div> Please select the number of rooms to be split and enter a label for each room: </div>
    <SelectButton 
      v-model="numRooms"
      :options
      :allowEmpty="false"
      optionLabel="name" 
      optionValue="value"
    />
    <div v-for="i in numRooms" :key="i">
      <div class='form-label'> Room {{ i }} Label </div>
      <InputText
        @update:modelValue="updateRoomLabel(i -1, $event)"
        :modelValue="roomLabels[i-1]"
        type="text"
      />
    </div>
    
    <div class="button-container">
        <Button 
          @click="$emit('back')"
          label="Go Back"
          severity="contrast"
        />
        <Button 
          @click="$emit('submit', roomLabels.slice(0,numRooms))"
          :disabled="!allRoomsHaveLabels"
          label="Submit"
          severity="contrast"
        />
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed, ref } from 'vue';
import Button from 'primevue/button';
import InputText from 'primevue/inputtext';
import SelectButton from 'primevue/selectbutton';

defineEmits(['back', 'submit']);

const options = [2, 3, 4, 5, 6, 7, 8, 9, 10].map(num => ({
    name: num.toString(),
    value: num,
}));

const numRooms = ref(2);

// 10 is the max number of rooms supported
const roomLabels = ref(Array(10).fill(''));

function updateRoomLabel(index : number, newLabel : string) {
    const roomLabelsCopy = [...roomLabels.value];
    roomLabelsCopy[index] = newLabel;
    roomLabels.value = roomLabelsCopy;
}

const allRoomsHaveLabels = computed(
    () => roomLabels.value.slice(0, numRooms.value).every(label => label)
)

</script>

<style lang="css">
.start-screen {
  min-width: 50%;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 16px;
}

.form-label {
  text-align: left;
  color: grey;
  font-size: 14px;
  margin-left: 4px;
}

.button-container {
  display: flex;
  gap: 16px;
}
</style>