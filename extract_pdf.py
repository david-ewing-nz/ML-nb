import PyPDF2
import fitz  # PyMuPDF
import os

# Extract questions
pdf_path = 'reference-ml/DATA420-25S2 Assignment 2 (Questions).pdf'
txt_path = 'assignment_questions.txt'

try:
    with open(pdf_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
    with open(txt_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print("Questions text extracted successfully to assignment_questions.txt")
except Exception as e:
    print(f"Error extracting questions: {e}")

# Extract grading
pdf_path = 'reference-ml/DATA420-25S2 Assignment 2 (Grading).pdf'
txt_path = 'assignment_grading.txt'

try:
    with open(pdf_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
    with open(txt_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print("Grading text extracted successfully to assignment_grading.txt")
except Exception as e:
    print(f"Error extracting grading: {e}")

# Extract images from both PDFs
def extract_images(pdf_path, output_dir):
    doc = fitz.open(pdf_path)
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        images = page.get_images(full=True)
        for img_index, img in enumerate(images):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            image_name = f"{os.path.basename(pdf_path).replace('.pdf', '')}_page{page_num+1}_img{img_index+1}.{image_ext}"
            with open(os.path.join(output_dir, image_name), "wb") as img_file:
                img_file.write(image_bytes)
    doc.close()

output_dir = 'images'
os.makedirs(output_dir, exist_ok=True)

try:
    extract_images('reference-ml/DATA420-25S2 Assignment 2 (Questions).pdf', output_dir)
    print("Images extracted from questions PDF")
except Exception as e:
    print(f"Error extracting images from questions PDF: {e}")

try:
    extract_images('reference-ml/DATA420-25S2 Assignment 2 (Grading).pdf', output_dir)
    print("Images extracted from grading PDF")
except Exception as e:
    print(f"Error extracting images from grading PDF: {e}")

print("Image extraction completed")