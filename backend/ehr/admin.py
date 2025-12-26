from django.contrib import admin
from .models import Patient, Encounter, Diagnosis, Medication, LabResult


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'date_of_birth', 'gender', 'phone_number']
    search_fields = ['first_name', 'last_name', 'phone_number', 'email']
    list_filter = ['gender', 'blood_type']


@admin.register(Encounter)
class EncounterAdmin(admin.ModelAdmin):
    list_display = ['patient', 'encounter_type', 'status', 'encounter_date', 'location']
    search_fields = ['patient__first_name', 'patient__last_name', 'location', 'provider_name']
    list_filter = ['encounter_type', 'status', 'encounter_date']
    date_hierarchy = 'encounter_date'


@admin.register(Diagnosis)
class DiagnosisAdmin(admin.ModelAdmin):
    list_display = ['encounter', 'icd_code', 'description', 'diagnosis_type', 'severity']
    search_fields = ['icd_code', 'description']
    list_filter = ['diagnosis_type', 'severity', 'diagnosed_date']


@admin.register(Medication)
class MedicationAdmin(admin.ModelAdmin):
    list_display = ['encounter', 'medication_name', 'dosage', 'frequency', 'status']
    search_fields = ['medication_name', 'indication']
    list_filter = ['status', 'route', 'prescribed_date']


@admin.register(LabResult)
class LabResultAdmin(admin.ModelAdmin):
    list_display = ['encounter', 'test_name', 'result_value', 'unit', 'status']
    search_fields = ['test_name', 'test_code']
    list_filter = ['test_category', 'status', 'collection_date']

