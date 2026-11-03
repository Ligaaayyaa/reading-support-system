import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Reading Support System",
    page_icon="📚",
    layout="wide"
)

# -----------------------------
# THEME AND CUSTOM CSS
# -----------------------------
st.markdown("""
<style>
.stApp {
    background: #F6F4FB;
    color: #29243A;
}

[data-testid="stSidebar"] {
    background: #30204F;
}

[data-testid="stSidebar"] * {
    color: white !important;
}

.block-container {
    padding-top: 1.5rem;
    padding-bottom: 2rem;
}

/* EXISTING TEXT STYLES */
.top-label {
    color: #8A7AA7;
    font-size: 13px;
    font-weight: 600;
}

.main-heading {
    color: #342052;
    font-size: 32px;
    font-weight: 800;
}

.sub-heading {
    color: #827894;
    font-size: 14px;
}

/* HERO BANNER */
.hero {
    background: linear-gradient(110deg,#493078,#7956B5);
    border-radius: 18px;
    padding: 28px;
    color: white;
    margin: 18px 0 25px 0;
}

.hero h2 {
    color: white;
    margin: 0;
}

.hero p {
    color: #EEE7FA;
    margin-bottom: 0;
}

/* STAT CARDS */
.stat-card {
    background: white;
    border: 1px solid #EAE4F2;
    border-radius: 15px;
    padding: 20px;
    min-height: 125px;
    box-shadow: 0 4px 15px rgba(50,30,80,.04);
}

.stat-name {
    color: #81758F;
    font-size: 13px;
}

.stat-number {
    color: #493078;
    font-size: 28px;
    font-weight: 800;
    margin-top: 8px;
}

.stat-note {
    color: #9A90A7;
    font-size: 11px;
}

/* PANELS */
.panel {
    background: white;
    border: 1px solid #EAE4F2;
    border-radius: 15px;
    padding: 20px;
    margin-bottom: 15px;
}

.panel-title {
    color: #493078;
    font-size: 18px;
    font-weight: 700;
}

/* SIDEBAR NAVIGATION BUTTONS */
[data-testid="stSidebar"] div.stButton > button {
    width: 100%;
    min-height: 48px;
    text-align: left;
    background: #493765;
    color: white;
    border: 1px solid #604B7C;
    border-radius: 10px;
    padding: 10px 15px;
    font-size: 14px;
    font-weight: 600;
    transition: 0.2s ease;
}

[data-testid="stSidebar"] div.stButton > button:hover {
    background: #7956B5;
    color: white;
    border-color: #A78BCE;
}

[data-testid="stSidebar"] div.stButton > button[kind="primary"] {
    background: #7956B5;
    color: white;
    border: 1px solid #A78BCE;
}

div.stButton > button {
    background: #67449B;
    color: white;
    border: 0;
    border-radius: 9px;
}

div.stButton > button:hover {
    background: #493078;
    color: white;
}

/* -----------------------------
   MODERN MINIMALIST TOP HEADER
----------------------------- */

.top-header {
    width: 100%;
    background: #FFFFFF;
    border: 1px solid #F0ECF7;
    border-radius: 18px;
    padding: 16px 26px;
    box-shadow: 0 4px 18px rgba(48, 32, 79, 0.08);
    display: flex;
    align-items: center;
    justify-content: space-between;
    box-sizing: border-box;
    margin-bottom: 25px;
}

.header-left {
    display: flex;
    align-items: center;
    gap: 16px;
}

.system-logo {
    width: 62px;
    height: 62px;
    min-width: 62px;
    border-radius: 14px;
    background: linear-gradient(135deg, #9560D8, #492477);
    display: flex;
    align-items: center;
    justify-content: center;
    color: #FFFFFF;
    font-size: 30px;
}

.system-name {
    color: #30204F;
    font-size: 25px;
    font-weight: 750;
    margin: 0;
    padding: 0;
    line-height: 1.3;
}

.header-profile {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-left: 15px;
}

.profile-icon {
    width: 48px;
    height: 48px;
    min-width: 48px;
    border-radius: 50%;
    background: #E9DDFB;
    color: #492477;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 23px;
}

.profile-name {
    color: #777184;
    font-size: 16px;
    font-weight: 500;
    white-space: nowrap;
}

/* RESPONSIVE HEADER */
@media (max-width: 600px) {
    .top-header {
        padding: 13px 15px;
        border-radius: 14px;
    }

    .header-left {
        gap: 10px;
    }

    .system-logo {
        width: 45px;
        height: 45px;
        min-width: 45px;
        font-size: 23px;
        border-radius: 11px;
    }

    .system-name {
        font-size: 16px;
    }

    .header-profile {
        gap: 7px;
        margin-left: 8px;
    }

    .profile-icon {
        width: 36px;
        height: 36px;
        min-width: 36px;
        font-size: 18px;
    }

    .profile-name {
        font-size: 12px;
    }
}

/* FOOTER */
.footer {
    text-align: center;
    color: #968BA4;
    font-size: 12px;
}
</style>
""", unsafe_allow_html=True)


