
import streamlit as st
import pandas as pd

# ---------------------------------
# PAGE CONFIGURATION
# ---------------------------------

st.set_page_config(
    page_title="Reading Support System",
    page_icon="📚",
    layout="wide"
)

# ---------------------------------
# CUSTOM CSS
# ---------------------------------

st.markdown("""
<style>

/* Main background */
.stApp {
    background-color: #F8F7FA;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #FFFFFF;
    border-right: 1px solid #EAE6EF;
}

/* Sidebar title */
.sidebar-title {
    color: #493078;
    font-size: 21px;
    font-weight: bold;
    padding-bottom: 15px;
}

/* Sidebar navigation buttons */
section[data-testid="stSidebar"] .stButton button {
    width: 100%;
    border-radius: 8px;
    border: none;
    padding: 12px;
    text-align: left;
    font-weight: 600;
}

/* Primary buttons */
.stButton button[kind="primary"] {
    background-color: #493078;
    color: white;
}

/* Secondary buttons */
.stButton button[kind="secondary"] {
    background-color: #F1EDF7;
    color: #493078;
}

/* Dashboard cards */
.dashboard-card {
    background-color: white;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #EAE6EF;
    min-height: 115px;
}

.card-title {
    color: #777777;
    font-size: 14px;
}

.card-value {
    color: #493078;
    font-size: 28px;
    font-weight: bold;
}

/* Section headings */
h1, h2, h3 {
    color: #30204F;
}

/* Divider */
hr {
    border-color: #EAE6EF;
}

</style>
""", unsafe_allow_html=True)


# ---------------------------------
# SAMPLE DATA
# ---------------------------------

student_data = pd.DataFrame({
    "Student ID": ["STU-001", "STU-002", "STU-003", "STU-004", "STU-005"],
    "Student Name": [
        "Student 1",
        "Student 2",
        "Student 3",
        "Student 4",
        "Student 5"
    ],
    "Reading Score": [75, 82, 68, 90, 77],
    "Performance": [
        "Proficient",
        "Proficient",
        "Needs Improvement",
        "Advanced",
        "Proficient"
    ]
})


# ---------------------------------
# SIDEBAR NAVIGATION
# ---------------------------------

pages = {
    "Overview": "🏠  Overview",
    "Student Dashboard": "👨‍🎓  Student Dashboard",
    "Teacher Dashboard": "👩‍🏫  Teacher Dashboard",
    "Reading Assessment": "📝  Reading Assessment",
    "Reading Support": "📖  Reading Support"
}

if "current_page" not in st.session_state:
    st.session_state.current_page = "Overview"

with st.sidebar:

    st.markdown(
        '<p class="sidebar-title">📚 Reading Support System</p>',
        unsafe_allow_html=True
    )

    st.divider()

    for page_name, label in pages.items():

        is_active = st.session_state.current_page == page_name

        if st.button(
            label,
            key=f"nav_{page_name}",
            use_container_width=True,
            type="primary" if is_active else "secondary"
        ):
            st.session_state.current_page = page_name
            st.rerun()

    st.divider()

    st.caption("Reading Support System")
    st.caption("Prototype Version 1.0")


page = st.session_state.current_page


# ---------------------------------
# TOP NAVBAR
# ---------------------------------

st.container()

left, right = st.columns([4, 1], vertical_alignment="center")

with left:
    logo, brand = st.columns([0.5, 5], vertical_alignment="center")

    with logo:
        st.markdown("# 📚")

    with brand:
        st.markdown("### Reading Support System")

with right:
    profile, username = st.columns([1, 3], vertical_alignment="center")

    with profile:
        st.markdown("## 👤")

    with username:
        st.markdown("**Administrator**")

st.divider()


# ---------------------------------
# OVERVIEW PAGE
# ---------------------------------

if page == "Overview":

    st.title("Overview")
    st.write("Welcome to the Reading Support System.")

    st.write(
        "Monitor student reading performance and access "
        "the system's learning support features."
    )

    st.write("")

    # Dashboard cards
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="dashboard-card">
            <div class="card-title">Registered Students</div>
            <div class="card-value">--</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="dashboard-card">
            <div class="card-title">Completed Assessments</div>
            <div class="card-value">--</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="dashboard-card">
            <div class="card-title">Machine Learning Status</div>
            <div class="card-value">Pending</div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.subheader("System Modules")

    module1, module2 = st.columns(2)

    with module1:
        st.info(
            "**Student Dashboard**\n\n"
            "View student reading performance and assessment records."
        )

        st.info(
            "**Reading Assessment**\n\n"
            "Provide reading comprehension assessments for students."
        )

    with module2:
        st.info(
            "**Teacher Dashboard**\n\n"
            "Monitor student assessment results and performance."
        )

        st.info(
            "**Reading Support**\n\n"
            "Provide learning activities based on reading needs."
        )


