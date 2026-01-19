<template>
  <div class="bg-[#0f2e1b] rounded-3xl p-6 text-white relative overflow-hidden shadow-lg h-full">
    <div class="flex justify-between items-center mb-6">
      <h3 class="text-lg font-medium">Growth analytics</h3>
      <a href="#" class="text-sm text-gray-400 hover:text-white transition-colors">Details</a>
    </div>

    <!-- Chart Container -->
    <div class="relative h-32 w-full mt-4">
      <!-- SVG Line Chart -->
      <svg class="w-full h-full overflow-visible" viewBox="0 0 300 100" preserveAspectRatio="none">
        <!-- Grid Lines -->
        <line x1="0" y1="25" x2="300" y2="25" stroke="rgba(255,255,255,0.05)" stroke-width="1" />
        <line x1="0" y1="50" x2="300" y2="50" stroke="rgba(255,255,255,0.05)" stroke-width="1" />
        <line x1="0" y1="75" x2="300" y2="75" stroke="rgba(255,255,255,0.05)" stroke-width="1" />

        <!-- Line Path -->
        <path 
            d="M0,80 C50,75 80,60 120,50 C160,40 200,60 250,30 L300,20" 
            fill="none" 
            stroke="#4ade80" 
            stroke-width="2"
            stroke-linecap="round"
        />
        
        <!-- Area fill (optional gradient) -->
        <defs>
          <linearGradient id="growthGradient" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="#4ade80" stop-opacity="0.2"/>
            <stop offset="100%" stop-color="#4ade80" stop-opacity="0"/>
          </linearGradient>
        </defs>
        <path 
            d="M0,80 C50,75 80,60 120,50 C160,40 200,60 250,30 L300,20 V100 H0 Z" 
            fill="url(#growthGradient)" 
        />
        
        <!-- Data Point -->
        <circle cx="120" cy="50" r="4" fill="#ffffff" stroke="#4ade80" stroke-width="2" />
      </svg>

      <!-- Tooltip -->
      <div class="absolute top-1/3 left-[35%] transform -translate-x-1/2 -translate-y-full bg-white text-gray-900 text-xs font-bold px-3 py-1 rounded-full shadow-lg mb-2">
        12 cm/day
        <div class="absolute bottom-0 left-1/2 transform -translate-x-1/2 translate-y-1/2 w-2 h-2 bg-white rotate-45"></div>
      </div>
    </div>

    <!-- X Axis -->
    <div class="flex justify-between text-xs text-gray-500 mt-4">
        <span>30 day</span>
        <span>30 day</span>
        <span>30 day</span>
    </div>
  </div>
</template>
