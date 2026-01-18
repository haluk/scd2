from typing import TYPE_CHECKING, Iterable

from sqlalchemy import tuple_

from scd2.domain.model import NaturalKey, SCDRow
from scd2.domain.ports import SCDRepository

if TYPE_CHECKING:
    from sqlalchemy.orm import DeclarativeMeta, Session


class SQLAlchemySCDRepository(SCDRepository):
    def __init__(self, session: "Session", model: "DeclarativeMeta", key_columns: tuple[str, ...]):
        self.session = session
        self.model = model
        self.key_columns = key_columns

    def _key_filter(self, key: NaturalKey) -> dict:
        return dict(zip(self.key_columns, key.values))

    def get_open(self, key: NaturalKey):
        return (
            self.session
            .query(self.model)
            .filter_by(**self._key_filter(key))
            .filter(self.model.closed_at.is_(None))
            .one_or_none()
        )

    def get_open_bulk(self, keys: Iterable[NaturalKey]):
        tuples = [k.values for k in keys]
        return (
            self.session
            .query(self.model)
            .filter(
                tuple_(*[getattr(self.model, c) for c in self.key_columns]).in_(tuples),
                self.model.closed_at.is_(None),
            )
            .all()
        )

    def close(self, row, at) -> None:
        row.closed_at = at

    def close_bulk(self, rows: Iterable, at) -> None:
        for r in rows:
            r.closed_at = at

    def insert(self, row: SCDRow) -> None:
        obj = self.model(
            **dict(zip(self.key_columns, row.key.values)),
            **row.attrs,
            row_hash=row.hash,
            created_at=row.created_at,
            updated_at=row.updated_at,
            closed_at=row.closed_at,
        )
        self.session.add(obj)

    def insert_bulk(self, rows: Iterable[SCDRow]) -> None:
        objs = [
            self.model(
                **dict(zip(self.key_columns, row.key.values)),
                **row.attrs,
                row_hash=row.hash,
                created_at=row.created_at,
                updated_at=row.updated_at,
                closed_at=row.closed_at,
            )
            for row in rows
        ]
        self.session.add_all(objs)
