from pdfminer.high_level import extract_text

# import field extractor
from extractors.name import extract_names
from extractors.education import extract_education
 
def extract_text_from_pdf(pdf_path):
    txt = extract_text(pdf_path)
    if txt:
        return txt.replace('\t', ' ')
    return None
 
 
if __name__ == '__main__':
    text = extract_text_from_pdf('my_cv.pdf')
    name_information = extract_names(text)
    education_information = extract_education(text)
 
    print(name_information)
    print(education_information) 