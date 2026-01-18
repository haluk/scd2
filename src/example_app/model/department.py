from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from example_app.db.base import Base
from scd2.adapters.sqlalchemy.mixin import SCD2Mixin, UUIDPrimaryKeyMixin


class Department(Base, UUIDPrimaryKeyMixin, SCD2Mixin):
    __tablename__ = "departments"

    department_id: Mapped[str] = mapped_column(String, index=True)
    name: Mapped[str] = mapped_column(String)

    employees = relationship("Employee", back_populates="department")
