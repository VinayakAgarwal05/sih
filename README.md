# SAARTHI AI — Complete Hackathon Prototype

AI-Based Predictive Personnel Stress and Welfare Monitoring System for Uniformed Forces.

## What is included
- Personnel wellness mobile-style PWA screen
- Welfare Officer dashboard
- Commander unit-level dashboard
- Role-based access control demo
- Synthetic personnel/duty/deployment/leave/training/wellness data
- AI risk engine with personal-baseline deviation, multi-factor risk, temporal trend, persistence rule and explainability
- 5-day persistent high-risk human welfare review trigger
- Welfare intervention recommendations
- Intervention tracking and follow-up
- Consent/privacy center
- Audit log
- Responsive UI
- Express API + Python FastAPI AI service

## Safety / scope
This is a hackathon prototype using synthetic data. It does not diagnose mental-health conditions and does not make disciplinary decisions. Risk is an early-warning welfare signal and persistent alerts require human review.

## Quick start
### 1. Frontend
```bash
cd frontend
npm install
npm run dev
```
Open the URL shown by Vite.

### 2. Backend API (optional for the demo; frontend has demo fallback)
```bash
cd backend
npm install
npm start
```
API: http://localhost:4000

### 3. AI engine (optional)
```bash
cd ai-engine
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```
AI API: http://localhost:8000

## Demo accounts
- Personnel: `personnel` / `demo123`
- Welfare Officer: `welfare` / `demo123`
- Commander: `commander` / `demo123`
- Administrator: `admin` / `demo123`

## Demo flow
1. Log in as Welfare Officer.
2. Open Priority Reviews.
3. Select P-1042.
4. Review the risk trajectory, contributing factors and explanation.
5. Create/confirm a welfare review.
6. Record a workload/rest intervention.
7. Use Simulation to advance the case and show risk falling after intervention.
8. Switch to Commander to show unit-level workload/welfare trends.
9. Switch to Personnel to show the private self-check and privacy controls.

## Important implementation note
The numeric risk thresholds are prototype/demo thresholds, not clinically validated cut-offs. Real deployment would require domain validation, governance, legal review, security assessment, bias evaluation and human oversight.
