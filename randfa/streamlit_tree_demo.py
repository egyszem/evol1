import sys

sys.path.append(".")

import random
import numpy as np
import pandas as pd

from randfa import tree_for_demoing
import streamlit as st

st.sidebar.header("Choosing the parameters")

seed = st.sidebar.slider(
    'Select seed',
    0, 100,
    value=[23]
)[0]

random.seed(seed)
np.random.seed(seed)

start_length = st.sidebar.slider(
    'Select initial length',
    40, 200,
    value=[100]
)[0]

min_length = st.sidebar.slider(
    'Select minimal length',
    4, 20,
    value = [6]
)[0]

curvature_step = st.sidebar.slider(
    'Select curvature step (* pi)',
    0.01, 0.6,
    value=[0.25]
)[0] * np.pi

branching_probability = st.sidebar.slider(
    'Select branching probability',
    0.05, 0.3,
    value=[0.18]
)[0]

branching_angle = st.sidebar.slider(
    'Select branching angle',
    0.1, 0.6,
    value=[0.45]
)[0] * np.pi

params = tree_for_demoing.Params(
    start_length=start_length,
    min_length=min_length,
    curvature_step=curvature_step,
    branching_probability=branching_probability,
    branching_angle=branching_angle,
    random_seed=seed
)

df = pd.Series(params.__dict__)

st.sidebar.header("Chosen parameters:")
st.sidebar.table(df.to_frame())

image = tree_for_demoing.generate_tree(params)

st.header("Your tree")
st.image(image)

pressed = st.button("Save tree")

