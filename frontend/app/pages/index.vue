<template>
  <div class="space-y-8">
    <!-- Hero Section -->
    <div class="bg-gradient-to-r from-blue-500 to-blue-600 rounded-2xl shadow-xl p-8 text-white">
      <div class="max-w-3xl">
        <h2 class="text-4xl font-bold mb-4">Welcome to Medical ERP System</h2>
        <p class="text-lg text-blue-50 mb-6">
          A comprehensive Electronic Health Record (EHR) system with support for longitudinal patient care using the SOAPO methodology.
        </p>
        <div class="flex gap-4">
          <UButton to="/patients" size="lg" color="white" variant="solid">
            <UIcon name="i-heroicons-user-group" class="w-5 h-5 mr-2" />
            View Patients
          </UButton>
          <UButton to="/encounters" size="lg" color="white" variant="outline">
            <UIcon name="i-heroicons-clipboard-document-list" class="w-5 h-5 mr-2" />
            View Encounters
          </UButton>
        </div>
      </div>
    </div>

    <!-- Quick Stats -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
      <UCard class="hover:shadow-lg transition-shadow">
        <div class="flex items-start justify-between">
          <div>
            <p class="text-sm font-medium text-gray-600 mb-1">Total Patients</p>
            <p class="text-3xl font-bold text-gray-900">--</p>
            <p class="text-xs text-gray-500 mt-1">Across all locations</p>
          </div>
          <div class="bg-blue-100 p-3 rounded-lg">
            <UIcon name="i-heroicons-user-group" class="w-6 h-6 text-blue-600" />
          </div>
        </div>
      </UCard>

      <UCard class="hover:shadow-lg transition-shadow">
        <div class="flex items-start justify-between">
          <div>
            <p class="text-sm font-medium text-gray-600 mb-1">Active Encounters</p>
            <p class="text-3xl font-bold text-gray-900">--</p>
            <p class="text-xs text-gray-500 mt-1">In progress today</p>
          </div>
          <div class="bg-green-100 p-3 rounded-lg">
            <UIcon name="i-heroicons-clipboard-document-check" class="w-6 h-6 text-green-600" />
          </div>
        </div>
      </UCard>

      <UCard class="hover:shadow-lg transition-shadow">
        <div class="flex items-start justify-between">
          <div>
            <p class="text-sm font-medium text-gray-600 mb-1">SOAPO Method</p>
            <p class="text-3xl font-bold text-gray-900">100%</p>
            <p class="text-xs text-gray-500 mt-1">Documentation complete</p>
          </div>
          <div class="bg-purple-100 p-3 rounded-lg">
            <UIcon name="i-heroicons-document-text" class="w-6 h-6 text-purple-600" />
          </div>
        </div>
      </UCard>
    </div>

    <!-- Feature Cards -->
    <div>
      <h3 class="text-2xl font-bold text-gray-900 mb-6">System Features</h3>
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        <UCard class="hover:shadow-lg transition-all hover:scale-105">
          <div class="text-center">
            <div class="bg-blue-100 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4">
              <UIcon name="i-heroicons-user-circle" class="w-8 h-8 text-blue-600" />
            </div>
            <h4 class="font-semibold text-gray-900 mb-2">Patient Management</h4>
            <p class="text-sm text-gray-600">Complete demographics, medical history, and allergy tracking</p>
          </div>
        </UCard>

        <UCard class="hover:shadow-lg transition-all hover:scale-105">
          <div class="text-center">
            <div class="bg-green-100 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4">
              <UIcon name="i-heroicons-document-chart-bar" class="w-8 h-8 text-green-600" />
            </div>
            <h4 class="font-semibold text-gray-900 mb-2">SOAPO Documentation</h4>
            <p class="text-sm text-gray-600">Structured clinical notes with full SOAPO methodology</p>
          </div>
        </UCard>

        <UCard class="hover:shadow-lg transition-all hover:scale-105">
          <div class="text-center">
            <div class="bg-orange-100 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4">
              <UIcon name="i-heroicons-beaker" class="w-8 h-8 text-orange-600" />
            </div>
            <h4 class="font-semibold text-gray-900 mb-2">Lab Results</h4>
            <p class="text-sm text-gray-600">Track test results with reference ranges and interpretations</p>
          </div>
        </UCard>

        <UCard class="hover:shadow-lg transition-all hover:scale-105">
          <div class="text-center">
            <div class="bg-purple-100 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4">
              <UIcon name="i-heroicons-beaker" class="w-8 h-8 text-purple-600" />
            </div>
            <h4 class="font-semibold text-gray-900 mb-2">Medications</h4>
            <p class="text-sm text-gray-600">Prescription management with dosage and refill tracking</p>
          </div>
        </UCard>
      </div>
    </div>

    <!-- SOAPO Info -->
    <UCard class="bg-gradient-to-br from-blue-50 to-indigo-50 border-blue-200">
      <div class="flex items-start gap-4">
        <div class="bg-blue-600 p-3 rounded-lg flex-shrink-0">
          <UIcon name="i-heroicons-information-circle" class="w-6 h-6 text-white" />
        </div>
        <div>
          <h4 class="font-semibold text-gray-900 mb-2">About SOAPO Methodology</h4>
          <p class="text-gray-700 mb-3">
            SOAPO stands for <strong>Subjective, Objective, Assessment, Plan, and Outcome</strong> - a comprehensive method for documenting patient encounters that ensures thorough and systematic clinical documentation.
          </p>
          <div class="grid grid-cols-1 sm:grid-cols-5 gap-3 mt-4">
            <div class="bg-white/70 rounded-lg p-3">
              <p class="font-semibold text-blue-600 text-sm">Subjective</p>
              <p class="text-xs text-gray-600 mt-1">Patient symptoms</p>
            </div>
            <div class="bg-white/70 rounded-lg p-3">
              <p class="font-semibold text-green-600 text-sm">Objective</p>
              <p class="text-xs text-gray-600 mt-1">Physical findings</p>
            </div>
            <div class="bg-white/70 rounded-lg p-3">
              <p class="font-semibold text-orange-600 text-sm">Assessment</p>
              <p class="text-xs text-gray-600 mt-1">Diagnosis</p>
            </div>
            <div class="bg-white/70 rounded-lg p-3">
              <p class="font-semibold text-purple-600 text-sm">Plan</p>
              <p class="text-xs text-gray-600 mt-1">Treatment</p>
            </div>
            <div class="bg-white/70 rounded-lg p-3">
              <p class="font-semibold text-pink-600 text-sm">Outcome</p>
              <p class="text-xs text-gray-600 mt-1">Results</p>
            </div>
          </div>
        </div>
      </div>
    </UCard>
  </div>
</template>

<script setup lang="ts">
definePageMeta({
  title: 'Home'
})
</script>
