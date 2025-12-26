<template>
  <div class="space-y-6">
    <!-- Back Button -->
    <UButton
      variant="ghost"
      color="gray"
      icon="i-heroicons-arrow-left"
      @click="$router.back()"
    >
      Back to Patients
    </UButton>
    
    <!-- Loading State -->
    <div v-if="loading" class="space-y-6">
      <USkeleton class="h-64 w-full" />
      <USkeleton class="h-96 w-full" />
    </div>
    
    <!-- Error State -->
    <UAlert v-else-if="error" color="red" variant="soft" icon="i-heroicons-exclamation-triangle">
      <template #title>Error loading patient</template>
      <template #description>{{ error }}</template>
    </UAlert>
    
    <!-- Patient Details -->
    <div v-else-if="patient" class="space-y-6">
      <!-- Patient Header Card -->
      <UCard class="bg-gradient-to-br from-blue-50 to-indigo-50 border-blue-200">
        <div class="flex items-start gap-6">
          <!-- Avatar -->
          <div 
            class="w-24 h-24 rounded-full flex items-center justify-center text-white font-bold text-3xl flex-shrink-0 shadow-lg"
            :class="{
              'bg-gradient-to-br from-blue-500 to-blue-600': patient.gender === 'M',
              'bg-gradient-to-br from-pink-500 to-pink-600': patient.gender === 'F',
              'bg-gradient-to-br from-gray-500 to-gray-600': patient.gender === 'O'
            }"
          >
            {{ patient.first_name[0] }}{{ patient.last_name[0] }}
          </div>
          
          <!-- Patient Info -->
          <div class="flex-1">
            <div class="flex items-center gap-3 mb-2">
              <h2 class="text-3xl font-bold text-gray-900">
                {{ patient.first_name }} {{ patient.last_name }}
              </h2>
              <UBadge 
                :color="patient.gender === 'M' ? 'blue' : patient.gender === 'F' ? 'pink' : 'gray'"
                size="lg"
              >
                {{ patient.gender === 'M' ? 'Male' : patient.gender === 'F' ? 'Female' : 'Other' }}
              </UBadge>
            </div>
            <p class="text-gray-600 text-lg mb-4">{{ patient.age }} years old</p>
            
            <div class="flex flex-wrap gap-4">
              <UButton color="primary" size="sm">
                <UIcon name="i-heroicons-pencil-square" class="w-4 h-4 mr-2" />
                Edit Patient
              </UButton>
              <UButton color="green" variant="soft" size="sm">
                <UIcon name="i-heroicons-plus" class="w-4 h-4 mr-2" />
                New Encounter
              </UButton>
            </div>
          </div>
        </div>

        <!-- Allergy Warning -->
        <div v-if="patient.allergies" class="mt-4 p-3 bg-red-50 border border-red-200 rounded-lg">
          <div class="flex items-center gap-2">
            <UIcon name="i-heroicons-exclamation-triangle" class="w-5 h-5 text-red-600" />
            <span class="font-semibold text-red-900">Allergies:</span>
            <span class="text-red-800">{{ patient.allergies }}</span>
          </div>
        </div>
      </UCard>
      
      <!-- Patient Information Grid -->
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <!-- Demographics Card -->
        <UCard>
          <template #header>
            <div class="flex items-center gap-2">
              <UIcon name="i-heroicons-user-circle" class="w-5 h-5 text-blue-600" />
              <h3 class="text-xl font-bold">Demographics</h3>
            </div>
          </template>
          
          <dl class="space-y-4">
            <div class="flex items-start gap-3">
              <UIcon name="i-heroicons-calendar" class="w-5 h-5 text-gray-400 mt-0.5" />
              <div class="flex-1">
                <dt class="text-sm text-gray-600">Date of Birth</dt>
                <dd class="font-medium text-gray-900">{{ patient.date_of_birth }}</dd>
              </div>
            </div>
            <div v-if="patient.phone_number" class="flex items-start gap-3">
              <UIcon name="i-heroicons-phone" class="w-5 h-5 text-gray-400 mt-0.5" />
              <div class="flex-1">
                <dt class="text-sm text-gray-600">Phone</dt>
                <dd class="font-medium text-gray-900">{{ patient.phone_number }}</dd>
              </div>
            </div>
            <div v-if="patient.email" class="flex items-start gap-3">
              <UIcon name="i-heroicons-envelope" class="w-5 h-5 text-gray-400 mt-0.5" />
              <div class="flex-1">
                <dt class="text-sm text-gray-600">Email</dt>
                <dd class="font-medium text-gray-900">{{ patient.email }}</dd>
              </div>
            </div>
            <div v-if="patient.address" class="flex items-start gap-3">
              <UIcon name="i-heroicons-map-pin" class="w-5 h-5 text-gray-400 mt-0.5" />
              <div class="flex-1">
                <dt class="text-sm text-gray-600">Address</dt>
                <dd class="font-medium text-gray-900">{{ patient.address }}</dd>
              </div>
            </div>
          </dl>
        </UCard>
        
        <!-- Medical Information Card -->
        <UCard>
          <template #header>
            <div class="flex items-center gap-2">
              <UIcon name="i-heroicons-heart" class="w-5 h-5 text-red-600" />
              <h3 class="text-xl font-bold">Medical Information</h3>
            </div>
          </template>
          
          <dl class="space-y-4">
            <div v-if="patient.blood_type" class="flex items-start gap-3">
              <UIcon name="i-heroicons-beaker" class="w-5 h-5 text-gray-400 mt-0.5" />
              <div class="flex-1">
                <dt class="text-sm text-gray-600">Blood Type</dt>
                <dd class="font-medium text-gray-900">{{ patient.blood_type }}</dd>
              </div>
            </div>
            <div v-if="patient.medical_history" class="flex items-start gap-3">
              <UIcon name="i-heroicons-document-text" class="w-5 h-5 text-gray-400 mt-0.5" />
              <div class="flex-1">
                <dt class="text-sm text-gray-600">Medical History</dt>
                <dd class="font-medium text-gray-900 whitespace-pre-wrap">{{ patient.medical_history }}</dd>
              </div>
            </div>
          </dl>
        </UCard>
      </div>
      
      <!-- Encounters Card -->
      <UCard>
        <template #header>
          <div class="flex justify-between items-center">
            <div class="flex items-center gap-2">
              <UIcon name="i-heroicons-clipboard-document-list" class="w-5 h-5 text-purple-600" />
              <h3 class="text-xl font-bold">Recent Encounters</h3>
            </div>
            <UButton color="primary" variant="soft" size="sm">
              <UIcon name="i-heroicons-plus" class="w-4 h-4 mr-2" />
              New Encounter
            </UButton>
          </div>
        </template>
        
        <div v-if="patient.recent_encounters && patient.recent_encounters.length > 0" class="space-y-4">
          <div
            v-for="encounter in patient.recent_encounters"
            :key="encounter.id"
            class="border border-gray-200 rounded-lg p-4 hover:shadow-md transition-all cursor-pointer hover:border-blue-300"
            @click="$router.push(`/encounters/${encounter.id}`)"
          >
            <div class="flex justify-between items-start">
              <div class="flex-1">
                <div class="flex items-center gap-2 mb-2">
                  <UBadge :color="getEncounterTypeColor(encounter.encounter_type)">
                    {{ encounter.encounter_type }}
                  </UBadge>
                  <UBadge :color="getStatusColor(encounter.status)">
                    {{ encounter.status.replace('_', ' ') }}
                  </UBadge>
                </div>
                <div class="text-sm text-gray-600 space-y-1">
                  <div class="flex items-center gap-2">
                    <UIcon name="i-heroicons-calendar" class="w-4 h-4 text-gray-400" />
                    <span>{{ formatDate(encounter.encounter_date) }}</span>
                  </div>
                  <div v-if="encounter.location" class="flex items-center gap-2">
                    <UIcon name="i-heroicons-map-pin" class="w-4 h-4 text-gray-400" />
                    <span>{{ encounter.location }}</span>
                  </div>
                  <div v-if="encounter.provider_name" class="flex items-center gap-2">
                    <UIcon name="i-heroicons-user" class="w-4 h-4 text-gray-400" />
                    <span>{{ encounter.provider_name }}</span>
                  </div>
                </div>
              </div>
              <UButton
                variant="ghost"
                color="gray"
                icon="i-heroicons-arrow-right"
                size="sm"
              />
            </div>
          </div>
        </div>
        <div v-else class="text-center py-12">
          <div class="bg-gray-100 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4">
            <UIcon name="i-heroicons-clipboard-document-list" class="w-8 h-8 text-gray-400" />
          </div>
          <p class="text-gray-600 mb-4">No encounters recorded yet</p>
          <UButton color="primary" size="sm">
            <UIcon name="i-heroicons-plus" class="w-4 h-4 mr-2" />
            Create First Encounter
          </UButton>
        </div>
      </UCard>
    </div>
  </div>
