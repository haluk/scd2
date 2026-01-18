from dataclasses import dataclass
from datetime import datetime
from typing import Generic, Mapping, Tuple, TypeVar

TKey = TypeVar("TKey")
TAttrs = TypeVar("TAttrs", bound=Mapping[str, object])


@dataclass(frozen=True)
class NaturalKey(Generic[TKey]):
    """Represents an ordered, composite natural key."""

    values: Tuple[object, ...]


@dataclass
class SCDRow(Generic[TKey, TAttrs]):
    """Represents a single SCD Type 2 versioned row."""

    key: NaturalKey[TKey]
    attrs: TAttrs
    hash: str
    created_at: datetime
    updated_at: datetime
    closed_at: datetime | None
