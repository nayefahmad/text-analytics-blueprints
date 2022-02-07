# # Analyzing the UN General Assembly Debates data
#
#

# ## Imports
import pandas as pd
from pathlib import Path

import sys

sys.path.extend(["C:/Nayef/text-analytics-blueprints"])

# ## Loading data
dir = Path("C:/Nayef/text-analytics-blueprints/data")
file = "un-general-debates.csv"
df_un_debates = pd.read_csv(dir.joinpath(file))

df_un_debates.head(5)
df_un_debates.sample(5)

df_un_debates.columns
df_un_debates.dtypes
df_un_debates.info()
df_un_debates.describe().T
# df_un_debates.describe(include=['0'])  # todo: include='0' should let us include categorical data  # noqa
