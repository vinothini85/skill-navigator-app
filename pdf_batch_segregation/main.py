import re
import PyPDF2


java_keywords = ['AWS certification', 'Java certification']
dotnet_keywords = ['Azure certification', '.NET certification']
data_eng_keywords = ['Python']

def read_pdf(file_path):
    content = ""
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            content += page.extract_text()
    return content

def allocate_batch(content):
    if any(re.search(r'\b' + keyword + r'\b', content, re.IGNORECASE) for keyword in java_keywords):
        return "Java Batch"
    
    elif any(re.search(r'\b' + keyword + r'\b', content, re.IGNORECASE) for keyword in dotnet_keywords):
        return ".NET Batch"
    
    elif any(re.search(r'\b' + keyword + r'\b', content, re.IGNORECASE) for keyword in data_eng_keywords):
        return "Data Engineering Batch"
    
    else:
        return "No Batch Found"

# Example usage
file_path = r'C:\Users\Alhaan\Desktop\skill_navigator_app\Python_Quickstart.pdf'
content = read_pdf(file_path)
batch = allocate_batch(content)
print(f"The candidate should be allocated to: {batch}")
