from typing import List

from pydantic import BaseModel

from example_app.schema.project import ProjectSchema
from example_app.schema.skill import SkillSchema


class EmployeeSchema(BaseModel):
    employee_id: str
    department_id: str
    name: str
    title: str
    skills: List[SkillSchema]
    projects: List[ProjectSchema]
