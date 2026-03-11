import streamlit as st
import pandas as pd

st.set_page_config(page_title="Studder", layout="wide")

# storage for study plans
if "plans" not in st.session_state:
    st.session_state.plans = []

# Sidebar Navigation
page = st.sidebar.selectbox(
    "Navigation",
    ["Home", "Study Planner", "Saved Plans", "Progress", "Resources", "Settings", "About"]
)

# ---------------- HOME ----------------
if page == "Home":

    st.title("📚 Studder: Student Study Planner App")
    st.header("Welcome!")
    st.subheader("Organize your study schedule easily")

    st.write(
        "This app helps students organize their study plans, manage subjects, "
        "and track progress in a simple and interactive way."
    )

    st.image("https://images.unsplash.com/photo-1524995997946-a1c2e315a42f")

    st.divider()

    st.info("Use the sidebar to navigate through the app.")

    if st.button("Start Planning"):
        st.success("Go to the Study Planner page using the sidebar!")

# ---------------- STUDY PLANNER ----------------
elif page == "Study Planner":

    st.title("📝 Create Your Study Plan")

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Student Name")
        subject = st.text_input("Subject")

        category = st.selectbox(
            "Subject Category",
            ["Math", "Science", "Programming", "History", "Language"]
        )

        study_date = st.date_input("Study Date")
        study_time = st.time_input("Study Time")

        hours = st.number_input("Study Hours", min_value=1, max_value=12)

    with col2:

        topics = st.multiselect(
            "Topics to Study",
            ["Chapter 1", "Chapter 2", "Exercises", "Practice Test"]
        )

        difficulty = st.slider(
            "Difficulty Level",
            1, 10
        )

        study_type = st.radio(
            "Study Type",
            ["Reading", "Practice", "Review"]
        )

        priority = st.checkbox("Mark as Priority")

        notes = st.text_area("Additional Notes")

        color = st.color_picker("Pick a highlight color")

    uploaded_file = st.file_uploader("Upload study materials")

if st.button("Save Study Plan"): 

    new_plan = {
        "Name": name,
        "Subject": subject,
        "Category": category,
        "Date": study_date,
        "Time": study_time,
        "Hours": hours,
        "Topics": ", ".join(topics),
        "Difficulty": difficulty,
        "Type": study_type,
        "Priority": priority,
        "Notes": notes,
    }

    st.session_state.plans.append(new_plan)

    st.success("Study plan saved successfully!")
    st.balloons()
    
# ---------------- Saved Plans ----------------
elif page == "Saved Plans":

    st.title("📂 Saved Study Plans")

    if len(st.session_state.plans) == 0:
        st.warning("No study plans saved yet.")

    else:
        df = pd.DataFrame(st.session_state.plans)

        st.dataframe(df)

        st.subheader("Review a Plan")

        selected_subject = st.selectbox(
            "Select a study plan",
            df["Subject"]
        )

        selected_plan = df[df["Subject"] == selected_subject]

        st.write(selected_plan)

# ---------------- PROGRESS ----------------
elif page == "Progress":

    st.title("📊 Study Progress")

    if len(st.session_state.plans) == 0:
        st.warning("No study plans yet.")

    else:

        df = pd.DataFrame(st.session_state.plans)

        total_subjects = len(df)
        total_hours = df["Hours"].sum()

        st.metric("Subjects Planned", total_subjects)
        st.metric("Total Study Hours", total_hours)

        completion = st.slider("Study Completion", 0, 100)

        st.progress(completion)

        st.subheader("Study Plan Overview")

        st.dataframe(df)

# ---------------- RESOURCES ----------------
elif page == "Resources":

    st.title("📖 Study Resources")

    tab1, tab2, tab3 = st.tabs(["Books", "Websites", "Videos"])

    with tab1:
        st.write("Recommended Study Books")
        st.checkbox("Atomic Habits")
        st.checkbox("Deep Work")
        st.checkbox("Make It Stick")

    with tab2:
        st.write("Useful Learning Websites")
        st.write("- Coursera")
        st.write("- Khan Academy")
        st.write("- edX")

    with tab3:
        st.write("Study Technique Videos")

    with st.expander("Study Tips"):
        st.write("Take breaks and review material regularly.")

# ---------------- SETTINGS ----------------
elif page == "Settings":

    st.title("⚙️ App Settings")

    theme = st.selectbox("Select Theme", ["Light", "Dark"])

    notifications = st.toggle("Enable Notifications")

    daily_goal = st.slider("Daily Study Goal (hours)", 1, 10)

    reminder_time = st.time_input("Reminder Time")

    st.toast("Settings updated!")

# ---------------- ABOUT ----------------
elif page == "About":

    st.title("ℹ️ About This App")

    st.header("What the app does")

    st.write(
        "The Student Study Planner app helps students organize their study schedule. "
        "Users can create study plans, set study hours, choose subjects, and track their progress."
    )

    st.header("Target Users")

    st.write(
        "The main users of this application are high school and college students "
        "who want a simple tool to manage their study time and improve productivity."
    )

    st.header("Inputs Collected")

    st.write(
        "The application collects several inputs from the user such as student name, "
        "subject name, study hours, study date and time, study topics, difficulty level, "
        "priority selection, and personal study notes."
    )

    st.header("Outputs Displayed")

    st.write(
        "The app displays a summary of study plans, progress indicators, metrics "
        "showing study hours and completed tasks, and a table showing subjects "
        "and study time."
    )

    st.info("This Streamlit UI project was created by Keith for the UI Flow assignment.")
