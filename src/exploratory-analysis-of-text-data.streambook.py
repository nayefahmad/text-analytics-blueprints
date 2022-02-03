import streamlit as __st
import streambook

__toc = streambook.TOCSidebar()


__toc.generate()
with __st.echo(), streambook.st_stdout("info"):
    import matplotlib.pyplot as plt
    import seaborn as sns
with __st.echo(), streambook.st_stdout("info"):
    tips = sns.load_dataset("tips")
    sns.lmplot(x="total_bill", y="tip", hue="smoker", data=tips)
    plt.show()
