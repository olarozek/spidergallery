# 🕸️ SpiderGallery — Streamlit Prototype
# Author: [Your Name]
# Description: First working prototype of the SpiderGallery AI tool

import streamlit as st
import pandas as pd
import random

# -----------------------------
# Mock data — gallery database
# -----------------------------
galleries = pd.DataFrame([
    {"name": "Urban Frame Gallery", "city": "Berlin", "style_focus": "contemporary", "description": "Focuses on abstract and modern works."},
    {"name": "Luna Fine Arts", "city": "Paris", "style_focus": "impressionism", "description": "Features impressionist painters and light studies."},
    {"name": "Studio Nova", "city": "New York", "style_focus": "digital", "description": "Specializes in digital art and mixed media."},
    {"name": "Echo Gallery", "city": "London", "style_focus": "minimalism", "description": "Curates minimalist and conceptual artists."},
    {"name": "Terra Forma", "city": "Lisbon", "style_focus": "nature-inspired", "description": "Highlights eco-conscious and organic themes."},
])

# -----------------------------
# Streamlit App UI
# -----------------------------
st.set_page_config(page_title="SpiderGallery", page_icon="🕸️", layout="centered")

st.title("🕸️ SpiderGallery")
st.subheader("Connecting Artists and Galleries Through AI")

st.write("Welcome to **SpiderGallery**, an experimental AI-driven tool that helps artists find galleries aligned with their creative style and location. This is an early prototype showing how the system will work.")

# Sidebar: Artist input
st.sidebar.header("🎨 Artist Profile")

artist_name = st.sidebar.text_input("Your Name", placeholder="e.g. Alex Rivera")
artist_style = st.sidebar.selectbox(
    "Artistic Style",
    ["Select...", "contemporary", "digital", "impressionism", "minimalism", "nature-inspired", "abstract", "other"]
)
artist_location = st.sidebar.text_input("Your City", placeholder="e.g. Berlin")

st.sidebar.markdown("---")
st.sidebar.info("🧠 Future versions will analyze your art style and use AI to find even deeper connections.")

# -----------------------------
# Matching Logic (basic mockup)
# -----------------------------
def match_galleries(style, city):
    """Return mock AI-matched galleries"""
    if style == "Select...":
        return []
    
    matched = galleries[galleries["style_focus"].str.contains(style, case=False, na=False)]
    
    if matched.empty:
        # fallback: random 2 galleries
        matched = galleries.sample(2)
    
    # Bonus: prioritize same city (mock weighting)
    matched["match_score"] = matched.apply(
        lambda x: random.uniform(0.7, 1.0) if x["city"].lower() == city.lower() else random.uniform(0.4, 0.8),
        axis=1
    )
    return matched.sort_values("match_score", ascending=False)

# -----------------------------
# Main Content
# -----------------------------
if st.button("✨ Find Matching Galleries"):
    if not artist_name or artist_style == "Select...":
        st.warning("Please enter your name and select an artistic style.")
    else:
        st.success(f"Searching for galleries that match **{artist_style}** art near **{artist_location or 'your area'}**...")
        
        results = match_galleries(artist_style, artist_location)
        
        if not results.empty:
            st.markdown("### 🖼️ Recommended Galleries")
            for _, row in results.iterrows():
                st.markdown(f"""
                **{row['name']}** — *{row['city']}*  
                *Focus:* {row['style_focus']}  
                _{row['description']}_  
                **Match Score:** {row['match_score']:.2f}  
                ---
                """)
        else:
            st.info("No perfect matches found — try another style or location.")

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.caption("🕸️ SpiderGallery © 2025 — Created by [Your Name]. Exploring the intersection of art and AI.")
