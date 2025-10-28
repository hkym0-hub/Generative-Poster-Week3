import streamlit as st
import random
import math
import numpy as np
import matplotlib.pyplot as plt

# --- App title ---
st.title("🎨 Generative Abstract Poster")

# --- Palette options ---
palette_option = st.selectbox(
    "🎨 Choose a Color Palette",
    ["Random", "Pastel", "Vibrant", "Earthy", "Cool Blues", "Warm Sunset"]
)

# --- Define palette generator ---
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

# --- Blob generator ---
def blob(center=(0.5, 0.5), r=0.3, points=200, wobble=0.5):
    angles = np.linspace(0, 2*math.pi, points)
    radii = r * (0.5 + wobble*(np.random.rand(points)-0.5))
    x = center[0] + radii * np.cos(angles)
    y = center[1] + radii * np.sin(angles)
    return x, y

# --- Button ---
if st.button("✨ Generate New Poster"):
    random.seed()
    plt.figure(figsize=(7,10))
    plt.axis('off')
    plt.gca().set_facecolor((0.98,0.98,0.97))

    palette = get_palette(palette_option)
    n_layers = 12
    for i in range(n_layers):
        cx, cy = random.random(), random.random()
        rr = random.uniform(0.15, 0.45)
        x, y = blob(center=(cx, cy), r=rr, wobble=random.uniform(0.05,0.25))
        color = random.choice(palette)
        alpha = random.uniform(0.25, 0.6)
        plt.fill(x, y, color=color, alpha=alpha, edgecolor=(0,0,0,0))

    plt.text(0.05, 0.95, "Generative Poster", fontsize=18, weight='bold', transform=plt.gca().transAxes)
    plt.text(0.05, 0.91, "Week 2 • Arts & Advanced Big Data", fontsize=11, transform=plt.gca().transAxes)

    plt.xlim(0,1); plt.ylim(0,1)
    st.pyplot(plt)
else:
    st.write("👆 Choose a palette and click the button to generate your poster!")

