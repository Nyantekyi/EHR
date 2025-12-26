from django.db import models
from django.core.validators import MinValueValidator


class Patient(models.Model):
    """Patient model for storing patient demographics and information."""
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    
    # Demographics
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    
    # Contact Information
    phone_number = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    address = models.TextField(blank=True)
    
    # Medical Information
    blood_type = models.CharField(max_length=5, blank=True)
    allergies = models.TextField(blank=True, help_text="Known allergies")
    medical_history = models.TextField(blank=True)
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['last_name', 'first_name']
        indexes = [
            models.Index(fields=['last_name', 'first_name']),
            models.Index(fields=['date_of_birth']),
        ]
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Encounter(models.Model):
    """Encounter model for tracking patient visits using SOAPO methodology."""
    ENCOUNTER_TYPE_CHOICES = [
        ('OUTPATIENT', 'Outpatient'),
        ('INPATIENT', 'Inpatient'),
        ('EMERGENCY', 'Emergency'),
        ('CLINIC', 'Clinic'),
        ('PHARMACY', 'Pharmacy'),
    ]
    
    STATUS_CHOICES = [
        ('SCHEDULED', 'Scheduled'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ]
    
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='encounters')
    encounter_type = models.CharField(max_length=20, choices=ENCOUNTER_TYPE_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='SCHEDULED')
    
    # SOAPO Fields
    subjective = models.TextField(blank=True, help_text="Patient's complaints and symptoms")
    objective = models.TextField(blank=True, help_text="Physical examination findings and vital signs")
    assessment = models.TextField(blank=True, help_text="Diagnosis and clinical impression")
    plan = models.TextField(blank=True, help_text="Treatment plan and recommendations")
    outcome = models.TextField(blank=True, help_text="Follow-up results and patient outcome")
    
    # Location and Provider
    location = models.CharField(max_length=200, blank=True)
    provider_name = models.CharField(max_length=100, blank=True)
    
    # Timestamps
    encounter_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-encounter_date']
        indexes = [
            models.Index(fields=['patient', '-encounter_date']),
            models.Index(fields=['status']),
        ]
    
    def __str__(self):
        return f"{self.patient} - {self.encounter_type} on {self.encounter_date.date()}"


class Diagnosis(models.Model):
    """Diagnosis model for storing patient diagnoses."""
    encounter = models.ForeignKey(Encounter, on_delete=models.CASCADE, related_name='diagnoses')
    
    # Diagnosis Information
    icd_code = models.CharField(max_length=20, help_text="ICD-10 or ICD-11 code")
    description = models.CharField(max_length=500)
    diagnosis_type = models.CharField(
        max_length=20,
        choices=[
            ('PRIMARY', 'Primary'),
            ('SECONDARY', 'Secondary'),
            ('DIFFERENTIAL', 'Differential'),
        ],
        default='PRIMARY'
    )
    
    # Clinical Details
    severity = models.CharField(
        max_length=20,
        choices=[
            ('MILD', 'Mild'),
            ('MODERATE', 'Moderate'),
            ('SEVERE', 'Severe'),
        ],
        blank=True
    )
    notes = models.TextField(blank=True)
    
    # Timestamps
    diagnosed_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-diagnosed_date']
        verbose_name_plural = 'Diagnoses'
    
    def __str__(self):
        return f"{self.icd_code}: {self.description}"


class Medication(models.Model):
    """Medication model for prescriptions and medication orders."""
    encounter = models.ForeignKey(Encounter, on_delete=models.CASCADE, related_name='medications')
    
    # Medication Information
    medication_name = models.CharField(max_length=200)
    dosage = models.CharField(max_length=100, help_text="e.g., 500mg, 10ml")
    frequency = models.CharField(max_length=100, help_text="e.g., twice daily, every 8 hours")
    route = models.CharField(
        max_length=20,
        choices=[
            ('ORAL', 'Oral'),
            ('IV', 'Intravenous'),
            ('IM', 'Intramuscular'),
            ('SC', 'Subcutaneous'),
            ('TOPICAL', 'Topical'),
            ('INHALATION', 'Inhalation'),
        ],
        default='ORAL'
    )
    
    # Prescription Details
    duration_days = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    quantity = models.PositiveIntegerField(help_text="Total quantity prescribed")
    refills = models.PositiveIntegerField(default=0)
    
    # Instructions
    instructions = models.TextField(blank=True, help_text="Special instructions for taking the medication")
    indication = models.CharField(max_length=200, blank=True, help_text="Reason for prescription")
    
    # Status
    status = models.CharField(
        max_length=20,
        choices=[
            ('ACTIVE', 'Active'),
            ('COMPLETED', 'Completed'),
            ('DISCONTINUED', 'Discontinued'),
        ],
        default='ACTIVE'
    )
    
    # Timestamps
    prescribed_date = models.DateField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-prescribed_date']
    
    def __str__(self):
        return f"{self.medication_name} - {self.dosage} {self.frequency}"


class LabResult(models.Model):
    """Lab Result model for storing laboratory test results."""
    encounter = models.ForeignKey(Encounter, on_delete=models.CASCADE, related_name='lab_results')
    
    # Test Information
    test_name = models.CharField(max_length=200)
    test_code = models.CharField(max_length=50, blank=True, help_text="LOINC or local lab code")
    test_category = models.CharField(
        max_length=50,
        choices=[
            ('HEMATOLOGY', 'Hematology'),
            ('CHEMISTRY', 'Chemistry'),
            ('MICROBIOLOGY', 'Microbiology'),
            ('RADIOLOGY', 'Radiology'),
            ('PATHOLOGY', 'Pathology'),
            ('OTHER', 'Other'),
        ],
        default='OTHER'
    )
    
    # Results
    result_value = models.CharField(max_length=200, help_text="Test result value")
    unit = models.CharField(max_length=50, blank=True, help_text="Unit of measurement")
    reference_range = models.CharField(max_length=200, blank=True, help_text="Normal reference range")
    
    # Interpretation
    status = models.CharField(
        max_length=20,
        choices=[
            ('NORMAL', 'Normal'),
            ('ABNORMAL', 'Abnormal'),
            ('CRITICAL', 'Critical'),
            ('PENDING', 'Pending'),
        ],
        default='PENDING'
    )
    interpretation = models.TextField(blank=True, help_text="Clinical interpretation of results")
    
    # Lab Details
    performing_lab = models.CharField(max_length=200, blank=True)
    specimen_type = models.CharField(max_length=100, blank=True, help_text="e.g., Blood, Urine")
    
    # Timestamps
    collection_date = models.DateTimeField()
    result_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-collection_date']
    
    def __str__(self):
        return f"{self.test_name}: {self.result_value} {self.unit}"

