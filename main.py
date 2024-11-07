import pandas as pd
import sys
from diy_tokenize import diy_tokenize
from data import Dictionary, InvertedIndex
from os import listdir
from os.path import isfile, join


cisi_files = [f for f in listdir("cisi_txt") if isfile(join("cisi_txt", f))]

init_data=pd.DataFrame({"Term": [],"Doc_ID": []})

print("tokenizing and concatenating...")
for f in cisi_files:
    id = int(f.split('.')[0])
    words = diy_tokenize("cisi_txt/"+ f)
    df=pd.DataFrame({"Term": words,"Doc_ID": ([id] * (len(words)))})
    init_data=pd.concat([init_data,df], ignore_index=True)


print("sorting..")
init_data.sort_values(['Term','Doc_ID'], inplace=True)
print("adding Freq...")
init_data['Frequency'] = ([1] * init_data.shape[0])
print("Groupby...")
init_data = init_data.groupby(['Term','Doc_ID'], as_index=False)['Frequency'].sum()
print("Building Dictionary...")
new_dict = Dictionary(init_data)
print("Building InvertedIndex...")
new_index = InvertedIndex(init_data)

