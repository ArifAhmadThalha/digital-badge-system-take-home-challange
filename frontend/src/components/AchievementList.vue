<template>
  <v-container>
    <v-row>
      <v-col v-for="ach in achievements" :key="ach.id" cols="12" sm="6" md="4">
        <v-card class="pa-3" :elevation="ach.earned ? 4 : 1">
          <v-avatar size="48" class="mb-2">{{ ach.icon_url }}</v-avatar>
          <div class="font-weight-medium">{{ ach.title }}</div>
          <div class="text-caption">{{ ach.description }}</div>

          <div v-if="ach.earned" class="text-success mt-1">
            ✅ Earned on {{ ach.earned_date }}
          </div>
          <div v-else class="text-error mt-1">❌ Not earned yet</div>

          <v-progress-linear
            v-if="
              typeof ach.progress === 'number' &&
              typeof ach.required === 'number' &&
              ach.required > 0
            "
            :model-value="(ach.progress / ach.required) * 100"
            height="12"
            color="primary"
            striped
            rounded
            class="mt-2"
          >
            <template #default>
              <strong>{{ ach.progress }}/{{ ach.required }}</strong>
            </template>
          </v-progress-linear>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
  <v-container>
    <h2 class="text-h6 mb-2">Achievements Progress</h2>
    <v-progress-linear
      :model-value="progressPercentage"
      height="14"
      color="green"
      rounded
    >
      <template #default>
        <strong>{{ progressCount }}/{{ totalCount }} earned</strong>
      </template>
    </v-progress-linear>
  </v-container>
</template>

<script setup>
import { computed } from "vue";

const props = defineProps({
  achievements: {
    type: Array,
    default: () => [],
  },
});

const progressCount = computed(
  () => props.achievements.filter((a) => a.earned).length
);
const totalCount = computed(() => props.achievements.length);

const progressPercentage = computed(() =>
  totalCount.value ? (progressCount.value / totalCount.value) * 100 : 0
);
</script>
