<template>
  <!-- 
    Temporary UI Placeholder for AI Assistant Trigger 
    TODO: Connect to actual AI functionality (Chat/Insights)
  -->
  <button 
    @click="handleClick"
    class="w-16 h-16 rounded-full bg-white/10 backdrop-blur-sm border border-white/20 flex items-center justify-center transition-all duration-200 hover:bg-white/20 hover:scale-110 hover:shadow-lg group"
    aria-label="AI Assistant"
    title="Open AI Assistant"
  >
    <!-- AI Bot Lottie Animation -->
    <dotlottie-player
        src="/images/AIBot.lottie"
        background="transparent"
        speed="1"
        style="width: 48px; height: 48px;"
        loop
        autoplay
    ></dotlottie-player>
  </button>
</template>

<script setup>
import '@dotlottie/player-component';
import { useAIPanel } from '../composables/useAIPanel';

const { toggleAIPanel } = useAIPanel();

const handleClick = () => {
  toggleAIPanel();
};
</script>
