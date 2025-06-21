from pydantic import Field, computed_field, BaseModel
from typing import Annotated, Optional, Literal
from pydantic import Field, computed_field, BaseModel

class UserInput(BaseModel):
    age: Annotated[int, Field(..., gt=0, lt=120, description= 'Age of the user')]
    weight: Annotated[float, Field(..., gt=0, description='Weight of the user')]
    height: Annotated[float, Field(..., gt=0, lt=5, description='Height of the user')]
    income_lpa: Annotated [float, Field(..., gt=0, description="Annual salary of the user in lpa")]
    smoker: Annotated [bool, Field(..., description= 'Is user a smoker')]
    city: Annotated [str, Field(..., description='The city that the user belongs to')]
    occupation: Annotated [Literal['retired', 'freelancer', 'student', 'government_job', 'business_owner', 'unemployed', 'private_job'], Field(...,description='Occupation of the user')]


    @computed_field
    @property
    def set_bmi(self) -> float:
        return round(self.weight/(self.height**2),2)
    
    @computed_field
    @property
    def set_city(self) -> int:
        if self.city.lower in ['delhi', 'mumbai', 'bangalore', 'kolkata', 'pune', 'hyderabad' ]:
            return 1
        return 2