from fastapi import FastAPI
from pydantic import BaseModel, Field
import numpy as np

app=FastAPI(title='SAARTHI AI Risk Engine',version='1.0.0')

class Signals(BaseModel):
    duty_hours: float=Field(8,ge=0,le=24)
    night_duties: float=Field(2,ge=0)
    consecutive_duty_days: float=Field(4,ge=0)
    rest_hours: float=Field(8,ge=0,le=24)
    deployment_days: float=Field(10,ge=0)
    leave_postponements: float=Field(0,ge=0)
    training_hours: float=Field(4,ge=0)
    wellness_score: float=Field(80,ge=0,le=100)
    baseline_duty_hours: float=Field(8,gt=0)
    baseline_rest_hours: float=Field(8,gt=0)

@app.get('/health')
def health(): return {'ok':True,'service':'risk-engine'}

def clamp(x): return max(0,min(100,x))

@app.post('/predict')
def predict(s: Signals):
    workload_dev=max(0,(s.duty_hours/s.baseline_duty_hours-1)*100)
    rest_dev=max(0,(1-s.rest_hours/s.baseline_rest_hours)*100)
    factors={
      'workload_deviation':round(workload_dev,1),
      'reduced_rest':round(rest_dev,1),
      'night_duty':round(min(100,s.night_duties*12),1),
      'consecutive_duty':round(min(100,s.consecutive_duty_days*7),1),
      'deployment_extension':round(min(100,max(0,s.deployment_days-10)*5),1),
      'leave_pattern':round(min(100,s.leave_postponements*15),1),
      'wellness_change':round(max(0,80-s.wellness_score),1)
    }
    score=(0.26*min(100,workload_dev)+0.20*rest_dev+0.13*factors['night_duty']+0.14*factors['consecutive_duty']+0.10*factors['deployment_extension']+0.07*factors['leave_pattern']+0.10*factors['wellness_change'])
    score=round(clamp(score),1)
    level='HIGH' if score>=80 else 'ELEVATED' if score>=60 else 'MODERATE' if score>=40 else 'LOW'
    top=sorted(factors.items(),key=lambda x:x[1],reverse=True)[:3]
    return {'risk_score':score,'risk_level':level,'contributors':[{'factor':k,'value':v} for k,v in top], 'human_review_required':score>=80, 'disclaimer':'Early-warning welfare signal; not a diagnosis or disciplinary decision.'}
