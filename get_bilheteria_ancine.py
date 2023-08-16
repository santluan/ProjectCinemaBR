# Author: Luan Santos
# Date: 16-08-2023

import os
import wget
import zipfile as zip
import pandas as pd
import glob

# set directory to download
os.chdir('C:/...')

# download Zipfile
url = 'https://dados.ancine.gov.br/dados-abertos/BilheteriaObrasDia.zip'
response = wget.download(url=url)

# unzip files
zipfile = 'BilheretiaObrasDia.zip'
with zip.ZipFile(zipfile, 'r') as zObject:
    zObject.extractall(path=os.getcwd)

# read all files and save into dataframe
csv_files = glob.glob('*.csv')
df_list = (pd.read_csv(file, sep=';') for file in csv_files)
df = pd.concat(df_list, ignore_index=True)

# save csv
df.to_csv('BilheteriaObrasDia_2014_2023.csv', index=False)