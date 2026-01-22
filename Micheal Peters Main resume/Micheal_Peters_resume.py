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
    resume_path = "Micheal_Peters_CV.pdf"
    
    if os.path.exists(resume_path):
        with open(resume_path, "rb") as file:
            pdf_byte = file.read()
        st.download_button(
            label="Download My Full CV",
            data=pdf_byte,
            file_name="Micheal_Peters_CV.pdf",
            mime="application/pdf",
            help="Click here to download my official academic CV."
        )
    else:
        st.info("Upload 'Micheal_Peters_CV.pdf' to GitHub to enable download.")

    st.markdown("---")
    
    select_option = st.radio("Go to", ("Resume", "Portfolio", "About", "Contact"))
    
    st.markdown("---")
    
    st.subheader("Settings")
    st.write("Pick a theme color:")
    selected_color = st.color_picker("", "#0000FF")
    st.markdown(f"<h1 style='color:{selected_color};'>My Title</h1>", unsafe_allow_html=True)
    
    st.markdown("---")
    st.subheader("📫 Contact Me")
    st.markdown("Feel free to reach out via [mmpeters626@gmail.com](mailto:mmpeters626@gmail.com) or connect on [LinkedIn](https://www.linkedin.com/in/petersmicheal/)")

# --- RESUME PAGE ---
if select_option == "Resume":
    st.header("MICHEAL PETERS' Portfolio and Resume")
    
    if not st.session_state.name:
        temp_name = st.text_input('Hi there!, Can you please provide your name😊?')
        temp_addressed = st.selectbox('How are you addressed?', options=['Mr', 'Miss', 'Mrs', 'Master', 'Mistress', 'Sir', 'Ma'])
        
        if st.button('Submit'):
            st.session_state.name = temp_name
            st.session_state.addressed = temp_addressed
            st.rerun()

    if st.session_state.name:
        st.write(f"Hi {st.session_state.addressed} {st.session_state.name}!, WELCOME!!! to my resume😍.")
        
        # --- PROFILE PICTURE LOGIC ---
        def get_base64_image(image_path):
            try:
                if os.path.exists(image_path):
                    with open(image_path, "rb") as img_file:
                        return base64.b64encode(img_file.read()).decode("utf-8")
                return None
            except Exception:
                return None

        profile_image_base64 = get_base64_image("My Profile Pics.jpg")
        
        if profile_image_base64:
            st.markdown(
                f"""
                <div style="display: flex; justify-content: center;">
                    <img src="data:image/jpg;base64,{profile_image_base64}" 
                         style="border-radius: 50%; width: 200px; height: 200px; object-fit: cover; border: 4px solid {selected_color};">
                </div>
                """, 
                unsafe_allow_html=True
            )
        else:
            st.warning("Profile picture 'My Profile Pics.jpg' not found in directory.")
        
        st.markdown("---")
    
    st.title("My Resume")
    st.markdown("### MICHEAL PETERS")
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
        **Customer Churn Prediction**
        - Developed a classification model using Python and Scikit-learn, achieving 85% accuracy.
        
        **Car Prices Prediction App**
        - Built a regression model to estimate market value of vehicles.

        **Student Performance Prediction**
        - Analyzed socio-economic factors to predict academic success.
        """
    )

# --- PORTFOLIO PAGE ---
elif select_option == "Portfolio":
    st.title("My Portfolio")
    
    greeting = f"Hi! {st.session_state.addressed} {st.session_state.name}, " if st.session_state.name else ""
    st.markdown(f"{greeting}Welcome to my portfolio! Here you will find my key Data Science projects.")

    st.subheader("Project Showcase")
    
    st.markdown("#### Customer Churn Prediction App")
    st.write("- Classification model achieving 85% accuracy using Scikit-learn.")
    
    st.markdown("#### Car Prices Prediction App")
    st.write("- Regression model achieving 81% accuracy for market valuation.")
    
    st.markdown("#### Student performance Prediction")
    st.write("- Predictive modeling for academic outcomes using behavioral data.")
    
    st.markdown("#### Weather App")
    st.write("- Real-time weather interface: [Launch App](https://whether-app-mop.streamlit.app)")

# --- ABOUT & CONTACT (Stay same as your original) ---
elif select_option == "About":
    st.title("About Me")
    st.markdown("I am an aspiring data scientist currently pursuing my degree at the University of Yaba, Lagos.")

elif select_option == "Contact":
    st.title("Contact")
    st.markdown("- **Email:** mmpeters626@gmail.com")
    st.markdown("- **LinkedIn:** https://www.linkedin.com/in/petersmicheal/")

# --- FOOTER ---
st.markdown("---")
st.markdown("**_Built Using Python and Streamlit_**")
st.markdown("### _Micheal Peters_")