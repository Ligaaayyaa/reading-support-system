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

/* READING ASSESSMENT - BLACK CHOICE TEXT */
div[data-testid="stRadio"] label,
div[data-testid="stRadio"] label p,
div[data-testid="stRadio"] label span {
    color: #000000 !important;
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
/* ================================
   ACCESSIBILITY: FORM TEXT CONTRAST
================================ */

/* General labels and form instructions */
.stTextInput label,
.stTextArea label,
.stNumberInput label,
.stSelectbox label,
.stMultiSelect label,
.stRadio label,
.stCheckbox label,
.stDateInput label,
.stTimeInput label,
.stSlider label,
[data-testid="stWidgetLabel"] p,
[data-testid="stMarkdownContainer"] p {
    color: #1F2937 !important;
}

/* Text inputs, text areas, number inputs, and date/time fields */
.stTextInput input,
.stTextArea textarea,
.stNumberInput input,
.stDateInput input,
.stTimeInput input {
    color: #1F2937 !important;
    background-color: #FFFFFF !important;
    -webkit-text-fill-color: #1F2937 !important;
    border: 1px solid #9CA3AF !important;
}

/* Placeholder text */
.stTextInput input::placeholder,
.stTextArea textarea::placeholder,
.stNumberInput input::placeholder {
    color: #6B7280 !important;
    opacity: 1 !important;
    -webkit-text-fill-color: #6B7280 !important;
}

/* Text area content */
.stTextArea textarea {
    color: #1F2937 !important;
    background-color: #FFFFFF !important;
}

/* Select boxes and multiselect fields */
.stSelectbox div[data-baseweb="select"] > div,
.stMultiSelect div[data-baseweb="select"] > div {
    color: #1F2937 !important;
    background-color: #FFFFFF !important;
    border-color: #9CA3AF !important;
}

/* Selected values and dropdown text */
.stSelectbox [data-testid="stMarkdownContainer"],
.stMultiSelect [data-testid="stMarkdownContainer"],
[role="option"] {
    color: #1F2937 !important;
}

/* Radio buttons and checkboxes */
.stRadio div[role="radiogroup"] label,
.stCheckbox label,
.stRadio div[role="radiogroup"] p,
.stCheckbox p {
    color: #1F2937 !important;
}

/* Form buttons */
.stButton button,
.stFormSubmitButton button {
    color: #FFFFFF !important;
    background-color: #30204F !important;
    border: 1px solid #30204F !important;
    font-weight: 600 !important;
}

/* Button hover */
.stButton button:hover,
.stFormSubmitButton button:hover {
    color: #FFFFFF !important;
    background-color: #49336F !important;
    border-color: #49336F !important;
}

/* Sidebar text and buttons */
section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] span {
    color: #FFFFFF !important;
}

/* Sidebar buttons */
section[data-testid="stSidebar"] .stButton button {
    color: #FFFFFF !important;
    background-color: #49336F !important;
    border-color: #49336F !important;
}

/* Focus indicator for keyboard accessibility */
.stTextInput input:focus,
.stTextArea textarea:focus,
.stNumberInput input:focus,
.stSelectbox div[data-baseweb="select"]:focus-within {
    border: 2px solid #30204F !important;
    box-shadow: 0 0 0 2px rgba(48, 32, 79, 0.20) !important;
    outline: none !important;
}

/* Disabled fields */
input:disabled,
textarea:disabled {
    color: #4B5563 !important;
    background-color: #E5E7EB !important;
    -webkit-text-fill-color: #4B5563 !important;
    opacity: 1 !important;
}

/* =====================================
   ACCESSIBILITY: BUTTON TEXT CONTRAST
===================================== */

/* Default button state */
.stButton > button,
.stFormSubmitButton > button {
    background-color: #30204F !important;
    color: #FFFFFF !important;
    -webkit-text-fill-color: #FFFFFF !important;
    border: 1px solid #30204F !important;
    font-weight: 600 !important;
    opacity: 1 !important;
}

/* Ensure nested button text is also white */
.stButton > button *,
.stFormSubmitButton > button * {
    color: #FFFFFF !important;
    -webkit-text-fill-color: #FFFFFF !important;
}

/* Hover state */
.stButton > button:hover,
.stFormSubmitButton > button:hover {
    background-color: #49336F !important;
    color: #FFFFFF !important;
    border-color: #49336F !important;
}

