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
      Error loading encounter: {{ error }}
    </div>
    
    <div v-else-if="encounter" class="space-y-6">
      <!-- Encounter Header -->
      <UCard>
        <template #header>
          <div class="flex justify-between items-start">
            <div>
              <h2 class="text-2xl font-bold mb-2">
                Encounter #{{ encounter.id }}
              </h2>
              <p class="text-gray-600">Patient: {{ encounter.patient_name }}</p>
            </div>
            <div class="flex gap-2">
              <UBadge :color="getEncounterTypeColor(encounter.encounter_type)" size="lg">
                {{ encounter.encounter_type }}
              </UBadge>
              <UBadge :color="getStatusColor(encounter.status)" size="lg">
                {{ encounter.status }}
              </UBadge>
            </div>
          </div>
        </template>
        
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div>
            <p class="text-sm text-gray-600">Date & Time</p>
            <p class="font-medium">{{ formatDate(encounter.encounter_date) }}</p>
          </div>
          <div v-if="encounter.location">
            <p class="text-sm text-gray-600">Location</p>
            <p class="font-medium">{{ encounter.location }}</p>
          </div>
          <div v-if="encounter.provider_name">
            <p class="text-sm text-gray-600">Provider</p>
            <p class="font-medium">{{ encounter.provider_name }}</p>
          </div>
        </div>
      </UCard>
      
      <!-- SOAPO Documentation -->
      <UCard>
        <template #header>
          <h3 class="text-xl font-bold">SOAPO Documentation</h3>
        </template>
        
        <div class="space-y-6">
          <!-- Subjective -->
          <div>
            <div class="flex items-center gap-2 mb-2">
              <UBadge color="blue">S</UBadge>
              <h4 class="font-semibold">Subjective</h4>
            </div>
            <p class="text-gray-700 whitespace-pre-wrap">
              {{ encounter.subjective || 'No data recorded' }}
            </p>
          </div>
          
          <!-- Objective -->
          <div>
            <div class="flex items-center gap-2 mb-2">
              <UBadge color="green">O</UBadge>
              <h4 class="font-semibold">Objective</h4>
            </div>
            <p class="text-gray-700 whitespace-pre-wrap">
              {{ encounter.objective || 'No data recorded' }}
            </p>
          </div>
          
          <!-- Assessment -->
          <div>
            <div class="flex items-center gap-2 mb-2">
              <UBadge color="yellow">A</UBadge>
              <h4 class="font-semibold">Assessment</h4>
            </div>
            <p class="text-gray-700 whitespace-pre-wrap">
              {{ encounter.assessment || 'No data recorded' }}
            </p>
          </div>
          
          <!-- Plan -->
          <div>
            <div class="flex items-center gap-2 mb-2">
              <UBadge color="purple">P</UBadge>
              <h4 class="font-semibold">Plan</h4>
            </div>
            <p class="text-gray-700 whitespace-pre-wrap">
              {{ encounter.plan || 'No data recorded' }}
            </p>
          </div>
          
          <!-- Outcome -->
          <div>
            <div class="flex items-center gap-2 mb-2">
              <UBadge color="orange">O</UBadge>
              <h4 class="font-semibold">Outcome</h4>
            </div>
            <p class="text-gray-700 whitespace-pre-wrap">
              {{ encounter.outcome || 'No data recorded' }}
            </p>
          </div>
        </div>
      </UCard>
      
      <!-- Diagnoses -->
      <UCard v-if="encounter.diagnoses && encounter.diagnoses.length > 0">
        <template #header>
          <h3 class="text-xl font-bold">Diagnoses</h3>
        </template>
        
        <div class="space-y-4">
          <div
            v-for="diagnosis in encounter.diagnoses"
            :key="diagnosis.id"
            class="border-b last:border-b-0 pb-4"
          >
            <div class="flex items-start justify-between">
              <div>
                <div class="flex items-center gap-2 mb-1">
                  <span class="font-semibold">{{ diagnosis.icd_code }}</span>
                  <UBadge :color="diagnosis.diagnosis_type === 'PRIMARY' ? 'blue' : 'gray'">
                    {{ diagnosis.diagnosis_type }}
                  </UBadge>
                  <UBadge v-if="diagnosis.severity" :color="getSeverityColor(diagnosis.severity)">
                    {{ diagnosis.severity }}
                  </UBadge>
                </div>
                <p class="text-gray-700">{{ diagnosis.description }}</p>
                <p v-if="diagnosis.notes" class="text-sm text-gray-600 mt-1">
                  {{ diagnosis.notes }}
                </p>
              </div>
            </div>
          </div>
        </div>
      </UCard>
      
      <!-- Medications -->
      <UCard v-if="encounter.medications && encounter.medications.length > 0">
        <template #header>
          <h3 class="text-xl font-bold">Medications</h3>
        </template>
        
        <div class="space-y-4">
          <div
            v-for="medication in encounter.medications"
            :key="medication.id"
            class="border-b last:border-b-0 pb-4"
          >
            <div class="flex justify-between items-start">
              <div class="flex-1">
                <div class="flex items-center gap-2 mb-1">
                  <span class="font-semibold">{{ medication.medication_name }}</span>
                  <UBadge :color="medication.status === 'ACTIVE' ? 'green' : 'gray'">
                    {{ medication.status }}
                  </UBadge>
                </div>
                <p class="text-gray-700">{{ medication.dosage }} - {{ medication.frequency }}</p>
                <p class="text-sm text-gray-600">
                  Route: {{ medication.route }} | Duration: {{ medication.duration_days }} days
                </p>
                <p v-if="medication.instructions" class="text-sm text-gray-600 mt-1">
                  Instructions: {{ medication.instructions }}
                </p>
              </div>
            </div>
          </div>
        </div>
      </UCard>
      
      <!-- Lab Results -->
      <UCard v-if="encounter.lab_results && encounter.lab_results.length > 0">
        <template #header>
          <h3 class="text-xl font-bold">Lab Results</h3>
        </template>
        
        <div class="space-y-4">
          <div
            v-for="labResult in encounter.lab_results"
            :key="labResult.id"
            class="border-b last:border-b-0 pb-4"
          >
            <div class="flex justify-between items-start">
              <div class="flex-1">
                <div class="flex items-center gap-2 mb-1">
                  <span class="font-semibold">{{ labResult.test_name }}</span>
                  <UBadge :color="getLabStatusColor(labResult.status)">
                    {{ labResult.status }}
                  </UBadge>
                  <UBadge color="gray">{{ labResult.test_category }}</UBadge>
                </div>
                <p class="text-gray-700">
                  Result: {{ labResult.result_value }} {{ labResult.unit }}
                </p>
                <p v-if="labResult.reference_range" class="text-sm text-gray-600">
                  Reference Range: {{ labResult.reference_range }}
                </p>
                <p v-if="labResult.interpretation" class="text-sm text-gray-600 mt-1">
                  {{ labResult.interpretation }}
                </p>
              </div>
            </div>
          </div>
        </div>
      </UCard>
    </div>
  </div>
</template>

<script setup lang="ts">
import type { Encounter } from '~/types/ehr'

const route = useRoute()
const api = useApi()

const encounterId = parseInt(route.params.id as string)

// Fetch encounter details
const { data: encounter, pending, error } = await useAsyncData<Encounter>(
  `encounter-${encounterId}`,
  () => api.encounters.get(encounterId)
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

const getSeverityColor = (severity: string) => {
  const colors: Record<string, string> = {
    MILD: 'green',
    MODERATE: 'yellow',
    SEVERE: 'red'
  }
  return colors[severity] || 'gray'
}

const getLabStatusColor = (status: string) => {
  const colors: Record<string, string> = {
    NORMAL: 'green',
    ABNORMAL: 'yellow',
    CRITICAL: 'red',
    PENDING: 'gray'
  }
  return colors[status] || 'gray'
}

const formatDate = (dateString: string) => {
  return new Date(dateString).toLocaleString()
}
</script>
