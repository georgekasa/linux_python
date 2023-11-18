import PyPDF2
import sys
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



#/home/gkasap/Desktop/very_good_2012-06-15_Armin_Tavakol_MSc_Thesis_DCO.pdf
if __name__ == "__main__":
    # Check if correct arguments are passed
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py <pdf_file_path>")
    else:
        pdf_file_path = sys.argv[1]
        try:
            # Extract text from the provided PDF file path
            extracted_text = extract_text_from_pdf(pdf_file_path)
            
            # Print the extracted text
            print("Text extracted from the PDF:\n", extracted_text)
        except FileNotFoundError:
            print("File not found. Please provide a valid path to the PDF file.")
        except Exception as e:
            print("An error occurred:", e)