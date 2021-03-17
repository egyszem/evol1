import sys

sys.path.append(".")

import random
import numpy as np
import pandas as pd

from randfa import line_for_demoing
import streamlit as st

st.sidebar.header("Choosing the parameters")

mm = st.sidebar.slider(
    'Select number of lines',
    1, 1000,
    value=[10]
)[0]

route = st.sidebar.slider(
    'Select route length',
    30, 300,
    value = [100]
)[0]

order = st.sidebar.slider(
    'Select order',
    1, 3,
    value=[1]
)[0]

seed = st.sidebar.slider(
    'Select random seed',
    0, 100,
    value=[23]
)[0]

random.seed(seed)
np.random.seed(seed)


params = line_for_demoing.Params(
    number_of_lines=mm,
    route=route,
    order=order,
    random_seed=seed
)

df = pd.Series(params.__dict__)

st.sidebar.header("Chosen parameters:")
st.sidebar.table(df.to_frame())

image = line_for_demoing.generate_lines(params)

st.header("Your lines")
st.image(image)

pressed = st.button("Save lines")

