# Quantori Python School Final Project


### Project Description

- [x] Html page
- [x] Transcription of DNA to RNA and RNA to amino
- [x] Written classes for the database
- [x] Function that plots G-C ratio in a DNA molecule has and saves the resulting graph to a .png file.
- [x] Docker
- [x] Unit tests
- [x] command line input

### How to Use the Project
0. (optional):

   `sudo systemctl stop postgresql`


1. from this directory type this to console:

    `sudo docker-compose up --build`


2. open this page in your browser

    `http://localhost/index.html`


3. type DNA (for example "ATTTGGCTACTAACAATCTA") to **DNA line**
4. push the button "GET PROTEIN"
5. scroll
6. type DNA to **DNA textarea** and step to the **Step line**
7. push the button "GET PLOT"

### How to use and Run the Project in command line:

1. from this directory type this to console:

`sudo docker-compose up --build --d`

2. type this here for open project command line:

`docker-compose exec fastapi bash`

3. type this for run functions:
    1. for "convert_dna_to_rna": `python3 command_line.py -dna <your string DNA>`
    2. for "convert_rna_to_protein": `python3 command_line.py -rna <your string RNA>`
    3. for "plot_gc_ratio": `python3 command_line.py -p <your string DNA> -s <step>`
       or `python3 command_line.py -p <your string DNA>` (default step is 100)
        1. if True, open "images/plot_gc_ratio.png"
        2. if False, open "images/wrong.png"

[//]: # (python3 command_line.py -p ATTTGGCTACTAACAATCTAGTTGTAATGGCCTACA -s 2 )

4. exit from project command line

`exit`

5. stop docker

`docker-compose stop`