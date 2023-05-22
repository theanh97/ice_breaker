from pydantic import BaseModel, Field
from typing import List
from langchain.output_parsers import PydanticOutputParser


class PersonItel(BaseModel):
    summary: str = Field(description="summary of the person")
    facts: List[str] = Field(description="interesting facts about the person")
    topics_of_interest: List[str] = Field(description="Topics that may interest the person")
    ice_breakers: List[str] = Field(description="Create ice breakers to open a conversation with the person")

    def to_dict(self):
        return {
            "summary": self.summary,
            "facts": self.facts,
            "topics_of_interest": self.topics_of_interest,
            "ice_breakers": self.ice_breakers
        }


