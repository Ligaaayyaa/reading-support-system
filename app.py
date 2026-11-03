
import streamlit as st
import pandas as pd

# ==========================================
# PAGE CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="Reading Support System",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# CUSTOM CSS - PURPLE AND WHITE THEME
# ==========================================
st.markdown("""
<style>
    .stApp {
        background-color: #F7F5FC;
        color: #29243A;
    }

    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #35245F, #51358A);
    }

    [data-testid="stSidebar"] * {
        color: white !important;
    }

    [data-testid="stSidebar"] .stRadio label {
        padding: 7px 4px;
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

    .welcome-card {
        background: linear-gradient(110deg, #493078, #7654B2);
        padding: 28px;
        border-radius: 18px;
        color: white;
        margin-bottom: 25px;
    }

    .welcome-card h2 {
        color: white;
        margin: 0;
    }

    .welcome-card p {
        color: #F0EAFB;
        margin-bottom: 0;
    }

    .metric-card {
        background: white;
        padding: 22px;
        border-radius: 15px;
        border: 1px solid #E9E3F5;
        box-shadow: 0 4px 14px rgba(50, 30, 90, 0.06);
        min-height: 125px;
    }

    .metric-label {
        color: #77718A;
        font-size: 14px;
    }

    .metric-value {
        color: #39246B;
        font-size: 29px;
        font-weight: 800;
        margin-top: 8px;
    }

    .section-title {
        color: #39246B;
        font-size: 22px;
        font-weight: 750;
        margin-top: 25px;
    }

    .module-card {
        background: white;
        padding: 20px;
        border-radius: 14px;
        border: 1px solid #E9E3F5;
        box-shadow: 0 3px 12px rgba(50, 30, 90, 0.05);
        min-height: 115px;
        margin-bottom: 12px;
    }

    .module-card h4 {
        color: #493078;
        margin-top: 0;
    }

    .module-card p {
        color: #77718A;
        margin-bottom: 0;
    }

    div.stButton > button {
        background-color: #6B46A5;
        color: white;
        border-radius: 9px;
        border: none;
        padding: 8px 18px;
    }

    div.stButton > button:hover {
        background-color: #50327F;
        color: white;
        border: none;
    }

    div[data-testid="stMetric"] {
        background: white;
        border: 1px solid #E9E3F5;
        padding: 16px;
        border-radius: 13px;
    }

    h1, h2, h3 {
        color: #39246B;
    }

    .footer {
        color: #888198;
        font-size: 12px;
        text-align: center;
        padding-top: 25px;
    }
</style>
""", unsafe_allow_html=True)


# ==========================================
# SAMPLE DATA ONLY
# ==========================================
student_data = pd.DataFrame({
    "Student": [
        "Student A", "Student B", "Student C",
        "Student D", "Student E"
    ],
    "Reading Score": [75, 82, 68, 90, 77],
    "Performance": [
        "Developing", "Proficient", "Developing",
        "Advanced", "Proficient"
    ]
})


# ==========================================
# SIDEBAR
# ==========================================
with st.sidebar:
    st.markdown("# 📚 Reading Support")
    st.caption("STUDENT LEARNING PLATFORM")
    st.divider()

    page = st.radio(
        "MAIN MENU",
        [
            "Overview",
            "Student Dashboard",
            "Teacher Dashboard",
            "Reading Assessment",
            "Reading Support"
        ],
        label_visibility="visible"
    )

    st.divider()
    st.caption("Prototype Version 1.0")
    st.caption("Academic Capstone Project")
    st.caption("For demonstration only")


# ==========================================
# HEADER
# ==========================================
st.markdown(
    '<p class="main-title">Reading Support System</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="subtitle">Machine Learning-Based Reading Performance '
    'Classification and Personalized Reading Support System</p>',
    unsafe_allow_html=True
)


# ==========================================
# OVERVIEW DASHBOARD
# ==========================================
if page == "Overview":

    st.markdown("""
    <div class="welcome-card">
        <h2>Welcome to your Dashboard 👋</h2>
        <p>
        Your learning platform for understanding and improving
        English reading performance.
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-label">👥 Registered Students</div>
            <div class="metric-value">--</div>
            <div class="metric-label">No student database connected</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-label">📝 Completed Assessments</div>
            <div class="metric-value">--</div>
            <div class="metric-label">Awaiting assessment records</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-label">🤖 ML Model Status</div>
            <div class="metric-value">Pending</div>
            <div class="metric-label">Model not yet trained</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown(
        '<p class="section-title">System Modules</p>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="module-card">
            <h4>📊 Student Dashboard</h4>
            <p>View reading assessment information and results.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="module-card">
            <h4>📝 Reading Assessment</h4>
            <p>Answer English reading comprehension questions.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="module-card">
            <h4>👩‍🏫 Teacher Dashboard</h4>
            <p>View student performance summaries and records.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="module-card">
            <h4>📖 Reading Support</h4>
            <p>Explore reading activities and learning resources.</p>
        </div>
        """, unsafe_allow_html=True)

    st.info(
        "This is an initial prototype. Student records and machine "
        "learning predictions are not yet connected."
    )


