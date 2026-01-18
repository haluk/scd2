from dataclasses import dataclass

from example_app.dto.project import ProjectDTO
from example_app.dto.skill import SkillDTO


@dataclass
class EmployeeDTO:
    employee_id: str
    department_id: str
    name: str
    title: str
    skills: list[SkillDTO]
    projects: list[ProjectDTO]
