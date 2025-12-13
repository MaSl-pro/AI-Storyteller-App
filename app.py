import streamlit as st
import json
import os

st.title("🎭 AI Storyteller")
with st.sidebar:
    st.header("Story Settings")
    genre = st.selectbox("Genre", ["Fantasy", "Horror", "Mystery","Crime"])
    tone = st.slider("Level", 1, 5)
    with st.expander("⚙️ Advanced Settings"):
        with st.expander("🎨 Choose Theme"):
            st.write("Select a theme")
        with st.expander("🎨 Create Custom Theme"):
            theme_name = st.text_input("Theme Name")
            primary_color = st.color_picker("Primary Color", "#FF4B4B")
            bg_color = st.color_picker("Background", "#0E1117")
            text_color = st.color_picker("Text Color", "#FAFAFA")
            
            if st.button("Save Theme"):
                custom_theme = {
                    "name": theme_name,
                    "primaryColor": primary_color,
                    "backgroundColor": bg_color,
                    "textColor": text_color
                }

tab1, tab2, tab3 = st.tabs(["Generate Story", "Generate Characters", "Generate World"])

with tab1:
    prompt = st.text_area("Describe your story idea...")
    if st.button("Generate"):
        st.write("Story appears here!")

with tab2:
    st.write("Character creator here")
    
    # Load character from file
    def load_character(filename):
        with open(f'data/characters/{filename}', 'r') as f:
            return json.load(f)
        
    # Save character to file
    def save_character(character, filename):
        os.makedirs('data/characters', exist_ok=True)
        with open(f'data/characters/{filename}', 'w') as f:
            json.dump(character, f, indent=2)

    character = {
        "name": st.text_input("Character Name"),
        "age": st.number_input("Age", min_value=0),
        "backstory": st.text_area("Backstory")
    }

    if st.button("Save Character"):
        save_character(character, f"{character['name']}.json")
        st.success("Character saved!")
        st.balloons()

with tab3:
    st.write("World Building you like")
