from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Patient, Encounter, Diagnosis, Medication, LabResult
from .serializers import (
    PatientSerializer, PatientDetailSerializer,
    EncounterSerializer, EncounterListSerializer,
    DiagnosisSerializer, MedicationSerializer, LabResultSerializer
)


class PatientViewSet(viewsets.ModelViewSet):
    """ViewSet for managing patients."""
    queryset = Patient.objects.all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['first_name', 'last_name', 'phone_number', 'email']
    ordering_fields = ['last_name', 'first_name', 'date_of_birth', 'created_at']
    ordering = ['last_name', 'first_name']
    
    def get_serializer_class(self):
        """Use detailed serializer for retrieve action."""
        if self.action == 'retrieve':
            return PatientDetailSerializer
        return PatientSerializer
    
    @action(detail=True, methods=['get'])
    def encounters(self, request, pk=None):
        """Get all encounters for a specific patient."""
        patient = self.get_object()
        encounters = patient.encounters.all()
        serializer = EncounterListSerializer(encounters, many=True)
        return Response(serializer.data)


class EncounterViewSet(viewsets.ModelViewSet):
    """ViewSet for managing encounters."""
    queryset = Encounter.objects.select_related('patient').prefetch_related(
        'diagnoses', 'medications', 'lab_results'
    )
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['patient', 'encounter_type', 'status']
    ordering_fields = ['encounter_date', 'created_at']
    ordering = ['-encounter_date']
    
    def get_serializer_class(self):
        """Use list serializer for list action, detailed for others."""
        if self.action == 'list':
            return EncounterListSerializer
        return EncounterSerializer


class DiagnosisViewSet(viewsets.ModelViewSet):
    """ViewSet for managing diagnoses."""
    queryset = Diagnosis.objects.select_related('encounter', 'encounter__patient')
    serializer_class = DiagnosisSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['encounter', 'diagnosis_type', 'severity']
    ordering_fields = ['diagnosed_date', 'created_at']
    ordering = ['-diagnosed_date']


class MedicationViewSet(viewsets.ModelViewSet):
    """ViewSet for managing medications."""
    queryset = Medication.objects.select_related('encounter', 'encounter__patient')
    serializer_class = MedicationSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['encounter', 'status', 'route']
    ordering_fields = ['prescribed_date', 'start_date', 'created_at']
    ordering = ['-prescribed_date']


class LabResultViewSet(viewsets.ModelViewSet):
    """ViewSet for managing lab results."""
    queryset = LabResult.objects.select_related('encounter', 'encounter__patient')
    serializer_class = LabResultSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['encounter', 'test_category', 'status']
    ordering_fields = ['collection_date', 'result_date', 'created_at']
    ordering = ['-collection_date']

