import streamlit as st
import pickle
import requests
import numpy as np

# Load the API data
api_data = requests.get("https://thronesapi.com/api/v2/Characters").json()

# Load the best z data with characters and their t-SNE coordinates
df = pickle.load(open('combined_character_tsne.pkl', 'rb'))

# Modify the DataFrame as needed
df['character'] = df['character'].str.replace('Jaime', 'Jamie')
df['character'] = df['character'].str.replace('Lord Varys', 'Varys')
df['character'] = df['character'].str.replace('Bronn', 'Lord Bronn')
df['character'] = df['character'].str.replace('Sandor Clegane', 'The Hound')
df['character'] = df['character'].str.replace('Robb Stark', 'Rob Stark')

# Function to fetch the image URL for a character
def fetch_image(name, api_data):
    for item in api_data:
        if item['fullName'] == name:
            return item['imageUrl']
    return None  # Return None if no image is found

# Add custom CSS for the full background image
st.markdown("""
    <style>
    body {
        background-image: url('https://example.com/path-to-your-game-of-thrones-image.jpg');  /* Replace with actual image URL */
        background-size: cover; /* Cover the entire screen */
        background-repeat: no-repeat; /* Prevent the image from repeating */
        background-attachment: fixed; /* Keep the background fixed during scrolling */
        color: white; /* Change text color for better visibility on dark backgrounds */
    }
    .title {
        font-family: 'Dancing Script', cursive;
        font-size: 48px; /* Adjust the size as needed */
        text-align: center;
        margin: 20px 0; /* Space above and below the title */
    }
    </style>
""", unsafe_allow_html=True)

# Streamlit title with custom styling
st.markdown('<div class="title">Game Of Thrones Personality Matcher</div>', unsafe_allow_html=True)

# Character selection
characters = df['character'].values
selected_character = st.selectbox("Select a character", characters)

# Fetch closest match
character_id = np.where(df['character'].values == selected_character)[0][0]
x = df[['x', 'y']].values

# Calculate distances and find the recommended character
distances = [np.linalg.norm(x[character_id] - x[i]) for i in range(len(x))]
recommended_id = sorted(list(enumerate(distances)), key=lambda x: x[1])[1][0]
recommended_character = df['character'].values[recommended_id]

# Fetch images for selected and recommended characters
image_url = fetch_image(selected_character, api_data)
recommended_character_image_url = fetch_image(recommended_character, api_data)

# Use columns for layout
col1, col2 = st.columns(2)

with col1:
    st.header(selected_character)
    if image_url:
        st.image(image_url)
    else:
        st.write(f"Image not found for {selected_character}")

with col2:
    st.header(recommended_character)
    if recommended_character_image_url:
        st.image(recommended_character_image_url)
    else:
        st.write(f"Image not found for {recommended_character}")
