# CIS 211 Lab 4 starter
# Build a fictional campus club or service information page.
# Read CIS_211_Lab4_Guide.pdf before editing this file.
# This starter runs, but its TODO sections are not a completed submission.

import streamlit as st


# TODO 1: Replace these values with your own fictional club or service details.
# Keep at least three key-value pairs. You may add more.
club_info = {
    "name": "Creative Minds Club",
    "day": "wednesday ",
    "time": "3:00 PM - 4:30 PM",
}

# TODO 2: Replace these sample strings with at least three relevant activities.
# During the list change check, add one new item and keep it in the final app.
activities = [
    "Arts and crafts workshops",
    "Group brainstorming sessions",
    "Creative writing activities",
]

st.title(club_info["name"])
st.caption("A fictional CIS 211 course project. These are not real campus arrangements.")

# Remove this starter message when your page is complete.
st.write("Starter page: complete the TODO sections using the Lab 4 guide.")

st.header("Welcome to the **Creative Minds Club**, a place where students can
share ideas, express themselves, and develop new skills.
Our goal is to create a fun and supportive environment where
*creativity and teamwork* come together.")
# TODO 3: Use st.markdown() to write your own two- or three-sentence introduction.
# Include both **bold** and *italic* text inside your Python string.
# The handout explains triple quotes if your Markdown spans several lines.

st.header( st.write("- " + activity)
)
# TODO 4: Write a for loop that displays every value from activities.
# Use Streamlit output inside the loop. Do not type each activity again.

st.header("Details")
st.write("**Meeting Day:**", club_info["day"])
st.write("**Meeting Time:**", club_info["time"])
st.write("**Location:**", club_info["location"])
# TODO 5: Display at least two dictionary values by looking them up by key.
# Give the displayed values meaningful labels such as Day and Time.

st.header("Prepare for a visit")
# TODO 6: Use st.markdown() to display a three-item Markdown list.
# Add one meaningful, working external Markdown link.
st.markdown("""
- Bring a notebook and something to write with.
- Come ready to share ideas and participate.
- Bring a positive attitude and an open mind.

# TODO 7: Add at least three comments explaining your OWN completed code.
# TODO 8: Perform both change checks and complete the private submission template.
# Upload your final source files, links, reflection, and app screenshots to Brightspace.
