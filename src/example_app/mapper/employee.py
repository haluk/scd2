from example_app.dto.employee import EmployeeDTO
from example_app.dto.project import ProjectDTO
from example_app.dto.skill import SkillDTO
from example_app.schema.employee import EmployeeSchema


class EmployeeMapper:
    @staticmethod
    def schema_to_dto(schema: EmployeeSchema) -> EmployeeDTO:
        return EmployeeDTO(
            employee_id=schema.employee_id,
            department_id=schema.department_id,
            name=schema.name,
            title=schema.title,
            skills=[SkillDTO(**s.dict()) for s in schema.skills],
            projects=[ProjectDTO(**p.dict()) for p in schema.projects],
        )

    @staticmethod
    def dto_to_attrs(dto: EmployeeDTO) -> dict:
        return {
            "department_id": dto.department_id,
            "name": dto.name,
            "title": dto.title,
        }
