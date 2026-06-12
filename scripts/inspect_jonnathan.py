import PyPDF2

def inspect_jonnathan():
    files = [
        "/Users/ricardomarimodinger/Desktop/NUEVO AMANECER/curriculum Jonnathan alister/CV Jonnathan Harddy Alister Maldonado.pdf",
        "/Users/ricardomarimodinger/Desktop/NUEVO AMANECER/curriculum Jonnathan alister/GOBIERNO.pdf"
    ]
    for file_path in files:
        print(f"=====================================")
        print(f"File: {file_path}")
        try:
            with open(file_path, 'rb') as f:
                reader = PyPDF2.PdfReader(f)
                print(f"Total pages: {len(reader.pages)}")
                for i in range(min(5, len(reader.pages))):
                    text = reader.pages[i].extract_text()
                    if text and text.strip():
                        print(f"--- Page {i+1} ---")
                        print(text[:1000])
                    else:
                        print(f"--- Page {i+1}: No selectable text ---")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    inspect_jonnathan()
