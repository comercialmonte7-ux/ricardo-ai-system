import sys
import zipfile
import xml.etree.ElementTree as ET

def read_docx(file_path):
    try:
        doc = zipfile.ZipFile(file_path)
        xml_content = doc.read('word/document.xml')
        root = ET.fromstring(xml_content)
        
        # Word XML namespaces
        ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
        
        text = []
        for paragraph in root.findall('.//w:p', ns):
            p_text = ""
            for run in paragraph.findall('.//w:r', ns):
                t = run.find('w:t', ns)
                if t is not None and t.text:
                    p_text += t.text
            if p_text:
                text.append(p_text)
        return "\n".join(text)
    except Exception as e:
        return f"Error reading {file_path}: {e}"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(read_docx(sys.argv[1]))
    else:
        print("Please provide a file path.")
