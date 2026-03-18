import streamlit as st
import base64
import os

# --- SESSION STATE ---
if 'name' not in st.session_state:
    st.session_state.name = None
if 'addressed' not in st.session_state:
    st.session_state.addressed = None

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.header("MICHEAL PETERS")
    
    if st.session_state.name and st.session_state.addressed:
        st.write(f"Welcome to my portfolio and resume {st.session_state.addressed} {st.session_state.name}. 👋")
    else:
        st.write("Welcome to my portfolio and resume. 👋")
    
    st.markdown("---")
    
    # --- DOWNLOAD CV BUTTON ---
    st.subheader("📄 Resume PDF")
    resume_path = "Mikes_full_cv.pdf"
    
    if os.path.exists(resume_path):
        with open(resume_path, "rb") as file:
            pdf_byte = file.read()
        st.download_button(
            label="Download My Full CV",
            data=pdf_byte,
            file_name="Mikes_full_cv.pdf",
            mime="application/pdf",
            help="Click here to download my official academic CV."
        )
    else:
        st.info("Upload 'Mikes_full_CV.pdf' to GitHub to enable download.")

    st.markdown("---")
    
    select_option = st.radio("Go to", ("Resume", "Portfolio", "About", "Contact"))
    
    st.markdown("---")
    
    st.subheader("Settings")
    st.write("Pick a theme color:")
    selected_color = st.color_picker("", "#0000FF")
    
    st.markdown("---")
    st.subheader("📫 Contact Me")
    st.markdown("Feel free to reach out via [mmpeters626@gmail.com](mailto:mmpeters626@gmail.com) or connect on [LinkedIn](https://www.linkedin.com/in/petersmicheal/)")

# --- RESUME PAGE ---
if select_option == "Resume":
    st.header("MICHEAL PETERS' Portfolio and Resume")
    
    # Optional Name Input - Content is NOT hidden behind this anymore
    if not st.session_state.name:
        temp_name = st.text_input('Hi there!, kindly provide your name😊?')
        temp_addressed = st.selectbox('How are you addressed?', options=['Mr', 'Miss', 'Mrs', 'Master', 'Mistress', 'Sir', 'Ma'])
        if st.button('Submit'):
            if temp_name:
                st.session_state.name = temp_name
                st.session_state.addressed = temp_addressed
                st.rerun()

    if st.session_state.name:
        st.write(f"Hi {st.session_state.addressed} {st.session_state.name}!, WELCOME!! to my resume.")
        
    # --- PROFILE PICTURE LOGIC (SQUARE) ---
    st.markdown("""
    <style>
    .stMarkdown p, .stMarkdown li {
        font-size: 14px !important;
        line-height: 1.5;
    }
    .profile-img {
        border-radius: 4px; 
        width: 250px;
        height: auto;
        object-fit: contain;
        display: block;
        margin-left: auto;
        margin-right: auto;
        border: 1px solid #ddd;
    }
    </style>
    """, unsafe_allow_html=True)

    def get_base64_image(image_path):
        try:
            if os.path.exists(image_path):
                with open(image_path, "rb") as img_file:
                    return base64.b64encode(img_file.read()).decode("utf-8")
        except Exception:
            return None
        return None

    profile_image_base64 = get_base64_image("My Profile Pics.jpg")
    
    if profile_image_base64:
        st.markdown(f'<img src="data:image/png;base64,{profile_image_base64}" class="profile-img">', unsafe_allow_html=True)
    else:
        st.info("Upload your photo as 'My Profile Pics.jpg' to see it here.")

    st.markdown("---")

    # --- RESUME BODY (ALWAYS VISIBLE) ---
    st.title("My Resume")
    st.markdown(f"<h2 style='color:{selected_color};'>MICHEAL PETERS</h2>", unsafe_allow_html=True)
    st.markdown(
        """
        - Address: 3, Lalubu Street, Okeilewo, Abeokuta, Ogun State
        - Phone: 08146399129
        - Email: mmpeters626@gmail.com
        - LinkedIn: https://www.linkedin.com/in/petersmicheal/
        """
    )
    st.markdown("---")

    st.markdown("### OBJECTIVE")
    st.markdown(
        """
        Enthusiastic and detail-oriented aspiring Data Scientist with a strong foundation 
        in statistical analysis, machine learning, and data visualization. Eager to apply 
        academic knowledge and technical skills to real-world projects.
        """
    )
    st.markdown("---")

    st.markdown("### SKILLS")
    st.markdown(
        """
        - Programming: Python (Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn)
        - Data Analysis & Visualization
        - Machine Learning: Linear Regression, Logistic Regression, Decision Trees, Random Forest
        - SQL & Databases
        - Statistical Analysis & Hypothesis Testing
        """
    )
    st.markdown("---")

    st.markdown("### EDUCATION")
    st.markdown(
        """
        **Bachelor of Science in Education (BSc.Ed) in Technology Education (in view)**
        University of Yaba, Lagos
        *Expected Graduation: August 2026*
        *Relevant Coursework: Engineering Mathematics, Data Structures, Statistics, Machine Learning*
        """
    )
    st.markdown("---")

    st.markdown("### PROJECTS")
    st.markdown(
        """
        Explainable MTN Customer Churn Prediction App | Live Link: mtn customerchurn.streamlit.app
        - Developed a classification model using Scikit-learn to identify high-risk customers, 
        achieving 75% accuracy.
        - Performed end-to-end data cleaning and feature engineering to address class 
        imbalances.
        - Deployed via Streamlit to provide stakeholders with an interactive interface for real time retention insights.
                
        Student Performance Analytics Engine
        - Built a predictive system to forecast student outcomes with 85% accuracy.
        - Leveraged pedagogical insights from my Technology Education background to 
        engineer features related to socio-economic factors.
        - Aimed at providing early-warning systems for educational institutions to improve 
        intervention strategies.
        
        Car Price Prediction
        - Engineered a Regression model to estimate vehicle market values, achieving 81% 
        accuracy.
        - Optimized model performance through outlier detection and advanced categorical 
        encoding of vehicle specifications.
        
        Predictive Diabetes Health Tracker
        - Developed a healthcare-focused model to predict the likelihood of diabetes based 
        on clinical metrics.
        - Conducted deep EDA to identify critical correlations between BMI, glucose levels, 
        and patient outcomes.
        Real-Time Global Weather Intelligence | Live link: https://whether-appmop.streamlit.app/
        - Architected a Python application using Streamlit that fetches and visualizes live 
        meteorological data via API.
        - Demonstrated proficiency in handling real-time data streams and cloud-based 
        deployment.
                
        """
    )
    st.markdown("---")

    st.markdown("### CERTIFICATIONS AND COURSES")
    st.markdown(
        """
        - What is Data Science – Coursera, hopkin University
        - Datascience EDA and PREP – Udemy, Stanford University
        - Data Analysis with Python – freeCodeCamp
        """
    )
    st.markdown("---")

    st.markdown("### EXTRACURRICULAR ACTIVITIES")
    st.markdown(
        """
        - Member of [University Data Science Club]
        - Participated in Kaggle competitions (if applicable)
        - Volunteered for data analysis projects at [Organization Name]
        """
    )
    st.markdown("---")

    st.markdown("### LANGUAGES")
    st.markdown("- English (Fluent)")


