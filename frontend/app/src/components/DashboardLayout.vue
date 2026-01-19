<template>
  <div class="min-h-screen bg-gray-100 font-sans text-gray-900 overflow-x-hidden">
    <!-- The layout is simple: Header is part of the flow, content follows -->
    <slot name="header"></slot>
    
    <main class="relative z-10 px-4 sm:px-6 lg:px-8 pb-12 -mt-20">
        <div class="max-w-7xl mx-auto space-y-6">
             <slot></slot>
        </div>
    </main>
  </div>
</template>

<script setup>
// No script needed for this simple layout
</script>
