import streamlit as st
import requests

WEB_APP_URL = "https://script.google.com/macros/s/AKfycbyC0SDJ3SF47UD96AL8TNB_UDxi3-ku3hpLCog-dMgZGHTxi1gJBKaILkmXKvY05bV7/exec"

#------------------page config------------------------
st.set_page_config(
    page_title="Deepanshu portfolio",
    page_icon="🤖",
    layout="wide"
)
#-------------------side bar-----------------------
st.sidebar.title("🤖 Deepanshu")
page=st.sidebar.radio(
    "Navigation",
    ["Home","About","Projects","Skills","Contact"]
)
if page=="Home":
    col1,col2=st.columns([1,2])

    with col1:
        st.image(
            "myphoto.png",
            width=220
        )

    with col2:
        st.title("Hi 👋")
        st.header("I'm Deepanshu")
        st.subheader("AI & ML Learning Student")
        st.write(
                    """
                    Welcome to my personal portfolio website.
        
                    I build AI, Machine Learning and Data Science projects using
                    Python, Scikit-Learn and Streamlit.
                    """
        )
    st.divider()
    c1,c2,c3=st.columns(3)

    c1.metric("Projects","15+")
    c2.metric("Skills","10+")
    c3.metric("Experience","Student")

elif page=="About":
    st.subheader("🎓 Education")
    st.write("""
    B.Tech CSE (AI & ML)
    1st Year
    """)

    st.subheader("🎯 Career Goal")
    st.write("""
    To become an AI & Machine Learning Engineer by building real-world projects.
    """)

    st.subheader("🏆 Achievements")
    st.write("""
    ✅ 15+ Projects
    ✅ Python & Machine Learning
    ✅ Streamlit Web Apps
    """)

elif page=="Projects":

    

    st.title("🚀 My Projects")

    # ================= Machine Learning =================

    st.subheader("🤖 Machine Learning Projects")

    with st.container(border=True):
        c1, c2 = st.columns([5,1])

        with c1:
            st.markdown("### 🏠 House Price Prediction")
            st.write("Regression model using Scikit-Learn to predict house prices.")

        with c2:
            st.link_button("🔗 GitHub", "https://github.com/deepanshurajpoot777-cpu/House-Price-Prediction-ML")

    with st.container(border=True):
        c1, c2 = st.columns([5,1])

        with c1:
            st.markdown("### 💰 Loan Approval Prediction")
            st.write("Machine Learning model for loan approval prediction.")

        with c2:
            st.link_button("🔗 GitHub", "https://github.com/deepanshurajpoot777-cpu/loan-approval-prediction-ML")

    with st.container(border=True):
        c1, c2 = st.columns([5,1])

        with c1:
            st.markdown("### 💼 Student Salary Predictor")
            st.write("Regression model to predict employee salaries.")

        with c2:
            st.link_button("🔗 GitHub", "https://github.com/deepanshurajpoot777-cpu/student-salary-prediction")

    with st.container(border=True):
        c1, c2 = st.columns([5,1])

        with c1:
            st.markdown("### 🛒 Customer Segmentation")
            st.write("Customer clustering using K-Means algorithm.")

        with c2:
            st.link_button("🔗 GitHub", "YOUR_REPO_LINK")

    with st.container(border=True):
        c1, c2 = st.columns([5,1])

        with c1:
            st.markdown("### 🛍 Mall Customer Segmentation")
            st.write("Unsupervised learning project using K-Means clustering.")

        with c2:
            st.link_button("🔗 GitHub", "YOUR_REPO_LINK")

    with st.container(border=True):
        c1, c2 = st.columns([5,1])

        with c1:
            st.markdown("### 💳 Credit Card Fraud Detection")
            st.write("Machine Learning model to detect fraudulent transactions.")

        with c2:
            st.link_button("🔗 GitHub", "YOUR_REPO_LINK")

    st.divider()

    # ================= Python =================

    st.subheader("🐍 Python Projects")

    with st.container(border=True):
        c1, c2 = st.columns([5,1])

        with c1:
            st.markdown("### 💰 Expense Tracker")
            st.write("Track daily income and expenses using Python.")

        with c2:
            st.link_button("🔗 GitHub", "https://github.com/deepanshurajpoot777-cpu/Expense-Tracker")

    with st.container(border=True):
        c1, c2 = st.columns([5,1])

        with c1:
            st.markdown("### 🏧 ATM Management System")
            st.write("Console-based ATM application with account operations.")

        with c2:
            st.link_button("🔗 GitHub", "https://github.com/deepanshurajpoot777-cpu/ATM-Managment-System")

    with st.container(border=True):
        c1, c2 = st.columns([5,1])

        with c1:
            st.markdown("### 🎬 Movie Recommender System")
            st.write("Content-based movie recommendation project.")

        with c2:
            st.link_button("🔗 GitHub", "https://github.com/deepanshurajpoot777-cpu/Movie-Recommender-project")

    with st.container(border=True):
        c1, c2 = st.columns([5,1])

        with c1:
            st.markdown("### 📝 Quiz Game (MCQ)")
            st.write("Interactive quiz application developed in Python.")

        with c2:
            st.link_button("🔗 GitHub", "https://github.com/deepanshurajpoot777-cpu/quiz-game-python-mcq")

    st.divider()

    # ================= C =================

    st.subheader("💻 C Language Projects")

    with st.container(border=True):
        c1, c2 = st.columns([5,1])

        with c1:
            st.markdown("### 🧮 Scientific Calculator")
            st.write("Scientific calculator developed using C language.")

        with c2:
            st.link_button("🔗 GitHub", "https://github.com/deepanshurajpoot777-cpu/scientific-calculator-c")

    with st.container(border=True):
        c1, c2 = st.columns([5,1])

        with c1:
            st.markdown("### 📚 Student Record Management System")
            st.write("Student record management system using file handling in C.")

        with c2:
            st.link_button("🔗 GitHub", "https://github.com/deepanshurajpoot777-cpu/student-record-system-c")

    st.divider()

    # ================= Data Analysis =================

    st.subheader("📊 Data Analysis Projects")

    with st.container(border=True):
        c1, c2 = st.columns([5,1])

        with c1:
            st.markdown("### 🌍 World Happiness Data Analysis")
            st.write("Exploratory Data Analysis using Pandas and Matplotlib.")

        with c2:
            st.link_button("🔗 GitHub", "https://github.com/deepanshurajpoot777-cpu/World-Happiness-Data-Analysis")

    with st.container(border=True):
        c1, c2 = st.columns([5,1])

        with c1:
            st.markdown("### 🎥 Netflix Data Analysis")
            st.write("Data visualization and insights using Matplotlib.")

        with c2:
            st.link_button("🔗 GitHub", "YOUR_REPO_LINK")

