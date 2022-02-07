import streamlit as __st
import streambook

__toc = streambook.TOCSidebar()
__toc._add(streambook.H1("Analyzing the UN General Assembly Debates data"))
__toc._add(streambook.H2("Imports"))
__toc._add(streambook.H2("Loading data"))

__toc.generate()
__st.markdown(
    r"""<span id='Analyzing the UN General Assembly Debates data'> </span>
# Analyzing the UN General Assembly Debates data

""",
    unsafe_allow_html=True,
)
__st.markdown(
    r"""<span id='Imports'> </span>
## Imports""",
    unsafe_allow_html=True,
)
with __st.echo(), streambook.st_stdout("info"):
    import pandas as pd
    from pathlib import Path
with __st.echo(), streambook.st_stdout("info"):
    import sys
with __st.echo(), streambook.st_stdout("info"):
    sys.path.extend(["C:/Nayef/text-analytics-blueprints"])
with __st.echo(), streambook.st_stdout("info"):
    from IPython.core.interactiveshell import InteractiveShell

    InteractiveShell.ast_node_interactivity = "all"
__st.markdown(
    r"""<span id='Loading data'> </span>
## Loading data""",
    unsafe_allow_html=True,
)
with __st.echo(), streambook.st_stdout("info"):
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
    df_un_debates.describe(include="all").T  # in book, they use include='0'
