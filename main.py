from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Annotated

app = FastAPI()

class ChoiceBase(BaseModel):
    id: int
    choice_text: str
    is_correct: bool

class QuestionBase(ChoiceBase):
    id: int
    question_text: str
    choices: List[ChoiceBase]

    