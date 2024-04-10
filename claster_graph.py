import plotly.graph_objects as go
import pandas as pd


df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/hobbs-pearson-trials.csv")

fig = go.Figure()

fig.add_trace(go.Scatterpolargl(
      r = df.trial_1_r,
      theta = df.trial_1_theta,
      name = "Trial 1",
      marker=dict(size=15, color="mediumseagreen")
    ))
fig.add_trace(go.Scatterpolargl(
      r = df.trial_2_r,
      theta = df.trial_2_theta,
      name = "Trial 2",
      marker=dict(size=20, color="darkorange")
    ))
fig.add_trace(go.Scatterpolargl(
      r = df.trial_3_r,
      theta = df.trial_3_theta,
      name = "Trial 3",
      marker=dict(size=12, color="mediumpurple")
    ))
fig.add_trace(go.Scatterpolargl(
      r = df.trial_4_r,
      theta = df.trial_4_theta,
      name = "Trial 4",
      marker=dict(size=22, color = "magenta")
    ))
fig.add_trace(go.Scatterpolargl(
      r = df.trial_5_r,
      theta = df.trial_5_theta,
      name = "Trial 5",
      marker=dict(size=19, color = "limegreen")
      ))
fig.add_trace(go.Scatterpolargl(
      r = df.trial_6_r,
      theta = df.trial_6_theta,
      name = "Trial 6",
      marker=dict(size=10, color = "gold")
      ))

# Common parameters for all traces
fig.update_traces(mode="markers", marker=dict(line_color='white', opacity=0.7))

fig.update_layout(
    title = "Hobbs-Pearson Trials",
    font_size = 15,
    showlegend = False,
    polar = dict(
      bgcolor = "rgb(223, 223, 223)",
      angularaxis = dict(
        linewidth = 3,
        showline=True,
        linecolor='black'
      ),
      radialaxis = dict(
        side = "counterclockwise",
        showline = True,
        linewidth = 2,
        gridcolor = "white",
        gridwidth = 2,
      )
    ),
    paper_bgcolor = "rgb(223, 223, 223)"
)

fig.show()