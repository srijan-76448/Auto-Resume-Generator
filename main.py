import json, os


mainDir = os.path.dirname(os.path.abspath(__file__))
data_file_path = os.path.join(mainDir, "data.jsonc")
html_file_path = os.path.join(mainDir, "cv.html")
css_file_path = os.path.join(mainDir, "cv.css")
pdf_file_path = os.path.join(mainDir, "cv.pdf")

fileDB = ["json", "jsonc"]

emojis = {
    "email": "📧",
    "phone": "📞",
    "location": "📍",
    "url": "🌐"
}


def exteractData(json_file_path: os.path) -> dict:
    file_extention = os.path.splitext(json_file_path)[1].replace(".", "")
    raw_data = []

    if file_extention not in fileDB:
        print(f"\033[91;1m[-] FileExtentionError:\033[0m Extention '\033[1m.{file_extention}\033[0m' is not processable.")
        exit()

    if not os.path.exists(json_file_path):
        print(f"\033[91;1m[-] FileNotFoundError:\033[0m File not found at path '\033[1m{json_file_path}\033[0m'.")
        exit()

    with open(json_file_path, "r", encoding="utf-8") as f:
        raw_data = [i.strip() for i in f.readlines()]

    raw_json_data = "\n".join([i for i in raw_data if not i.startswith("//")])
        
    return dict(json.loads(raw_json_data))


def generate_html_resume(json_data):
    # Initiater
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{json_data['title']} - Resume</title>
    <link rel="stylesheet" href="cv.css" />
</head>
<body>
    <div class="resume-container">"""

    # Left section
    html += f"""
        <div class="left-section">
            <h1>{json_data['name']}</h1>
            <p>{json_data['position'].upper()}</p>"""

    # Contact information
    if 'contact' in json_data.keys():
        html += f"""
            <div class="contact-info">
                <h2>CONTACT</h2>"""

        for contact_type, contact in json_data['contact'].items():
            if type(contact) == list and contact_type != "url":
                for i in contact:
                    html += f"""
                <p>{emojis[contact_type]} {i}</p>"""

            elif contact_type == "location":
                html += f"""
                <p>{emojis[contact_type]} <a href="{contact['url']}">{contact['address']}</a></p>"""

            elif contact_type == "url":
                for i in contact:
                    html += f"""
                <p>{emojis[contact_type]} <a href="{i}">{i.replace('https://', '').replace('www.', '')}</a></p>"""

            else:
                html += f"""
                <p>{emojis[contact_type]} {contact}</p>"""

        html += f"""
            </div>"""

    # Skills
    if 'skills' in json_data.keys():
        html += f"""
            <div class="skills">
                <h2>SKILLS</h2>
                <ul>"""

        for skill in json_data['skills']:
            html += f"""
                    <li>{skill['name']} <div class="skill-bar"><div class="skill-level" style="width: {skill['strength']}%;"></div></div></li>"""

        html += f"""
                </ul>
            </div>"""
            
    # Known Languages
    if 'languages' in json_data.keys():
        html += f"""
            <div class="languages">
                <h2>LANGUAGES</h2>
                <ul>"""

        for language in json_data['languages']:
            html += f"""
                    <li>{language['name']} <div class="skill-bar"><div class="skill-level" style="width: {language['strength']}%;"></div></div></li>"""

        html += f"""
                </ul>
            </div>"""
            
    # Personal Skills
    if 'personal_skills' in json_data.keys():
        html += f"""
            <div class="personal-skills">
                <h2>PERSONAL SKILLS</h2>
                <ul>"""

        for skill in json_data['personal_skills']:
            html += f"""
                    <li>{skill['name']} <div class="skill-bar"><div class="skill-level" style="width: {skill['strength']}%;"></div></div></li>"""

        html += f"""
                </ul>
            </div>"""

    # Education
    if 'education' in json_data.keys():
        html += f"""
            <div class="education">
                <h2>EDUCATION</h2>"""

        for edu in json_data['education']:
            html += f"""
                <p><strong>{edu['degree']}</strong>[{edu['duration']}]<br>{edu['institution']}<br><strong>GPA</strong> - {edu['gpa']}</p>"""

        html += f"""
            </div>"""

    # End of left section
    html += f"""
        </div>"""

    # Right section
    html += f"""
        <div class="right-section">"""
        
    # Summary
    if 'summary' in json_data.keys():
        html += f"""
        <h2>SUMMARY</h2>
        <p>{json_data['summary']}</p>"""
            
    # Experience
    if 'experience' in json_data.keys():
        html += f"""

        <h2>EXPERIENCE</h2>"""

        for exp in json_data['experience']:
            html += f"""
            <div class="experience-item">
                <div class="title-date">
                    <h3>{exp['title']}</h3>
                    <p>{exp['duration']}</p>
                </div>
                <p>{exp['company']}</p>
            </div>
            """

    # Projects
    if 'projects' in json_data.keys():
        html += f"""
            <h2>PROJECTS</h2>"""

        for project in json_data['projects']:
            html += f"""
            <div class="project-item">
                <div class="title-date">
                    <h3 class="project-title"><a href="{project['url']}">{project['title']}</a></h3>
                    <p class="project-timeline">{project['date']}</p>
                </div>
                <p class="project-description">{project['description']}</p>
            </div>"""

    # End
    html += f"""
        </div>
    </div>
</body>
</html>
"""

    return html


def exportInPDF(html_file_path: os.path, css_file_path: os.path, output_pdf_path: os.path):
    pass


def main():
    resume_data = exteractData(data_file_path)
    html_content = generate_html_resume(resume_data)

    if os.path.exists(html_file_path):
        os.remove(html_file_path)

    with open(html_file_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"\033[92;1m[+]\033[0m Successfully created the html file at '\033[1m{html_file_path}\033[0m'.")
    
    print(f"\033[93;1m[*]\033[0m Exporting the file in PDF format...")
    exportInPDF(html_file_path, css_file_path, pdf_file_path)
    print(f"\033[92;1m[+]\033[0m Successfully created the pdf file at '\033[1m{pdf_file_path}\033[0m'.")


if __name__ == "__main__":
    try:
        main()
        
    except Exception as e:
        print(f"\033[91;1m[-] Error:\033[0m {e}")
        exit()
