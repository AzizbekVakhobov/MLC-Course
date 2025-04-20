from pydantic import BaseModel

class DiabetesRequest(BaseModel):
    gender: str  # "Male" or "Female"
    age: float
    hypertension: int  # 0 or 1
    heart_disease: int  # 0 or 1
    smoking_history: str  # "never", "former", "current", etc.
    bmi: float
    HbA1c_level: float
    blood_glucose_level: int

    def to_features(self):
        return [
            self.gender,
            self.age,
            self.hypertension,
            self.heart_disease,
            self.smoking_history,
            self.bmi,
            self.HbA1c_level,
            self.blood_glucose_level
        ]
