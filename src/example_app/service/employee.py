from datetime import datetime

from example_app.mapper.employee import EmployeeMapper
from scd2.domain.model import NaturalKey
from scd2.domain.service import SCDType2Service
from scd2.util.hashing import stable_hash


class EmployeeService:
    def __init__(self, repo):
        self.scd = SCDType2Service(repo, stable_hash)

    def ingest(self, employee_dto, now: datetime):
        key = NaturalKey((employee_dto.employee_id,))
        attrs = EmployeeMapper.dto_to_attrs(employee_dto)
        self.scd.upsert(key, attrs, now)
