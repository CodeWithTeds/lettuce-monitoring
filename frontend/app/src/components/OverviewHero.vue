<template>
  <div class="relative pb-12 lg:pb-20">
    <div class="flex flex-col lg:flex-row items-start lg:items-center justify-between">
      <!-- Left Content -->
      <div class="space-y-8 z-10 relative max-w-2xl">
        <h1 class="text-5xl md:text-7xl font-bold text-white tracking-tight">Overview</h1>
        
        <div class="flex flex-wrap gap-8 md:gap-16">
          <!-- Water -->
          <div class="space-y-1">
            <div class="flex items-center space-x-2 text-yellow-300">
               <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM9.555 7.168A1 1 0 008 8v4a1 1 0 001.555.832l3-2a1 1 0 000-1.664l-3-2z" clip-rule="evenodd"></path></svg> <!-- Droplet icon proxy -->
               <span class="text-sm font-medium text-white/90">Water</span>
            </div>
            <div class="text-4xl md:text-5xl font-bold text-white">85%</div>
          </div>

          <!-- pH Level -->
          <div class="space-y-1">
            <div class="flex items-center space-x-2 text-green-300">
               <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19.428 15.428a2 2 0 00-1.022-.547l-2.384-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z"></path></svg>
               <span class="text-sm font-medium text-white/90">pH Level</span>
            </div>
            <div class="text-4xl md:text-5xl font-bold text-white">6.5 pH</div>
          </div>

          <!-- Temperature -->
          <div class="space-y-1">
            <div class="flex items-center space-x-2 text-yellow-300">
               <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"></path></svg>
               <span class="text-sm font-medium text-white/90">Temperature (°C)</span>
            </div>
            <div class="text-4xl md:text-5xl font-bold text-white">24°C</div>
          </div>
        </div>
      </div>

      <!-- Plant Image with Floating Labels -->
      <div class="absolute right-0 top-10 md:-top-10 w-full md:w-1/2 lg:w-[45%] h-full pointer-events-none flex justify-center lg:justify-end">
        <div class="relative w-full max-w-[500px] aspect-square">
            <!-- Main Image -->
            <img 
                src="/images/lettuce.png" 
                alt="Monitoring Plant" 
                class="w-full h-full object-contain drop-shadow-2xl filter brightness-110"
            />
            
            <!-- Floating Labels -->
            <!-- Health -->
            <div class="absolute top-10 left-10 bg-white px-3 py-1 rounded-full shadow-lg flex items-center space-x-2 animate-bounce-slow">
                <span class="text-xs font-bold text-gray-800">Health</span>
                <div class="w-2 h-2 bg-green-500 rounded-full"></div>
            </div>

            <!-- pH Level -->
            <div class="absolute bottom-20 left-0 bg-white px-3 py-1 rounded-full shadow-lg flex items-center space-x-2">
                <span class="text-xs font-bold text-gray-800">pH Level</span>
                <div class="w-16 h-1 bg-gray-200 rounded-full overflow-hidden">
                    <div class="w-2/3 h-full bg-green-500"></div>
                </div>
            </div>

            <!-- Water -->
            <div class="absolute bottom-32 right-10 bg-white px-3 py-1 rounded-full shadow-lg flex items-center space-x-2">
                <span class="text-xs font-bold text-gray-800">Water</span>
                <div class="w-2 h-2 bg-blue-400 rounded-full"></div>
            </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.animate-bounce-slow {
  animation: bounce 3s infinite;
}
@keyframes bounce {
  0%, 100% { transform: translateY(-5%); }
  50% { transform: translateY(5%); }
}
</style>
