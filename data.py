import pandas as pd
import plotly.graph_objects as go


df=pd.read_csv("data.csv")
print(df.loc[df["student_id"]=="TRL_abc"])

studentData=df.loc[df["student_id"]=="TRL_abc"]
print(studentData.groupby("level")["attempt"].mean())

fig=go.Figure(go.Bar(
    x=studentData.groupby("level")["attempt"].mean(),
    y=["level1","level2","level3","level4"],
    orientation="h",
))
fig.update_layout(title_text="TRL_abc")
fig.show()