import streamlit as st
import random
import math
import numpy as np
import matplotlib.pyplot as plt

# --- App title ---
st.title("🎨 Generative Abstract Poster")

# --- Button ---
if st.button("Generate New Poster"):
    # Set up plot
    random.seed()
    plt.figure(figsize=(7,10))
    plt.axis('off')
    plt.gca().set_facecolor((0.98,0.98,0.97))

    # Color palette
    def random_palette(k=5):
        return [(random.random(), random.random(), random.random()) for _ in range(k)]

    def blob(center=(0.5, 0.5), r=0.3, points=200, wobble=0.5):
        angles = np.linspace(0, 2*math.pi, points)
        radii = r * (0.5 + wobble*(np.random.rand(points)-0.5))
        x = center[0] + radii * np.cos(angles)
        y = center[1] + radii * np.sin(angles)
        return x, y

    palette = random_palette(6)
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
    st.write("👆 Click the button to generate your poster!")
