import sys

sys.path.append(".")

import random
import numpy as np
import pandas as pd

from randfa import randline_for_demoing

import streamlit as st

st.sidebar.header("Choosing the parameters")

min_step = st.sidebar.slider(
    'Select min_step step (* pi)',
    0.01, 10.6,
    value=[2.81]
)[0] * np.pi

ray = st.sidebar.slider(
    'Select initial length',
    10, 70,
    value=[40]
)[0]

number_of_rays = st.sidebar.slider(
    'Select number of rays',
    4, 40,
    value=[20]
)[0]

generation = st.sidebar.slider(
    'Select generation',
    3, 30,
    value=[10]
)[0]

seed = st.sidebar.slider(
    'Select seed',
    0, 100,
    value=[23]
)[0]

random.seed(seed)
np.random.seed(seed)



params = randline_for_demoing.Params(
    min_step=min_step,
    ray=ray,
    number_of_rays = number_of_rays,
    generation=generation,
    seed=seed
)

df = pd.Series(params.__dict__)

st.sidebar.header("Chosen parameters:")
st.sidebar.table(df.to_frame())

image = randline_for_demoing.generate_lines(params)

st.header("Your rand_lines")
st.image(image)

pressed = st.button("Save tree")
