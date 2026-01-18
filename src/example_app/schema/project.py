from pydantic import BaseModel


class ProjectSchema(BaseModel):
    project_id: str
    name: str
