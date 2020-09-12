# Libraries needed for the tutorial

import pandas as pd
import requests
import io
    
# Downloading the csv file from your GitHub account
## NEEDS TO BE RAW LINK OR IT WILL NOT WORK
url = "https://raw.githubusercontent.com/slu-openGIS/MO_HEALTH_Covid_Tracking/master/data/zip/zip_stl_county.csv?_sm_au_=iTV0t3Dkn0R3M7DNHftsvK0JJcR7F" # Make sure the url is the raw version of the file on GitHub
download = requests.get(url).content

# Reading the downloaded content and turning it into a pandas dataframe

df = pd.read_csv(io.StringIO(download.decode('utf-8')))

# Printing out the first 5 rows of the dataframe

print (df.head())