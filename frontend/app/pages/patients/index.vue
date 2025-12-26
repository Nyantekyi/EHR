<template>
  <div>
    <div class="flex justify-between items-center mb-6">
      <h2 class="text-2xl font-bold">Patients</h2>
    </div>
    
    <UCard>
      <div v-if="loading" class="flex justify-center py-8">
        <div class="text-gray-500">Loading patients...</div>
      </div>
      
      <div v-else-if="error" class="text-red-600 py-4">
        Error loading patients: {{ error }}
      </div>
      
      <div v-else>
        <div v-if="patients.length === 0" class="text-center py-8 text-gray-500">
          No patients found
        </div>
        <div v-else class="space-y-4">
          <div
            v-for="patient in patients"
            :key="patient.id"
            class="border-b last:border-b-0 pb-4 cursor-pointer hover:bg-gray-50 p-4"
            @click="$router.push(`/patients/${patient.id}`)"
          >
            <div class="flex justify-between items-start">
              <div class="flex-1">
                <div class="flex items-center gap-2 mb-2">
                  <span class="font-semibold text-lg">{{ patient.first_name }} {{ patient.last_name }}</span>
                  <UBadge :color="patient.gender === 'M' ? 'blue' : patient.gender === 'F' ? 'pink' : 'gray'">
                    {{ patient.gender === 'M' ? 'Male' : patient.gender === 'F' ? 'Female' : 'Other' }}
                  </UBadge>
                </div>
                <p class="text-sm text-gray-600">DOB: {{ patient.date_of_birth }} ({{ patient.age }} years old)</p>
                <p v-if="patient.phone_number" class="text-sm text-gray-600">Phone: {{ patient.phone_number }}</p>
                <p v-if="patient.blood_type" class="text-sm text-gray-600">Blood Type: {{ patient.blood_type }}</p>
              </div>
              <UButton
                variant="ghost"
                icon="i-heroicons-chevron-right"
              />
            </div>
          </div>
        </div>
      </div>
    </UCard>
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