</template>

<script setup lang="ts">
import type { Patient } from '~/types/ehr'

const route = useRoute()
const config = useRuntimeConfig()

const patientId = parseInt(route.params.id as string)

const { data: patient, pending: loading, error } = await useFetch<Patient>(
  `${config.public.apiBase}/patients/${patientId}/`
)

// Helper functions
const getEncounterTypeColor = (type: string) => {
  const colors: Record<string, string> = {
    OUTPATIENT: 'blue',
    INPATIENT: 'purple',
    EMERGENCY: 'red',
    CLINIC: 'green',
    PHARMACY: 'orange'
  }
  return colors[type] || 'gray'
}

const getStatusColor = (status: string) => {
  const colors: Record<string, string> = {
    SCHEDULED: 'yellow',
    IN_PROGRESS: 'blue',
    COMPLETED: 'green',
    CANCELLED: 'red'
  }
  return colors[status] || 'gray'
}

const formatDate = (dateString: string) => {
  return new Date(dateString).toLocaleString('en-US', {
    month: 'short',
    day: 'numeric',
    year: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  })
}
</script>

        
        <div v-if="patient.recent_encounters && patient.recent_encounters.length > 0">
          <div
            v-for="encounter in patient.recent_encounters"
            :key="encounter.id"
            class="border-b last:border-b-0 py-4"
          >
            <div class="flex justify-between items-start">
              <div>
                <div class="flex items-center gap-2">
                  <UBadge :color="getEncounterTypeColor(encounter.encounter_type)">
                    {{ encounter.encounter_type }}
                  </UBadge>
                  <UBadge :color="getStatusColor(encounter.status)">
                    {{ encounter.status }}
                  </UBadge>
                </div>
                <p class="mt-2 text-sm text-gray-600">
                  {{ formatDate(encounter.encounter_date) }}
                </p>
                <p v-if="encounter.location" class="text-sm text-gray-600">
                  Location: {{ encounter.location }}
                </p>
                <p v-if="encounter.provider_name" class="text-sm text-gray-600">
                  Provider: {{ encounter.provider_name }}
                </p>
              </div>
              <UButton
                variant="ghost"
                icon="i-heroicons-eye"
                @click="$router.push(`/encounters/${encounter.id}`)"
              >
                View
              </UButton>
            </div>
          </div>
        </div>
        <div v-else class="text-center py-8 text-gray-500">
          No encounters recorded yet
        </div>
      </UCard>
    </div>
  </div>
</template>

<script setup lang="ts">
import type { Patient } from '~/types/ehr'

const route = useRoute()
const config = useRuntimeConfig()

const patientId = parseInt(route.params.id as string)

const { data: patient, pending: loading, error } = await useFetch<Patient>(
  `${config.public.apiBase}/patients/${patientId}/`
)

// Helper functions
const getEncounterTypeColor = (type: string) => {
  const colors: Record<string, string> = {
    OUTPATIENT: 'blue',
    INPATIENT: 'purple',
    EMERGENCY: 'red',
    CLINIC: 'green',
    PHARMACY: 'orange'
  }
  return colors[type] || 'gray'
}

const getStatusColor = (status: string) => {
  const colors: Record<string, string> = {
    SCHEDULED: 'yellow',
    IN_PROGRESS: 'blue',
    COMPLETED: 'green',
    CANCELLED: 'red'
  }
  return colors[status] || 'gray'
}

const formatDate = (dateString: string) => {
  return new Date(dateString).toLocaleString()
}
</script>
