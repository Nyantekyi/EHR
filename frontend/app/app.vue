<template>
  <div class="min-h-screen bg-gray-50">
    <!-- Header -->
    <header class="bg-white shadow-sm sticky top-0 z-50">
      <UContainer>
        <div class="flex justify-between items-center py-4">
          <NuxtLink to="/" class="flex items-center gap-3 group">
            <div class="bg-gradient-to-br from-blue-500 to-blue-600 p-2 rounded-lg shadow-md group-hover:shadow-lg transition-shadow">
              <UIcon name="i-heroicons-heart" class="w-8 h-8 text-white" />
            </div>
            <div>
              <h1 class="text-xl font-bold text-gray-900">Medical ERP</h1>
              <p class="text-xs text-gray-500">Electronic Health Records</p>
            </div>
          </NuxtLink>
          
          <nav class="flex gap-2">
            <UButton 
              to="/" 
              variant="ghost" 
              color="gray"
              :class="$route.path === '/' ? 'bg-gray-100' : ''"
            >
              <UIcon name="i-heroicons-home" class="w-4 h-4 mr-2" />
              Home
            </UButton>
            <UButton 
              to="/patients" 
              variant="ghost"
              color="gray"
              :class="$route.path.startsWith('/patients') ? 'bg-gray-100' : ''"
            >
              <UIcon name="i-heroicons-user-group" class="w-4 h-4 mr-2" />
              Patients
            </UButton>
            <UButton 
              to="/encounters" 
              variant="ghost"
              color="gray"
              :class="$route.path.startsWith('/encounters') ? 'bg-gray-100' : ''"
            >
              <UIcon name="i-heroicons-clipboard-document-list" class="w-4 h-4 mr-2" />
              Encounters
            </UButton>
          </nav>
        </div>
      </UContainer>
    </header>
    
    <!-- Main Content -->
    <main class="py-8">
      <UContainer>
        <NuxtPage />
      </UContainer>
    </main>
    
    <!-- Footer -->
    <footer class="bg-white border-t border-gray-200 mt-16">
      <UContainer>
        <div class="py-6 text-center text-sm text-gray-600">
          <p>Medical ERP System with SOAPO Methodology</p>
          <p class="mt-1 text-xs text-gray-500">Secure • Compliant • Comprehensive</p>
        </div>
      </UContainer>
    </footer>
  </div>
</template>
