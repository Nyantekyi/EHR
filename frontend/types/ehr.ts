/**
 * TypeScript types for EHR models
 */

export interface Patient {
  id: number
  first_name: string
  last_name: string
  date_of_birth: string
  age?: number
  gender: 'M' | 'F' | 'O'
  phone_number?: string
  email?: string
  address?: string
  blood_type?: string
  allergies?: string
  medical_history?: string
  created_at: string
  updated_at: string
}

export interface Encounter {
  id: number
  patient: number
  patient_name?: string
  encounter_type: 'OUTPATIENT' | 'INPATIENT' | 'EMERGENCY' | 'CLINIC' | 'PHARMACY'
  status: 'SCHEDULED' | 'IN_PROGRESS' | 'COMPLETED' | 'CANCELLED'
  subjective?: string
  objective?: string
  assessment?: string
  plan?: string
  outcome?: string
  location?: string
  provider_name?: string
  encounter_date: string
  diagnoses?: Diagnosis[]
  medications?: Medication[]
  lab_results?: LabResult[]
  created_at: string
  updated_at: string
}

export interface Diagnosis {
  id: number
  encounter: number
  icd_code: string
  description: string
  diagnosis_type: 'PRIMARY' | 'SECONDARY' | 'DIFFERENTIAL'
  severity?: 'MILD' | 'MODERATE' | 'SEVERE'
  notes?: string
  diagnosed_date: string
  created_at: string
  updated_at: string
}

export interface Medication {
  id: number
  encounter: number
  medication_name: string
  dosage: string
  frequency: string
  route: 'ORAL' | 'IV' | 'IM' | 'SC' | 'TOPICAL' | 'INHALATION'
  duration_days: number
  quantity: number
  refills: number
  instructions?: string
  indication?: string
  status: 'ACTIVE' | 'COMPLETED' | 'DISCONTINUED'
  prescribed_date: string
  start_date: string
  end_date?: string
  created_at: string
  updated_at: string
}

export interface LabResult {
  id: number
  encounter: number
  test_name: string
  test_code?: string
  test_category: 'HEMATOLOGY' | 'CHEMISTRY' | 'MICROBIOLOGY' | 'RADIOLOGY' | 'PATHOLOGY' | 'OTHER'
  result_value: string
  unit?: string
  reference_range?: string
  status: 'NORMAL' | 'ABNORMAL' | 'CRITICAL' | 'PENDING'
  interpretation?: string
  performing_lab?: string
  specimen_type?: string
  collection_date: string
  result_date?: string
  created_at: string
  updated_at: string
}

export interface PaginatedResponse<T> {
  count: number
  next: string | null
  previous: string | null
  results: T[]
}