elif page=="Skills":

    st.title("💻 Programming Languages")

    col1, col2 = st.columns(2)

    with col1:
        st.success("🐍 Python")
        st.success("💾 SQL")

    with col2:
        st.success("💻 C")
        st.success("🔧 Git")

    st.title("🤖 AI & Machine Learning")

    col1, col2 = st.columns(2)

    with col1:
        st.success("Machine Learning")
        st.success("Data Analysis")
        st.success("Data Processing")

    with col2:
        st.success("Scikit-Learn")
        st.success("Data Visualization")
        st.success("Model Evaluation")

    st.title("📚 Libraries")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.success("Pandas")
        st.success("NumPy")

    with col2:
       st.success("Matplotlib")
       st.success("Streamlit")

    with col3:
       st.success("Scikit-Learn")
       st.success("FastAPI")

    st.title("🛠️ Tools")

    col1, col2 = st.columns(2)

    with col1:
       st.success("Git")
       st.success("GitHub")

    with col2:
     st.success("VS Code")

elif page == "Contact":

    st.title("📩 Contact Me")

    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")

    if st.button("Send"):

        if not name or not email or not message:
            st.warning("⚠️ Please fill all the fields.")

        elif "@" not in email:
            st.error("Enter a valid email.")
        else:
            data = {
                "name": name,
                "email": email,
                "message": message
            }

            try:
                with st.spinner("Sending..."):
                     response = requests.post(WEB_APP_URL, json=data)
                if response.status_code == 200:
                    st.success("✅ Thank you! Your message has been sent.")
                else:
                    st.error("❌ Failed to send message.")
        
            except Exception as e:
                st.error(f"Error: {e}")

    st.divider()

    st.caption("© 2026 Deepanshu | Built with ❤️ using Streamlit")

    st.write("📧 Email : deepanshurajpoot777@gmail.com")
    st.link_button(
    "⭐ Visit My GitHub",
    "https://github.com/deepanshurajpoot777-cpu"
    )
    st.link_button(
    "💼 Connect on LinkedIn",
    "https://www.linkedin.com/in/deepanshu-rajpoot-a67467380"
    )