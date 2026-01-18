from typing import Iterable, Optional

from .model import NaturalKey, SCDRow


class SCDRepository:
    def get_open(self, key: NaturalKey) -> Optional[SCDRow]:
        """Return open row for the given natural key."""
        raise NotImplementedError

    def get_open_bulk(self, keys: Iterable[NaturalKey]) -> list[SCDRow]:
        """Return all open rows for the given keys."""
        raise NotImplementedError

    def close(self, row: SCDRow, at) -> None:
        """Close a single row."""
        raise NotImplementedError

    def close_bulk(self, rows: Iterable[SCDRow], at) -> None:
        """Close multiple rows."""
        raise NotImplementedError

    def insert(self, row: SCDRow) -> None:
        """Insert a new row."""
        raise NotImplementedError

    def insert_bulk(self, rows: Iterable[SCDRow]) -> None:
        """Insert multiple rows."""
        raise NotImplementedError
