import sys

sys.path.append(".")

import random
import numpy as np
import pandas as pd

from labirintusok import maze_for_demoing

import streamlit as st

st.sidebar.header("Choosing the parameters")

maze_width = st.sidebar.slider(
    'Select maze width',
    4, 100,
    value=[64]
)[0]



maze_height = st.sidebar.slider(
    'Select maze height',
    4, 80,
    value = [48]
)[0]

maze_wall = st.sidebar.slider(
    'Select maze wall width',
    10, 60,
    value=[40]
)[0]

line_width = st.sidebar.slider(
    'Select line width',
    4, 20,
    value=[16]
)[0]
dot_radius = st.sidebar.slider(
    'Select dot radius',
    6, 30,
    value=[20]
)[0]

maze_version = st.sidebar.slider(
    'Select maze version (0-3)',
    0, 3,
    value=[0]
)[0]

show_version = st.sidebar.slider(
    'Select display version (0-2)',
    0, 2,
    value=[0]
)[0]

wall_version: int = 0
wall_version = st.sidebar.slider(
    'Select maze with wall (0) or no wall (1)',
    0, 1,
    value=[0]
)[0]
color = st.sidebar.slider(
    'Select maze color (0-255)',
    0, 255,
    value=[192]
)[0]

seed = st.sidebar.slider(
    'Select seed',
    0, 100,
    value=[23]
)[0]

random.seed(seed)
np.random.seed(seed)

params = maze_for_demoing.Params(
    width=maze_width,
    height=maze_height,
    wall=maze_wall,
    line_width=line_width,
    radius=dot_radius,
    maze_version=maze_version,
    show_version=show_version,
    wall_version=wall_version,
    color=color,
    random_seed=seed
)

df = pd.Series(params.__dict__)

st.sidebar.header("Chosen parameters:")
st.sidebar.table(df.to_frame())

if st.button("Generate"):
    image = maze_for_demoing.generate_maze(params)

    st.header("Your maze")
    st.image(image)

    pressed = st.button("Save maze")

