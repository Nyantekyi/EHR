<template>
  <div class="space-y-6">
    <!-- Page Header -->
    <div class="flex justify-between items-center">
      <div>
        <h2 class="text-3xl font-bold text-gray-900">Patients</h2>
        <p class="text-gray-600 mt-1">Manage patient demographics and medical records</p>
      </div>
      <UButton color="primary" size="lg">
        <UIcon name="i-heroicons-plus" class="w-5 h-5 mr-2" />
        Add Patient
      </UButton>
    </div>

    <!-- Search and Filters -->
    <UCard>
      <div class="flex gap-4">
        <UInput
          icon="i-heroicons-magnifying-glass"
          placeholder="Search patients by name, phone, or email..."
          class="flex-1"
        />
        <UButton color="gray" variant="outline">
          <UIcon name="i-heroicons-funnel" class="w-4 h-4 mr-2" />
          Filters
        </UButton>
      </div>
    </UCard>
    
    <!-- Patients List -->
    <div v-if="loading" class="space-y-4">
      <USkeleton class="h-32 w-full" v-for="i in 3" :key="i" />
    </div>
    
    <UAlert v-else-if="error" color="red" variant="soft" icon="i-heroicons-exclamation-triangle">
      <template #title>Error loading patients</template>
      <template #description>{{ error }}</template>
    </UAlert>
    
    <div v-else-if="patients.length === 0" class="text-center py-16">
      <div class="bg-gray-100 w-20 h-20 rounded-full flex items-center justify-center mx-auto mb-4">
        <UIcon name="i-heroicons-user-group" class="w-10 h-10 text-gray-400" />
      </div>
      <h3 class="text-lg font-semibold text-gray-900 mb-2">No patients found</h3>
      <p class="text-gray-600 mb-6">Get started by adding your first patient</p>
      <UButton color="primary">
        <UIcon name="i-heroicons-plus" class="w-4 h-4 mr-2" />
        Add Patient
      </UButton>
    </div>
    
    <div v-else class="grid grid-cols-1 gap-4">
      <UCard
        v-for="patient in patients"
        :key="patient.id"
        class="hover:shadow-lg transition-all cursor-pointer border-l-4"
        :class="{
          'border-l-blue-500': patient.gender === 'M',
          'border-l-pink-500': patient.gender === 'F',
          'border-l-gray-500': patient.gender === 'O'
        }"
        @click="$router.push(`/patients/${patient.id}`)"
      >
        <div class="flex items-center justify-between">
          <div class="flex items-center gap-4 flex-1">
            <!-- Avatar -->
            <div class="flex-shrink-0">
              <div 
                class="w-16 h-16 rounded-full flex items-center justify-center text-white font-bold text-xl"
                :class="{
                  'bg-blue-500': patient.gender === 'M',
                  'bg-pink-500': patient.gender === 'F',
                  'bg-gray-500': patient.gender === 'O'
                }"
              >
                {{ patient.first_name[0] }}{{ patient.last_name[0] }}
              </div>
            </div>
            
            <!-- Patient Info -->
            <div class="flex-1 min-w-0">
              <div class="flex items-center gap-3 mb-2">
                <h3 class="text-lg font-bold text-gray-900 truncate">
                  {{ patient.first_name }} {{ patient.last_name }}
                </h3>
                <UBadge 
                  :color="patient.gender === 'M' ? 'blue' : patient.gender === 'F' ? 'pink' : 'gray'"
                  variant="subtle"
                >
                  {{ patient.gender === 'M' ? 'Male' : patient.gender === 'F' ? 'Female' : 'Other' }}
                </UBadge>
                <UBadge color="gray" variant="subtle">
                  {{ patient.age }} years
                </UBadge>
              </div>
              
              <div class="grid grid-cols-1 sm:grid-cols-3 gap-2 text-sm text-gray-600">
                <div class="flex items-center gap-2">
                  <UIcon name="i-heroicons-calendar" class="w-4 h-4 text-gray-400" />
                  <span>DOB: {{ patient.date_of_birth }}</span>
                </div>
                <div v-if="patient.phone_number" class="flex items-center gap-2">
                  <UIcon name="i-heroicons-phone" class="w-4 h-4 text-gray-400" />
                  <span>{{ patient.phone_number }}</span>
                </div>
                <div v-if="patient.blood_type" class="flex items-center gap-2">
                  <UIcon name="i-heroicons-beaker" class="w-4 h-4 text-gray-400" />
                  <span>Blood Type: {{ patient.blood_type }}</span>
                </div>
              </div>

              <div v-if="patient.allergies" class="mt-2 flex items-center gap-2">
                <UBadge color="red" variant="soft" size="xs">
                  <UIcon name="i-heroicons-exclamation-triangle" class="w-3 h-3 mr-1" />
                  Allergies: {{ patient.allergies }}
                </UBadge>
              </div>
            </div>
          </div>
          
          <!-- Action Button -->
          <div class="flex-shrink-0 ml-4">
            <UButton
              variant="ghost"
              color="gray"
              icon="i-heroicons-chevron-right"
              size="lg"
            />
          </div>
        </div>
      </UCard>
    </div>
  </div>
</template>

<script setup lang="ts">
import type { Patient, PaginatedResponse } from '~/types/ehr'

definePageMeta({
  title: 'Patients'
})

const config = useRuntimeConfig()

const { data, pending: loading, error } = await useFetch<PaginatedResponse<Patient>>(`${config.public.apiBase}/patients/`)

const patients = computed(() => data.value?.results || [])
</script>