# --- PORTFOLIO PAGE ---
elif select_option == "Portfolio":
    st.title("My Portfolio")
    
    if st.session_state.name:
        st.markdown(f"Hi! {st.session_state.addressed} {st.session_state.name}, welcome to my portfolio!")
    else:
        st.markdown("Welcome to my portfolio!")
        
    st.markdown(
        """
        Here you will find some of my key projects and work. 
        Each project showcases my skills in data science, machine learning, and data visualization.
        """
    )

    st.subheader("Project Showcase")
    
    st.markdown("#### Customer Churn Prediction App")
    st.write("- Developed a classification model to predict customer churn using Python and Scikit-learn, achieving 85% accuracy \n"
              "- Performed data cleaning, feature engineering, and model evaluation.")
    st.markdown("---")
    
    st.markdown("#### Car Prices Prediction App")
    st.write("- Developed a Regression model to predict car prices using Python and Scikit-learn, achieving 81% accuracy \n"
              "- Performed data cleaning, feature engineering, and model evaluation.")
    st.markdown("---")
    
    st.markdown("#### Student performance Prediction")
    st.write("- Developed a classification model to predict students perfomances using Python and Scikit-learn, achieving 85% accuracy \n"
              "- Performed data cleaning, feature engineering, and model evaluation.")
    st.markdown("---")
    
    st.markdown("#### Diabetes Prediction")
    st.write("- Developed a classification model to predict the tendency of an individual to have diabetes \n"
              "- Performed data cleaning, feature engineering, and model evaluation.")
    st.markdown("---")
    
    st.markdown("#### Weather App")
    st.write("- Built a Python application using Streamlit for real-time weather info.\n"
              "[Launch App](https://whether-app-mop.streamlit.app)")
    st.markdown("---")

# --- ABOUT & CONTACT ---
elif select_option == "About":
    st.title("About Me")
    if st.session_state.name:
        st.markdown(f"### Hi {st.session_state.addressed} {st.session_state.name}!!, This a brief overview about me")
    else:
        st.markdown("## Hi!!, This a brief overview about me")

    st.markdown(
        """
        I am a passionate and driven aspiring data scientist with a knack for solving problems
        and uncovering insights from data. I am currently pursuing my Bachelor of Science in 
        Education (BSc.Ed) in Technology Education at the University of Yaba, Lagos. 
        My goal is to leverage my skills in data science and machine learning to contribute
        to meaningful, data-driven solutions.
        """
    )
    st.markdown("---")

    st.markdown("### My Hobbies")
    st.markdown("- Studying")
    st.markdown("- Making Researches")
    st.markdown("- Praying")

elif select_option == "Contact":
    st.title("Contact")
    if st.session_state.name:
        st.markdown(
            f"""
            Thank you for visiting my portfolio and resume! {st.session_state.addressed} {st.session_state.name} 🙏👏🤗🤩
            feel free to connect with me via.
            """
        )
    else:
        st.markdown(
            """
            Thank you for visiting my portfolio and resume! 🙏👏🤗🤩
            Please feel free to connect with me via.
            """
        )
    st.markdown(
        """
        - **Email:** mmpeters626@gmail.com
        - **Phone:** 08146399129 0r 08112398005
        - **LinkedIn:** https://www.linkedin.com/in/petersmicheal/
        """
    )


st.markdown("---")
st.markdown(r"""
            **_Built Using Python and Streamlit_**
            """)
st.markdown("### _Micheal Peters_")

st.markdown("---")


#py -m streamlit run Micheal_Peters_resume.py