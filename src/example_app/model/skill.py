from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from example_app.db.base import Base
from scd2.adapters.sqlalchemy.mixin import SCD2Mixin, UUIDPrimaryKeyMixin


class Skill(Base, UUIDPrimaryKeyMixin, SCD2Mixin):
    __tablename__ = "skills"

    skill_id: Mapped[str] = mapped_column(String, index=True)
    name: Mapped[str] = mapped_column(String)
