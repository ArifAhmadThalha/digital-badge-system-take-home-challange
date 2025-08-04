<template>
  <v-navigation-drawer v-model="drawer" location="right" temporary>
    <v-list>
      <v-list-item>
        <v-list-item-title class="text-h6">Settings</v-list-item-title>
      </v-list-item>
      <v-list-item>
        <v-switch v-model="isDark" label="Dark Mode" @change="toggleDarkMode" />
      </v-list-item>
    </v-list>
  </v-navigation-drawer>
  <v-navigation-drawer
    app
    permanent
    width="80"
    class="d-flex flex-column align-center py-4"
  >
    <v-btn
      icon
      @click="goTo('/dashboard')"
      :color="currentRoute === '/dashboard' ? 'primary' : 'default'"
      variant="plain"
    >
      <v-icon>mdi-view-dashboard</v-icon>
    </v-btn>

    <v-btn
      icon
      @click="goTo('/chatpage')"
      :color="currentRoute === '/chatpage' ? 'primary' : 'default'"
      variant="plain"
    >
      <v-icon>mdi-chat</v-icon>
    </v-btn>

    <v-btn
      icon
      @click="goTo('/feedbackpage')"
      :color="currentRoute === '/feedbackpage' ? 'primary' : 'default'"
      variant="plain"
    >
      <v-icon>mdi-message-text</v-icon>
    </v-btn>

    <v-btn
      icon
      @click="goTo('/postpage')"
      :color="currentRoute === '/postpage' ? 'primary' : 'default'"
      variant="plain"
    >
      <v-icon>mdi-post-outline</v-icon>
    </v-btn>
    <v-btn icon @click="drawer = !drawer" class="mb-2">
      <v-icon>mdi-cog</v-icon>
    </v-btn>
  </v-navigation-drawer>
</template>

<script setup lang="ts">
const drawer = ref(false);
import { useRoute } from "vue-router";
import { useTheme } from "vuetify";
import { useAchievementStore } from "@/stores/achievementStore";

const route = useRoute();
const router = useRouter();
const currentRoute = route.path;
const theme = useTheme();
const isDark = ref(theme.global.current.value.dark);
const achievementStore = useAchievementStore();
const userId = 1;

const toggleDarkMode = async () => {
  theme.global.name.value = isDark.value ? "dark" : "light";
  await achievementStore.earnAchievement(userId, 4);
};

const goTo = async (path: string) => {
  try {
    const res = await fetch(
      "http://127.0.0.1:8000/api/users/1/achievements/increament/7",
      {
        method: "POST",
      }
    );
    const data = await res.json();

    if (data.earned === true) {
      await achievementStore.earnAchievement(1, 7);
    }

    console.log("Achievement progress updated:", data);
  } catch (err) {
    console.error("Failed to update achievement progress:", err);
  }

  router.push(path);
};
</script>
