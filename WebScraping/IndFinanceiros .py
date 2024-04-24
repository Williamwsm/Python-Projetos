from io import StringIO
from IPython.display import display
import pandas as pd
import requests

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36' }
url = 'https://br.investing.com/equities/brazil'

request = requests.get(url, headers= header)

html_file = StringIO(request.text)
df= pd.read_html( html_file)

df = pd.DataFrame(df[0])
df['Último'] = df['Último']/100
df['Máxima'] = df['Máxima']/100
df['Mínima'] = df['Mínima']/100
display(df)
