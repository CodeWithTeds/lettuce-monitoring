<template>
  <header class="flex items-center justify-between px-6 py-4 max-w-7xl mx-auto">
    <!-- Logo -->
    <div class="flex items-center space-x-2">
      <div class="w-8 h-8 bg-yellow-400 rounded-full flex items-center justify-center rounded-bl-none transform rotate-45">
        <!-- Simple Leaf/Plant Icon approximation -->
        <div class="w-3 h-3 bg-green-800 rounded-full"></div>
      </div>
      <span class="text-2xl font-bold text-white tracking-tight">greenish</span>
    </div>

    <!-- Navigation -->
    <nav class="hidden md:flex items-center space-x-8">
      <a v-for="item in navItems" :key="item" href="#" 
         class="text-sm font-medium text-white/80 hover:text-white transition-colors">
        {{ item }}
      </a>
    </nav>

    <!-- Right Actions -->
    <div class="flex items-center space-x-4">
      <!-- Search -->
      <div class="hidden md:flex items-center bg-white/10 backdrop-blur-sm rounded-full px-4 py-2 border border-white/10 focus-within:bg-white/20 transition-all">
        <svg class="w-4 h-4 text-white/70" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
        <input 
            type="text" 
            placeholder="Search" 
            class="bg-transparent border-none focus:ring-0 text-sm text-white placeholder-white/70 ml-2 w-24 lg:w-48"
        />
      </div>

      <!-- Profile -->
      <button class="w-10 h-10 rounded-full bg-white text-green-800 flex items-center justify-center font-bold hover:bg-gray-100 transition-colors">
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"></path></svg>
      </button>
    </div>
  </header>
</template>

<script setup>
const navItems = ['Dashboard', 'Analytics', 'Containers', 'Notifications'];
</script>
