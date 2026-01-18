from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from example_app.db.base import Base
from example_app.model import employee_skill, project_employee
from scd2.adapters.sqlalchemy.mixin import SCD2Mixin, UUIDPrimaryKeyMixin


class Employee(Base, UUIDPrimaryKeyMixin, SCD2Mixin):
    __tablename__ = "employees"

    employee_id: Mapped[str] = mapped_column(String, index=True)
    department_id: Mapped[str] = mapped_column(ForeignKey("departments.department_id"))
    name: Mapped[str] = mapped_column(String)
    title: Mapped[str] = mapped_column(String)

    department = relationship("Department", back_populates="employees")
    skills = relationship("Skill", secondary=employee_skill, backref="employees")
    projects = relationship("Project", secondary=project_employee, backref="employees")