# ---------------------------------
# STUDENT DASHBOARD
# ---------------------------------

elif page == "Student Dashboard":

    st.title("Student Dashboard")

    st.write(
        "This section displays student reading performance "
        "and assessment information."
    )

    st.subheader("Student Information")

    student_id = st.text_input(
        "Enter Student ID",
        placeholder="Example: STU-001"
    )

    if student_id:

        selected_student = student_data[
            student_data["Student ID"] == student_id
        ]

        if not selected_student.empty:

            student = selected_student.iloc[0]

            st.success("Student record found.")

            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "Reading Score",
                    student["Reading Score"]
                )

            with col2:
                st.metric(
                    "Reading Performance",
                    student["Performance"]
                )

        else:
            st.warning("No student record found.")

    else:
        st.info("Enter a Student ID to view the student record.")


# ---------------------------------
# TEACHER DASHBOARD
# ---------------------------------

elif page == "Teacher Dashboard":

    st.title("Teacher Dashboard")

    st.write(
        "Monitor student reading assessment results "
        "and review their reading performance."
    )

    st.subheader("Student Performance Records")

    st.dataframe(
        student_data,
        use_container_width=True,
        hide_index=True
    )

    st.subheader("Reading Score Overview")

    chart_data = student_data.set_index("Student Name")[
        ["Reading Score"]
    ]

    st.bar_chart(chart_data)

    st.subheader("Performance Distribution")

    performance_counts = student_data["Performance"].value_counts()

    st.bar_chart(performance_counts)


# ---------------------------------
# READING ASSESSMENT
# ---------------------------------

elif page == "Reading Assessment":

    st.title("Reading Assessment")

    st.write(
        "Answer the following reading comprehension question."
    )

    st.subheader("Sample Reading Passage")

    st.write("""
    Education plays an important role in developing students'
    knowledge and skills. Through reading, students can understand
    information, develop critical thinking, and improve their
    communication skills.
    """)

    st.subheader("Comprehension Question")

    st.write(
        "According to the passage, what is one benefit of reading?"
    )

    answer = st.radio(
        "Choose your answer:",
        [
            "It improves critical thinking.",
            "It removes the need to study.",
            "It prevents students from learning.",
            "It replaces communication skills."
        ],
        index=None
    )

    if st.button("Submit Answer", type="primary"):

        if answer is None:
            st.warning("Please select an answer.")

        elif answer == "It improves critical thinking.":
            st.success("Correct answer!")

        else:
            st.error("Incorrect answer. Please review the passage.")


# ---------------------------------
# READING SUPPORT
# ---------------------------------

elif page == "Reading Support":

    st.title("Reading Support")

    st.write(
        "Explore learning activities that can help develop "
        "reading comprehension skills."
    )

    st.subheader("Recommended Learning Activities")

    with st.expander("1. Vocabulary Development"):

        st.write("""
        Learn new words and understand their meanings through
        vocabulary exercises and contextual clues.
        """)

        st.write("**Suggested Activity:**")

        st.write(
            "Read a short paragraph and identify unfamiliar words."
        )

    with st.expander("2. Reading Comprehension"):

        st.write("""
        Practice understanding written passages by identifying
        the main idea and supporting details.
        """)

        st.write("**Suggested Activity:**")

        st.write(
            "Read a short passage and answer comprehension questions."
        )

    with st.expander("3. Critical Thinking"):

        st.write("""
        Develop the ability to analyze information and make
        conclusions based on what has been read.
        """)

        st.write("**Suggested Activity:**")

        st.write(
            "Read a passage and explain its message in your own words."
        )

    with st.expander("4. Reading Practice"):

        st.write("""
        Improve reading skills through regular reading practice
        and comprehension exercises.
        """)

        st.write("**Suggested Activity:**")

        st.write(
            "Read an English article and summarize its main points."
        )


# ---------------------------------
# FOOTER
# ---------------------------------

st.divider()

st.caption(
    "Reading Support System | Prototype Version 1.0"
)
