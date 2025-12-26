# Medical/Pharmacy ERP System with EHR Module

A comprehensive Electronic Health Record (EHR) system built with Django REST Framework for the backend and Nuxt 3 with Nuxt UI for the frontend. The system supports longitudinal patient care using the SOAPO methodology (Subjective, Objective, Assessment, Plan, Outcome).

## Features

### Core Functionality
- **Patient Management**: Track patient demographics, medical history, allergies, and contact information
- **Encounter Tracking**: Record patient visits across different locations (hospital, clinic, pharmacy) with comprehensive SOAPO documentation
- **Diagnoses**: Manage patient diagnoses with ICD codes, severity levels, and clinical notes
- **Medication Management**: Track prescriptions, dosages, frequencies, and medication status
- **Lab Results**: Store and monitor laboratory test results with reference ranges and interpretations

### SOAPO Documentation
The system implements the complete SOAPO methodology for clinical documentation:
- **S**ubjective: Patient's complaints and symptoms
- **O**bjective: Physical examination findings and vital signs
- **A**ssessment: Diagnosis and clinical impression
- **P**lan: Treatment plan and recommendations
- **O**utcome: Follow-up results and patient outcome

## Technology Stack

### Backend
- Django 6.0
- Django REST Framework 3.16
- django-filter for advanced filtering
- django-cors-headers for CORS support
- SQLite database (easily configurable to PostgreSQL/MySQL)

### Frontend
- Nuxt 3 (v4.2.2)
- Nuxt UI for component library
- TypeScript for type safety
- Vue 3.5 with Composition API

## Project Structure

```
EHR/
├── backend/              # Django backend
│   ├── config/          # Django project settings
│   ├── ehr/             # EHR application
│   │   ├── models.py    # Patient, Encounter, Diagnosis, Medication, LabResult models
│   │   ├── serializers.py  # DRF serializers
│   │   ├── views.py     # API ViewSets
│   │   └── urls.py      # API routes
│   ├── manage.py
│   └── requirements.txt
│
├── frontend/            # Nuxt 3 frontend
│   ├── app/
│   │   ├── pages/      # Page components (patients, encounters)
│   │   └── app.vue     # Main layout
│   ├── composables/    # API client composable
│   ├── types/          # TypeScript type definitions
│   └── nuxt.config.ts
│
└── README.md
```

## Setup Instructions

### Backend Setup

1. **Navigate to backend directory**:
   ```bash
   cd backend
   ```

2. **Create and activate virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (optional)**:
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

   The backend API will be available at `http://127.0.0.1:8000/api/`

### Frontend Setup

1. **Navigate to frontend directory**:
   ```bash
   cd frontend
   ```

2. **Install dependencies**:
   ```bash
   npm install
   ```

3. **Start the development server**:
   ```bash
   npm run dev
   ```

   The frontend will be available at `http://localhost:3000`

## API Endpoints

### Patients
- `GET /api/patients/` - List all patients
- `POST /api/patients/` - Create new patient
- `GET /api/patients/{id}/` - Get patient details
- `PUT /api/patients/{id}/` - Update patient
- `DELETE /api/patients/{id}/` - Delete patient
- `GET /api/patients/{id}/encounters/` - Get patient's encounters

### Encounters
- `GET /api/encounters/` - List all encounters
- `POST /api/encounters/` - Create new encounter
- `GET /api/encounters/{id}/` - Get encounter details (includes SOAPO data)
- `PUT /api/encounters/{id}/` - Update encounter
- `DELETE /api/encounters/{id}/` - Delete encounter

### Diagnoses
- `GET /api/diagnoses/` - List all diagnoses
- `POST /api/diagnoses/` - Create new diagnosis
- `GET /api/diagnoses/{id}/` - Get diagnosis details
- `PUT /api/diagnoses/{id}/` - Update diagnosis
- `DELETE /api/diagnoses/{id}/` - Delete diagnosis

### Medications
- `GET /api/medications/` - List all medications
- `POST /api/medications/` - Create new medication
- `GET /api/medications/{id}/` - Get medication details
- `PUT /api/medications/{id}/` - Update medication
- `DELETE /api/medications/{id}/` - Delete medication

### Lab Results
- `GET /api/lab-results/` - List all lab results
- `POST /api/lab-results/` - Create new lab result
- `GET /api/lab-results/{id}/` - Get lab result details
- `PUT /api/lab-results/{id}/` - Update lab result
- `DELETE /api/lab-results/{id}/` - Delete lab result

## Usage Examples

### Creating a Patient
```bash
curl -X POST http://127.0.0.1:8000/api/patients/ \
  -H "Content-Type: application/json" \
  -d '{
    "first_name": "John",
    "last_name": "Doe",
    "date_of_birth": "1990-01-01",
    "gender": "M",
    "phone_number": "+1234567890",
    "blood_type": "O+",
    "allergies": "Penicillin"
  }'
```

### Creating an Encounter with SOAPO
```bash
curl -X POST http://127.0.0.1:8000/api/encounters/ \
  -H "Content-Type: application/json" \
  -d '{
    "patient": 1,
    "encounter_type": "OUTPATIENT",
    "status": "COMPLETED",
    "encounter_date": "2025-12-26T10:00:00Z",
    "subjective": "Patient complains of persistent headache for 3 days",
    "objective": "BP: 120/80, Temp: 98.6F, No signs of neurological deficit",
    "assessment": "Tension headache",
    "plan": "Prescribe ibuprofen 400mg, advise rest and hydration",
    "outcome": "Patient reported improvement after 2 days",
    "location": "Main Clinic",
    "provider_name": "Dr. Smith"
  }'
```

## Development

### Running Tests
```bash
# Backend tests
cd backend
python manage.py test

# Frontend tests (if configured)
cd frontend
npm run test
```

### Building for Production

**Backend**:
- Configure production database in `backend/config/settings.py`
- Set `DEBUG = False`
- Configure proper `SECRET_KEY` and `ALLOWED_HOSTS`
- Use a production WSGI server like Gunicorn

**Frontend**:
```bash
cd frontend
npm run build
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License.

## Support

For issues or questions, please open an issue on the GitHub repository.