# -----------------------------
# DEMONSTRATION DATA
# -----------------------------
data = pd.DataFrame({
    "Student": [
        "Student A",
        "Student B",
        "Student C",
        "Student D",
        "Student E"
    ],
    "Reading Score": [75, 82, 68, 90, 77],
    "Performance": [
        "Developing",
        "Proficient",
        "Developing",
        "Advanced",
        "Proficient"
    ]
})


# -----------------------------
# SIDEBAR NAVIGATION
# -----------------------------
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
    st.markdown("# 📚 Reading Support")
    st.caption("STUDENT LEARNING PLATFORM")
    st.divider()

    st.markdown("**MAIN MENU**")

    for page_name, label in pages.items():

        is_active = (
            st.session_state.current_page == page_name
        )

        if st.button(
            label,
            key=f"nav_{page_name}",
            use_container_width=True,
            type="primary" if is_active else "secondary"
        ):
            st.session_state.current_page = page_name
            st.rerun()

    st.divider()
    st.caption("CAPSTONE PROTOTYPE")
    st.caption("Version 2.0")

page = st.session_state.current_page


# -----------------------------
# TOP HEADER - MODERN DESIGN
# -----------------------------

st.markdown("""
<div class="top-header">

    <div class="header-left">

        <div class="system-logo">
            📖
        </div>

        <h2 class="system-name">
            Reading Support System
        </h2>

    </div>

    <div class="header-profile">

        <div class="profile-icon">
            👤
        </div>

        <span class="profile-name">
            Administrator
        </span>

    </div>

</div>
""", unsafe_allow_html=True)


