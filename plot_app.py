import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.title('Plot Funny Shapes!!')

st.write("Draw a flower!")

alpha = np.linspace(0, 2 * np.pi, 1000)


def flower(n):
    r = np.cos(n * alpha) + 1
    x = r * np.cos(alpha)
    y = r * np.sin(alpha)

    fig, ax = plt.subplots()
    ax.plot(y, x)
    return fig


df = pd.DataFrame({
    'nPetals': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
})

option = st.selectbox(
    'How many petals do you want?',
    df['nPetals'],
    index=5)

st.pyplot(flower(option))
