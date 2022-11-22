from data.genetic_codes import GENETIC_CODE_REVERSE
from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from data.base_classes import convert_dna_to_rna, convert_rna_to_protein
from data.db import Session

app = FastAPI()

# for allow CORS requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.post("/")
async def root(dna_string: str = Form()):
    rna = convert_dna_to_rna(Session(), dna_string)
    protein = convert_rna_to_protein(Session(), rna)
    return {"rna": rna, "protein": protein}

# type to console "uvicorn main:app --reload"
