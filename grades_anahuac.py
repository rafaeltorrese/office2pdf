import os

import numpy as np
import pandas as pd

from data import filepath, files


path_files = os.path.join(*filepath, files[0])


df_list = []

for file in files:
    df = pd.read_excel(os.path.join(*filepath, file))
    df_list.append(df)

grades = pd.concat(df_list)

print(grades)

