
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

/* MODERN MINIMALIST TOP HEADER */
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
st.html("""
<div class="top-header">

    <div class="header-left">
        <div class="system-logo">📖</div>
        <h2 class="system-name">Reading Support System</h2>
    </div>

    <div class="header-profile">
        <div class="profile-icon">👤</div>
        <span class="profile-name">Administrator</span>
    </div>

</div>
""")


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
        st.markdown('<div class="panel">', unsafe_allow_html=True)
        st.markdown("**Sample Reading Scores**")
        st.caption("Illustrative demonstration data only.")

        st.bar_chart(
            data.set_index("Student")["Reading Score"],
            color="#7956B5"
        )

        st.markdown('</div>', unsafe_allow_html=True)

    with dist_col:
        st.markdown('<div class="panel">', unsafe_allow_html=True)
        st.markdown("**Performance Distribution**")
        st.caption("Illustrative demonstration data only.")

        distribution = data["Performance"].value_counts()

        st.bar_chart(
            distribution,
            color="#A78BCE"
        )

        st.markdown('</div>', unsafe_allow_html=True)

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
        st.metric("Latest Reading Score", "Not assessed")

    with c2:
        st.metric("Performance Classification", "Pending")

    st.subheader("Your Reading Progress")

    st.info(
        "Your assessment results will appear here once assessment records are connected."
    )

    st.subheader("Learning Areas")

    x, y = st.columns(2)

    with x:
        st.markdown("**📖 Reading Comprehension**")
        st.write("Understand passages and identify key details.")

    with y:
        st.markdown("**📝 Vocabulary Development**")
        st.write("Develop vocabulary and context clue skills.")


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

    st.title("📖 English Reading Assessment")
    st.caption(
        "Measure your reading comprehension through an educational passage."
    )

    st.markdown("""
    <div class="hero">
        <h2>Welcome to Your Reading Assessment!</h2>
        <p>
            Read the passage carefully and answer the comprehension questions.
            This activity will help evaluate your understanding of written information.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # ASSESSMENT INFORMATION
    info1, info2, info3 = st.columns(3)

    assessment_info = [
        (info1, "📚 Assessment Type", "Reading Comprehension"),
        (info2, "📝 Total Questions", "8 Questions"),
        (info3, "⏱️ Estimated Time", "15 Minutes")
    ]

    for col, label, value in assessment_info:
        with col:
            st.markdown(f"""
            <div class="stat-card">
                <div class="stat-name">{label}</div>
                <div class="stat-number" style="font-size:20px;">
                    {value}
                </div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")

    # READING PASSAGE
    st.markdown("### 📖 Reading Passage")

    st.markdown("""
    <div class="panel">
        <h2 style="color:#493078;">
            Small Actions, A Greener Future
        </h2>

        <p style="color:#9A90A7; font-size:12px;">
            Topic: Environmental Awareness | Reading Level: Secondary Education
        </p>

        <p style="line-height:1.9; text-align:justify;">
            Environmental problems have become a major concern in many
            communities. Issues such as plastic pollution, improper waste
            disposal, and excessive energy consumption affect both people
            and the natural environment. Although these problems may seem
            difficult to solve, small actions performed by individuals can
            contribute to meaningful improvements.
        </p>

        <p style="line-height:1.9; text-align:justify;">
            One practical way to protect the environment is through proper
            waste management. Separating biodegradable, recyclable, and
            non-recyclable materials helps reduce the amount of waste sent
            to landfills. Reusing containers, bringing reusable bags, and
            avoiding unnecessary single-use plastics are also simple habits
            that can reduce pollution.
        </p>

        <p style="line-height:1.9; text-align:justify;">
            Technology can also support environmental protection. Mobile
            applications and online platforms provide information about
            recycling programs, environmental campaigns, and sustainable
            practices. Schools can use digital tools to educate students
            about environmental issues and encourage participation in
            community activities. However, technology should be used
            responsibly because electronic waste and excessive energy
            consumption can create additional environmental challenges.
        </p>

        <p style="line-height:1.9; text-align:justify;">
            Students play an important role in promoting environmental
            awareness. They can participate in clean-up drives, organize
            recycling projects, and encourage their families and classmates
            to practice responsible waste disposal. These activities develop
            not only environmental responsibility but also cooperation,
            leadership, and problem-solving skills.
        </p>

        <p style="line-height:1.9; text-align:justify;">
            Protecting the environment does not require one person to make
            a dramatic change overnight. What matters is consistency and
            collective effort. When individuals make responsible choices
            and work together, small actions can create positive and lasting
            effects on the community and the environment.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # INSTRUCTIONS
    st.markdown("### 📌 Assessment Instructions")

    st.info("""
    1. Read the passage carefully before answering.
    2. Answer all eight comprehension questions.
    3. Select only one answer for each question.
    4. Review your answers before submitting.
    5. Click the Submit Assessment button to view your results.
    """)

    st.markdown("---")
    st.markdown("### 📝 Comprehension Questions")

    # QUESTIONS
    questions = [
        {
            "skill": "Main Idea",
            "question": "1. What is the main idea of the passage?",
            "options": [
                "A. Technology is the only solution to environmental problems.",
                "B. Small individual actions and collective efforts can help protect the environment.",
                "C. Environmental protection is only the responsibility of government organizations.",
                "D. Students should avoid using technology."
            ],
            "answer": "B. Small individual actions and collective efforts can help protect the environment."
        },
        {
            "skill": "Vocabulary",
            "question": "2. What does the word 'biodegradable' mean in the passage?",
            "options": [
                "A. Materials that can naturally decompose.",
                "B. Materials that cannot be reused.",
                "C. Materials that are harmful to all living things.",
                "D. Materials that are made only from plastic."
            ],
            "answer": "A. Materials that can naturally decompose."
        },
        {
            "skill": "Supporting Details",
            "question": "3. Which of the following is mentioned as a way to reduce plastic pollution?",
            "options": [
                "A. Buying more disposable products.",
                "B. Burning plastic waste.",
                "C. Bringing reusable bags.",
                "D. Throwing all waste into one container."
            ],
            "answer": "C. Bringing reusable bags."
        },
        {
            "skill": "Supporting Details",
            "question": "4. How can technology help promote environmental protection?",
            "options": [
                "A. By replacing all environmental programs.",
                "B. By providing information about recycling and environmental campaigns.",
                "C. By increasing the use of disposable materials.",
                "D. By preventing students from joining community activities."
            ],
            "answer": "B. By providing information about recycling and environmental campaigns."
        },
        {
            "skill": "Inference",
            "question": "5. What can be inferred about the role of students in environmental protection?",
            "options": [
                "A. Students are too young to make a difference.",
                "B. Students can influence others through responsible actions.",
                "C. Students should leave environmental activities to adults.",
                "D. Students can solve all environmental problems independently."
            ],
            "answer": "B. Students can influence others through responsible actions."
        },
        {
            "skill": "Cause and Effect",
            "question": "6. What may happen when people fail to manage waste properly?",
            "options": [
                "A. Pollution may increase.",
                "B. Natural resources will automatically recover.",
                "C. Communities will produce less waste.",
                "D. Recycling programs will no longer be needed."
            ],
            "answer": "A. Pollution may increase."
        },
        {
            "skill": "Critical Thinking",
            "question": "7. Which action best demonstrates responsible environmental behavior?",
            "options": [
                "A. Using disposable plastic products every day.",
                "B. Ignoring community clean-up activities.",
                "C. Separating waste and participating in recycling programs.",
                "D. Leaving waste in public places."
            ],
            "answer": "C. Separating waste and participating in recycling programs."
        },
        {
            "skill": "Conclusion",
            "question": "8. What message does the author emphasize in the final paragraph?",
            "options": [
                "A. Only large organizations can protect the environment.",
                "B. Environmental protection requires expensive technology.",
                "C. Consistent individual actions and cooperation can create lasting improvements.",
                "D. Environmental problems cannot be solved."
            ],
            "answer": "C. Consistent individual actions and cooperation can create lasting improvements."
        }
    ]

    # INITIALIZE SESSION STATE
    if "assessment_submitted" not in st.session_state:
        st.session_state.assessment_submitted = False

    if "assessment_score" not in st.session_state:
        st.session_state.assessment_score = None

    # PROGRESS TRACKING
    answered = sum(
        1 for i in range(len(questions))
        if st.session_state.get(f"question_{i}") is not None
    )

    progress = answered / len(questions)

    st.markdown(
        f"**Assessment Progress: {answered}/{len(questions)} questions answered**"
    )
    st.progress(progress)

    st.caption(
        "Select one answer for every question before submitting your assessment."
    )

    # DISPLAY QUESTIONS
    for i, item in enumerate(questions):

        st.markdown(f"""
        <div class="panel">
            <span style="
                color:#7956B5;
                font-size:12px;
                font-weight:700;
                text-transform:uppercase;
            ">
                {item["skill"]}
            </span>
            <h4 style="color:#493078; margin-top:8px;">
                {item["question"]}
            </h4>
        </div>
        """, unsafe_allow_html=True)

        st.radio(
            item["question"],
            item["options"],
            key=f"question_{i}",
            index=None,
            label_visibility="collapsed",
            disabled=st.session_state.assessment_submitted
        )

    st.markdown("---")

    # SUBMIT ASSESSMENT
    if not st.session_state.assessment_submitted:

        if st.button(
            "Submit Assessment",
            type="primary",
            use_container_width=True
        ):

            if answered < len(questions):
                st.warning(
                    f"Please answer all questions first. "
                    f"You still have {len(questions) - answered} unanswered question(s)."
                )

            else:
                score = 0

                for i, item in enumerate(questions):
                    selected = st.session_state.get(f"question_{i}")

                    if selected == item["answer"]:
                        score += 1

                st.session_state.assessment_score = score
                st.session_state.assessment_submitted = True

                st.rerun()

    # ASSESSMENT RESULTS
    if st.session_state.assessment_submitted:

        score = st.session_state.assessment_score
        percentage = (score / len(questions)) * 100

        st.markdown("## 📊 Assessment Results")

        result1, result2, result3 = st.columns(3)

        with result1:
            st.metric("Total Score", f"{score}/{len(questions)}")

        with result2:
            st.metric("Percentage", f"{percentage:.1f}%")

        with result3:
            st.metric("Questions Answered", f"{len(questions)}/{len(questions)}")

        if percentage >= 80:
            st.success(
                "Excellent! You demonstrated a strong understanding of the passage."
            )
        elif percentage >= 60:
            st.info(
                "Good effort! Continue practicing to improve your reading comprehension."
            )
        else:
            st.warning(
                "You may need additional reading practice. Review the passage and "
                "focus on identifying important details and ideas."
            )

        st.markdown("### Answer Review")

        for i, item in enumerate(questions):

            selected = st.session_state.get(f"question_{i}")
            correct = selected == item["answer"]

            if correct:
                st.success(f"Question {i + 1}: Correct")
            else:
                st.error(f"Question {i + 1}: Incorrect")
                st.write(f"Your answer: {selected}")
                st.write(f"Correct answer: {item['answer']}")

        if st.button(
            "Take Assessment Again",
            use_container_width=True
        ):

            for i in range(len(questions)):
                st.session_state.pop(f"question_{i}", None)

            st.session_state.assessment_submitted = False
            st.session_state.assessment_score = None

            st.rerun()

    st.caption(
        "Academic prototype assessment. Questions and scoring are for demonstration "
        "and require validation before use as a formal research instrument."
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
