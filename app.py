import streamlit as st
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_resume(name, job_title, email, mobile, education, skills, experience, projects, achievements, activities, filename="Resume.pdf"):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    # Job Title as Main Heading (Centered)
    c.setFont("Times-Bold", 18)
    c.drawCentredString(width / 2, height - 50, job_title)
    
    # Name (Centered)
    c.setFont("Times-Bold", 16)
    c.drawCentredString(width / 2, height - 80, name)
    
    # Contact Info
    c.setFont("Times-Roman", 12)
    c.drawCentredString(width / 2, height - 100, f"Email: {email}")
    c.drawCentredString(width / 2, height - 120, f"Mobile: {mobile}")
    
    y = height - 150
    section_spacing = 20

    def add_section(title, content_list):
        nonlocal y
        if y < 50:
            c.showPage()
            y = height - 50
        c.setFont("Times-Bold", 14)
        c.drawString(50, y, title)
        c.setFont("Times-Roman", 12)
        y -= section_spacing
        for item in content_list:
            c.drawString(60, y, f"- {item}")
            y -= section_spacing
        y -= 10  # Extra space after section
    
    # Sections
    add_section("Education:", education)
    add_section("Skills:", [skills])
    add_section("Experience:", experience)
    add_section("Projects:", projects)
    add_section("Achievements:", achievements)
    add_section("Other Activities:", [activities])
    
    c.save()
    return filename

def main():
    st.title("Resume Generator")
    
    name = st.text_input("Enter your name:")
    job_title = st.text_input("Enter your job title:")
    email = st.text_input("Enter your email:")
    mobile = st.text_input("Enter your mobile number:")
    
    education = st.text_area("Enter your education details (one per line):").split("\n")
    skills = st.text_input("Enter your skills (comma-separated):")
    experience = st.text_area("Enter your experience details (one per line):").split("\n")
    projects = st.text_area("Enter your project details (one per line):").split("\n")
    achievements = st.text_area("Enter your achievements (one per line):").split("\n")
    activities = st.text_area("Enter your other activities or hobbies:")
    
    if st.button("Generate Resume"):
        filename = generate_resume(name, job_title, email, mobile, education, skills, experience, projects, achievements, activities)
        with open(filename, "rb") as file:
            st.download_button("Download Resume", file, file_name=filename, mime="application/pdf")

if __name__ == "__main__":
    main()
