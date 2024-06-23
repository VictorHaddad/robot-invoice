from settings import *
import PyPDF2

def get_values_pdf() -> Dict[str, str]:
    try:
        path_pdf = os.path.join(BASE_DIR, "pdf")
       
        for pdf in os.listdir(path_pdf):

            with open(f'{path_pdf}\\{pdf}', 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                
                num_pages = len(reader.pages)
                
                for page in range(num_pages):
                    current_page = reader.pages[page]
                    text = current_page.extract_text()
                    value = text.split("\n")

            file.close()

    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return {"error": True, "message": str(e), 'data': None}
    
    return {"error": False, "message": None, 'data': value}