from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Sameer Singh"
PAGE_ICON = ":wave:"
NAME = "Sameer Singh"
DESCRIPTION = """
Experienced software developer, proficient in Python Django and SQL. Seeking roles aligned with ETL or data science projects, driven to
contribute innovative solutions and deliver measurable results.
"""
EMAIL = "singhsameer121295@email.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/sameer-s-25a102134/",
    "GitHub": "https://github.com/Sameer1295",
    "Kaggle": "https://www.kaggle.com/sameersingh112"
}
PROJECTS = {
    "🏆 Clothify - Ecommerce clothing store (09/2023 - 10/2023) - Built clothing ecommerce web application using Django, Mysql, Jquery, Ajax and Bootstrap.": "https://github.com/Sameer1295/Clothify-Ecommerce-Django",
    "🏆 Secure File Storage System - Secure web app which encrypts and stores files into AWS s3": "https://github.com/Sameer1295/secure-file-storage-app",
    "🏆 Real time Cryptocurrency Prices Tracker - Built Real time Cryptocurrency price tracker using Django Celery and Redis": "https://github.com/Sameer1295/Real-time-Cryptocurrency-Prices-Tracker",
    "🏆 Imdb data analysis - Jupyter notebook for analysing Imdb data using Pandas Seaborn": "https://github.com/Sameer1295/IMDB-Data-analysis-using-Python",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Education")

# Education details in a concise format
education_details = [
    "🎓 **MSc** (Information Technology) - University of Mumbai",
    "🎓 **BSc** (Information Technology) - Ramanand Arya DAV College"
]

for edu_detail in education_details:
    st.write(f"{edu_detail}")


st.write('\n')
st.subheader("Soft Skills")
soft_skills = [
    "✉️  Client Communication",
    "🧩 Problem-Solving",
    "🤝 Teamwork and Collaboration",
    "🔍 Strong Analytical Skills",
    "🔄 Adaptability"
]

num_columns = 2
col1, col2 = st.columns(num_columns)

for i, skill in enumerate(soft_skills):
    if i % 2 == 0:
        col1.write(skill)
    else:
        col2.write(skill) 

# --- SKILLS ---
st.write('\n')
st.subheader("Technical Skills")
st.write(
    """
- 👩‍💻 Programming: Python, Javascript, PHP
- 🌐 Backend: Django, Flask
- 🌐 Web Technologies: HTML, CSS, Bootstrap
- 📊 Big Data: Hadoop, MapReduce, Hive, Spark, AWS Glue, AWS Athena
- 🗃️ Databases: MySQL, PGSQL, and MongoDB
- 📊 Data Visulization: MS Excel, Pandas, Seaborn, Plotly
- ☁️ Cloud: AWS IAM, S3, SES, AWS Glue
- ⚙️ Tools: VS Code, Git Bash, Postman, Jira, and Confluence
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Software Developer | Osian Software Pvt. Ltd**")
st.write("03/2022 - Present")
st.write(
    """
- ► Developed and maintained a complex web application using Python Django and Django Rest Framework (DRF)
- ► Implemented Wrapper APIs in DRF to communicate with external BI Apis and Recommendation services.
- ► Designed and generated dynamic PDF documents using Plotly to add interactive visual elements, enhancing reporting functionalities and data visualization.
- ► Improved the UI/UX of a Laravel web application designed for managing talent profiles for a prominent global entertainment provider. 
- ► Collaborated closely with a cross-functional team to test and successfully deploy the application. 
- ► Assumed responsibility for maintaining and enhancing existing applications , proactively addressing security issues identified by the Infosec team.
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Software Developer | Hridayam Soft Solutions**")
st.write("03/2021 - 02/2022")
st.write(
    """
- ► Developing and maintaining Rest Apis to meet project requirements and desired functionality using best practices.
- ► Maintaining Database by creating tables and writing triggers for audit trail and SQL functions for fetching data.
- ► Contributing ideas and suggestions in team meetings with Colleagues and effectively sharing task progress, evaluations and process issues.
- ► Fixed bugs from existing Document Management Solution and implemented enhancements that improved web functionality.
"""
)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.markdown(
        f"""
            <div class="card-body">
                <p class="card-title">{project}</p>
                <a href="{link}" class="btn btn-primary" target="_blank">Github Link</a>
            </div>
        """,
        unsafe_allow_html=True
    )
    # st.write(f"[{project}]({link})")

st.write('\n')
st.subheader("Awards and Achievements")

# Awards and achievements details
awards_details = [
    "🏆 1st Rank in SYIT (Bachelor of Science in Information Technology)",
    "🥈 2nd Rank in overall BSCIT (Bachelor of Science in Information Technology)",
    "🏆 1st Rank in Project Implementation during BSCIT",
    "🥈 Runners-up in Seed Infotech One-Day Project Event"
]

for award_detail in awards_details:
    st.write(f"• {award_detail}")


st.write('\n')
st.subheader("Volunteer Experience")

# Volunteer experience details
volunteer_details = [
    "🌊 Participated in Juhu Beach Clean-up Drive",
    "🎉 Volunteered for college fest Vibrations"
]

for volunteer_detail in volunteer_details:
    st.write(f"• {volunteer_detail}")