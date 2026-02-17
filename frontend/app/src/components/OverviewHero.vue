<script setup>
import { ref, onMounted, onUnmounted } from 'vue';

const sensorData = ref({
  temperature: 0,
  humidity: 0,
  ph: 0,
  tds: 0,
  pump_status: false,
  fan_status: false,
});

const deviceStates = ref({
  pump: false,
  fan: false,
});

const activeTab = ref('monitor');

const fetchData = async () => {
  try {
    const response = await fetch('http://localhost:8000/api/sensor-readings/latest');
    const data = await response.json();
    if (data) {
      sensorData.value = data;
    }
  } catch (error) {
    console.error('Error fetching sensor data:', error);
  }
};

const fetchDeviceStates = async () => {
  try {
    const response = await fetch('http://localhost:8000/api/device-states');
    const data = await response.json();
    if (data) {
      data.forEach(device => {
        if (device.device === 'pump') deviceStates.value.pump = device.is_on;
        if (device.device === 'fan') deviceStates.value.fan = device.is_on;
      });
    }
  } catch (error) {
    console.error('Error fetching device states:', error);
  }
};

const toggleDevice = async (device) => {
  try {
    // Optimistic update
    deviceStates.value[device] = !deviceStates.value[device];

    const response = await fetch(`http://localhost:8000/api/device-states/${device}/toggle`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
    });

    if (!response.ok) {
      // Revert on error
      deviceStates.value[device] = !deviceStates.value[device];
      console.error('Failed to toggle device');
    }
  } catch (error) {
    deviceStates.value[device] = !deviceStates.value[device];
    console.error('Error toggling device:', error);
  }
};

let intervalId;

onMounted(() => {
  fetchData();
  fetchDeviceStates();
  intervalId = setInterval(() => {
    fetchData();
    // Optional: poll device states too if other users might change it
    // fetchDeviceStates(); 
  }, 5000);
});

onUnmounted(() => {
  clearInterval(intervalId);
});
</script>

