/**
 * Composable for API interactions with the Django backend
 */
export const useApi = () => {
  const config = useRuntimeConfig()
  const apiBase = config.public.apiBase

  const apiFetch = async <T>(endpoint: string, options: any = {}): Promise<T> => {
    try {
      const response = await $fetch<T>(`${apiBase}${endpoint}`, {
        ...options,
        credentials: 'include',
      })
      return response
    } catch (error) {
      console.error('API Error:', error)
      throw error
    }
  }

  return {
    // Patient endpoints
    patients: {
      list: (params?: any) => apiFetch('/patients/', { params }),
      get: (id: number) => apiFetch(`/patients/${id}/`),
      create: (data: any) => apiFetch('/patients/', { method: 'POST', body: data }),
      update: (id: number, data: any) => apiFetch(`/patients/${id}/`, { method: 'PUT', body: data }),
      delete: (id: number) => apiFetch(`/patients/${id}/`, { method: 'DELETE' }),
      encounters: (id: number) => apiFetch(`/patients/${id}/encounters/`),
    },

    // Encounter endpoints
    encounters: {
      list: (params?: any) => apiFetch('/encounters/', { params }),
      get: (id: number) => apiFetch(`/encounters/${id}/`),
      create: (data: any) => apiFetch('/encounters/', { method: 'POST', body: data }),
      update: (id: number, data: any) => apiFetch(`/encounters/${id}/`, { method: 'PUT', body: data }),
      delete: (id: number) => apiFetch(`/encounters/${id}/`, { method: 'DELETE' }),
    },

    // Diagnosis endpoints
    diagnoses: {
      list: (params?: any) => apiFetch('/diagnoses/', { params }),
      get: (id: number) => apiFetch(`/diagnoses/${id}/`),
      create: (data: any) => apiFetch('/diagnoses/', { method: 'POST', body: data }),
      update: (id: number, data: any) => apiFetch(`/diagnoses/${id}/`, { method: 'PUT', body: data }),
      delete: (id: number) => apiFetch(`/diagnoses/${id}/`, { method: 'DELETE' }),
    },

    // Medication endpoints
    medications: {
      list: (params?: any) => apiFetch('/medications/', { params }),
      get: (id: number) => apiFetch(`/medications/${id}/`),
      create: (data: any) => apiFetch('/medications/', { method: 'POST', body: data }),
      update: (id: number, data: any) => apiFetch(`/medications/${id}/`, { method: 'PUT', body: data }),
      delete: (id: number) => apiFetch(`/medications/${id}/`, { method: 'DELETE' }),
    },

    // Lab Results endpoints
    labResults: {
      list: (params?: any) => apiFetch('/lab-results/', { params }),
      get: (id: number) => apiFetch(`/lab-results/${id}/`),
      create: (data: any) => apiFetch('/lab-results/', { method: 'POST', body: data }),
      update: (id: number, data: any) => apiFetch(`/lab-results/${id}/`, { method: 'PUT', body: data }),
      delete: (id: number) => apiFetch(`/lab-results/${id}/`, { method: 'DELETE' }),
    },
  }
}
