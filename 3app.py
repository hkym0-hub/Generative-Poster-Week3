# app.py
# Generative Abstract Poster
# Concepts: randomness, lists, loops, functions, matplotlib

import random
import math
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# --- Streamlit UI ---
st.set_page_config(page_title="Generative Abstract Poster", layout="centered")

st.title("🎨 Generative Abstract Poster")
st.caption("Week 2 • Arts & Advanced Big Data")

# --- Sidebar Controls ---
st.sidebar.header("🎛️ Controls")

n_layers = st.sidebar.slider("Number of Layers", 3, 20, 8)
random_seed = st.sidebar.number_input("Random Seed (for reproducibility)", value=0, step=1)

palette_option = st.sidebar.selectbox(
    "🎨 Color Palette",
    ["Random", "Pastel", "Vibrant", "Earthy", "Cool Blues", "Warm Sunset"]
)

wobble_min = st.sidebar.slider("Minimum Wobble", 0.0, 0.5, 0.05, 0.01)
wobble_max = st.sidebar.slider("Maximum Wobble", 0.0, 0.5, 0.25, 0.01)
radius_min = st.sidebar.slider("Minimum Radius", 0.05, 0.5, 0.15, 0.01)
radius_max = st.sidebar.slider("Maximum Radius", 0.05, 0.5, 0.45, 0.01)

generate = st.sidebar.button("🎲 Generate Poster")

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
    angles = np.linspace(0, 2 * math.pi, points)
    radii = r * (1 + wobble * (np.random.rand(points) - 0.5))
    x = center[0] + radii * np.cos(angles)
    y = center[1] + radii * np.sin(angles)
    return x, y

# --- Generate artwork ---
if generate or random_seed >= 0:
    random.seed(random_seed)
    plt.figure(figsize=(7,10))

    # Turn off axes completely
    ax = plt.gca()
    ax.set_facecolor((0.98, 0.98, 0.97))
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_frame_on(False)

    palette = get_palette(palette_option, k=6)

    for i in range(n_layers):
        cx, cy = random.random(), random.random()
        rr = random.uniform(radius_min, radius_max)
        x, y = blob(center=(cx, cy), r=rr, wobble=random.uniform(wobble_min, wobble_max))
        color = random.choice(palette)
        alpha = random.uniform(0.25, 0.6)
        plt.fill(x, y, color=color, alpha=alpha, edgecolor=(0, 0, 0, 0))

    # text labels
    plt.text(0.05, 0.95, "Generative Poster", fontsize=18, weight='bold', transform=ax.transAxes)
    plt.text(0.05, 0.91, "Week 2 • Arts & Advanced Big Data", fontsize=11, transform=ax.transAxes)

    plt.xlim(0,1)
    plt.ylim(0,1)

    st.pyplot(plt)
