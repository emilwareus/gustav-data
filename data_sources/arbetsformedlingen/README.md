
# Arbetsförmedlingen

## Setup: 

1. Download the dataset from https://jobtechdev.se/docs/apis/historical/
2. Unzip into /downloads/
3. Kör `python preprocessing.py` för att lägga in all entries i samma csv-fil (af_prepro.csv). Detta är viktigt för att vi ska kunna använda dask senare.


### INFO

JobTechDev (https://jobtechdev.se/) har massor med information, apier och data för att ananlysera den svenska jobb-marknaden. 

Historiska jobb går att hitta på https://jobtechdev.se/docs/apis/historical/, samt att ladda ner från https://simonbe.blob.core.windows.net/afhistorik/pb2006_2019.zip


De har även repos här: https://github.com/jobtechswe

