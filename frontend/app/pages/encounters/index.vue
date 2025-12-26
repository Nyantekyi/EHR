<template>
  <div>
    <div class="flex justify-between items-center mb-6">
      <h2 class="text-2xl font-bold">Encounters</h2>
    </div>
    
    <UCard>
      <div v-if="loading" class="flex justify-center py-8">
        <div class="text-gray-500">Loading encounters...</div>
      </div>
      
      <div v-else-if="error" class="text-red-600 py-4">
        Error loading encounters: {{ error }}
      </div>
      
      <div v-else>
        <div
          v-for="encounter in encounters"
          :key="encounter.id"
          class="border-b last:border-b-0 py-4 cursor-pointer hover:bg-gray-50 p-4"
          @click="$router.push(`/encounters/${encounter.id}`)"
        >
          <div class="flex justify-between items-start">
            <div class="flex-1">
              <div class="flex items-center gap-2 mb-2">
                <span class="font-semibold">{{ encounter.patient_name }}</span>
                <UBadge :color="getEncounterTypeColor(encounter.encounter_type)">
                  {{ encounter.encounter_type }}
                </UBadge>
                <UBadge :color="getStatusColor(encounter.status)">
                  {{ encounter.status }}
                </UBadge>
              </div>
              <p class="text-sm text-gray-600">{{ formatDate(encounter.encounter_date) }}</p>
              <p v-if="encounter.location" class="text-sm text-gray-600">
                Location: {{ encounter.location }}
              </p>
              <p v-if="encounter.provider_name" class="text-sm text-gray-600">
                Provider: {{ encounter.provider_name }}
              </p>
            </div>
            <UButton
              variant="ghost"
              icon="i-heroicons-chevron-right"
            />
          </div>
        </div>
        
        <div v-if="encounters.length === 0" class="text-center py-8 text-gray-500">
          No encounters found
        </div>
      </div>
    </UCard>
  </div>
</template>

<script setup lang="ts">
import type { Encounter } from '~/types/ehr'

definePageMeta({
  title: 'Encounters'
})

const config = useRuntimeConfig()

const encounters = ref<Encounter[]>([])
const loading = ref(true)
const error = ref('')

onMounted(async () => {
  try {
    const response = await $fetch<any>(`${config.public.apiBase}/encounters/`)
    encounters.value = response.results || response
  } catch (err: any) {
    error.value = err.message || 'Failed to load encounters'
    console.error('Error loading encounters:', err)
  } finally {
    loading.value = false
  }
})

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
