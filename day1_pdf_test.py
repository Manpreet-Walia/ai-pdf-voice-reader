import pymupdf as fitz

doc = fitz.open("sample.pdf")

all_text = ""

for page in doc:
    all_text += page.get_text()

with open("extracted_text.txt", "w", encoding="utf-8") as f:
    f.write(all_text)

print("Done! Text saved to extracted_text.txt")

