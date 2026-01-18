from sqlalchemy import Column, ForeignKey, Table

from example_app.db.base import Base

employee_skill = Table(
    "employee_skill",
    Base.metadata,
    Column("employee_uuid", ForeignKey("employees.id"), primary_key=True),
    Column("skill_id", ForeignKey("skills.id"), primary_key=True),
)

project_employee = Table(
    "project_employee",
    Base.metadata,
    Column("project_id", ForeignKey("projects.id"), primary_key=True),
    Column("employee_uuid", ForeignKey("employees.id"), primary_key=True),
)
