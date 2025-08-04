<template>
  <v-container class="d-flex justify-center align-center fill-height">
    <v-card class="pa-6" width="400">
      <h2 class="text-h5 mb-4">Login to Digital Badge System</h2>

      <v-text-field v-model="username" label="Username" required />
      <v-text-field
        v-model="password"
        label="Password"
        type="password"
        required
      />

      <v-btn color="primary" block class="mt-4" @click="login"> Login </v-btn>
    </v-card>
  </v-container>
</template>

<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";

const router = useRouter();
const username = ref("");
const password = ref("");

const login = () => {
  if (username.value && password.value) {
    router.push("/dashboard");
  } else {
    alert("Please enter both fields.");
  }
};
</script>
