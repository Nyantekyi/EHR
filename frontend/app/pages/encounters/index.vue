<template>
  <div class="space-y-6">
    <!-- Page Header -->
    <div class="flex justify-between items-center">
      <div>
        <h2 class="text-3xl font-bold text-gray-900">Encounters</h2>
        <p class="text-gray-600 mt-1">Track patient visits with SOAPO documentation</p>
      </div>
      <UButton color="primary" size="lg">
        <UIcon name="i-heroicons-plus" class="w-5 h-5 mr-2" />
        New Encounter
      </UButton>
    </div>

    <!-- Search and Filters -->
    <UCard>
      <div class="flex gap-4">
        <UInput
          icon="i-heroicons-magnifying-glass"
          placeholder="Search encounters by patient, location, or provider..."
          class="flex-1"
        />
        <UButton color="gray" variant="outline">
          <UIcon name="i-heroicons-funnel" class="w-4 h-4 mr-2" />
          Filters
        </UButton>
      </div>
    </UCard>
    
    <!-- Encounters List -->
    <div v-if="loading" class="space-y-4">
      <USkeleton class="h-40 w-full" v-for="i in 3" :key="i" />
    </div>
    
    <UAlert v-else-if="error" color="red" variant="soft" icon="i-heroicons-exclamation-triangle">
      <template #title>Error loading encounters</template>
      <template #description>{{ error }}</template>
    </UAlert>
    
    <div v-else-if="encounters.length === 0" class="text-center py-16">
      <div class="bg-gray-100 w-20 h-20 rounded-full flex items-center justify-center mx-auto mb-4">
        <UIcon name="i-heroicons-clipboard-document-list" class="w-10 h-10 text-gray-400" />
      </div>
      <h3 class="text-lg font-semibold text-gray-900 mb-2">No encounters found</h3>
      <p class="text-gray-600 mb-6">Start documenting patient visits</p>
      <UButton color="primary">
        <UIcon name="i-heroicons-plus" class="w-4 h-4 mr-2" />
        New Encounter
      </UButton>
    </div>
    
    <div v-else class="space-y-4">
      <UCard
        v-for="encounter in encounters"
        :key="encounter.id"
        class="hover:shadow-lg transition-all cursor-pointer"
        @click="$router.push(`/encounters/${encounter.id}`)"
      >
        <div class="flex items-start justify-between gap-4">
          <!-- Main Content -->
          <div class="flex-1 min-w-0">
            <!-- Header with badges -->
            <div class="flex flex-wrap items-center gap-2 mb-3">
              <h3 class="text-lg font-bold text-gray-900">
                {{ encounter.patient_name }}
              </h3>
              <UBadge :color="getEncounterTypeColor(encounter.encounter_type)" variant="subtle">
                <UIcon :name="getEncounterIcon(encounter.encounter_type)" class="w-3 h-3 mr-1" />
                {{ encounter.encounter_type }}
              </UBadge>
              <UBadge :color="getStatusColor(encounter.status)" variant="subtle">
                {{ encounter.status.replace('_', ' ') }}
              </UBadge>
            </div>
            
            <!-- Details Grid -->
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3 text-sm">
              <div class="flex items-center gap-2 text-gray-600">
                <UIcon name="i-heroicons-calendar-days" class="w-4 h-4 text-gray-400" />
                <span>{{ formatDate(encounter.encounter_date) }}</span>
              </div>
              <div v-if="encounter.location" class="flex items-center gap-2 text-gray-600">
                <UIcon name="i-heroicons-map-pin" class="w-4 h-4 text-gray-400" />
                <span>{{ encounter.location }}</span>
              </div>
              <div v-if="encounter.provider_name" class="flex items-center gap-2 text-gray-600">
                <UIcon name="i-heroicons-user" class="w-4 h-4 text-gray-400" />
                <span>{{ encounter.provider_name }}</span>
              </div>
            </div>

            <!-- SOAPO Indicators -->
            <div class="mt-3 flex items-center gap-2">
              <span class="text-xs text-gray-500">SOAPO:</span>
              <div class="flex gap-1">
                <UBadge size="xs" :color="encounter.subjective ? 'blue' : 'gray'" variant="soft">S</UBadge>
                <UBadge size="xs" :color="encounter.objective ? 'green' : 'gray'" variant="soft">O</UBadge>
                <UBadge size="xs" :color="encounter.assessment ? 'yellow' : 'gray'" variant="soft">A</UBadge>
                <UBadge size="xs" :color="encounter.plan ? 'purple' : 'gray'" variant="soft">P</UBadge>
                <UBadge size="xs" :color="encounter.outcome ? 'pink' : 'gray'" variant="soft">O</UBadge>
              </div>
            </div>
          </div>
          
          <!-- Action Button -->
          <div class="flex-shrink-0">
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
import type { Encounter, PaginatedResponse } from '~/types/ehr'

definePageMeta({
  title: 'Encounters'
})

const config = useRuntimeConfig()

const { data, pending: loading, error } = await useFetch<PaginatedResponse<Encounter>>(`${config.public.apiBase}/encounters/`)

const encounters = computed(() => data.value?.results || [])

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

const getEncounterIcon = (type: string) => {
  const icons: Record<string, string> = {
    OUTPATIENT: 'i-heroicons-user',
    INPATIENT: 'i-heroicons-home',
    EMERGENCY: 'i-heroicons-bolt',
    CLINIC: 'i-heroicons-building-office',
    PHARMACY: 'i-heroicons-beaker'
  }
  return icons[type] || 'i-heroicons-clipboard-document'
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
