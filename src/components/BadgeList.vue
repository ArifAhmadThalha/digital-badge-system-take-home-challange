<template>
  <v-container>
    <v-row>
      <v-col v-for="badge in badges" :key="badge.id" cols="12" sm="6" md="4">
        <v-card
          class="pa-4"
          :elevation="badge.earned ? 4 : 1"
          @click="toggleExpanded(badge.id)"
          style="cursor: pointer"
        >
          <v-img
            :src="badge.icon_url"
            alt="Badge icon"
            width="120"
            aspect-ratio="1"
            class="mb-3 mx-auto d-block position-relative"
            rounded="circle"
            cover
          >
            <template #placeholder>
              <div class="text-caption text-center pa-4">Loading...</div>
            </template>
            <template #error>
              <div class="text-caption text-center pa-4">
                Icon failed to load
              </div>
            </template>
            <template v-if="!badge.earned">
              <v-icon
                icon="mdi-lock"
                color="grey-darken-3"
                size="56"
                class="position-absolute"
                style="
                  top: 50%;
                  left: 50%;
                  transform: translate(-50%, -50%);
                  background-color: rgba(255, 255, 255, 0.8);
                  border-radius: 50%;
                  padding: 4px;
                "
              />
            </template>
          </v-img>

          <div class="font-weight-medium mb-1">{{ badge.title }}</div>

          <div class="text-caption mb-2">
            <strong>Status:</strong>
            <span :class="badge.earned ? 'text-success' : 'text-error'">
              {{
                badge.earned
                  ? "🏆 Earned on " + badge.earned_date
                  : "Not earned yet"
              }}
            </span>
          </div>

          <v-expand-transition>
            <div v-if="expandedBadge === badge.id">
              <div class="text-caption mb-1">
                <strong>Description:</strong> {{ badge.description }}
              </div>

              <div class="text-caption mb-1">
                <strong>Required Achievements:</strong>
                <ul class="pl-4">
                  <li
                    v-for="id in badge.criteria"
                    :key="id"
                    :class="
                      getStatus(id).earned ? 'text-success' : 'text-error'
                    "
                  >
                    {{ getStatus(id).earned ? "✅" : "❌" }}
                    {{ getStatus(id).title }}
                  </li>
                </ul>
              </div>

              <div class="text-caption mt-2">
                <strong>Progress:</strong> {{ countEarned(badge.criteria) }}/{{
                  badge.criteria.length
                }}
                Achievements completed
              </div>
            </div>
          </v-expand-transition>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { ref } from "vue";

const props = defineProps({
  badges: Array,
  achievements: {
    type: Array,
    default: () => [],
  },
});

const expandedBadge = ref(null);

const toggleExpanded = (id) => {
  expandedBadge.value = expandedBadge.value === id ? null : id;
};

const getStatus = (id) => {
  return (
    props.achievements.find((a) => a.id === id) || {
      title: "Unknown",
      earned: false,
    }
  );
};

const countEarned = (criteria) => {
  return criteria.filter((id) => getStatus(id).earned).length;
};
</script>
