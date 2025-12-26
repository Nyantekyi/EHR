<template>
  <div>
    <UContainer>
      <header class="py-6 border-b border-gray-200">
        <div class="flex justify-between items-center">
          <h1 class="text-2xl font-bold text-primary">Medical ERP System</h1>
          <nav class="flex gap-4">
            <UButton to="/" variant="ghost">Home</UButton>
            <UButton to="/patients" variant="ghost">Patients</UButton>
            <UButton to="/encounters" variant="ghost">Encounters</UButton>
          </nav>
        </div>
      </header>
      <main class="py-8">
        <NuxtPage />
      </main>
    </UContainer>
  </div>
</template>
