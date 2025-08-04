<template>
  <v-card class="pa-6 mb-6" elevation="4">
    <v-row>
      <v-col cols="12" md="3" class="d-flex align-center justify-center">
        <v-avatar size="96">
          <v-img :src="user.avatar" alt="User avatar" />
        </v-avatar>
      </v-col>

      <v-col cols="12" md="9">
        <h2 class="text-h5 font-weight-bold">{{ user.name }}</h2>
        <p class="text-subtitle-1 mb-1"><strong>Email:</strong> {{ user.email }}</p>
        <p class="text-subtitle-1 mb-1"><strong>Role:</strong> {{ user.role }}</p>
        <p class="text-subtitle-2"><strong>Badges Earned:</strong> {{ earnedCount }} / {{ totalBadges }}</p>
        <p class="text-subtitle-2"><strong>Achievements Earned:</strong> {{ earnedCount2 }} / {{ totalAchievements }}</p>
      </v-col>
    </v-row>
  </v-card>
</template>

<script setup>
const props = defineProps({
  user: Object,
  badges: Array,
  achievements: Array
})

const earnedCount = computed(() => props.badges.filter(b => b.earned).length)
const earnedCount2 = computed(() => props.achievements.filter(a => a.earned).length)
const totalBadges = computed(() => props.badges.length)
const totalAchievements = computed(() => props.achievements.length)
</script>

