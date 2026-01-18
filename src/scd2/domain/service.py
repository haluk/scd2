from datetime import datetime
from typing import Iterable, Tuple

from .model import NaturalKey, SCDRow


class SCDType2Service:
    def __init__(self, repo, hash_fn):
        self.repo = repo
        self.hash_fn = hash_fn

    def upsert(self, key: NaturalKey, attrs: dict, now: datetime) -> None:
        """Insert or version a single entity."""
        h = self.hash_fn(attrs)
        current = self.repo.get_open(key)

        if current:
            if current.row_hash == h:
                current.updated_at = now
                return

            self.repo.close(current, now)

        self.repo.insert(SCDRow(key, attrs, h, now, now, None))

    def bulk_upsert(self, items: Iterable[Tuple[NaturalKey, dict]], now: datetime) -> None:
        """Bulk version entities efficiently."""
        keys = [k for k, _ in items]
        current_rows = self.repo.get_open_bulk(keys)
        current_map = {r.key: r for r in current_rows}

        to_close = []
        to_insert = []

        for key, attrs in items:
            h = self.hash_fn(attrs)
            current = current_map.get(key)

            if current and current.row_hash == h:
                continue

            if current:
                to_close.append(current)

            to_insert.append(SCDRow(key, attrs, h, now, now, None))

        if to_close:
            self.repo.close_bulk(to_close, now)

        if to_insert:
            self.repo.insert_bulk(to_insert)