/* Active state */
.stButton > button:active,
.stFormSubmitButton > button:active {
    background-color: #24183D !important;
    color: #FFFFFF !important;
    border-color: #24183D !important;
}

/* Disabled state */
.stButton > button:disabled,
.stFormSubmitButton > button:disabled {
    background-color: #5B5368 !important;
    color: #FFFFFF !important;
    -webkit-text-fill-color: #FFFFFF !important;
    border-color: #5B5368 !important;
    opacity: 1 !important;
    cursor: not-allowed !important;
}

/* Keyboard focus state */
.stButton > button:focus-visible,
.stFormSubmitButton > button:focus-visible {
    outline: 3px solid #8B70D6 !important;
    outline-offset: 3px !important;
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
    "Reading Assessment": "📝  Assessment Management",
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
# ADMIN - ASSESSMENT MANAGEMENT
# 3-STEP WIZARD
# -----------------------------
elif page == "Reading Assessment":

    st.title("📝 Assessment Management")
    st.caption(
        "Create and manage English reading assessments through a guided process."
    )

    # -----------------------------
    # DEFAULT CONTENT
    # -----------------------------
    default_passage = """
Environmental problems have become a major concern in many communities.
Issues such as plastic pollution, improper waste disposal, and excessive
energy consumption affect both people and the natural environment.
Although these problems may seem difficult to solve, small actions
performed by individuals can contribute to meaningful improvements.

One practical way to protect the environment is through proper waste
management. Separating biodegradable, recyclable, and non-recyclable
materials helps reduce the amount of waste sent to landfills. Reusing
containers, bringing reusable bags, and avoiding unnecessary single-use
plastics are also simple habits that can reduce pollution.

Technology can also support environmental protection. Mobile applications
and online platforms provide information about recycling programs,
environmental campaigns, and sustainable practices. Schools can use
digital tools to educate students about environmental issues and encourage
participation in community activities. However, technology should be used
responsibly because electronic waste and excessive energy consumption can
create additional environmental challenges.

Students play an important role in promoting environmental awareness.
They can participate in clean-up drives, organize recycling projects,
and encourage their families and classmates to practice responsible waste
disposal. These activities develop not only environmental responsibility
but also cooperation, leadership, and problem-solving skills.

Protecting the environment does not require one person to make a dramatic
change overnight. What matters is consistency and collective effort.
When individuals make responsible choices and work together, small actions
can create positive and lasting effects on the community and the environment.
"""

    default_questions = [
        {
            "skill": "Main Idea",
            "question": "What is the main idea of the passage?",
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
            "question": "What does the word 'biodegradable' mean in the passage?",
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
            "question": "Which of the following is mentioned as a way to reduce plastic pollution?",
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
            "question": "How can technology help promote environmental protection?",
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
            "question": "What can be inferred about the role of students in environmental protection?",
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
            "question": "What may happen when people fail to manage waste properly?",
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
            "question": "Which action best demonstrates responsible environmental behavior?",
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
            "question": "What message does the author emphasize in the final paragraph?",
            "options": [
                "A. Only large organizations can protect the environment.",
                "B. Environmental protection requires expensive technology.",
                "C. Consistent individual actions and cooperation can create lasting improvements.",
                "D. Environmental problems cannot be solved."
            ],
            "answer": "C. Consistent individual actions and cooperation can create lasting improvements."
        }
    ]

    # -----------------------------
    # INITIALIZE SESSION STATE
    # -----------------------------
    defaults = {
        "admin_questions": [
            question.copy() for question in default_questions
        ],
        "admin_passage_title": "Small Actions, A Greener Future",
        "admin_passage_topic": "Environmental Awareness",
        "admin_passage_level": "Secondary Education",
        "admin_passage_content": default_passage,
        "passage_info_saved": False,
        "reading_material_saved": False
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

    if "saved_assessments" not in st.session_state:
        st.session_state.saved_assessments = []

    if "pending_delete_id" not in st.session_state:
        st.session_state.pending_delete_id = None

    skill_options = [
        "Main Idea",
        "Vocabulary",
        "Supporting Details",
        "Inference",
        "Cause and Effect",
        "Critical Thinking",
        "Conclusion"
    ]

    level_options = [
        "Elementary",
        "Junior High School",
        "Secondary Education",
        "Senior High School"
    ]

    # -----------------------------
    # WIZARD PROGRESS
    # -----------------------------
    st.markdown("## Assessment Creation Wizard")

    step1_done = st.session_state.passage_info_saved
    step2_done = st.session_state.reading_material_saved

    current_step = (
        3 if step2_done
        else 2 if step1_done
        else 1
    )

    progress_col1, progress_col2, progress_col3 = st.columns(3)

    with progress_col1:
        st.markdown(
            f"### {'✅' if step1_done else '🟣'} Step 1"
        )
        st.caption("Passage Information")

    with progress_col2:
        st.markdown(
            f"### {'✅' if step2_done else '🟣' if step1_done else '🔒'} Step 2"
        )
        st.caption("Reading Material")

    with progress_col3:
        st.markdown(
            f"### {'🟣' if step2_done else '🔒'} Step 3"
        )
        st.caption("Comprehension Questions")

    st.progress(current_step / 3)

    st.divider()

    # -----------------------------
    # STEP 1: PASSAGE INFORMATION
    # -----------------------------
    st.markdown("## 1. 📚 Passage Information")

    st.caption(
        "Enter the basic information about the reading passage. "
        "Complete this section before proceeding to the reading material."
    )

    if step1_done:
        st.success("Passage Information has been saved.")

    with st.container(border=True):

        with st.form("passage_information_form"):

            passage_title = st.text_input(
                "Passage Title",
                value=st.session_state.admin_passage_title
            )

            passage_topic = st.text_input(
                "Topic",
                value=st.session_state.admin_passage_topic
            )

            current_level = st.session_state.admin_passage_level

            passage_level = st.selectbox(
                "Reading Level",
                level_options,
                index=(
                    level_options.index(current_level)
                    if current_level in level_options else 2
                )
            )

            save_passage_info = st.form_submit_button(
                "Save Passage Information",
                use_container_width=True
            )

            if save_passage_info:

                if passage_title.strip() and passage_topic.strip():

                    st.session_state.admin_passage_title = passage_title.strip()
                    st.session_state.admin_passage_topic = passage_topic.strip()
                    st.session_state.admin_passage_level = passage_level

                    st.session_state.passage_info_saved = True

                    # Require reading material to be reviewed again
                    # whenever passage information is saved.
                    st.session_state.reading_material_saved = False

                    st.success(
                        "Passage Information saved successfully! "
                        "You may now proceed to Step 2."
                    )
                    st.rerun()

                else:
                    st.error(
                        "Please complete the Passage Title and Topic."
                    )

    # -----------------------------
    # STEP 2: READING MATERIAL
    # -----------------------------
    st.markdown("---")
    st.markdown("## 2. 📖 Reading Material")

    if not st.session_state.passage_info_saved:

        st.warning(
            "🔒 This section is locked. Please complete and save "
            "Step 1: Passage Information first."
        )

    else:

        st.caption(
            "Enter the actual reading passage that students will read "
            "during the assessment."
        )

        if step2_done:
            st.success("Reading Material has been saved.")

        with st.container(border=True):

            st.markdown(
                f"**Passage:** {st.session_state.admin_passage_title}"
            )
            st.markdown(
                f"**Topic:** {st.session_state.admin_passage_topic}"
            )
            st.markdown(
                f"**Reading Level:** {st.session_state.admin_passage_level}"
            )

            st.divider()

            with st.form("reading_material_form"):

                reading_content = st.text_area(
                    "Reading Passage Content",
                    value=st.session_state.admin_passage_content,
                    height=350,
                    help="Enter the complete reading passage here."
                )

                save_reading_material = st.form_submit_button(
                    "Save Reading Material",
                    use_container_width=True
                )

                if save_reading_material:

                    if reading_content.strip():

                        st.session_state.admin_passage_content = reading_content.strip()
                        st.session_state.reading_material_saved = True

                        st.success(
                            "Reading Material saved successfully! "
                            "You may now proceed to Step 3."
                        )
                        st.rerun()

                    else:
                        st.error(
                            "Please enter the reading passage before saving."
                        )

            if st.session_state.reading_material_saved:

                with st.expander("👁️ Preview Saved Reading Material"):

                    st.markdown(
                        f"### {st.session_state.admin_passage_title}"
                    )
                    st.caption(
                        f"{st.session_state.admin_passage_topic} | "
                        f"{st.session_state.admin_passage_level}"
                    )
                    st.write(st.session_state.admin_passage_content)

    # -----------------------------
    # STEP 3: COMPREHENSION QUESTIONS
    # -----------------------------
    st.markdown("---")
    st.markdown("## 3. 📝 Comprehension Questions")

    if not st.session_state.passage_info_saved:

        st.warning(
            "🔒 Questions are locked. Please complete Step 1 first."
        )

    elif not st.session_state.reading_material_saved:

        st.warning(
            "🔒 Questions are locked. Please save the Reading Material "
            "in Step 2 before creating comprehension questions."
        )

    else:

        st.success(
            "All required sections are complete. "
            "You can now manage comprehension questions."
        )

        st.caption(
            "Add, edit, or delete questions, answer choices, "
            "and correct answers for this reading passage."
        )

        # -----------------------------
        # EXISTING QUESTIONS
        # -----------------------------
        st.markdown("### Existing Questions")

        total_questions = len(st.session_state.admin_questions)

        if total_questions == 0:
            st.info("No comprehension questions have been added yet.")

        for i, item in enumerate(st.session_state.admin_questions):

            with st.expander(
                f"Question {i + 1} — {item['skill']}"
            ):

                st.markdown(f"**{item['question']}**")
                st.markdown("**Answer Choices:**")

                for option in item["options"]:

                    if option == item["answer"]:
                        st.markdown(
                            f"<span style='color:green; font-weight:700;'>"
                            f"✓ {option} — Correct Answer</span>",
                            unsafe_allow_html=True
                        )
                    else:
                        st.markdown(
                            f"<span style='color:#1F2937;'>{option}</span>",
                            unsafe_allow_html=True
                        )

                st.caption(f"Question Skill: {item['skill']}")

                with st.form(f"edit_question_form_{i}"):

                    current_skill_index = (
                        skill_options.index(item["skill"])
                        if item["skill"] in skill_options else 0
                    )

                    edited_skill = st.selectbox(
                        "Question Skill",
                        skill_options,
                        index=current_skill_index
                    )

                    edited_question = st.text_input(
                        "Question",
                        value=item["question"]
                    )

                    edited_options = []

                    for j, option in enumerate(item["options"]):

                        edited_options.append(
                            st.text_input(
                                f"Choice {chr(65 + j)}",
                                value=option
                            )
                        )

                    current_answer_index = item["options"].index(
                        item["answer"]
                    )

                    edited_answer = st.selectbox(
                        "Correct Answer",
                        options=[0, 1, 2, 3],
                        index=current_answer_index,
                        format_func=lambda x: f"Choice {chr(65 + x)}"
                    )

                    save_question = st.form_submit_button(
                        "Save Question Changes",
                        use_container_width=True
                    )

                    if save_question:

                        if (
                            edited_question.strip()
                            and all(option.strip() for option in edited_options)
                        ):

                            st.session_state.admin_questions[i] = {
                                "skill": edited_skill,
                                "question": edited_question.strip(),
                                "options": [
                                    option.strip()
                                    for option in edited_options
                                ],
                                "answer": edited_options[edited_answer].strip()
                            }

                            st.success("Question updated successfully.")
                            st.rerun()

                        else:
                            st.error(
                                "Please complete the question and all choices."
                            )

                if st.button(
                    "🗑️ Delete Question",
                    key=f"delete_admin_question_{i}"
                ):

                    st.session_state.admin_questions.pop(i)
                    st.success("Question deleted successfully.")
                    st.rerun()

        # -----------------------------
        # ADD NEW QUESTION
        # -----------------------------
        st.markdown("---")
        st.markdown("### ➕ Add New Question")

        with st.container(border=True):

            with st.form("add_new_question_form"):

                new_skill = st.selectbox(
                    "Question Skill",
                    skill_options,
                    key="new_question_skill"
                )

                new_question = st.text_input(
                    "Question",
                    key="new_question_text"
                )

                new_options = []

                for i in range(4):

                    new_options.append(
                        st.text_input(
                            f"Choice {chr(65 + i)}",
                            key=f"new_question_choice_{i}"
                        )
                    )

                new_correct_answer = st.selectbox(
                    "Correct Answer",
                    options=[0, 1, 2, 3],
                    format_func=lambda x: f"Choice {chr(65 + x)}",
                    key="new_correct_answer"
                )

                add_question = st.form_submit_button(
                    "➕ Add Question",
                    use_container_width=True
                )

                if add_question:

                    if (
                        new_question.strip()
                        and all(option.strip() for option in new_options)
                    ):

                        st.session_state.admin_questions.append({
                            "skill": new_skill,
                            "question": new_question.strip(),
                            "options": [
                                option.strip()
                                for option in new_options
                            ],
                            "answer": new_options[new_correct_answer].strip()
                        })

                        st.success("New question added successfully.")
                        st.rerun()

                    else:
                        st.error(
                            "Please complete the question and all four choices."
                        )

    
        # -----------------------------
        # SAVE ASSESSMENT
        # -----------------------------
        st.markdown("---")
        st.markdown("### 💾 Save Assessment")

        st.caption(
            "Once all comprehension questions are ready, "
            "save the complete assessment as a new record."
        )

        if st.button(
            "💾 Save Assessment",
            key="save_assessment_button",
            use_container_width=True
        ):

            if not st.session_state.admin_questions:
                st.error(
                    "Please add at least one comprehension question."
                )

            else:
                existing_ids = [
                    item["Assessment ID"]
                    for item in st.session_state.saved_assessments
                ]

                next_id = max(existing_ids, default=0) + 1

                new_assessment = {
                    "Assessment ID": next_id,
                    "Passage Title": st.session_state.admin_passage_title,
                    "Topic": st.session_state.admin_passage_topic,
                    "Reading Level": st.session_state.admin_passage_level,
                    "Reading Material": st.session_state.admin_passage_content,
                    "Questions": [
                        question.copy()
                        for question in st.session_state.admin_questions
                    ],
                    "Total Questions": len(
                        st.session_state.admin_questions
                    ),
                    "Status": "Saved"
                }

                st.session_state.saved_assessments.append(
                    new_assessment
                )

                # Reset the wizard for a new assessment
                st.session_state.admin_passage_title = ""
                st.session_state.admin_passage_topic = ""
                st.session_state.admin_passage_level = "Secondary Education"
                st.session_state.admin_passage_content = ""
                st.session_state.admin_questions = []

                st.session_state.passage_info_saved = False
                st.session_state.reading_material_saved = False

                for key in [
                    "new_question_skill",
                    "new_question_text",
                    "new_question_choice_0",
                    "new_question_choice_1",
                    "new_question_choice_2",
                    "new_question_choice_3",
                    "new_correct_answer"
                ]:
                    if key in st.session_state:
                        del st.session_state[key]

                st.session_state.selected_assessment_id = None

                st.success(
                    "New assessment saved successfully!"
                )
                st.rerun()

    # -----------------------------
    # SAVED ASSESSMENTS TABLE
    # -----------------------------
    st.markdown("---")
    st.markdown("## 📋 Saved Assessments")

    if "selected_assessment_id" not in st.session_state:
        st.session_state.selected_assessment_id = None

    if st.session_state.saved_assessments:

        # TABLE HEADER
        header_cols = st.columns([0.6, 2, 1.3, 1, 1, 1.5])

        header_cols[0].markdown("**ID**")
        header_cols[1].markdown("**Passage Title**")
        header_cols[2].markdown("**Reading Level**")
        header_cols[3].markdown("**Questions**")
        header_cols[4].markdown("**Status**")
        header_cols[5].markdown("**Action**")

        st.divider()

        # DISPLAY SAVED ASSESSMENTS
        for assessment in st.session_state.saved_assessments:

            cols = st.columns([0.6, 2, 1.3, 1, 1, 1.5])

            cols[0].write(assessment["Assessment ID"])
            cols[1].write(assessment["Passage Title"])
            cols[2].write(assessment["Reading Level"])
            cols[3].write(assessment["Total Questions"])
            cols[4].write(assessment["Status"])

            # VIEW DETAILS BUTTON
            if cols[5].button(
                "View Details",
                key=f"view_assessment_{assessment['Assessment ID']}",
                use_container_width=True
            ):
                st.session_state.selected_assessment_id = assessment["Assessment ID"]
                st.rerun()

           # -----------------------------
        # INTERACTIVE ASSESSMENT DETAILS
        # -----------------------------
        selected_assessment = next(
            (
                assessment
                for assessment in st.session_state.saved_assessments
                if assessment["Assessment ID"]
                == st.session_state.selected_assessment_id
            ),
            None
        )

        if selected_assessment:

            assessment_id = selected_assessment["Assessment ID"]

            st.markdown("---")
            st.markdown("## 📖 Assessment Details")

            st.markdown(
                f"### {selected_assessment['Passage Title']}"
            )

            detail_cols = st.columns(3)

            detail_cols[0].metric(
                "Assessment ID",
                assessment_id
            )

            detail_cols[1].metric(
                "Reading Level",
                selected_assessment["Reading Level"]
            )

            detail_cols[2].metric(
                "Total Questions",
                len(selected_assessment["Questions"])
            )

            st.divider()

            # ==================================
            # EDIT PASSAGE INFORMATION
            # ==================================
            st.markdown("### 📚 Passage Information")

            with st.expander(
                "✏️ Edit Passage Information",
                expanded=False
            ):

                with st.form(
                    f"edit_passage_details_{assessment_id}"
                ):

                    edited_title = st.text_input(
                        "Passage Title",
                        value=selected_assessment["Passage Title"]
                    )

                    edited_topic = st.text_input(
                        "Topic",
                        value=selected_assessment["Topic"]
                    )

                    level_options = [
                        "Elementary",
                        "Junior High School",
                        "Secondary Education",
                        "Senior High School"
                    ]

                    current_level = selected_assessment["Reading Level"]

                    edited_level = st.selectbox(
                        "Reading Level",
                        level_options,
                        index=(
                            level_options.index(current_level)
                            if current_level in level_options else 2
                        )
                    )

                    save_passage_changes = st.form_submit_button(
                        "Save Passage Information",
                        use_container_width=True
                    )

                    if save_passage_changes:

                        if edited_title.strip() and edited_topic.strip():

                            for assessment in st.session_state.saved_assessments:

                                if assessment["Assessment ID"] == assessment_id:

                                    assessment["Passage Title"] = edited_title.strip()
                                    assessment["Topic"] = edited_topic.strip()
                                    assessment["Reading Level"] = edited_level

                                    break

                            st.success(
                                "Passage Information updated successfully!"
                            )
                            st.rerun()

                        else:
                            st.error(
                                "Please complete the Passage Title and Topic."
                            )

            # ==================================
            # EDIT READING MATERIAL
            # ==================================
            st.markdown("### 📖 Reading Material")

            with st.expander(
                "✏️ Edit Reading Material",
                expanded=False
            ):

                with st.form(
                    f"edit_reading_material_{assessment_id}"
                ):

                    edited_material = st.text_area(
                        "Reading Passage Content",
                        value=selected_assessment["Reading Material"],
                        height=350
                    )

                    save_material = st.form_submit_button(
                        "Save Reading Material",
                        use_container_width=True
                    )

                    if save_material:

                        if edited_material.strip():

                            for assessment in st.session_state.saved_assessments:

                                if assessment["Assessment ID"] == assessment_id:

                                    assessment["Reading Material"] = (
                                        edited_material.strip()
                                    )

                                    break

                            st.success(
                                "Reading Material updated successfully!"
                            )
                            st.rerun()

                        else:
                            st.error(
                                "Reading Material cannot be empty."
                            )

            with st.expander("👁️ Preview Reading Material"):

                st.write(selected_assessment["Reading Material"])

            # ==================================
            # ADD NEW QUESTION - COLLAPSIBLE FORM
            # ==================================
            st.markdown("---")
            st.markdown("### ➕ Add New Question")

            # Unique state key for each assessment
            show_add_question_key = f"show_add_question_{assessment_id}"

            if show_add_question_key not in st.session_state:
                st.session_state[show_add_question_key] = False

            # SHOW ADD QUESTION BUTTON
            if not st.session_state[show_add_question_key]:

                if st.button(
                    "➕ Add Question",
                    key=f"open_add_question_{assessment_id}",
                    use_container_width=True
                ):
                    st.session_state[show_add_question_key] = True
                    st.rerun()

            # DISPLAY FORM ONLY WHEN OPENED
            if st.session_state[show_add_question_key]:

                with st.container(border=True):

                    st.markdown("#### New Comprehension Question")
                    st.caption(
                        "Enter the question, four answer choices, "
                        "and select the correct answer."
                    )

                    # COLLAPSE FORM BUTTON
                    if st.button(
                        "▲ Hide Form",
                        key=f"hide_add_question_{assessment_id}"
                    ):
                        st.session_state[show_add_question_key] = False
                        st.rerun()

                    with st.form(
                        f"add_question_details_{assessment_id}"
                    ):

                        added_skill = st.selectbox(
                            "Question Skill",
                            skill_options,
                            key=f"detail_skill_{assessment_id}"
                        )

                        added_question = st.text_input(
                            "Question",
                            key=f"detail_question_{assessment_id}"
                        )

                        added_options = []

                        for i in range(4):

                            added_options.append(
                                st.text_input(
                                    f"Choice {chr(65 + i)}",
                                    key=f"detail_option_{assessment_id}_{i}"
                                )
                            )

                        added_correct_answer = st.selectbox(
                            "Correct Answer",
                            options=[0, 1, 2, 3],
                            format_func=lambda x: f"Choice {chr(65 + x)}",
                            key=f"detail_answer_{assessment_id}"
                        )

                        add_question_details = st.form_submit_button(
                            "💾 Save Question",
                            use_container_width=True
                        )

                        if add_question_details:

                            if (
                                added_question.strip()
                                and all(
                                    option.strip()
                                    for option in added_options
                                )
                            ):

                                for assessment in st.session_state.saved_assessments:

                                    if assessment["Assessment ID"] == assessment_id:

                                        assessment["Questions"].append({
                                            "skill": added_skill,
                                            "question": added_question.strip(),
                                            "options": [
                                                option.strip()
                                                for option in added_options
                                            ],
                                            "answer": added_options[
                                                added_correct_answer
                                            ].strip()
                                        })

                                        assessment["Total Questions"] = len(
                                            assessment["Questions"]
                                        )

                                        break

                                st.session_state[show_add_question_key] = False

                                st.success(
                                    "New question added successfully!"
                                )
                                st.rerun()

                            else:
                                st.error(
                                    "Please complete the question and all four choices."
                                )

                    # CANCEL BUTTON - OUTSIDE THE FORM
                    if st.button(
                        "Cancel",
                        key=f"cancel_add_question_{assessment_id}",
                        use_container_width=True
                    ):
                        st.session_state[show_add_question_key] = False
                        st.rerun()
            # ==================================
            # EXISTING QUESTIONS
            # ==================================
            st.markdown("---")
            st.markdown("### 📝 Comprehension Questions")

            for index, question in enumerate(
                selected_assessment["Questions"]
            ):

                with st.expander(
                    f"Question {index + 1} — {question['skill']}"
                ):

                    st.write(f"**{question['question']}**")

                    for option_index, option in enumerate(
                        question["options"]
                    ):
                        st.write(
                            f"{chr(65 + option_index)}. {option}"
                        )

                    st.write(
                        f"**Correct Answer:** {question['answer']}"
                    )

                    # EDIT QUESTION
                    with st.form(
                        f"edit_detail_question_{assessment_id}_{index}"
                    ):

                        current_skill_index = (
                            skill_options.index(question["skill"])
                            if question["skill"] in skill_options else 0
                        )

                        updated_skill = st.selectbox(
                            "Question Skill",
                            skill_options,
                            index=current_skill_index
                        )

                        updated_question = st.text_input(
                            "Question",
                            value=question["question"]
                        )

                        updated_options = []

                        for option_index, option in enumerate(
                            question["options"]
                        ):

                            updated_options.append(
                                st.text_input(
                                    f"Choice {chr(65 + option_index)}",
                                    value=option
                                )
                            )

                        current_answer_index = question["options"].index(
                            question["answer"]
                        )

                        updated_answer = st.selectbox(
                            "Correct Answer",
                            options=[0, 1, 2, 3],
                            index=current_answer_index,
                            format_func=lambda x: f"Choice {chr(65 + x)}"
                        )

                        update_question = st.form_submit_button(
                            "Save Question Changes",
                            use_container_width=True
                        )

                        if update_question:

                            if (
                                updated_question.strip()
                                and all(
                                    option.strip()
                                    for option in updated_options
                                )
                            ):

                                for assessment in st.session_state.saved_assessments:

                                    if assessment["Assessment ID"] == assessment_id:

                                        assessment["Questions"][index] = {
                                            "skill": updated_skill,
                                            "question": updated_question.strip(),
                                            "options": [
                                                option.strip()
                                                for option in updated_options
                                            ],
                                            "answer": updated_options[
                                                updated_answer
                                            ].strip()
                                        }

                                        break

                                st.success("Question updated successfully!")
                                st.rerun()

                            else:
                                st.error(
                                    "Please complete the question and all choices."
                                )

                    # DELETE QUESTION
                    if st.button(
                        "🗑️ Delete Question",
                        key=f"delete_detail_question_{assessment_id}_{index}",
                        use_container_width=True
                    ):

                        for assessment in st.session_state.saved_assessments:

                            if assessment["Assessment ID"] == assessment_id:

                                assessment["Questions"].pop(index)

                                assessment["Total Questions"] = len(
                                    assessment["Questions"]
                                )

                                break

                        st.success("Question deleted successfully!")
                        st.rerun()

            # ==================================
            # ASSESSMENT ACTION PANEL
            # ==================================
            st.markdown("---")

            with st.container(border=True):

                st.markdown("### ⚙️ Assessment Actions")

                st.caption(
                    "Manage the changes made to this assessment."
                )

                action_col1, action_col2, action_col3 = st.columns(
                    [2, 1.5, 1]
                )

                # SAVE CHANGES - PRIMARY ACTION
                with action_col1:

                    if st.button(
                        "💾 Save Changes",
                        key=f"save_assessment_changes_{assessment_id}",
                        type="primary",
                        use_container_width=True
                    ):

                        for assessment in st.session_state.saved_assessments:

                            if assessment["Assessment ID"] == assessment_id:

                                assessment["Total Questions"] = len(
                                    assessment["Questions"]
                                )

                                assessment["Status"] = "Saved"
                                break

                        st.success("Assessment changes saved successfully!")
                        st.rerun()

                # DELETE ASSESSMENT - SECONDARY ACTION
                with action_col2:

                    if st.button(
                        "🗑️ Delete Assessment",
                        key=f"delete_assessment_{assessment_id}",
                        type="secondary",
                        use_container_width=True
                    ):

                        st.session_state.pending_delete_id = assessment_id
                        st.rerun()

                # CLOSE DETAILS
                with action_col3:

                    if st.button(
                        "Close Details",
                        key=f"close_details_{assessment_id}",
                        type="secondary",
                        use_container_width=True
                    ):

                        st.session_state.selected_assessment_id = None
                        st.session_state.pending_delete_id = None
                        st.rerun()

                # DELETE CONFIRMATION
                if st.session_state.pending_delete_id == assessment_id:

                    st.divider()

                    st.warning(
                        f"Are you sure you want to delete "
                        f"'{selected_assessment['Passage Title']}'? "
                        "This will also remove its reading material "
                        "and all associated questions."
                    )

                    confirm_col, cancel_col = st.columns(2)

                    with confirm_col:

                        if st.button(
                            "Yes, Delete Assessment",
                            key=f"confirm_delete_{assessment_id}",
                            type="primary",
                            use_container_width=True
                        ):

                            st.session_state.saved_assessments = [
                                item
                                for item in st.session_state.saved_assessments
                                if item["Assessment ID"] != assessment_id
                            ]

                            st.session_state.selected_assessment_id = None
                            st.session_state.pending_delete_id = None

                            st.success("Assessment deleted successfully!")
                            st.rerun()

                    with cancel_col:

                        if st.button(
                            "Cancel",
                            key=f"cancel_delete_{assessment_id}",
                            use_container_width=True
                        ):

                            st.session_state.pending_delete_id = None
                            st.rerun()

    # -----------------------------
    # DYNAMIC ASSESSMENT SUMMARY
    # -----------------------------
    st.markdown("---")
    st.markdown("### 📊 Assessment Summary")

    selected_summary = next(
        (
            assessment
            for assessment in st.session_state.saved_assessments
            if assessment["Assessment ID"]
            == st.session_state.selected_assessment_id
        ),
        None
    )

    if selected_summary:

        passage_completed = (
            bool(selected_summary.get("Passage Title", "").strip())
            and bool(selected_summary.get("Topic", "").strip())
            and bool(selected_summary.get("Reading Level", "").strip())
        )

        material_completed = bool(
            selected_summary.get("Reading Material", "").strip()
        )

        questions_completed = (
            len(selected_summary.get("Questions", [])) > 0
        )

        summary_col1, summary_col2, summary_col3 = st.columns(3)

        with summary_col1:
            st.metric(
                "Passage Information",
                "Completed" if passage_completed else "Pending"
            )

        with summary_col2:
            st.metric(
                "Reading Material",
                "Completed" if material_completed else "Pending"
            )

        with summary_col3:
            st.metric(
                "Comprehension Questions",
                "Completed" if questions_completed else "Pending"
            )

        st.caption(
            f"Assessment ID: {selected_summary['Assessment ID']} | "
            f"{selected_summary['Passage Title']}"
        )

    else:
        st.info(
            "Click View Details on a saved assessment "
            "to display its assessment summary."
        )

    st.caption(
        "Administrator content management prototype. Changes are stored "
        "in the current Streamlit session only and are not yet saved permanently."
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
