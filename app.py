
import streamlit as st
import pandas as pd

# ---------------------------------
# PAGE CONFIGURATION
# ---------------------------------
st.set_page_config(
    page_title="Reading Support System",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------
# CUSTOM DESIGN
# ---------------------------------
st.markdown("""
<style>
    .stApp {
        background-color: #F8F7FC;
        color: #29243A;
    }

    [data-testid="stSidebar"] {
        background-color: #33245A;
    }

    [data-testid="stSidebar"] * {
        color: white !important;
    }

    .main-title {
        color: #39246B;
        font-size: 34px;
        font-weight: 800;
        margin-bottom: 0;
    }

    .subtitle {
        color: #77718A;
        font-size: 15px;
        margin-bottom: 25px;
    }

    .metric-card {
        background: white;
        padding: 22px;
        border-radius: 14px;
        border: 1px solid #E9E3F5;
        box-shadow: 0 3px 12px rgba(50, 30, 90, 0.05);
    }

    .metric-label {
        color: #77718A;
        font-size: 14px;
    }

    .metric-value {
        color: #39246B;
        font-size: 29px;
        font-weight: 800;
    }

    .section-title {
        color: #39246B;
        font-size: 22px;
        font-weight: 700;
        margin-top: 25px;
    }

    div.stButton > button {
        background-color: #6B46A5;
        color: white;
        border-radius: 9px;
        border: none;
    }

    div.stButton > button:hover {
        background-color: #50327F;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------
# SAMPLE DATA ONLY
# ---------------------------------
student_data = pd.DataFrame({
    "Student": ["Student A", "Student B", "Student C",
                "Student D", "Student E"],
    "Reading Score": [75, 82, 68, 90, 77],
    "Performance": [
        "Developing", "Proficient", "Developing",
        "Advanced", "Proficient"
    ]
})

# ---------------------------------
# SIDEBAR
# ---------------------------------
st.sidebar.markdown("# 📚 Reading Support")
st.sidebar.caption("Student Learning Platform")
st.sidebar.divider()

page = st.sidebar.radio(
    "MAIN MENU",
    [
        "Overview",
        "Student Dashboard",
        "Teacher Dashboard",
        "Reading Assessment",
        "Reading Support"
    ]
)

st.sidebar.divider()
st.sidebar.caption("Prototype Version 1.0")
st.sidebar.caption("For demonstration only")

# ---------------------------------
# HEADER
# ---------------------------------
st.markdown(
    '<p class="main-title">Reading Support System</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="subtitle">Machine Learning-Based Reading Performance '
    'Classification and Personalized Reading Support System</p>',
    unsafe_allow_html=True
)

# ---------------------------------
# OVERVIEW
# ---------------------------------
if page == "Overview":

    st.markdown("## Welcome to your Dashboard")
    st.write(
        "A platform designed to support Grade 10 and Grade 11 "
        "students in understanding their English reading performance."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-label">Registered Students</div>
            <div class="metric-value">--</div>
            <div class="metric-label">Sample data not connected</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-label">Completed Assessments</div>
            <div class="metric-value">--</div>
            <div class="metric-label">Awaiting assessment module</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-label">ML Model Status</div>
            <div class="metric-value">Pending</div>
            <div class="metric-label">Not yet trained</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown(
        '<p class="section-title">System Modules</p>',
        unsafe_allow_html=True
    )

    c1, c2 = st.columns(2)

    with c1:
        st.info("📊 **Student Dashboard**\n\n"
                "View reading assessment information and results.")

        st.info("📝 **Reading Assessment**\n\n"
                "A future module for English reading assessments.")

    with c2:
        st.info("👩‍🏫 **Teacher Dashboard**\n\n"
                "View student performance summaries.")

        st.info("📖 **Reading Support**\n\n"
                "Explore reading activities and learning resources.")

# ---------------------------------
# STUDENT DASHBOARD
# ---------------------------------
elif page == "Student Dashboard":

    st.header("Student Dashboard")
    st.write("Welcome, Student!")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Latest Reading Score", "Not assessed")

    with col2:
        st.metric("Performance Classification", "Pending")

    st.info(
        "Your reading assessment results and personalized "
        "support recommendations will appear here."
    )

# ---------------------------------
# TEACHER DASHBOARD
# ---------------------------------
elif page == "Teacher Dashboard":

    st.header("Teacher Dashboard")
    st.write("Student reading performance overview")

    st.caption("Illustrative sample data only. Not actual student records.")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Sample Records", "5")

    with col2:
        st.metric("Average Sample Score", "78.4")

    with col3:
        st.metric("Model Status", "Pending")

    st.markdown("### Sample Reading Performance")

    st.bar_chart(
        student_data.set_index("Student")["Reading Score"]
    )

    st.markdown("### Sample Student Records")

    st.dataframe(
        student_data,
        use_container_width=True,
        hide_index=True
    )

# ---------------------------------
# READING ASSESSMENT
# ---------------------------------
elif page == "Reading Assessment":

    st.header("English Reading Assessment")

    st.write(
        "This section will contain reading comprehension "
        "passages and assessment questions."
    )

    st.info("Assessment module is under development.")

    st.subheader("Sample Reading Question")

    passage = """
    Reading is an important skill that helps students understand
    information, develop ideas, and communicate effectively.
    Through regular reading practice, students can improve their
    vocabulary and comprehension skills.
    """

    st.write(passage)

    answer = st.radio(
        "What is one benefit of regular reading?",
        [
            "It improves vocabulary and comprehension.",
            "It eliminates the need to study.",
            "It prevents students from learning new ideas."
        ],
        index=None
    )

    if st.button("Check Sample Answer"):
        if answer is None:
            st.warning("Please select an answer.")
        elif answer == "It improves vocabulary and comprehension.":
            st.success("Correct answer!")
        else:
            st.error("Try again. Read the passage carefully.")

# ---------------------------------
# READING SUPPORT
# ---------------------------------
elif page == "Reading Support":

    st.header("Personalized Reading Support")

    st.write(
        "This section will provide educational reading activities "
        "based on students' assessed reading needs."
    )

    st.info(
        "The recommendations below are general sample activities, "
        "not machine learning-generated recommendations."
    )

    with st.expander("📖 Reading Comprehension"):
        st.write(
            "Read short English passages and identify their "
            "main ideas and supporting details."
        )

    with st.expander("📝 Vocabulary Development"):
        st.write(
            "Practice identifying unfamiliar words and understanding "
            "their meanings through context clues."
        )

    with st.expander("🔍 Critical Reading"):
        st.write(
            "Practice analyzing information, identifying facts, "
            "and making conclusions from written texts."
        )

    with st.expander("📚 Reading Fluency"):
        st.write(
            "Practice reading short passages with appropriate "
            "accuracy, pacing, and expression."
        )

st.divider()

st.caption(
    "Reading Support System | Academic Capstone Prototype | Version 1.0"
)
