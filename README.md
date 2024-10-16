# Game-of-Thrones-Personality-Matcher
This project is a web-based application built with Streamlit that allows users to select their favorite character from the Game of Thrones series and receive a recommended character that closely matches their personality based on t-SNE clustering. The clustering is derived from analyzing the characters' dialogues, identifying shared patterns and similarities between their spoken words. By comparing how similar characters express themselves, the app provides an engaging experience where users can explore character connections in a unique way.




![App Screenshot](Screenshot%202024-10-16%20171527.png)

# Features
* Select a Game of Thrones character from a dropdown.
* Get a personality-based character recommendation.
* View images of both the selected and recommended characters using the Thrones API.

#  How It Works
The project uses t-SNE (t-distributed Stochastic Neighbor Embedding) to visualize character personalities in a 2D space. The distances between these characters are used to recommend a similar personality match based on the selected character.

## Thrones API Integration
The Thrones API (https://thronesapi.com/api/v2/Characters) is used to fetch the character images, adding a visual element to the recommendations.

# Acknowledgements
* Streamlit for the web framework.
* Thrones API for providing Game of Thrones character data.
* Game of Thrones fans for inspiration!

