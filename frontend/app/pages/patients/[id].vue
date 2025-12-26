<template>
  <div>
    <div class="mb-6">
      <UButton
        variant="ghost"
        icon="i-heroicons-arrow-left"
        @click="$router.back()"
      >
        Back
      </UButton>
    </div>
    
    <div v-if="pending" class="flex justify-center py-8">
      <UIcon name="i-heroicons-arrow-path" class="animate-spin text-2xl" />
    </div>
    
    <div v-else-if="error" class="text-red-600 py-4">
      Error loading patient: {{ error }}
    </div>
    
    <div v-else-if="patient" class="space-y-6">
      <UCard>
        <template #header>
          <div class="flex justify-between items-center">
            <h2 class="text-2xl font-bold">{{ patient.first_name }} {{ patient.last_name }}</h2>
            <UBadge :color="patient.gender === 'M' ? 'blue' : patient.gender === 'F' ? 'pink' : 'gray'">
              {{ patient.gender === 'M' ? 'Male' : patient.gender === 'F' ? 'Female' : 'Other' }}
            </UBadge>
          </div>
        </template>
        
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div>
            <h3 class="text-lg font-semibold mb-4">Demographics</h3>
            <dl class="space-y-2">
              <div>
                <dt class="text-sm text-gray-600">Date of Birth</dt>
                <dd class="font-medium">{{ patient.date_of_birth }} ({{ patient.age }} years old)</dd>
              </div>
              <div v-if="patient.phone_number">
                <dt class="text-sm text-gray-600">Phone</dt>
                <dd class="font-medium">{{ patient.phone_number }}</dd>
              </div>
              <div v-if="patient.email">
                <dt class="text-sm text-gray-600">Email</dt>
                <dd class="font-medium">{{ patient.email }}</dd>
              </div>
              <div v-if="patient.address">
                <dt class="text-sm text-gray-600">Address</dt>
                <dd class="font-medium">{{ patient.address }}</dd>
              </div>
            </dl>
          </div>
          
          <div>
            <h3 class="text-lg font-semibold mb-4">Medical Information</h3>
            <dl class="space-y-2">
              <div v-if="patient.blood_type">
                <dt class="text-sm text-gray-600">Blood Type</dt>
                <dd class="font-medium">{{ patient.blood_type }}</dd>
              </div>
              <div v-if="patient.allergies">
                <dt class="text-sm text-gray-600">Allergies</dt>
                <dd class="font-medium">{{ patient.allergies }}</dd>
              </div>
              <div v-if="patient.medical_history">
                <dt class="text-sm text-gray-600">Medical History</dt>
                <dd class="font-medium">{{ patient.medical_history }}</dd>
              </div>
            </dl>
          </div>
        </div>
      </UCard>
      
      <UCard>
        <template #header>
          <div class="flex justify-between items-center">
            <h3 class="text-xl font-bold">Encounters</h3>
            <UButton @click="createEncounter" icon="i-heroicons-plus">New Encounter</UButton>
          </div>
        </template>
        
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
const router = useRouter()
const api = useApi()

const patientId = parseInt(route.params.id as string)

// Fetch patient details
const { data: patient, pending, error } = await useAsyncData<Patient>(
  `patient-${patientId}`,
  () => api.patients.get(patientId)
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

const createEncounter = () => {
  router.push(`/encounters/new?patient=${patientId}`)
}
</script>
