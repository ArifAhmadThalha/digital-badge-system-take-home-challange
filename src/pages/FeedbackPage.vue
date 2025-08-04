<template>
  <v-snackbar
    v-model="achievementStore.popupVisible"
    color="success"
    timeout="3000"
  >
    🎉 {{ achievementStore.popupTitle }}
  </v-snackbar>
  <SideNav></SideNav>
  <v-container>
    <h2 class="text-h5 mb-4">Submit Feedback</h2>
    <v-textarea v-model="feedback" label="Your feedback" rows="5" outlined />
    <v-btn class="mt-3" color="primary" @click="submitFeedback"> Submit </v-btn>
  </v-container>
</template>

<script setup lang="ts">
import { ref } from "vue";
import { useAchievementStore } from "@/stores/achievementStore";

const feedback = ref("");
const achievementStore = useAchievementStore();
const userId = 1;

const submitFeedback = async () => {
  await achievementStore.earnAchievement(userId, 5);
  console.log("Feedback submitted:", feedback.value);
  feedback.value = "";
  alert("Thanks for your feedback!");
};
</script>
