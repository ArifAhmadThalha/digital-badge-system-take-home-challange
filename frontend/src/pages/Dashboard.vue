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
    <UserProfile :user="user" :badges="badges" :achievements="achievements" />
    <v-tabs v-model="activeTab" class="mb-4">
      <v-tab value="badges">🏅 Badges</v-tab>
      <v-tab value="achievements">🎯 Achievements</v-tab>
    </v-tabs>
    <div v-if="activeTab === 'badges'">
      <BadgeList :badges="badges" :achievements="achievements" />
    </div>

    <div v-else>
      <v-text-field
        v-model="search"
        label="Search Achievements"
        prepend-inner-icon="mdi-magnify"
        class="mb-4"
        clearable
      />
      <AchievementList :achievements="filteredAchievements" />
    </div>
  </v-container>
</template>

<script setup>
import { ref, computed, onMounted } from "vue";
import UserProfile from "@/components/UserProfile.vue";
import BadgeList from "@/components/BadgeList.vue";
import AchievementList from "@/components/AchievementList.vue";
import SideNav from "@/components/SideNav.vue";
import { useAchievementStore } from "@/stores/achievementStore";
const achievementStore = useAchievementStore();
const activeTab = ref("badges");
const user = ref({});
const badges = ref([]);
const achievements = ref([]);
const search = ref("");

const filteredAchievements = computed(() =>
  achievements.value.filter(
    (a) =>
      a.title.toLowerCase().includes(search.value.toLowerCase()) ||
      a.description.toLowerCase().includes(search.value.toLowerCase())
  )
);

onMounted(async () => {
  const [badgeRes, achievementRes] = await Promise.all([
    fetch("http://127.0.0.1:8000/api/users/1/badges"),
    fetch("http://127.0.0.1:8000/api/users/1/achievements"),
  ]);
  const badgeData = await badgeRes.json();
  const achData = await achievementRes.json();

  user.value = badgeData.user;
  badges.value = badgeData.badges;
  achievements.value = achData.achievements;
});
</script>
