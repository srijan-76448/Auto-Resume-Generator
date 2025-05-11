# Resume Generator Script Manual

## Overview

This Python script, `resume_generator.py`, processes data from a JSON or JSONC (JSON with comments) file to generate an HTML resume. It reads personal and professional information, such as contact details, skills, education, experience, and projects, and structures it into a well-formatted HTML file (`cv.html`). The script is designed to be straightforward to use, requiring a data file in the specified format.

## Requirements

- Python 3.x installed on your system.
- A JSON or JSONC file containing your resume data.

## Installation

No specific installation is required. Simply save the Python script (`resume_generator.py`) in your desired directory.

## Usage

1.  **Prepare your data file:** Create a JSON or JSONC file (e.g., `data.jsonc`) in the same directory as the script. This file should contain your resume information organized in a specific structure. Refer to the "Data File Format" section for details.

2.  **Run the script:** Open your terminal or command prompt, navigate to the directory where you saved the script, and execute the following command:

    ```bash
    python3 resume_generator.py
    ```

3.  **Output:** Upon successful execution, the script will generate an HTML file named `cv.html` in the same directory. This file contains your resume formatted as a webpage. The script will also attempt to export this HTML file to a PDF file named `cv.pdf`, although the PDF export functionality (`exportInPDF` function) is currently a placeholder and does not perform any actual conversion.

## Data File Format

The JSON/JSONC data file should adhere to the following structure:

```jsonc
{
  "title": "Your Desired Job Title", // Title of the resume/page
  "name": "Your Full Name",
  "position": "Your Current/Desired Position",
  "contact": {
    "email": "your.email@example.com",
    "phone": "+91 1234567890",
    "location": {
      "address": "Your Address",
      "url": "[https://maps.google.com/?q=Your+Address+Coordinates](https://maps.google.com/?q=Your+Address+Coordinates)" // Optional Google Maps link
    },
    "url": [ // List of URLs (e.g., LinkedIn, Portfolio)
      "[https://linkedin.com/in/yourprofile](https://linkedin.com/in/yourprofile)",
      "[https://github.com/yourusername](https://github.com/yourusername)"
    ]
  },
  "skills": [
    {
      "name": "Programming",
      "strength": 80 // Percentage representing skill level
    },
    {
      "name": "Communication",
      "strength": 90
    }
    // ... more skills
  ],
  "languages": [
    {
      "name": "English",
      "strength": 100
    },
    {
      "name": "Hindi",
      "strength": 95
    }
    // ... more languages
  ],
  "personal_skills": [
    {
      "name": "Teamwork",
      "strength": 95
    },
    {
      "name": "Problem-solving",
      "strength": 85
    }
    // ... more personal skills
  ],
  "education": [
    {
      "degree": "Bachelor of Science in Computer Science",
      "duration": "2018 - 2022",
      "institution": "University Name",
      "gpa": "3.8/4.0"
    }
    // ... more education entries
  ],
  "summary": "A brief professional summary highlighting your key skills and experience.",
  "experience": [
    {
      "title": "Software Engineer",
      "company": "Tech Company Inc.",
      "duration": "2022 - Present"
      // You can add more details here if needed
    }
    // ... more experience entries
  ],
  "projects": [
    {
      "title": "Personal Portfolio Website",
      "url": "[https://yourportfolio.com](https://yourportfolio.com)",
      "date": "2023",
      "description": "A website showcasing your skills and projects."
    }
    // ... more project entries
  ]
  // You can include comments in JSONC files using double slashes (//)
}
```

-   **Top-level keys:** The JSON object should contain keys like `title`, `name`, `position`, `contact`, `skills`, `languages`, `personal_skills`, `education`, `summary`, `experience`, and `projects`. Not all keys are mandatory, but providing relevant information for each section will result in a more comprehensive resume.
-   **Contact:** The `contact` section is an object containing contact details like `email`, `phone`, `location` (which is an object with `address` and optional `url`), and `url` (a list of website URLs).
-   **Skills, Languages, Personal Skills:** These are lists of objects, where each object has a `name` (the skill/language) and a `strength` (an integer representing the proficiency level as a percentage).
-   **Education:** A list of education entries, each containing `degree`, `duration`, `institution`, and `gpa`.
-   **Experience:** A list of work experience entries, each with `title`, `company`, and `duration`. You can extend these objects with more details if required by modifying the `generate_html_resume` function.
-   **Projects:** A list of project entries, each with `title`, `url`, `date`, and `description`.

## CSS Styling

The HTML resume generated by the script links to a CSS file named `cv.css`. To customize the appearance of your resume, you need to create this CSS file in the same directory as the script and the generated `cv.html` file. You can define styles for various elements like the container, sections, headings, paragraphs, lists, and skill bars.

## PDF Export

The script includes a function `exportInPDF`, but it is currently a placeholder. To enable PDF export, you would need to integrate a library like `pdfkit` or `weasyprint`. This would involve:

1.  Installing the required library (e.g., `pip install pdfkit` and ensuring you have wkhtmltopdf installed if using `pdfkit`).
2.  Modifying the `exportInPDF` function to use the chosen library to convert the `cv.html` file (along with `cv.css`) into a PDF.

## Error Handling

The script includes basic error handling for the following scenarios:

-   **Unsupported File Extension:** If the provided data file has an extension other than `.json` or `.jsonc`, the script will print an error message and exit.
-   **File Not Found:** If the specified data file does not exist at the given path, the script will print an error message and exit.
-   **JSON Decoding Error:** If the content of the JSON/JSONC file is not valid JSON, the `json.loads()` function will raise an exception, which the script catches and prints as an error.

## Customization

To further customize the generated resume:

-   **Modify the HTML structure:** Edit the `generate_html_resume` function to change the arrangement and elements of the HTML output.
-   **Enhance CSS styling:** Create or modify the `cv.css` file to control the visual presentation of the resume.
-   **Add more data fields:** Extend the data file format and update the `generate_html_resume` function to handle additional information.
-   **Implement PDF export:** Integrate a PDF generation library in the `exportInPDF` function.