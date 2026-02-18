<script setup>
import { ref, nextTick, watch } from 'vue';
import '@dotlottie/player-component';
import { useAIPanel } from '../composables/useAIPanel';
import { GoogleGenAI } from '@google/genai';
import { marked } from 'marked';
import DOMPurify from 'dompurify';

const { isAIPanelOpen, closeAIPanel } = useAIPanel();

const userInput = ref('');
const recommendedQuestions = [
  "How is my lettuce doing right now? 🥬",
  "Are the pH and TDS levels optimal? 💧",
  "Do I need to adjust the environment? 🌡️"
];

const sendRecommendedQuestion = (question) => {
  userInput.value = question;
  sendMessage();
};
const messages = ref([
  {
    role: 'assistant',
    content: "Hello! How can I help with your lettuce today? 🌱",
    timestamp: new Date()
  }
]);
const isLoading = ref(false);
const chatContainer = ref(null);

const scrollToBottom = async () => {
  await nextTick();
  if (chatContainer.value) {
    chatContainer.value.scrollTop = chatContainer.value.scrollHeight;
  }
};

watch(messages, () => {
  scrollToBottom();
}, { deep: true });

// Function to render Markdown safely
const renderMarkdown = (text) => {
  const rawHtml = marked(text);
  return DOMPurify.sanitize(rawHtml);
};

const sendMessage = async () => {
  if (!userInput.value.trim() || isLoading.value) return;

  const message = userInput.value.trim();
  userInput.value = '';

  // Add user message
  messages.value.push({
    role: 'user',
    content: message,
    timestamp: new Date()
  });

  isLoading.value = true;

  try {
    // 1. Fetch latest sensor data for context
    let context = "You are an AI assistant for a hydroponic lettuce monitoring system. Your name is 'Lettuce AI'.\n";
    context += "Your goal is to answer the user's question based on the sensor data provided.\n";
    context += "IMPORTANT INSTRUCTIONS:\n";
    context += "1. LANGUAGE: Respond in English.\n";
    context += "2. TECHNICAL TERMS: Use standard technical terms (e.g., 'pH Level', 'TDS', 'Pump', 'Temperature', 'Nutrients').\n";
    context += "3. ANALYSIS: Analyze the sensor data carefully. If a value is outside the optimal range, explain clearly why it is bad.\n";
    context += "4. SENSOR ERRORS: If pH > 14 or < 0, mention it might be a sensor error.\n";
    context += "5. TONE: Be friendly, helpful, and encouraging.\n\n";

    context += "Optimal Ranges for Lettuce:\n";
    context += "- Temperature: 18°C - 24°C\n";
    context += "- Humidity: 50% - 70%\n";
    context += "- pH Level: 5.5 - 6.5\n";
    context += "- TDS (Nutrients): 560 - 840 ppm\n\n";

    try {
      const sensorResponse = await fetch('http://localhost:8000/api/sensor-readings/latest');
      if (sensorResponse.ok) {
        const latestReading = await sensorResponse.json();
        if (latestReading) {
          context += "CURRENT SYSTEM STATUS:\n";
          context += `- Temperature: ${latestReading.temperature}°C\n`;
          context += `- Humidity: ${latestReading.humidity}%\n`;
          context += `- pH Level: ${latestReading.ph}\n`;
          context += `- TDS (Nutrients): ${latestReading.tds} ppm\n`;
          context += `- Water Pump: ${latestReading.pump_status ? 'ON' : 'OFF'}\n`;
          context += `- Ventilation Fan: ${latestReading.fan_status ? 'ON' : 'OFF'}\n`;
        }
      }
    } catch (err) {
      console.warn('Failed to fetch sensor context:', err);
      context += "System status is currently unavailable.\n";
    }

    context += "\nUser Question: " + message;

    // 2. Call Gemini API directly
    const genAI = new GoogleGenAI({ apiKey: import.meta.env.VITE_GEMINI_API_KEY });
    const response = await genAI.models.generateContent({
      model: "gemma-3-1b-it",
      contents: [{
        parts: [{ text: context }]
      }],
    });

    // In the new @google/genai SDK, response.text is a property/getter, not a function
    const aiResponse = response.text ||
      response.candidates?.[0]?.content?.parts?.[0]?.text ||
      "I received a response, but couldn't parse the text.";

    messages.value.push({
      role: 'assistant',
      content: aiResponse,
      timestamp: new Date()
    });

  } catch (error) {
    console.error('AI Chat Error:', error);
    messages.value.push({
      role: 'assistant',
      content: "Sorry, I encountered an error communicating with the AI service. " + (error.message || ''),
      timestamp: new Date()
    });
  } finally {
    isLoading.value = false;
  }
};

