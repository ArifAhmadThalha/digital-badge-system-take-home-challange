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
    <h2 class="text-h5 mb-4">Community Chat</h2>

    <v-card class="mb-4" height="300" style="overflow-y: auto">
      <v-list>
        <v-list-item v-for="(msg, index) in messages" :key="index">
          <v-list-item-content>
            <v-list-item-title
              ><strong>{{ msg.user }}:</strong>
              {{ msg.text }}</v-list-item-title
            >
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-card>

    <v-text-field
      v-model="newMessage"
      label="Type a message"
      @keydown.enter="sendMessage"
    />
    <v-btn color="primary" @click="sendMessage">Send</v-btn>
  </v-container>
</template>

<script setup lang="ts">
import { useAchievementStore } from "@/stores/achievementStore";
const achievementStore = useAchievementStore();
import { ref } from "vue";

const messages = ref([
  { user: "Alice", text: "Hey everyone!" },
  { user: "Bob", text: "Hello Alice!" },
]);

const newMessage = ref("");

const sendMessage = async () => {
  if (newMessage.value.trim()) {
    messages.value.push({ user: "You", text: newMessage.value });

    try {
      const res = await fetch(
        "http://127.0.0.1:8000/api/users/1/achievements/increament/8",
        {
          method: "POST",
        }
      );
      const data = await res.json();

      if (data.earned === true) {
        await achievementStore.earnAchievement(1, 8);
      }

      console.log("Achievement progress updated:", data);
    } catch (err) {
      console.error("Failed to update achievement progress:", err);
    }

    newMessage.value = "";
  }
};
</script>
