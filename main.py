from data.genetic_codes import *
from data.base_classes import *
from utilities import *
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

genetic_code = dict_reverse_from_list(GENETIC_CODE)
print(genetic_code)
genetic_code = change_amino_to_letters(genetic_code, AMINO_LETTERS)
print(genetic_code)

my_result = []
for dna in DNA:
    temp_rna = convert_dna_to_rna(dna)
    my_result.append(convert_rna_to_protein(temp_rna, genetic_code))


# for allow CORS requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.post("/")
async def root():
    return {"message": "Hello World"}

# type to console "uvicorn main:app --reload"
