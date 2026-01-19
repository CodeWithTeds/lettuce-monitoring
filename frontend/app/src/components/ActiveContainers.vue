<template>
  <div class="bg-white rounded-3xl p-6 shadow-lg overflow-x-auto">
    <div class="flex justify-between items-center mb-6">
       <h3 class="text-lg font-bold text-gray-900">Active Containers</h3>
       <a href="#" class="text-sm font-medium text-gray-500 hover:text-gray-900">Explore all</a>
    </div>

    <table class="w-full min-w-[800px]">
      <thead>
        <tr class="text-left text-xs font-bold text-gray-400 uppercase tracking-wider border-b border-gray-100">
          <th class="pb-4">Health</th>
          <th class="pb-4">Vitality</th> <!-- Renamed from Wealth -->
          <th class="pb-4">Water</th>
          <th class="pb-4">pH Level</th>
          <th class="pb-4">Nutrients</th>
          <th class="pb-4">Temperature</th>
          <th class="pb-4"></th>
        </tr>
      </thead>
      <tbody class="text-sm">
        <!-- Row 1 -->
        <tr class="group hover:bg-gray-50 transition-colors">
          <td class="py-4 font-bold text-gray-900 flex items-center space-x-3">
             <span>Ns1</span>
             <svg class="w-6 h-4 text-gray-800" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 12l3-3 3 3 4-4 7 7M5 12a1 1 0 110-2 1 1 0 010 2z"></path></svg>
          </td>
          <td class="py-4">
            <div class="flex items-center space-x-2 text-gray-700 font-bold">
               <svg class="w-4 h-4 text-red-400" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M3.172 5.172a4 4 0 015.656 0L10 6.343l1.172-1.171a4 4 0 115.656 5.656L10 17.657l-6.828-6.829a4 4 0 010-5.656z" clip-rule="evenodd"></path></svg>
               <span>80%</span>
            </div>
          </td>
          <td class="py-4">
             <div class="flex items-center space-x-2 text-gray-700 font-bold">
               <svg class="w-4 h-4 text-green-600" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM9.555 7.168A1 1 0 008 8v4a1 1 0 001.555.832l3-2a1 1 0 000-1.664l-3-2z" clip-rule="evenodd"></path></svg>
               <span>65%</span>
            </div>
          </td>
          <td class="py-4">
             <div class="flex items-center space-x-2 text-gray-700 font-bold">
               <svg class="w-4 h-4 text-gray-400" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M4 4a2 2 0 012-2h4.586A2 2 0 0112 2.586L15.414 6A2 2 0 0116 7.414V16a2 2 0 01-2 2h-6a2 2 0 01-2-2V4z" clip-rule="evenodd"></path></svg>
               <span>6.5</span>
            </div>
          </td>
          <td class="py-4">
             <div class="flex items-center space-x-2 text-gray-700 font-bold">
               <svg class="w-4 h-4 text-green-500" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M6 2a1 1 0 00-1 1v1H4a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2h-1V3a1 1 0 10-2 0v1H7V3a1 1 0 00-1-1zm0 5a1 1 0 000 2h8a1 1 0 100-2H6z" clip-rule="evenodd"></path></svg>
               <span>85%</span>
            </div>
          </td>
          <td class="py-4 font-bold text-gray-700">24°C</td>
          <td class="py-4 text-right">
             <button class="bg-[#0f2e1b] text-white text-xs font-bold px-4 py-2 rounded-full hover:bg-green-900 transition-colors">Details</button>
          </td>
        </tr>

        <!-- Row 2 -->
        <tr class="group hover:bg-gray-50 transition-colors border-t border-gray-50">
          <td class="py-4 font-bold text-gray-900 flex items-center space-x-3">
             <span>Ns2</span>
             <svg class="w-6 h-4 text-gray-800" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 12l3-3 3 3 4-4 7 7M5 12a1 1 0 110-2 1 1 0 010 2z"></path></svg>
          </td>
          <td class="py-4">
            <div class="flex items-center space-x-2 text-gray-700 font-bold">
               <svg class="w-4 h-4 text-red-400" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M3.172 5.172a4 4 0 015.656 0L10 6.343l1.172-1.171a4 4 0 115.656 5.656L10 17.657l-6.828-6.829a4 4 0 010-5.656z" clip-rule="evenodd"></path></svg>
               <span>80%</span>
            </div>
          </td>
          <td class="py-4">
             <div class="flex items-center space-x-2 text-gray-700 font-bold">
               <svg class="w-4 h-4 text-green-600" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM9.555 7.168A1 1 0 008 8v4a1 1 0 001.555.832l3-2a1 1 0 000-1.664l-3-2z" clip-rule="evenodd"></path></svg>
               <span>65%</span>
            </div>
          </td>
          <td class="py-4">
             <div class="flex items-center space-x-2 text-gray-700 font-bold">
               <svg class="w-4 h-4 text-gray-400" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M4 4a2 2 0 012-2h4.586A2 2 0 0112 2.586L15.414 6A2 2 0 0116 7.414V16a2 2 0 01-2 2h-6a2 2 0 01-2-2V4z" clip-rule="evenodd"></path></svg>
               <span>6.5</span>
            </div>
          </td>
          <td class="py-4">
             <div class="flex items-center space-x-2 text-gray-700 font-bold">
               <svg class="w-4 h-4 text-green-500" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M6 2a1 1 0 00-1 1v1H4a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2h-1V3a1 1 0 10-2 0v1H7V3a1 1 0 00-1-1zm0 5a1 1 0 000 2h8a1 1 0 100-2H6z" clip-rule="evenodd"></path></svg>
               <span>85%</span>
            </div>
          </td>
          <td class="py-4 font-bold text-gray-700">24°C</td>
          <td class="py-4 text-right">
             <button class="bg-[#0f2e1b] text-white text-xs font-bold px-4 py-2 rounded-full hover:bg-green-900 transition-colors">Details</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
