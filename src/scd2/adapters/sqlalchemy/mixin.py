from datetime import datetime
from uuid import uuid4

from sqlalchemy import DateTime, String, Uuid
from sqlalchemy.orm import Mapped, mapped_column


class SCD2Mixin:
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    closed_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True, index=True)
    row_hash: Mapped[str] = mapped_column(String(64), nullable=False)


class UUIDPrimaryKeyMixin:
    id: Mapped[str] = mapped_column(
        Uuid(as_uuid=True),
        primary_key=True,
        default=uuid4,
    )
