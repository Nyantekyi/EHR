from rest_framework import serializers
from .models import Patient, Encounter, Diagnosis, Medication, LabResult


class PatientSerializer(serializers.ModelSerializer):
    """Serializer for Patient model."""
    age = serializers.SerializerMethodField()
    
    class Meta:
        model = Patient
        fields = [
            'id', 'first_name', 'last_name', 'date_of_birth', 'age', 'gender',
            'phone_number', 'email', 'address', 'blood_type', 'allergies',
            'medical_history', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def get_age(self, obj):
        """Calculate patient's age from date of birth."""
        from datetime import date
        today = date.today()
        age = today.year - obj.date_of_birth.year
        if today.month < obj.date_of_birth.month or (
            today.month == obj.date_of_birth.month and today.day < obj.date_of_birth.day
        ):
            age -= 1
        return age


class DiagnosisSerializer(serializers.ModelSerializer):
    """Serializer for Diagnosis model."""
    
    class Meta:
        model = Diagnosis
        fields = [
            'id', 'encounter', 'icd_code', 'description', 'diagnosis_type',
            'severity', 'notes', 'diagnosed_date', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class MedicationSerializer(serializers.ModelSerializer):
    """Serializer for Medication model."""
    
    class Meta:
        model = Medication
        fields = [
            'id', 'encounter', 'medication_name', 'dosage', 'frequency', 'route',
            'duration_days', 'quantity', 'refills', 'instructions', 'indication',
            'status', 'prescribed_date', 'start_date', 'end_date',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class LabResultSerializer(serializers.ModelSerializer):
    """Serializer for LabResult model."""
    
    class Meta:
        model = LabResult
        fields = [
            'id', 'encounter', 'test_name', 'test_code', 'test_category',
            'result_value', 'unit', 'reference_range', 'status', 'interpretation',
            'performing_lab', 'specimen_type', 'collection_date', 'result_date',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class EncounterSerializer(serializers.ModelSerializer):
    """Serializer for Encounter model with nested related data."""
    patient_name = serializers.SerializerMethodField()
    diagnoses = DiagnosisSerializer(many=True, read_only=True)
    medications = MedicationSerializer(many=True, read_only=True)
    lab_results = LabResultSerializer(many=True, read_only=True)
    
    class Meta:
        model = Encounter
        fields = [
            'id', 'patient', 'patient_name', 'encounter_type', 'status',
            'subjective', 'objective', 'assessment', 'plan', 'outcome',
            'location', 'provider_name', 'encounter_date',
            'diagnoses', 'medications', 'lab_results',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def get_patient_name(self, obj):
        """Get patient's full name."""
        return str(obj.patient)


class EncounterListSerializer(serializers.ModelSerializer):
    """Lightweight serializer for listing encounters without nested data."""
    patient_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Encounter
        fields = [
            'id', 'patient', 'patient_name', 'encounter_type', 'status',
            'location', 'provider_name', 'encounter_date', 'created_at'
        ]
        read_only_fields = ['id', 'created_at']
    
    def get_patient_name(self, obj):
        """Get patient's full name."""
        return str(obj.patient)


class PatientDetailSerializer(PatientSerializer):
    """Detailed patient serializer with recent encounters."""
    recent_encounters = serializers.SerializerMethodField()
    
    class Meta(PatientSerializer.Meta):
        fields = PatientSerializer.Meta.fields + ['recent_encounters']
    
    def get_recent_encounters(self, obj):
        """Get patient's 5 most recent encounters."""
        encounters = obj.encounters.all()[:5]
        return EncounterListSerializer(encounters, many=True).data
