<script setup>
import DashboardLayout from './components/DashboardLayout.vue';
import Header from './components/Header.vue';
import OverviewHero from './components/OverviewHero.vue';
import GrowthAnalytics from './components/GrowthAnalytics.vue';
import CriticalAlerts from './components/CriticalAlerts.vue';
import ActivityOverview from './components/ActivityOverview.vue';
import ActiveContainers from './components/ActiveContainers.vue';
</script>

<template>
  <DashboardLayout>
    <template #header>
      <div class="bg-[#15803d] pb-24"> <!-- Green background container -->
        <Header />
        <div class="max-w-7xl mx-auto px-6 mt-6">
            <OverviewHero />
        </div>
      </div>
    </template>

    <!-- Widgets Grid -->
    <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
        
        <!-- Left Column (2/3 width) -->
        <div class="lg:col-span-2 space-y-8">
            <!-- Top Row: Growth & Alerts -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                <GrowthAnalytics />
                <CriticalAlerts />
            </div>

            <!-- Bottom Row: Containers -->
            <ActiveContainers />
        </div>

        <!-- Right Column (1/3 width) -->
        <div class="lg:col-span-1">
            <ActivityOverview />
        </div>
    </div>
  </DashboardLayout>
</template>
