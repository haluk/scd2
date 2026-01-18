from datetime import datetime

from example_app.mapper.employee import EmployeeMapper
from example_app.schema.employee import EmployeeSchema


class EmployeeController:
    def __init__(self, service):
        self.service = service

    def ingest_from_external(self, payload: dict):
        schema = EmployeeSchema.model_validate(payload)
        dto = EmployeeMapper.schema_to_dto(schema)
        self.service.ingest(dto, datetime.utcnow())
