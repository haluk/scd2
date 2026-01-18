from pydantic import BaseModel


class SkillSchema(BaseModel):
    skill_id: str
    name: str
