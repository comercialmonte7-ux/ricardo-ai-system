import PyPDF2

def inspect_niksa():
    file_path = "/Users/ricardomarimodinger/Desktop/NUEVO AMANECER/Documentos Niksa Peralta.pdf"
    try:
        with open(file_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            print(f"Total pages: {len(reader.pages)}")
            # Read all pages
            for i in range(len(reader.pages)):
                text = reader.pages[i].extract_text()
                if text and text.strip():
                    print(f"--- Page {i+1} ---")
                    print(text[:1000])
                else:
                    print(f"--- Page {i+1}: No selectable text ---")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    inspect_niksa()