# ==========================================
# STUDENT DASHBOARD
# ==========================================
elif page == "Student Dashboard":

    st.header("📊 Student Dashboard")
    st.write("Welcome to your personal reading dashboard!")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Latest Reading Score", "Not assessed")

    with col2:
        st.metric("Performance Classification", "Pending")

    st.markdown("### Reading Progress")

    st.info(
        "Your reading assessment results and personalized "
        "support recommendations will appear here once the "
        "assessment and database modules are connected."
    )

    st.markdown("### Recommended Learning Areas")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="module-card">
            <h4>📖 Reading Comprehension</h4>
            <p>Understand passages and identify important details.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="module-card">
            <h4>📝 Vocabulary Development</h4>
            <p>Improve word knowledge and context clue skills.</p>
        </div>
        """, unsafe_allow_html=True)


# ==========================================
# TEACHER DASHBOARD
# ==========================================
elif page == "Teacher Dashboard":

    st.header("👩‍🏫 Teacher Dashboard")
    st.write("Student reading performance overview.")

    st.warning(
        "Illustrative sample data only. These are not actual "
        "student records or machine learning predictions."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Sample Records", "5")

    with col2:
        st.metric("Average Sample Score", "78.4")

    with col3:
        st.metric("ML Model Status", "Pending")

    st.markdown("### Sample Reading Performance")

    chart_data = student_data.set_index("Student")
    st.bar_chart(chart_data["Reading Score"])

    st.markdown("### Sample Student Records")

    st.dataframe(
        student_data,
        use_container_width=True,
        hide_index=True
    )


# ==========================================
# READING ASSESSMENT
# ==========================================
elif page == "Reading Assessment":

    st.header("📝 English Reading Assessment")

    st.write(
        "Read the passage carefully and answer the question below."
    )

    st.markdown("### Reading Passage")

    st.markdown("""
    <div class="module-card">
        <h4>The Importance of Reading</h4>
        <p>
        Reading is an important skill that helps students understand
        information, develop ideas, and communicate effectively.
        Through regular reading practice, students can improve their
        vocabulary and comprehension skills. Reading also allows
        learners to explore new ideas and gain knowledge about
        different topics.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### Question 1")

    answer = st.radio(
        "What is one benefit of regular reading?",
        [
            "It improves vocabulary and comprehension.",
            "It eliminates the need to study.",
            "It prevents students from learning new ideas."
        ],
        index=None
    )

    if st.button("Check Answer"):

        if answer is None:
            st.warning("Please select an answer.")

        elif answer == "It improves vocabulary and comprehension.":
            st.success("Correct! You understood the passage.")

        else:
            st.error(
                "Not quite. Try reading the passage again "
                "and look for the correct information."
            )

    st.caption(
        "Sample question only. This is not yet the official "
        "research assessment instrument."
    )


# ==========================================
# READING SUPPORT
# ==========================================
elif page == "Reading Support":

    st.header("📖 Personalized Reading Support")

    st.write(
        "Explore educational activities that can help develop "
        "different English reading skills."
    )

    st.info(
        "These are general sample activities. They are not yet "
        "generated by a trained machine learning model."
    )

    with st.expander("📖 Reading Comprehension"):
        st.write(
            "Read short English passages and identify their "
            "main ideas, supporting details, and conclusions."
        )
        st.write("Suggested activity: Read a short passage and summarize it.")

    with st.expander("📝 Vocabulary Development"):
        st.write(
            "Practice identifying unfamiliar words and understanding "
            "their meanings through context clues."
        )
        st.write("Suggested activity: Create a vocabulary journal.")

    with st.expander("🔍 Critical Reading"):
        st.write(
            "Practice analyzing information, identifying facts, "
            "and making conclusions from written texts."
        )
        st.write("Suggested activity: Distinguish facts from opinions.")

    with st.expander("📚 Reading Fluency"):
        st.write(
            "Practice reading short passages with appropriate "
            "accuracy, pacing, and expression."
        )
        st.write("Suggested activity: Read a short passage aloud and record your time.")


# ==========================================
# FOOTER
# ==========================================
st.divider()

st.markdown("""
<div class="footer">
    Reading Support System | Academic Capstone Prototype |
    Version 1.0
</div>
""", unsafe_allow_html=True)
