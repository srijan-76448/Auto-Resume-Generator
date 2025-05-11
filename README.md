# Auto Resume Generator
This Python script processes data from a JSON or JSONC file to generate an HTML resume. It reads contact information, skills, education, experience, and projects, then structures them into a well-formatted HTML file.

**Before executing this script, please read the [manual.md](manual.md) file for detailed instructions on data file format and usage.**
**Please check the [sample resume](https://sam.arg.76448.in)**

## Prerequisites
- Python 3.x installed on your system.

## Usage
1.  **Download/Clone the repository:** Clone the repository or download the zip file and extract it.
2.  **Update the `data.jsonc` file:** Update the `data.jsonc` file with your contact information, skills, education, experience, and projects, etc.
3.  **Run the script:** Open your terminal or command prompt, navigate to the directory where you saved the files, and execute the script using:
    ```bash
    python main.py
    ```
4.  **Output:** The script will generate a `cv.html` file in the same directory, containing your resume in HTML format. It will also attempt to export the resume as a `cv.pdf` file.
5.  **View the resume:** Open the `cv.html` file in your web browser to view your resume.
6.  **Export the resume:** If the script was able to export the resume as a PDF file, you can find it in the same directory as the HTML file. Else, just press `Ctrl + P` on your keyboard to print the HTML file into pdf.

> NOTE:
>     Currently, the PDF export functionality is currently a placeholder.
>     This feature is not yet implemented.
>     The PDF export feature will be added in the future, when I'm able to find a way to generate a PDF file from HTML and CSS using a python script.

## Data File Format (`data.json` or `data.jsonc`)
The data file should be structured as a JSON object with the following keys (all keys are optional, but including relevant information is recommended). Please fillup the `data.jsonc` file with your information in order to run this program.
