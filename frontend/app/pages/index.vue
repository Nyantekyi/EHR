<template>
  <div>
    <UCard>
      <template #header>
        <h2 class="text-3xl font-bold">Welcome to the Medical ERP System</h2>
      </template>
      
      <div class="space-y-6">
        <p class="text-lg text-gray-600">
          A comprehensive Electronic Health Record (EHR) system with support for longitudinal patient care using the SOAPO methodology.
        </p>
        
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
          <UCard>
            <template #header>
              <h3 class="text-xl font-semibold">Patients</h3>
            </template>
            <p class="mb-4">Manage patient demographics, medical history, and records.</p>
            <UButton to="/patients" block>View Patients</UButton>
          </UCard>
          
          <UCard>
            <template #header>
              <h3 class="text-xl font-semibold">Encounters</h3>
            </template>
            <p class="mb-4">Track patient visits across different locations using SOAPO.</p>
            <UButton to="/encounters" block>View Encounters</UButton>
          </UCard>
          
          <UCard>
            <template #header>
              <h3 class="text-xl font-semibold">System Features</h3>
            </template>
            <ul class="list-disc list-inside space-y-2 mb-4">
              <li>SOAPO Documentation</li>
              <li>Diagnoses & ICD Codes</li>
              <li>Medication Management</li>
              <li>Lab Results Tracking</li>
            </ul>
          </UCard>
        </div>
        
        <UAlert
          icon="i-heroicons-information-circle"
          color="primary"
          variant="soft"
          title="About SOAPO"
          description="SOAPO stands for Subjective, Objective, Assessment, Plan, and Outcome - a comprehensive method for documenting patient encounters."
        />
      </div>
    </UCard>
  </div>
</template>

<script setup lang="ts">
definePageMeta({
  title: 'Home'
})
</script>
