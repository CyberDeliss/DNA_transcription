from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from data.base_classes import convert_dna_to_rna, convert_rna_to_protein
from data.db import Session
import data.create_db
from utilities import plot_gc_ratio

app = FastAPI()

# for allow CORS requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# ATTTGGCTACTAACAATCTAGTTGTAATGGCCTACATTACAGGTGGTGTTGTTCAGTTGCTAACTAACGCTAACTAACATCTTTGGCACTGTTTATGAAAAACTCAAACCCGTCCTTGATTGGCTTGAAGAGAAGTTT


@app.post("/dna_to_rna/")
async def root(dna_string: str = Form()):
    rna = convert_dna_to_rna(Session(), dna_string)
    protein = convert_rna_to_protein(Session(), rna)
    return {"rna": rna, "protein": protein}


@app.post("/plot/")
async def root(for_plot_string: str = Form(), step: int = Form()):
    plot_gc_ratio(for_plot_string, step)
    return {"plot_img": "plot_gc_ratio.png"}

# type to console "uvicorn main:app --reload"
