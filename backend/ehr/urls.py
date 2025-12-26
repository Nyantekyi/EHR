from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PatientViewSet, EncounterViewSet, DiagnosisViewSet,
    MedicationViewSet, LabResultViewSet
)

router = DefaultRouter()
router.register(r'patients', PatientViewSet, basename='patient')
router.register(r'encounters', EncounterViewSet, basename='encounter')
router.register(r'diagnoses', DiagnosisViewSet, basename='diagnosis')
router.register(r'medications', MedicationViewSet, basename='medication')
router.register(r'lab-results', LabResultViewSet, basename='labresult')

urlpatterns = [
    path('', include(router.urls)),
]
