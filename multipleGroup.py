import pandas as pd
import plotly.graph_objects as go


df=pd.read_csv("data.csv")
print(df.groupby(["student_id","level"])["attempt"].mean())


fig=go.Figure(go.Bar(
    x=df.groupby(["student_id","level"])["attempt"].mean(),
    y=df.groupby(["student_id","level"])["attempt"].mean(),
    orientation="h",
))

fig.show()