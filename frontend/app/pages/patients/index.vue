<template>
  <div>
    <div class="flex justify-between items-center mb-6">
      <h2 class="text-2xl font-bold">Patients</h2>
      <UButton @click="isModalOpen = true" icon="i-heroicons-plus">Add Patient</UButton>
    </div>
    
    <UCard>
      <div class="mb-4">
        <UInput
          v-model="searchQuery"
          icon="i-heroicons-magnifying-glass"
          placeholder="Search patients..."
          @input="debouncedSearch"
        />
      </div>
      
      <div v-if="pending" class="flex justify-center py-8">
        <UIcon name="i-heroicons-arrow-path" class="animate-spin text-2xl" />
      </div>
      
      <div v-else-if="error" class="text-red-600 py-4">
        Error loading patients: {{ error }}
      </div>
      
      <UTable
        v-else
        :rows="patients"
        :columns="columns"
        @select="viewPatient"
      >
        <template #actions-data="{ row }">
          <UButton
            variant="ghost"
            icon="i-heroicons-eye"
            @click="viewPatient(row)"
          />
        </template>
      </UTable>
    </UCard>
    
    <!-- Add Patient Modal -->
    <UModal v-model="isModalOpen">
      <UCard>
        <template #header>
          <h3 class="text-xl font-bold">Add New Patient</h3>
        </template>
        
        <form @submit.prevent="addPatient" class="space-y-4">
          <UFormGroup label="First Name" required>
            <UInput v-model="newPatient.first_name" required />
          </UFormGroup>
          
          <UFormGroup label="Last Name" required>
            <UInput v-model="newPatient.last_name" required />
          </UFormGroup>
          
          <UFormGroup label="Date of Birth" required>
            <UInput v-model="newPatient.date_of_birth" type="date" required />
          </UFormGroup>
          
          <UFormGroup label="Gender" required>
            <USelect
              v-model="newPatient.gender"
              :options="[
                { label: 'Male', value: 'M' },
                { label: 'Female', value: 'F' },
                { label: 'Other', value: 'O' }
              ]"
              required
            />
          </UFormGroup>
          
          <UFormGroup label="Phone Number">
            <UInput v-model="newPatient.phone_number" />
          </UFormGroup>
          
          <UFormGroup label="Email">
            <UInput v-model="newPatient.email" type="email" />
          </UFormGroup>
          
          <UFormGroup label="Address">
            <UTextarea v-model="newPatient.address" />
          </UFormGroup>
          
          <UFormGroup label="Blood Type">
            <UInput v-model="newPatient.blood_type" placeholder="e.g., A+" />
          </UFormGroup>
          
          <UFormGroup label="Allergies">
            <UTextarea v-model="newPatient.allergies" placeholder="Known allergies" />
          </UFormGroup>
          
          <div class="flex justify-end gap-2">
            <UButton variant="ghost" @click="isModalOpen = false">Cancel</UButton>
            <UButton type="submit" :loading="submitting">Add Patient</UButton>
          </div>
        </form>
      </UCard>
    </UModal>
  </div>
</template>

<script setup lang="ts">
import type { Patient } from '~/types/ehr'

definePageMeta({
  title: 'Patients'
})

const api = useApi()
const router = useRouter()

// State
const searchQuery = ref('')
const isModalOpen = ref(false)
const submitting = ref(false)

// Fetch patients
const { data: patients, pending, error, refresh } = await useLazyAsyncData<Patient[]>(
  'patients',
  () => api.patients.list({ search: searchQuery.value }),
  { default: () => [] }
)

// Table columns
const columns = [
  { key: 'id', label: 'ID' },
  { key: 'first_name', label: 'First Name' },
  { key: 'last_name', label: 'Last Name' },
  { key: 'date_of_birth', label: 'Date of Birth' },
  { key: 'age', label: 'Age' },
  { key: 'gender', label: 'Gender' },
  { key: 'phone_number', label: 'Phone' },
  { key: 'actions', label: 'Actions' }
]

// New patient form
const newPatient = ref({
  first_name: '',
  last_name: '',
  date_of_birth: '',
  gender: 'M',
  phone_number: '',
  email: '',
  address: '',
  blood_type: '',
  allergies: ''
})

// Debounced search
const debouncedSearch = useDebounceFn(() => {
  refresh()
}, 500)

// Methods
const viewPatient = (patient: Patient) => {
  router.push(`/patients/${patient.id}`)
}

const addPatient = async () => {
  submitting.value = true
  try {
    await api.patients.create(newPatient.value)
    isModalOpen.value = false
    newPatient.value = {
      first_name: '',
      last_name: '',
      date_of_birth: '',
      gender: 'M',
      phone_number: '',
      email: '',
      address: '',
      blood_type: '',
      allergies: ''
    }
    refresh()
  } catch (err) {
    console.error('Error adding patient:', err)
  } finally {
    submitting.value = false
  }
}
</script>
