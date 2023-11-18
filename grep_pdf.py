import sys
import os
import PyPDF2

def extract_text_from_pdf(pdf_path):
    text = ''
    # Open the PDF file
    with open(pdf_path, 'rb') as pdf_file:
        # Create a PDF reader object
        
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        
        # Iterate through each page
        for page_num in range(len(pdf_reader.pages)):
            # Get a specific page
            page = pdf_reader.pages[page_num]
            
            # Extract text from the page
            text += page.extract_text()
    
    return text

def filter_text_for_keyword(text, keyword):
    lines = text.split('\n')
    filtered_lines = [line for line in lines if keyword.lower() in line.lower()]
    return '\n'.join(filtered_lines)

if __name__ == "__main__":
    # Check if correct arguments are passed

    if len(sys.argv) != 3:
        print("Usage: python3 script_name.py <keyword> <pdf_file_path>")
    else:
        keyword = sys.argv[1]
        user_input = sys.argv[2]
        
        # Get a list of PDF files in the current directory if user enters "."
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
                
                # Filter text for the provided keyword in a case-insensitive way
                filtered_text = filter_text_for_keyword(extracted_text, keyword)
                empty_check = ""
                if empty_check != filtered_text:
                # Print the extracted and filtered text for each PDF file
                    print(f"Filtered Text from {pdf_file}:")
                    lines = filtered_text.split('\n')
                    
    
                    for line in lines:
                    #  if f" {keyword.lower()} " in line.lower():
                        #  line_parts = line.split(keyword)
                        # line = f"{keyword}\n################{line_parts[0]}"
                        print(line)
                    print("################################################################################")
                
        except FileNotFoundError:
            print("File not found. Please provide a valid path to the PDF file.")
        except Exception as e:
            print("An error occurred:", e)
