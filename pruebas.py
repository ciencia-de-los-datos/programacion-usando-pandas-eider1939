import pandas as pd
from datetime import datetime, timedelta

tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
tbl1 = pd.read_csv("tbl1.tsv", sep="\t")
tbl2 = pd.read_csv("tbl2.tsv", sep="\t")
tbl0['año']=tbl0['_c3'].map(lambda x: x.split('-')[0])
print(tbl0)
print(type(tbl0))