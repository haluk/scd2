from example_app.config.settings import db_url
from example_app.controller.employee import EmployeeController
from example_app.db.base import Base
from example_app.db.session import Database
from example_app.model.employee import Employee
from example_app.repository.employee import EmployeeRepository
from example_app.service.employee import EmployeeService

db = Database(db_url)

Base.metadata.create_all(db.engine)

session = db.session()
repo = EmployeeRepository(session, Employee, ("employee_id",))
service = EmployeeService(repo)
controller = EmployeeController(service)

# Initial ingest
controller.ingest_from_external({
    "employee_id": "E1",
    "department_id": "D1",
    "name": "Alice",
    "title": "Engineer",
    "skills": [{"skill_id": "S1", "name": "Python"}],
    "projects": [{"project_id": "P1", "name": "Platform"}],
})
session.commit()

# Update title
controller.ingest_from_external({
    "employee_id": "E1",
    "department_id": "D1",
    "name": "Alice",
    "title": "Senior Engineer",
    "skills": [{"skill_id": "S1", "name": "Python"}],
    "projects": [{"project_id": "P1", "name": "Platform"}],
})
session.commit()

# Add new employee
controller.ingest_from_external({
    "employee_id": "E2",
    "department_id": "D2",
    "name": "Bob",
    "title": "Manager",
    "skills": [{"skill_id": "S2", "name": "Leadership"}],
    "projects": [{"project_id": "P2", "name": "Strategy"}],
})
session.commit()

# Update department
controller.ingest_from_external({
    "employee_id": "E1",
    "department_id": "D3",
    "name": "Alice",
    "title": "Senior Engineer",
    "skills": [{"skill_id": "S1", "name": "Python"}],
    "projects": [{"project_id": "P1", "name": "Platform"}],
})
session.commit()
