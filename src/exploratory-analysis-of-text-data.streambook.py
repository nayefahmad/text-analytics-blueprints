import streamlit as __st
import streambook

__toc = streambook.TOCSidebar()
__toc._add(streambook.H1("Analyzing the UN General Assembly Debates data"))

__toc.generate()
__st.markdown(
    r"""<span id='Analyzing the UN General Assembly Debates data'> </span>
# Analyzing the UN General Assembly Debates data

""",
    unsafe_allow_html=True,
)
with __st.echo(), streambook.st_stdout("info"):
    # ## Imports
    import pandas as pd
    from pathlib import Path
with __st.echo(), streambook.st_stdout("info"):
    import sys

    sys.path.extend(["C:/Nayef/text-analytics-blueprints"])
with __st.echo(), streambook.st_stdout("info"):
    # ## Loading data
    dir = Path("C:/Nayef/text-analytics-blueprints/data")
    file = "un-general-debates.csv"
    df_un_debates = pd.read_csv(dir.joinpath(file))
with __st.echo(), streambook.st_stdout("info"):
    df_un_debates.head(5)
    df_un_debates.sample(5)
with __st.echo(), streambook.st_stdout("info"):
    df_un_debates.columns
    df_un_debates.dtypes
    df_un_debates.info()
    df_un_debates.describe().T
    # df_un_debates.describe(include=['0'])  # todo: include='0' should let us include categorical data  # noqa
