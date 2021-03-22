import pandas as pd
import numpy as np
from scipy import stats

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.figure_factory as ff
import plotly.express as px
import plotly.graph_objects as go
import altair as alt

import streamlit as st

def nhanes_multivariate_analysis(df):
  st.write(""" 
  ### Quantitative bivariate data

  Bivariate data arise when every "unit of analysis" (e.g. a person in the NHANES dataset) is assessed with respect to two traits (the NHANES subjects were assessed for many more than two traits, but we can consider two traits at a time here).
  
  Below we make a scatterplot of arm length against leg length.  This means that arm length ([BMXARML](https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/BMX_I.htm#BMXARML)) is plotted on the vertical axis and leg length ([BMXLEG](https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/BMX_I.htm#BMXLEG)) is plotted on the horizontal axis).  We see a positive dependence between the two measures -- people with longer arms tend to have longer legs, and vice-versa.  However it is far from a perfect relationship.
  """)

  df["RIAGENDRx"] = df.RIAGENDR.replace({1: "Male", 2: "Female"}) 
  fig = px.scatter(df, x="BMXLEG", y="BMXARML", color="RIAGENDRx", opacity=0.5, title="Correlation arm length against leg length")
  st.plotly_chart(fig)

  st.write(""" 
  This plot also shows the Pearson correlation coefficient between the arm length and leg length, which is 0.62. The Pearson correlation coefficient ranges from -1 to 1, with values approaching 1 indicating a more perfect positive dependence.  In many settings, a correlation of 0.62 would be considered a moderately strong positive dependence. 
  """)

  fig = px.density_contour(df, x="BMXLEG", y="BMXARML", title="Contour correlation between arm length and leg length")
  fig.add_annotation(x=50, y=45, text="p=0.62", font=dict(color="white",size=12), showarrow=False)
  fig.update_traces(contours_coloring="fill", contours_showlabels = True)
  st.plotly_chart(fig)

  st.write(""" 
  As another example with slightly different behavior, we see that systolic and diastolic blood pressure (essentially the maximum and minimum blood pressure between two consecutive heart beats) are more weakly correlated than arm and leg length, with a correlation coefficient of 0.32. This weaker correlation indicates that some people have unusually high systolic blood pressure but have average diastolic blood pressure, and vice versa.
  """)
  fig = px.density_contour(df, x="BPXSY1", y="BPXDI1", marginal_x="rug", marginal_y="rug", title="BPXSY1 and BPXDI1 correlation")
  fig.add_annotation(x=200, y=100, text="p=0.32",font=dict(size=15, color="black"), showarrow=False)
  st.plotly_chart(fig)

  st.write("""
  Next we look at two repeated measures of systolic blood pressure, taken a few minutes apart on the same person. These values are very highly correlated, with a correlation coefficient of around 0.96.
  """)
  x = df["BPXSY1"].to_numpy()
  y = df["BPXSY2"].to_numpy()
  fig = go.Figure(go.Histogram2dContour(
        x = x,
        y = y,
        colorscale = 'Jet',
        contours = dict(
            showlabels = True,
            labelfont = dict(
                family = 'Raleway',
                color = 'white'
            )
        ),
        hoverlabel = dict(
            bgcolor = 'white',
            bordercolor = 'black',
            font = dict(
                family = 'Raleway',
                color = 'black'
            )
        )
  ))

  fig.update_layout(title_text="BPXSY1 and BPXSY2 correlation",)
  fig.add_annotation(x=200, y=200, text="p=0.96",font=dict(size=15, color="white"), showarrow=False)
  st.plotly_chart(fig)

  st.write(""" 
  ### Heterogeneity and stratification

  Most human characteristics are complex -- they vary by gender, age, ethnicity, and other factors.  This type of variation is often referred to as "heterogeneity".  When such heterogeneity is present, it is usually productive to explore the data more deeply by stratifying on relevant factors, as we did in the univariate analyses.  

  Below, we continue to probe the relationship between leg length and arm length, stratifying first by gender, then by gender and ethnicity. The gender-stratified plot indicates that men tend to have somewhat longer arms and legs than women -- this is reflected in the fact that the cloud of points on the left is shifted slightly up and to the right relative to the cloud of points on the right.  In addition, the correlation between arm length and leg length appears to be somewhat weaker in women than in men.
  """)

  fig_fem = px.scatter(df, x="BMXLEG", y="BMXARML", facet_row="RIAGENDRx")
  st.plotly_chart(fig_fem, use_container_width=True)

  st.write(""" 
  Next we look to stratifying the data by both gender and ethnicity.  This results in 2 x 5 = 10 total strata, since there are 2 gender strata and 5 ethnicity strata. These scatterplots reveal differences in the means as well a diffrences in the degree of association (correlation) between different pairs of variables.  We see that although some ethnic groups tend to have longer/shorter arms and legs than others, the relationship between arm length and leg length within genders is roughly similar across the ethnic groups.  

  One notable observation is that ethnic group 5, which consists of people who report being multi-racial or are of any race not treated as a separate group (due to small sample size), the correlation between arm length and leg length is stronger, especially for men.  This is not surprising, as greater heterogeneity can allow correlations to emerge that are indiscernible in more homogeneous data.   
  """)

  fig = px.density_contour(df, x="BMXLEG", y="BMXARML", facet_col="RIDRETH1", facet_row="RIAGENDRx")
  fig.update_traces(contours_coloring="fill", contours_showlabels = True)
  st.plotly_chart(fig)