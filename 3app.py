# app.py
import random
import math
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(page_title="Generative Abstract Poster", layout="centered")

st.title("🎨 Generative Abstract Poster")
st.caption("Week 3 • Arts & Advanced Big Data")

# --- Palette Options ---
palette_option = st.selectbox(
    "🎨 Choose a Color Palette",
    ["Random", "Pastel", "Vibrant", "Earthy", "Cool Blues", "Warm Sunset"]
)

# --- Functions ---
def get_palette(option, k=6):
    if option == "Random":
        return [(random.random(), random.random(), random.random()) for _ in range(k)]
    elif option == "Pastel":
        return [(random.uniform(0.6, 1.0), random.uniform(0.6, 1.0), random.uniform(0.6, 1.0)) for _ in range(k)]
    elif option == "Vibrant":
        return [(random.uniform(0.5, 1.0), random.uniform(0.0, 0.8), random.uniform(0.0, 0.8)) for _ in range(k)]
    elif option == "Earthy":
        return [(random.uniform(0.4, 0.7), random.uniform(0.3, 0.6), random.uniform(0.2, 0.4)) for _ in range(k)]
    elif option == "Cool Blues":
        return [(random.uniform(0.2, 0.5), random.uniform(0.4, 0.8), random.uniform(0.7, 1.0)) for _ in range(k)]
    elif option == "Warm Sunset":
        return [(random.uniform(0.8, 1.0), random.uniform(0.3, 0.5), random.uniform(0.2, 0.4)) for _ in range(k)]
    else:
        return [(random.random(), random.random(), random.random()) for _ in range(k)]

def blob(center=(0.5, 0.5), r=0.3, points=200, wobble=0.15):
    angles = np.linspace(0, 2*math.pi, points)
    radii = r * (1 + wobble*(np.random.rand(points)-0.5))
    x = center[0] + radii * np.cos(angles)
    y = center[1] + radii * np.sin(angles)
    return x, y

# --- Parameters ---
n_layers = st.slider("Number of Layers", 3, 20, 8)
random_seed = st.number_input("Random Seed (for reproducibility)", value=0, step=1)
random.seed(random_seed)

# --- Generate art ---
plt.figure(figsize=(7,10))
plt.axis('off')
plt.gca().set_facecolor((0.98,0.98,0.97))

palette = get_palette(palette_option, k=6)

for i in range(n_layers):
    cx, cy = random.random(), random.random()
    rr = random.uniform(0.15, 0.45)
    x, y = blob(center=(cx, cy), r=rr, wobble=random.uniform(0.05,0.25))
    color = random.choice(palette)
    alpha = random.uniform(0.25, 0.6)
    plt.fill(x, y, color=color, alpha=alpha, edgecolor=(0,0,0,0))

st.pyplot(plt)