# -----------------------------
# OVERVIEW PAGE
# -----------------------------
if page == "Overview":

    st.markdown("""
    <div class="hero">
        <h2>Welcome to your Dashboard 👋</h2>
        <p>Monitor reading performance and explore learning support tools.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### Dashboard Overview")

    c1, c2, c3, c4 = st.columns(4)

    metrics = [
        ("👥", "Registered Students", "--", "Database not connected"),
        ("📝", "Assessments Completed", "--", "No records yet"),
        ("📊", "Average Reading Score", "--", "Awaiting assessment"),
        ("🤖", "ML Model Status", "Pending", "Not yet trained")
    ]

    for col, item in zip([c1, c2, c3, c4], metrics):
        with col:
            st.markdown(f"""
            <div class="stat-card">
                <div class="stat-name">{item[0]} {item[1]}</div>
                <div class="stat-number">{item[2]}</div>
                <div class="stat-note">{item[3]}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("### Reading Performance Analytics")

    chart_col, dist_col = st.columns([2, 1])

    with chart_col:
        st.markdown(
            '<div class="panel">',
            unsafe_allow_html=True
        )

        st.markdown("**Sample Reading Scores**")
        st.caption("Illustrative demonstration data only.")

        st.bar_chart(
            data.set_index("Student")["Reading Score"],
            color="#7956B5"
        )

        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )

    with dist_col:
        st.markdown(
            '<div class="panel">',
            unsafe_allow_html=True
        )

        st.markdown("**Performance Distribution**")
        st.caption("Illustrative demonstration data only.")

        distribution = data["Performance"].value_counts()

        st.bar_chart(
            distribution,
            color="#A78BCE"
        )

        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )

    st.markdown("### Recent Assessment Activity")
    st.caption("Sample records only; not actual student information.")

    st.dataframe(
        data,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("### System Modules")

    a, b, c, d = st.columns(4)

    modules = [
        (a, "📊", "Student Dashboard", "Student results and progress"),
        (b, "👩‍🏫", "Teacher Dashboard", "Class performance overview"),
        (c, "📝", "Reading Assessment", "English comprehension tasks"),
        (d, "📖", "Reading Support", "Learning activities and resources")
    ]

    for col, icon, title, desc in modules:
        with col:
            st.markdown(f"""
            <div class="stat-card">
                <div style="font-size:25px">{icon}</div>
                <b style="color:#493078">{title}</b>
                <div class="stat-note">{desc}</div>
            </div>
            """, unsafe_allow_html=True)


# -----------------------------
# STUDENT DASHBOARD
# -----------------------------
elif page == "Student Dashboard":

    st.title("Student Dashboard")
    st.caption("Your personal reading performance space.")

    c1, c2 = st.columns(2)

    with c1:
        st.metric(
            "Latest Reading Score",
            "Not assessed"
        )

    with c2:
        st.metric(
            "Performance Classification",
            "Pending"
        )

    st.subheader("Your Reading Progress")

    st.info(
        "Your assessment results will appear here once assessment records are connected."
    )

    st.subheader("Learning Areas")

    x, y = st.columns(2)

    with x:
        st.markdown("**📖 Reading Comprehension**")
        st.write(
            "Understand passages and identify key details."
        )

    with y:
        st.markdown("**📝 Vocabulary Development**")
        st.write(
            "Develop vocabulary and context clue skills."
        )


# -----------------------------
# TEACHER DASHBOARD
# -----------------------------
elif page == "Teacher Dashboard":

    st.title("Teacher Dashboard")
    st.caption("Reading performance monitoring.")

    st.warning(
        "All records below are illustrative sample data."
    )

    c1, c2, c3 = st.columns(3)

    c1.metric("Sample Students", "5")
    c2.metric("Average Sample Score", "78.4")
    c3.metric("ML Model", "Pending")

    st.subheader("Student Performance Chart")

    st.bar_chart(
        data.set_index("Student")["Reading Score"],
        color="#7956B5"
    )

    st.subheader("Student Records")

    st.dataframe(
        data,
        use_container_width=True,
        hide_index=True
    )


# -----------------------------
# READING ASSESSMENT
# -----------------------------
elif page == "Reading Assessment":

    st.title("English Reading Assessment")

    st.write(
        "Read the passage and answer the question."
    )

    st.markdown("### The Importance of Reading")

    st.info("""
    Reading is an important skill that helps students understand
    information, develop ideas, and communicate effectively.
    Regular reading practice can improve vocabulary and
    comprehension skills.
    """)

    answer = st.radio(
        "What is one benefit of regular reading?",
        [
            "It improves vocabulary and comprehension.",
            "It eliminates the need to study.",
            "It prevents students from learning new ideas."
        ],
        index=None
    )

    if st.button("Submit Answer"):

        if answer is None:
            st.warning("Please select an answer.")

        elif answer == "It improves vocabulary and comprehension.":
            st.success("Correct answer!")

        else:
            st.error(
                "Incorrect. Please review the passage."
            )

    st.caption(
        "Demonstration question only. Not the final research instrument."
    )


# -----------------------------
# READING SUPPORT
# -----------------------------
elif page == "Reading Support":

    st.title("Personalized Reading Support")

    st.write(
        "Explore educational activities for reading development."
    )

    st.info(
        "These are general sample activities, not ML-generated recommendations."
    )

    activities = {
        "📖 Reading Comprehension":
            "Read passages and identify main ideas and supporting details.",

        "📝 Vocabulary Development":
            "Practice word meanings using context clues.",

        "🔍 Critical Reading":
            "Distinguish facts from opinions and analyze information.",

        "📚 Reading Fluency":
            "Practice reading accuracy, pacing, and expression."
    }

    for title, description in activities.items():

        with st.expander(title):
            st.write(description)


# -----------------------------
# FOOTER
# -----------------------------
st.divider()

st.markdown(
    '<div class="footer">Reading Support System | Academic Capstone Prototype | Version 2.0</div>',
    unsafe_allow_html=True
)
