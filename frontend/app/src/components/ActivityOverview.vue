<template>
    <div class="bg-white rounded-3xl p-6 shadow-lg h-full">
        <h3 class="text-xl font-bold text-gray-900 mb-6">Activity Overview</h3>

        <!-- Week Days Header -->
        <div class="flex justify-between text-sm text-gray-500 mb-4 font-medium">
            <span>Mon</span>
            <span>Tue</span>
            <span>Wed</span>
            <span>Thu</span>
            <span class="text-black font-bold">Sch</span>
            <span>Sun</span>
        </div>

        <!-- Wave Chart -->
        <div class="relative h-24 w-full mb-8">
            <svg class="w-full h-full overflow-visible" viewBox="0 0 300 100" preserveAspectRatio="none">
                <!-- Grid -->
                <line x1="0" y1="20" x2="300" y2="20" stroke="#f3f4f6" stroke-width="1" />
                <line x1="0" y1="50" x2="300" y2="50" stroke="#f3f4f6" stroke-width="1" />
                <line x1="0" y1="80" x2="300" y2="80" stroke="#f3f4f6" stroke-width="1" />

                <!-- Wave Path -->
                <path d="M0,80 C40,80 60,50 100,50 C140,50 160,20 200,40 C240,60 260,80 300,50" fill="none"
                    stroke="#0f2e1b" stroke-width="2" stroke-linecap="round" />

                <!-- Highlighted Point (Orange Bulb?) -->
                <!-- Using a simple marker for now -->
                <circle cx="100" cy="50" r="6" fill="#f97316" stroke="white" stroke-width="2" />
            </svg>

            <!-- Time Labels -->
            <div class="flex justify-between text-xs text-gray-400 mt-2">
                <span>10:00</span>
                <span>12:00</span>
                <span>12:00</span>
                <span>16:00</span>
                <span>18:00</span>
            </div>
        </div>

        <!-- Schedule List -->
        <div class="space-y-6">
            <!-- Item 1 -->
            <div class="flex items-start justify-between">
                <div>
                    <h4 class="font-bold text-gray-900 text-sm">Watering System Adjustment</h4>
                    <p class="text-xs text-gray-500 mt-1">10:00 - 11:00</p>
                </div>
                <button class="bg-[#0f2e1b] text-white text-xs font-bold px-3 py-1.5 rounded-full">Details</button>
            </div>

            <!-- Item 2 -->
            <div class="flex items-start justify-between">
                <div>
                    <h4 class="font-bold text-gray-900 text-sm">Fertilizer Check</h4>
                    <p class="text-xs text-gray-500 mt-1">12:00 - 12:30</p>
                </div>
                <span class="bg-gray-100 text-gray-600 text-xs font-bold px-3 py-1.5 rounded-full">Completed</span>
            </div>

            <!-- Item 3 -->
            <div class="flex items-start justify-between">
                <div>
                    <h4 class="font-bold text-gray-900 text-sm">Lighting Adjustment</h4>
                    <p class="text-xs text-gray-500 mt-1">16:00 - 18:00</p>
                </div>
                <span class="bg-gray-100 text-gray-600 text-xs font-bold px-3 py-1.5 rounded-full">In Progress</span>
            </div>
        </div>
    </div>
</template>