<template>
  <!-- Desktop Layout -->
  <div class="relative pb-12 lg:pb-20 hidden lg:block">
    <div class="flex flex-col lg:flex-row items-start lg:items-center justify-between">
      <!-- Left Content -->
      <div class="space-y-6 z-10 relative max-w-lg w-full">
        <h1 class="text-3xl md:text-5xl font-bold text-white tracking-tight">Overview</h1>

        <!-- Modern Inline Sensor Display -->
        <div class="grid grid-cols-2 gap-4 w-full items-start">

          <!-- Humidity -->
          <div
            class="bg-white/10 backdrop-blur-md border border-white/20 rounded-2xl p-3 flex flex-col justify-between hover:bg-white/15 transition-all duration-300 group">
            <div class="flex items-center space-x-2 mb-1">
              <div
                class="p-1.5 bg-blue-500/20 rounded-lg text-blue-300 group-hover:text-blue-200 group-hover:bg-blue-500/30 transition-colors">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4"></path>
                </svg>
              </div>
              <span class="text-xs font-medium text-white/80 uppercase tracking-wider">Humidity</span>
            </div>
            <div class="flex items-end space-x-2">
              <span class="text-2xl font-bold text-white">{{ sensorData.humidity }}</span>
              <span class="text-sm text-white/60 mb-1">%</span>
            </div>
          </div>

          <!-- pH Level -->
          <div
            class="bg-white/10 backdrop-blur-md border border-white/20 rounded-2xl p-3 flex flex-col justify-between hover:bg-white/15 transition-all duration-300 group mt-12">
            <div class="flex items-center space-x-2 mb-1">
              <div
                class="p-1.5 bg-green-500/20 rounded-lg text-green-300 group-hover:text-green-200 group-hover:bg-green-500/30 transition-colors">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M19.428 15.428a2 2 0 00-1.022-.547l-2.384-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z">
                  </path>
                </svg>
              </div>
              <span class="text-xs font-medium text-white/80 uppercase tracking-wider">pH Level</span>
            </div>
            <div class="flex items-end space-x-2">
              <span class="text-2xl font-bold text-white">{{ sensorData.ph }}</span>
              <span class="text-sm text-white/60 mb-1">pH</span>
            </div>
          </div>

          <!-- Temperature -->
          <div
            class="bg-white/10 backdrop-blur-md border border-white/20 rounded-2xl p-3 flex flex-col justify-between hover:bg-white/15 transition-all duration-300 group">
            <div class="flex items-center space-x-2 mb-1">
              <div
                class="p-1.5 bg-yellow-500/20 rounded-lg text-yellow-300 group-hover:text-yellow-200 group-hover:bg-yellow-500/30 transition-colors">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z">
                  </path>
                </svg>
              </div>
              <span class="text-xs font-medium text-white/80 uppercase tracking-wider">Temp</span>
            </div>
            <div class="flex items-end space-x-2">
              <span class="text-2xl font-bold text-white">{{ sensorData.temperature }}</span>
              <span class="text-sm text-white/60 mb-1">°C</span>
            </div>
          </div>

          <!-- TDS Level -->
          <div
            class="bg-white/10 backdrop-blur-md border border-white/20 rounded-2xl p-3 flex flex-col justify-between hover:bg-white/15 transition-all duration-300 group mt-12">
            <div class="flex items-center space-x-2 mb-1">
              <div
                class="p-1.5 bg-purple-500/20 rounded-lg text-purple-300 group-hover:text-purple-200 group-hover:bg-purple-500/30 transition-colors">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z">
                  </path>
                </svg>
              </div>
              <span class="text-xs font-medium text-white/80 uppercase tracking-wider">TDS</span>
            </div>
            <div class="flex items-end space-x-2">
              <span class="text-2xl font-bold text-white">{{ sensorData.tds }}</span>
              <span class="text-sm text-white/60 mb-1">ppm</span>
            </div>
          </div>

        </div>

        <!-- Device Controls -->
        <div class="flex flex-wrap gap-3 mt-6">
          <!-- Pump Toggle -->
          <button @click="toggleDevice('pump')"
            class="flex items-center justify-between w-full md:w-auto min-w-[160px] px-4 py-3 rounded-2xl transition-all duration-300 border backdrop-blur-sm group"
            :class="deviceStates.pump
              ? 'bg-white border-white text-[#15803d] shadow-xl translate-y-[-2px]'
              : 'bg-white/5 border-white/10 text-white hover:bg-white/10'">
            <div class="flex items-center space-x-3">
              <div class="p-1.5 rounded-full transition-colors duration-300"
                :class="deviceStates.pump ? 'bg-[#15803d]/10 text-[#15803d]' : 'bg-white/10 text-white/60'">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M19.428 15.428a2 2 0 00-1.022-.547l-2.384-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z">
                  </path>
                </svg>
              </div>
              <div class="text-left">
                <div class="text-[10px] font-bold uppercase tracking-wider opacity-70">Water Pump</div>
                <div class="text-lg font-bold">{{ deviceStates.pump ? 'ON' : 'OFF' }}</div>
              </div>
            </div>
            <div class="w-2.5 h-2.5 rounded-full shadow-inner transition-colors duration-300"
              :class="deviceStates.pump ? 'bg-green-500 shadow-green-500/50' : 'bg-red-500/50'"></div>
          </button>

          <!-- Fan Toggle -->
          <button @click="toggleDevice('fan')"
            class="flex items-center justify-between w-full md:w-auto min-w-[160px] px-4 py-3 rounded-2xl transition-all duration-300 border backdrop-blur-sm group"
            :class="deviceStates.fan
              ? 'bg-white border-white text-[#15803d] shadow-xl translate-y-[-2px]'
              : 'bg-white/5 border-white/10 text-white hover:bg-white/10'">
            <div class="flex items-center space-x-3">
              <div class="p-1.5 rounded-full transition-colors duration-300"
                :class="deviceStates.fan ? 'bg-[#15803d]/10 text-[#15803d]' : 'bg-white/10 text-white/60'">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M14 10l-2 1m0 0l-2-1m2 1v2.5M20 7l-2 1m2-1l-2-1m2 1v2.5M14 4l-2-1-2 1M4 7l2-1M4 7l2 1M4 7v2.5M12 21l-2-1m2 1l2-1m-2 1v-2.5M6 18l-2-1v-2.5M18 18l2-1v-2.5">
                  </path>
                </svg>
              </div>
              <div class="text-left">
                <div class="text-[10px] font-bold uppercase tracking-wider opacity-70">Vent Fan</div>
                <div class="text-lg font-bold">{{ deviceStates.fan ? 'ON' : 'OFF' }}</div>
              </div>
            </div>
            <div class="w-2.5 h-2.5 rounded-full shadow-inner transition-colors duration-300"
              :class="deviceStates.fan ? 'bg-green-500 shadow-green-500/50' : 'bg-red-500/50'"></div>
          </button>
        </div>
      </div>

      <!-- Plant Image with Floating Labels -->
      <div
        class="absolute right-0 top-10 md:-top-10 w-full md:w-1/2 lg:w-[40%] h-full pointer-events-none flex justify-center lg:justify-end opacity-20 lg:opacity-100 transition-opacity duration-500">
        <div class="relative w-full max-w-[500px] aspect-square">
          <!-- Main Image -->
          <img src="/images/lettuce.png" alt="Monitoring Plant"
            class="w-full h-full object-contain drop-shadow-2xl filter brightness-110" />

          <!-- Floating Labels -->
          <!-- Health -->
          <div
            class="absolute top-10 left-10 bg-white/90 backdrop-blur-sm px-4 py-2 rounded-2xl shadow-xl flex items-center space-x-3 animate-bounce-slow border border-white/50">
            <div class="w-3 h-3 bg-green-500 rounded-full shadow-lg shadow-green-500/50"></div>
            <span class="text-sm font-bold text-gray-800">Health: Good</span>
          </div>

          <!-- Harvest Time -->
          <div
            class="absolute top-20 right-0 bg-white/90 backdrop-blur-sm px-4 py-2 rounded-2xl shadow-xl flex items-center space-x-3 animate-bounce-delayed border border-white/50">
            <div class="p-1 bg-green-100 rounded-lg text-green-600">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                  d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path>
              </svg>
            </div>
            <div>
              <div class="text-[10px] uppercase text-gray-500 font-bold tracking-wider">Est. Harvest</div>
              <div class="text-sm font-bold text-gray-800">~14 Days</div>
            </div>
          </div>

          <!-- Growth Stage -->
          <div
            class="absolute bottom-20 left-0 bg-white/90 backdrop-blur-sm px-4 py-2 rounded-2xl shadow-xl flex items-center space-x-3 animate-bounce-reverse border border-white/50">
            <div class="p-1 bg-blue-100 rounded-lg text-blue-600">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                  d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"></path>
              </svg>
            </div>
            <div>
              <div class="text-[10px] uppercase text-gray-500 font-bold tracking-wider">Growth Rate</div>
              <div class="text-sm font-bold text-gray-800">Optimal</div>
            </div>
          </div>


          <div
            class="absolute bottom-10 right-10 bg-green-600 text-white px-3 py-1 rounded-full text-xs font-bold shadow-lg animate-pulse">
            Lettuce
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Mobile Layout -->
  <div class="fixed inset-0 lg:hidden flex flex-col bg-[#15803d] text-white z-50 overflow-hidden">
    <!-- Top Header -->
    <div class="px-6 pt-12 pb-4 flex justify-between items-center">
      <div class="flex items-center space-x-2">
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path>
        </svg>
        <span class="text-xl font-bold">My Garden</span>
      </div>
      <button class="p-2 bg-white/10 rounded-full backdrop-blur-md">
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
            d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z">
          </path>
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z">
          </path>
        </svg>
      </button>
    </div>

    <!-- Main Plant Section -->
    <div class="flex-1 relative flex flex-col">
      <!-- Plant Image & Info Row -->
      <div class="flex items-start px-6 pt-4 h-[45%]">
        <!-- Plant Image (Left) -->
        <div class="w-1/2 relative z-20">
          <img src="/images/image.png" alt="Lettuce" class="w-full h-full object-contain drop-shadow-2xl scale-90" />
        </div>

        <!-- Right Side Stats -->
        <div class="w-1/2 pl-4 space-y-6 pt-4">
          <div>
            <h2 class="text-3xl font-bold leading-tight">Lettuce</h2>
            <p class="text-white/70 text-sm font-medium">Week 4 • Harvest Soon</p>
          </div>

          <!-- Humidity -->
          <div class="flex items-center space-x-3">
            <div class="p-2 bg-white/10 rounded-xl backdrop-blur-md">
              <svg class="w-5 h-5 text-blue-200" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                  d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4"></path>
              </svg>
            </div>
            <div>
              <div class="text-xl font-bold">{{ sensorData.humidity }}%</div>
              <div class="text-xs text-white/60 font-medium uppercase tracking-wide">Humidity</div>
            </div>
          </div>

          <!-- TDS -->
          <div class="flex items-center space-x-3">
            <div class="p-2 bg-white/10 rounded-xl backdrop-blur-md">
              <svg class="w-5 h-5 text-purple-200" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z">
                </path>
              </svg>
            </div>
            <div>
              <div class="text-xl font-bold">{{ sensorData.tds }}</div>
              <div class="text-xs text-white/60 font-medium uppercase tracking-wide">Nutrients</div>
            </div>
          </div>

          <!-- Fan Status (as Next Watering equiv) -->
          <div class="flex items-center space-x-3">
            <div class="p-2 bg-white/10 rounded-xl backdrop-blur-md">
              <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                  d="M14 10l-2 1m0 0l-2-1m2 1v2.5M20 7l-2 1m2-1l-2-1m2 1v2.5M14 4l-2-1-2 1M4 7l2-1M4 7l2 1M4 7v2.5M12 21l-2-1m2 1l2-1m-2 1v-2.5M6 18l-2-1v-2.5M18 18l2-1v-2.5">
                </path>
              </svg>
            </div>
            <div>
              <div class="text-lg font-bold">{{ deviceStates.fan ? 'Active' : 'Idle' }}</div>
              <div class="text-xs text-white/60 font-medium uppercase tracking-wide">Ventilation</div>
            </div>
          </div>
        </div>
      </div>

      <!-- Bottom White Card -->
      <div class="bg-white rounded-t-[40px] flex-1 mt-auto relative z-10 px-8 pt-10 pb-6 shadow-2xl overflow-y-auto">

        <!-- Alert Banner -->
        <div v-if="!deviceStates.pump" class="flex items-start space-x-3 mb-8 pl-2 border-l-4 border-orange-500">
          <div>
            <h3 class="text-gray-900 font-bold text-lg">Check Water Pump!</h3>
            <p class="text-gray-500 text-sm">Pump is currently OFF. Ensure proper irrigation.</p>
          </div>
        </div>
        <div v-else class="flex items-start space-x-3 mb-8 pl-2 border-l-4 border-green-500">
          <div>
            <h3 class="text-gray-900 font-bold text-lg">System Healthy</h3>
            <p class="text-gray-500 text-sm">All systems running optimally.</p>
          </div>
        </div>

        <!-- Primary Metrics Row -->
        <div class="flex justify-between items-end mb-10">
          <!-- Pump/Water -->
          <div class="text-center group cursor-pointer" @click="toggleDevice('pump')">
            <div class="relative inline-block mb-2">
              <div class="w-2 h-8 bg-gray-200 rounded-full overflow-hidden mx-auto">
                <div class="w-full bg-blue-500 transition-all duration-500"
                  :style="{ height: deviceStates.pump ? '100%' : '20%' }"></div>
              </div>
              <!-- Indicator dot -->
              <div class="absolute -right-2 top-0 w-2 h-2 rounded-full"
                :class="deviceStates.pump ? 'bg-green-500' : 'bg-red-500'"></div>
            </div>
            <div class="text-3xl font-bold text-gray-900">{{ deviceStates.pump ? 'ON' : 'OFF' }}</div>
            <div class="text-sm text-gray-500 font-medium mt-1">Pump</div>
          </div>

          <!-- pH Level -->
          <div class="text-center">
            <div class="text-4xl font-bold text-gray-900">{{ sensorData.ph }}<span
                class="text-lg align-top text-gray-400">%</span></div>
            <div class="text-sm text-gray-500 font-medium mt-1 flex items-center justify-center gap-1">
              pH Level
              <svg class="w-3 h-3 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
              </svg>
            </div>
          </div>

          <!-- Temperature -->
          <div class="text-center">
            <div class="text-4xl font-bold text-gray-900">{{ sensorData.temperature }}<span
                class="text-lg align-top text-gray-400">°C</span></div>
            <div class="text-sm text-gray-500 font-medium mt-1 flex items-center justify-center gap-1">
              Temp.
              <svg class="w-3 h-3 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
              </svg>
            </div>
          </div>
        </div>

        <!-- Bottom Tabs -->
        <div class="flex items-center justify-between mt-auto pt-4 border-t border-gray-100">
          <button @click="activeTab = 'monitor'"
            class="flex items-center space-x-2 px-6 py-3 rounded-2xl transition-all duration-300"
            :class="activeTab === 'monitor' ? 'bg-[#15803d] text-white shadow-lg shadow-green-900/20' : 'text-gray-400 hover:bg-gray-50'">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z">
              </path>
            </svg>
            <span class="font-bold">Monitor</span>
          </button>

          <button @click="activeTab = 'controls'"
            class="flex items-center space-x-2 px-6 py-3 rounded-2xl transition-all duration-300"
            :class="activeTab === 'controls' ? 'bg-[#15803d] text-white shadow-lg shadow-green-900/20' : 'text-gray-400 hover:bg-gray-50'">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4">
              </path>
            </svg>
            <span class="font-bold">Controls</span>
          </button>
        </div>

        <!-- Quick Controls Overlay (visible when Controls tab active) -->
        <div v-if="activeTab === 'controls'"
          class="absolute inset-0 bg-white z-20 rounded-t-[40px] p-8 pt-12 animate-slide-up">
          <h3 class="text-2xl font-bold text-gray-900 mb-6">Device Controls</h3>
          <div class="space-y-4">
            <button @click="toggleDevice('pump')"
              class="w-full p-4 rounded-2xl flex items-center justify-between border-2 transition-all"
              :class="deviceStates.pump ? 'border-green-500 bg-green-50' : 'border-gray-200'">
              <div class="flex items-center space-x-4">
                <div class="p-3 rounded-full"
                  :class="deviceStates.pump ? 'bg-green-100 text-green-600' : 'bg-gray-100 text-gray-400'">
                  <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                      d="M19.428 15.428a2 2 0 00-1.022-.547l-2.384-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z">
                    </path>
                  </svg>
                </div>
                <div class="text-left">
                  <div class="font-bold text-gray-900">Water Pump</div>
                  <div class="text-sm text-gray-500">{{ deviceStates.pump ? 'Running' : 'Stopped' }}</div>
                </div>
              </div>
              <div class="w-12 h-6 bg-gray-200 rounded-full relative transition-colors duration-300"
                :class="{ 'bg-green-500': deviceStates.pump }">
                <div class="absolute top-1 left-1 bg-white w-4 h-4 rounded-full transition-transform duration-300"
                  :class="{ 'translate-x-6': deviceStates.pump }"></div>
              </div>
            </button>

            <button @click="toggleDevice('fan')"
              class="w-full p-4 rounded-2xl flex items-center justify-between border-2 transition-all"
              :class="deviceStates.fan ? 'border-green-500 bg-green-50' : 'border-gray-200'">
              <div class="flex items-center space-x-4">
                <div class="p-3 rounded-full"
                  :class="deviceStates.fan ? 'bg-green-100 text-green-600' : 'bg-gray-100 text-gray-400'">
                  <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                      d="M14 10l-2 1m0 0l-2-1m2 1v2.5M20 7l-2 1m2-1l-2-1m2 1v2.5M14 4l-2-1-2 1M4 7l2-1M4 7l2 1M4 7v2.5M12 21l-2-1m2 1l2-1m-2 1v-2.5M6 18l-2-1v-2.5M18 18l2-1v-2.5">
                    </path>
                  </svg>
                </div>
                <div class="text-left">
                  <div class="font-bold text-gray-900">Ventilation Fan</div>
                  <div class="text-sm text-gray-500">{{ deviceStates.fan ? 'Active' : 'Idle' }}</div>
                </div>
              </div>
              <div class="w-12 h-6 bg-gray-200 rounded-full relative transition-colors duration-300"
                :class="{ 'bg-green-500': deviceStates.fan }">
                <div class="absolute top-1 left-1 bg-white w-4 h-4 rounded-full transition-transform duration-300"
                  :class="{ 'translate-x-6': deviceStates.fan }"></div>
              </div>
            </button>
          </div>

          <button @click="activeTab = 'monitor'"
            class="mt-8 w-full py-4 text-gray-500 font-bold hover:text-gray-900 transition-colors">
            Close Controls
          </button>
        </div>

      </div>
    </div>
  </div>
</template>

<style scoped>
.animate-bounce-slow {
  animation: bounce 3s infinite ease-in-out;
}

.animate-bounce-delayed {
  animation: bounce 3s infinite ease-in-out;
  animation-delay: 1.5s;
}

.animate-bounce-reverse {
  animation: bounce-reverse 4s infinite ease-in-out;
  animation-delay: 0.5s;
}

@keyframes bounce {

  0%,
  100% {
    transform: translateY(-5%);
  }

  50% {
    transform: translateY(5%);
  }
}

@keyframes bounce-reverse {

  0%,
  100% {
    transform: translateY(5%);
  }

  50% {
    transform: translateY(-5%);
  }
}

.animate-slide-up {
  animation: slideUp 0.3s ease-out;
}

@keyframes slideUp {
  from {
    transform: translateY(100%);
  }

  to {
    transform: translateY(0);
  }
}
</style>
