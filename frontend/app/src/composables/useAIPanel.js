import { ref } from 'vue';

const isAIPanelOpen = ref(false);

export function useAIPanel() {
  const toggleAIPanel = () => {
    isAIPanelOpen.value = !isAIPanelOpen.value;
  };

  const openAIPanel = () => {
    isAIPanelOpen.value = true;
  };

  const closeAIPanel = () => {
    isAIPanelOpen.value = false;
  };

  return {
    isAIPanelOpen,
    toggleAIPanel,
    openAIPanel,
    closeAIPanel
  };
}