const formatTime = (date) => {
  return new Intl.DateTimeFormat('en-US', { hour: 'numeric', minute: 'numeric', hour12: true }).format(date);
};
</script>

<template>
  <Teleport to="body">
    <!-- Panel -->
    <Transition name="slide">
      <div v-if="isAIPanelOpen"
        class="fixed inset-y-4 right-4 w-96 bg-white/95 backdrop-blur-xl shadow-2xl z-50 transform transition-transform duration-300 ease-out flex flex-col rounded-3xl border border-white/20 overflow-hidden ring-1 ring-black/5">

        <!-- Header with Gradient -->
        <div class="relative p-6 pb-8 bg-gradient-to-br from-[#15803d] to-[#166534] text-white overflow-hidden">
          <!-- Decorative Background Elements -->
          <div
            class="absolute top-0 right-0 -mr-8 -mt-8 w-32 h-32 bg-yellow-400 rounded-full mix-blend-overlay opacity-20 blur-2xl">
          </div>
          <div
            class="absolute bottom-0 left-0 -ml-8 -mb-8 w-32 h-32 bg-white rounded-full mix-blend-overlay opacity-10 blur-2xl">
          </div>

          <div class="relative z-10 flex justify-between items-start">
            <div class="flex items-center space-x-4">
              <!-- Lottie Animation Logo -->
              <div
                class="w-12 h-12 relative flex items-center justify-center bg-white/10 backdrop-blur-md rounded-2xl shadow-inner border border-white/20">
                <dotlottie-player src="/images/AIBot.lottie" background="transparent" speed="1"
                  style="width: 40px; height: 40px;" loop autoplay></dotlottie-player>
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
              <svg class="w-5 h-5 text-green-100 group-hover:text-white transition-colors" fill="none"
                stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
              </svg>
            </button>
          </div>
        </div>

        <!-- Content Area -->
        <div ref="chatContainer" class="flex-1 p-5 overflow-y-auto bg-gray-50 scroll-smooth space-y-4">

          <div v-for="(msg, index) in messages" :key="index" class="flex items-start space-x-3 animate-fade-in-up"
            :class="msg.role === 'user' ? 'flex-row-reverse space-x-reverse' : ''">

            <!-- Avatar -->
            <div v-if="msg.role === 'assistant'"
              class="w-8 h-8 rounded-full bg-gradient-to-br from-green-100 to-green-200 flex items-center justify-center flex-shrink-0 border border-green-200">
              <svg class="w-4 h-4 text-green-700" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                  d="M9.75 17L9 20l-1 1h8l-1-1-.75-3M3 13h18M5 17h14a2 2 0 002-2V5a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
              </svg>
            </div>
            <div v-else
              class="w-8 h-8 rounded-full bg-blue-100 flex items-center justify-center flex-shrink-0 border border-blue-200">
              <svg class="w-4 h-4 text-blue-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                  d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
              </svg>
            </div>

            <!-- Message Bubble -->
            <div class="flex flex-col space-y-1 max-w-[85%]">
              <div class="p-4 rounded-2xl shadow-sm border text-sm leading-relaxed whitespace-pre-wrap" :class="msg.role === 'user'
                ? 'bg-green-600 text-white rounded-tr-none border-green-600'
                : 'bg-white text-gray-600 rounded-tl-none border-gray-100'">
                <!-- Render Markdown Content -->
                <div v-if="msg.role === 'assistant'" v-html="renderMarkdown(msg.content)"
                  class="prose prose-sm max-w-none"></div>
                <div v-else>{{ msg.content }}</div>
              </div>
              <span class="text-[10px] text-gray-400" :class="msg.role === 'user' ? 'text-right' : 'ml-1'">{{
                formatTime(msg.timestamp) }}</span>
            </div>
          </div>

          <!-- Recommended Questions -->
          <div v-if="messages.length === 1 && !isLoading" class="mt-4 px-2 space-y-3 animate-fade-in-up"
            style="animation-delay: 0.1s">
            <div class="flex flex-col gap-2">
              <button v-for="(question, index) in recommendedQuestions" :key="index"
                @click="sendRecommendedQuestion(question)"
                class="w-full text-left p-3.5 bg-white border border-green-100 rounded-xl text-sm font-medium text-gray-700 hover:bg-green-50 hover:border-green-300 hover:text-green-800 hover:shadow-md transition-all duration-200 flex items-center justify-between group">
                <span>{{ question }}</span>
                <svg
                  class="w-4 h-4 text-green-400 opacity-0 group-hover:opacity-100 -translate-x-2 group-hover:translate-x-0 transition-all duration-300"
                  fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
                </svg>
              </button>
            </div>
          </div>

          <!-- Loading Indicator -->
          <div v-if="isLoading" class="flex items-start space-x-3 animate-pulse">
            <div class="w-8 h-8 rounded-full bg-gray-200"></div>
            <div class="bg-white p-4 rounded-2xl rounded-tl-none shadow-sm border border-gray-100">
              <div class="flex space-x-1">
                <div class="w-2 h-2 bg-gray-400 rounded-full animate-bounce"></div>
                <div class="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style="animation-delay: 0.2s"></div>
                <div class="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style="animation-delay: 0.4s"></div>
              </div>
            </div>
          </div>

        </div>

        <!-- Input Area -->
        <div class="p-4 bg-white border-t border-gray-100">
          <div
            class="relative flex items-end gap-2 bg-gray-50 p-2 rounded-3xl border border-gray-200 focus-within:border-green-500/50 focus-within:ring-4 focus-within:ring-green-500/10 transition-all duration-300">
            <button class="p-2 text-gray-400 hover:text-green-600 transition-colors rounded-full hover:bg-white">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                  d="M15.172 7l-6.586 6.586a2 2 0 102.828 2.828l6.414-6.586a4 4 0 00-5.656-5.656l-6.415 6.585a6 6 0 108.486 8.486L20.5 13">
                </path>
              </svg>
            </button>
            <textarea v-model="userInput" @keydown.enter.prevent="sendMessage" placeholder="Ask about your lettuce..."
              rows="1"
              class="w-full bg-transparent border-none p-2 text-sm text-gray-700 placeholder-gray-400 focus:ring-0 resize-none max-h-32 focus:outline-none"
              @input="$event.target.style.height = 'auto'; $event.target.style.height = $event.target.scrollHeight + 'px'"></textarea>
            <button @click="sendMessage" :disabled="!userInput.trim() || isLoading"
              class="p-2 bg-[#15803d] text-white rounded-full hover:bg-[#166534] shadow-md hover:shadow-lg transform active:scale-95 transition-all duration-200 flex-shrink-0 disabled:opacity-50 disabled:cursor-not-allowed">
              <svg class="w-4 h-4 translate-x-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                  d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8"></path>
              </svg>
            </button>
          </div>
          <p class="text-[10px] text-center text-gray-400 mt-2">AI can make mistakes. Please verify important data.</p>
        </div>
      </div>
    </Transition>

    <!-- Overlay -->
    <Transition name="fade">
      <div v-if="isAIPanelOpen" @click="closeAIPanel"
        class="fixed inset-0 bg-black/20 backdrop-blur-[2px] z-40 transition-opacity duration-300"></div>
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
