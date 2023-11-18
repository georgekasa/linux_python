import sys
import os
import PyPDF2
import re

def extract_text_from_pdf(pdf_path):
    text = ''
    # Open the PDF file
    with open(pdf_path, 'rb') as pdf_file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        
        # Iterate through each page
        for page in pdf_reader.pages:
            # Extract text from the page
            text += page.extract_text()
    
    return text

def filter_text_with_context(text, keyword, before_context, after_context):
    lines = text.split('\n')
    matched_lines = []
    for idx, line in enumerate(lines):
        if keyword.lower() in line.lower():
            start_idx = max(0, idx - before_context)
            end_idx = min(len(lines), idx + after_context + 1)
            matched_lines.extend(lines[start_idx:end_idx])
    
    return '\n'.join(matched_lines)

def print_filtered_text_with_highlight(filtered_text, keyword):
    lines = filtered_text.split('\n')
    pattern = re.compile(re.escape(keyword), re.IGNORECASE)
    
    for line in lines:
        highlighted_line = pattern.sub(f"\033[91m{keyword}\033[0m", line)
        print(highlighted_line)



def filter_text_only_keyword(text, keyword):
    lines = text.split('\n')
    filtered_lines = [line for line in lines if keyword.lower() in line.lower()]
    return '\n'.join(filtered_lines)

if __name__ == "__main__":
    # Check if correct arguments are passed
    if len(sys.argv) < 3 or len(sys.argv) > 5:
        print("Usage with user input: python3 script_name.py <before_context> <after_context> <keyword> <pdf_file_path>")
        print("Usage with context: python3 script_name.py <before_context> <after_context> <keyword> .")
        sys.exit(1)

    before_context = 0
    after_context = 0
    keyword = sys.argv[1]
    user_input = sys.argv[-1]

    if len(sys.argv) == 5:
        before_context = int(sys.argv[1])
        after_context = int(sys.argv[2])
        keyword = sys.argv[3]
        user_input = sys.argv[4]


    if user_input == ".":
        pdf_files = []
        for root, dirs, files in os.walk("."):
            for file in files:
                if file.endswith(".pdf"):
                    pdf_files.append(os.path.abspath(os.path.join(root, file)))
    else:
        pdf_files = [os.path.abspath(user_input)]
    
    try:
        for pdf_file in pdf_files:
            # Extract text from each provided PDF file path
            extracted_text = extract_text_from_pdf(pdf_file)
            
            # Filter text based on user input
            filtered_text = filter_text_with_context(extracted_text, keyword, before_context, after_context)
            
            if filtered_text:
                # Print the extracted and filtered text for each PDF file
                print(f"\033[91m{pdf_file}\033[0m")
                print_filtered_text_with_highlight(filtered_text, keyword)
                print("################################################################################")
            
    except FileNotFoundError:
        print("File not found. Please provide a valid path to the PDF file.")
    except Exception as e:
        print("An error occurred:", e)
