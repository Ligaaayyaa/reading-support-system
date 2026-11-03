
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Reading Support System",
    page_icon="📚",
    layout="wide"
)

# Main title
st.title("📚 Reading Support System")

st.write(
    "A Machine Learning-Based Reading Performance "
    "Classification and Personalized Reading Support System"
)

st.divider()

# Sidebar navigation
st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select a page:",
    ["Home", "Student Dashboard", "Teacher Dashboard", "Reading Support"]
)

# Home page
if page == "Home":
    st.header("Welcome!")

    st.write(
        "This platform aims to support Grade 10 and Grade 11 "
        "students in understanding their English reading performance."
    )

    st.info("Select a page from the navigation menu.")

# Student dashboard
elif page == "Student Dashboard":
    st.header("Student Dashboard")

    st.write("Welcome, Student!")

    st.metric("Reading Performance", "Not yet assessed")

    st.info("Your reading assessment results will appear here.")

# Teacher dashboard
elif page == "Teacher Dashboard":
    st.header("Teacher Dashboard")

    st.write("Welcome, Teacher!")

    st.info("Student records and reading performance summaries will appear here.")

# Reading support
elif page == "Reading Support":
    st.header("Reading Support Activities")

    st.write("Explore these sample reading activities:")

    st.subheader("1. Reading Comprehension")
    st.write("Read a short passage and answer questions about it.")

    st.subheader("2. Vocabulary Development")
    st.write("Practice understanding unfamiliar English words.")

    st.subheader("3. Critical Reading")
    st.write("Identify the main idea and supporting details of a text.")
