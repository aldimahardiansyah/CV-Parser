# import pdfminer library
from pdfminer.high_level import extract_text

# import field extractor
from extractors.name import extract_names
from extractors.education import extract_education
from extractors.phone import extract_phone_number
from extractors.email import extract_emails
from extractors.skills import extract_skills

# extract text from pdf
def extract_text_from_pdf(pdf_path):
    txt = extract_text(pdf_path)
    if txt:
        return txt.replace('\t', ' ')
    return None
 
 
if __name__ == '__main__':
    text = extract_text_from_pdf('my_cv.pdf')
    name_information = extract_names(text)
    education_information = extract_education(text)
    phone = extract_phone_number(text)
 
    print("Name: ", name_information)
    print("Education: ", education_information)
    print("Phone: ", phone)
    print("Email: ", extract_emails(text))
    print("Skills: ", extract_skills(text))