import os
import re
import zipfile
import xml.etree.ElementTree as ET

def extract_text_from_docx(file_path):
    try:
        doc = zipfile.ZipFile(file_path)
        xml_content = doc.read('word/document.xml')
        root = ET.fromstring(xml_content)
        ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
        text = []
        for paragraph in root.findall('.//w:p', ns):
            p_text = "".join(t.text for run in paragraph.findall('.//w:r', ns) for t in [run.find('w:t', ns)] if t is not None and t.text)
            if p_text:
                text.append(p_text)
        return " ".join(text)
    except Exception:
        return ""

def extract_text_from_pdf(file_path):
    try:
        import PyPDF2
        text = []
        with open(file_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                t = page.extract_text()
                if t:
                    text.append(t)
        return " ".join(text)
    except Exception as e:
        return ""

def search_ruts():
    folder_path = "/Users/ricardomarimodinger/Desktop/NUEVO AMANECER"
    # Regex for RUT: e.g. 12.345.678-9 or 12345678-9 or 5.904.132-0
    rut_pattern = re.compile(r'\b\d{1,2}(?:\.?\d{3}){2}-[\dkK]\b')
    
    results = {}
    
    for root_dir, dirs, files in os.walk(folder_path):
        for filename in files:
            filepath = os.path.join(root_dir, filename)
            text = ""
            if filename.endswith(".docx"):
                text = extract_text_from_docx(filepath)
            elif filename.endswith(".pdf"):
                text = extract_text_from_pdf(filepath)
            elif filename.endswith(".doc"):
                try:
                    with open(filepath, 'rb') as f:
                        content = f.read()
                        text = "".join(chr(c) if 32 <= c < 127 or c == 10 else " " for c in content)
                except Exception:
                    pass
            
            if text:
                ruts = rut_pattern.findall(text)
                if ruts:
                    results[filename] = list(set(ruts))
                
    # Also search the ivan documentos folder
    ivan_folder = "/Users/ricardomarimodinger/Desktop/ivan documentos"
    for filename in os.listdir(ivan_folder):
        filepath = os.path.join(ivan_folder, filename)
        text = ""
        if filename.endswith(".docx"):
            text = extract_text_from_docx(filepath)
        elif filename.endswith(".pdf"):
            text = extract_text_from_pdf(filepath)
            
        if text:
            ruts = rut_pattern.findall(text)
            if ruts:
                results[filename] = list(set(ruts))
                
    print("RUTs found:")
    for file, ruts in results.items():
        print(f"{file}: {ruts}")

if __name__ == "__main__":
    search_ruts()
