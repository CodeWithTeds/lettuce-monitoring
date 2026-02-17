<script setup>
import '@dotlottie/player-component';
import { useAIPanel } from '../composables/useAIPanel';

const { isAIPanelOpen, closeAIPanel } = useAIPanel();
</script>

<template>
  <Teleport to="body">
    <!-- Panel -->
    <Transition name="slide">
      <div v-if="isAIPanelOpen" class="fixed inset-y-4 right-4 w-96 bg-white/95 backdrop-blur-xl shadow-2xl z-50 transform transition-transform duration-300 ease-out flex flex-col rounded-3xl border border-white/20 overflow-hidden ring-1 ring-black/5">
        
        <!-- Header with Gradient -->
        <div class="relative p-6 pb-8 bg-gradient-to-br from-[#15803d] to-[#166534] text-white overflow-hidden">
          <!-- Decorative Background Elements -->
          <div class="absolute top-0 right-0 -mr-8 -mt-8 w-32 h-32 bg-yellow-400 rounded-full mix-blend-overlay opacity-20 blur-2xl"></div>
          <div class="absolute bottom-0 left-0 -ml-8 -mb-8 w-32 h-32 bg-white rounded-full mix-blend-overlay opacity-10 blur-2xl"></div>

          <div class="relative z-10 flex justify-between items-start">
            <div class="flex items-center space-x-4">
              <!-- Lottie Animation Logo -->
              <div class="w-12 h-12 relative flex items-center justify-center bg-white/10 backdrop-blur-md rounded-2xl shadow-inner border border-white/20">
                 <dotlottie-player
                    src="/images/AIBot.lottie"
                    background="transparent"
                    speed="1"
                    style="width: 40px; height: 40px;"
                    loop
                    autoplay
                ></dotlottie-player>
              </div>
              <div>
                <h2 class="text-xl font-bold text-white tracking-tight">Lettuce AI</h2>
                <p class="text-xs text-green-100 font-medium flex items-center mt-1">
                  <span class="w-2 h-2 bg-green-400 rounded-full mr-1.5 animate-pulse"></span>
                  Online & Ready
                </p>
              </div>
            </div>
            <button @click="closeAIPanel" class="group p-2 rounded-xl hover:bg-white/10 transition-all duration-200">
              <svg class="w-5 h-5 text-green-100 group-hover:text-white transition-colors" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
            </button>
          </div>
        </div>
        
        <!-- Content Area -->
        <div class="flex-1 p-5 overflow-y-auto bg-gray-50 scroll-smooth">
          <!-- Welcome Message -->
          <div class="flex items-start space-x-3 mb-6 animate-fade-in-up">
            <div class="w-8 h-8 rounded-full bg-gradient-to-br from-green-100 to-green-200 flex items-center justify-center flex-shrink-0 border border-green-200">
               <svg class="w-4 h-4 text-green-700" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.75 17L9 20l-1 1h8l-1-1-.75-3M3 13h18M5 17h14a2 2 0 002-2V5a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
               </svg>
            </div>
            <div class="flex flex-col space-y-1 max-w-[85%]">
              <div class="bg-white p-4 rounded-2xl rounded-tl-none shadow-sm border border-gray-100 text-gray-600 text-sm leading-relaxed">
                <p>Hello! I'm your specialized Lettuce Monitoring Assistant. 🌱</p>
                <p class="mt-2">I can help you analyze growth patterns, check pH levels, or detect potential issues in your containers.</p>
              </div>
              <span class="text-[10px] text-gray-400 ml-1">Just now</span>
            </div>
          </div>
          
          <!-- Suggested Actions -->
          <div class="grid grid-cols-1 gap-2 mb-6 ml-11 animate-fade-in-up" style="animation-delay: 100ms;">
            <button class="text-left px-4 py-3 bg-white hover:bg-green-50 border border-gray-100 hover:border-green-200 rounded-xl text-xs font-medium text-gray-600 hover:text-green-700 transition-all duration-200 shadow-sm flex items-center group">
              <span class="w-6 h-6 rounded-lg bg-green-100 text-green-600 flex items-center justify-center mr-3 group-hover:bg-green-200 transition-colors">
                <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"></path></svg>
              </span>
              Analyze current growth rates
            </button>
            <button class="text-left px-4 py-3 bg-white hover:bg-red-50 border border-gray-100 hover:border-red-200 rounded-xl text-xs font-medium text-gray-600 hover:text-red-700 transition-all duration-200 shadow-sm flex items-center group">
              <span class="w-6 h-6 rounded-lg bg-red-100 text-red-600 flex items-center justify-center mr-3 group-hover:bg-red-200 transition-colors">
                <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"></path></svg>
              </span>
              Check for critical alerts
            </button>
          </div>

        </div>

        <!-- Input Area -->
        <div class="p-4 bg-white border-t border-gray-100">
          <div class="relative flex items-end gap-2 bg-gray-50 p-2 rounded-3xl border border-gray-200 focus-within:border-green-500/50 focus-within:ring-4 focus-within:ring-green-500/10 transition-all duration-300">
            <button class="p-2 text-gray-400 hover:text-green-600 transition-colors rounded-full hover:bg-white">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.172 7l-6.586 6.586a2 2 0 102.828 2.828l6.414-6.586a4 4 0 00-5.656-5.656l-6.415 6.585a6 6 0 108.486 8.486L20.5 13"></path></svg>
            </button>
            <textarea 
              placeholder="Ask about your lettuce..." 
              rows="1"
              class="w-full bg-transparent border-none p-2 text-sm text-gray-700 placeholder-gray-400 focus:ring-0 resize-none max-h-32"
              @input="$event.target.style.height = 'auto'; $event.target.style.height = $event.target.scrollHeight + 'px'"
            ></textarea>
            <button class="p-2 bg-[#15803d] text-white rounded-full hover:bg-[#166534] shadow-md hover:shadow-lg transform active:scale-95 transition-all duration-200 flex-shrink-0">
              <svg class="w-4 h-4 translate-x-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8"></path></svg>
            </button>
          </div>
          <p class="text-[10px] text-center text-gray-400 mt-2">AI can make mistakes. Please verify important data.</p>
        </div>
      </div>
    </Transition>
    
    <!-- Overlay -->
    <Transition name="fade">
      <div v-if="isAIPanelOpen" @click="closeAIPanel" class="fixed inset-0 bg-black/20 backdrop-blur-[2px] z-40 transition-opacity duration-300"></div>
    </Transition>
  </Teleport>
</template>

<style scoped>
.slide-enter-active,
.slide-leave-active {
  transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.3s ease;
}

.slide-enter-from,
.slide-leave-to {
  transform: translateX(20px);
  opacity: 0;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

.animate-fade-in-up {
  animation: fadeInUp 0.5s ease-out forwards;
  opacity: 0;
  transform: translateY(10px);
}

@keyframes fadeInUp {
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Custom scrollbar for the content area */
.overflow-y-auto::-webkit-scrollbar {
  width: 4px;
}

.overflow-y-auto::-webkit-scrollbar-track {
  background: transparent;
}

.overflow-y-auto::-webkit-scrollbar-thumb {
  background-color: rgba(0, 0, 0, 0.1);
  border-radius: 20px;
}
</style>
