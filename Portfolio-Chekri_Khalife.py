import streamlit as st
from PIL import Image

# Page configuration
st.set_page_config(page_title="Portfolio - Chekri Khalife", layout="wide", initial_sidebar_state="expanded")
st.markdown(
    """
    <style>
    .big-font {
        font-size:30px !important;
        font-weight: bold;
    }
    .medium-font {
        font-size:20px !important;
        font-weight: bold;
    }
    .info-text {
        font-size:16px !important;
    }
    .sidebar .sidebar-content {
        background-image: linear-gradient(#D6EAF8, #D4E6F1);
    }
    .img-box {
        max-width: 300px;
        max-height: 300px;
        margin: 10px;
    }
    </style>
    """, unsafe_allow_html=True
)

# Sidebar
st.sidebar.title("Portfolio Sections")
options = st.sidebar.radio("Navigate", ["About Me", "Education", "Experience", "Extracurricular Activities", "Awards", "Projects"])

# About Me Section
if options == "About Me":
    st.markdown('<p class="big-font">About Me</p>', unsafe_allow_html=True)
    try:
        image = Image.open('Chekri Image.jpeg')
        image = image.resize((300, 300))  # Resize the image
        st.image(image, caption='Chekri Khalife', use_column_width=False, output_format='PNG')
    except:
        st.error("Profile image not found. Please update the path.")
    st.markdown("""
    **Name:** Chekri Khalife  
    **Age:** 22  
    **Education:** Master of Science in Business Analytics, American University of Beirut  
    **Background:**  
    As a Master of Science in Business Analytics student at the American University of Beirut, I am passionate about applying my research and analytical skills to solve complex business and developmental challenges. With a Bachelor of Arts in Economics and a Minor in Data Science, I have a strong foundation in quantitative methods, statistical modeling, and data visualization.  
    **Scholarships:** USAID Scholarship (Undergraduate), Mastercard Scholarship (Graduate)
    """, unsafe_allow_html=True)

# Other Sections
elif options == "Education":
    st.markdown('<p class="big-font">Education</p>', unsafe_allow_html=True)
    st.markdown("""
    - **Master’s in Business Analytics** (Aug 2023 - Present)
        - GPA: 4.00, Mastercard Scholarship awardee
    - **BA in Economics** (Sep 2019 – Dec 2022)
        - GPA: 4.00 High Distinction, USAID Scholarship awardee
        - Minor in Data Science
    - **Lebanese Baccalaureate**, MSA Abra– Abra, Lebanon (Sep 2004- Jun 2019)
        - General Sciences section, Honor and Distinction
    """)

elif options == "Experience":
    st.markdown('<p class="big-font">Professional Experience</p>', unsafe_allow_html=True)
    st.markdown("""
    **Senior Business Analyst at Maids.cc (Jan 2023 – Aug 2023):**
    - Led a team of three analysts and the onboarding department, as well as the YAYA app, coordinating with various cross-departmental teams.
    - Managed detailed project requirements and authored specifications processed through Jira for validation by technical BAs for development.
    - Analyzed reports to identify operational problems, implementing data-driven solutions to enhance business processes.
    - Conducted extensive testing of new requirements to ensure high-quality functionality across an ERP system, two applications, and a website.
    - Streamlined the maid onboarding process, reducing the time for maids to become available to clients by 70%, enhancing client satisfaction and operational efficiency.
    - Automated financial transactions, improving both the accuracy and time efficiency of financial operations.
    - Collaborated with the medical department to create an ERP system screen for managing maids' medical data, facilitating medical leaves, and ensuring appropriate medication and care.

    **Business Analyst Intern at Bennett&Ranville (Jun 2022 - Aug 2022):**
    - Conducted market research using SWOT analysis to guide product development and improve competitive positioning.
    - Utilized data analytics and designed Tableau dashboards to evaluate and visualize product features, providing actionable insights for product enhancement.
    
    **Market Research Intern at Charity Donation Foundation (Jun 2021 – Aug 2021):**
    - Conducted market research on the Lebanese cracker industry, identifying key trends and strategic positioning opportunities.
    - Set pricing strategies for Love Bites products, aligning with market standards and consumer expectations.
    - Collaborated with the sales and delivery platform NokNok to feature Love Bites products, expanding market reach and customer accessibility.
    """, unsafe_allow_html=True)

elif options == "Extracurricular Activities":
    st.markdown('<p class="big-font">Extracurricular Activities</p>', unsafe_allow_html=True)
    st.markdown("""
    - **USAID Community Service Project Team Leader** at AUB (May 2021 – Nov 2023)
        - Led a $4000 educational initiative at Bissan Secondary School, Saida
        - Designed and executed a three-day workshop for 20 Palestinian refugee students covering chemistry experiments, Python programming, and SAT preparation
    - **Mentor in the Economics Department** at AUB (Aug 2021- Aug 2022)
        - Facilitated orientation and adaptation sessions for sophomores
        - Offered personalized course selection advice
    - **Student Representative** (SRC), Faculty of Arts and Sciences at AUB (Jan 2021 – Sep 2021)
        - Designed an Economics curriculum track specifically for Economics majors
        - Acted as a liaison between first-year students and faculty
    """)

elif options == "Awards":
    st.markdown('<p class="big-font">Awards</p>', unsafe_allow_html=True)
    st.markdown("""
    - **Beta Gamma Sigma (BGS) Society** (March 2024)
        - Qualified by ranking in the top 20% of my class at AUB
    - **Second place in Design2Transform Competition** at AUB (November 2023)
        - Developed "APEX," an AI educational software
    - **Mona Chemali Khalaf Award in Economics** (2023-2024)
        - Achieved the highest GPA in the fall term of the graduating year
    - **Remy Rubeiz Award in Economics** (2021-2022)
        - Attained the top cumulative GPA in the first two years of study
    """)

elif options == "Projects":
    st.markdown('<p class="big-font">Notable University Projects</p>', unsafe_allow_html=True)
    st.markdown("""
    - **From Feed to Food** [November 2023]
        - Implemented a digital and social media strategy using Python and Tableau
    - **Term Deposit Subscription Predictor** [November 2023]
        - Developed an R-based analytical model using linear regression and decision trees
    - **Pothole Detection Using ML** [June 2022]
        - Machine learning project using image recognition and convolutional neural networks
    - **Credit Suisse Stock Price Prediction** [June 2022]
        - Employed time-series analysis and econometric modeling using EViews and Python
    """)
