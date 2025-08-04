import { defineStore } from "pinia";

export const useAchievementStore = defineStore("achievement", {
  state: () => ({
    earnedAchievements: new Set<number>(),
    popupVisible: false,
    popupTitle: "",
  }),

  actions: {
    async earnAchievement(userId: number, achievementId: number) {
      if (this.earnedAchievements.has(achievementId)) {
        return;
      }

      try {
        const res = await fetch("http://127.0.0.1:8000/api/achievements/earn", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            user_id: userId,
            achievement_id: achievementId,
          }),
        });

        if (res.ok) {
          this.earnedAchievements.add(achievementId);

          // 🎉 Show popup
          this.popupTitle = `Achievement Unlocked!`;
          this.popupVisible = true;

          setTimeout(() => {
            this.popupVisible = false;
          }, 3000);
        } else {
          console.warn(`Server error: ${res.status}`);
        }
      } catch (err) {
        console.error(`Failed to earn achievement ${achievementId}:`, err);
      }
    },

    isEarned(achievementId: number) {
      return this.earnedAchievements.has(achievementId);
    },
  },
});
