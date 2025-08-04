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
    <h2 class="text-h5 mb-4">Create a Post</h2>

    <v-text-field v-model="title" label="Post title" outlined class="mb-3" />
    <v-textarea v-model="content" label="Content" rows="6" outlined />

    <v-btn color="success" class="mt-4" @click="submitPost"> Post </v-btn>

    <v-divider class="my-6" />

    <h3 class="text-h6">Recent Posts</h3>
    <v-card v-for="(post, i) in posts" :key="i" class="mb-3">
      <v-card-title>{{ post.title }}</v-card-title>
      <v-card-text>{{ post.content }}</v-card-text>
    </v-card>
  </v-container>
</template>

<script setup lang="ts">
import { useAchievementStore } from "@/stores/achievementStore";
const achievementStore = useAchievementStore();
import { ref } from "vue";
const title = ref("");
const content = ref("");
const posts = ref([
  {
    title: "Welcome to the community!",
    content: "Feel free to post updates here.",
  },
]);

const submitPost = async () => {
  if (title.value && content.value) {
    posts.value.unshift({ title: title.value, content: content.value });
    title.value = "";
    content.value = "";
  }
  try {
    const res = await fetch(
      "http://127.0.0.1:8000/api/users/1/achievements/increament/2",
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
};
</script>
