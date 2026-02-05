import pdfplumber
import re

pdf_path = "harrypotter.pdf"

page_ranges = [
    (12, 274),
    (282, 565),
    (573, 939),
    (949, 1560),
    (1570, 2406),
    (2415, 2964),
    (2976, 3622),
]

with pdfplumber.open(pdf_path) as pdf, \
     open("Harry_Potter.txt", "w", encoding="utf-8") as out:

    total_pages = len(pdf.pages)

    for start, end in page_ranges:
        start_idx = max(0, start - 1)
        end_idx = min(total_pages - 1, end - 1)

        for i in range(start_idx, end_idx + 1):
            page = pdf.pages[i]
            text = page.extract_text()

            if text:
                text = re.sub(r'-\n', '', text)
                text = re.sub(r'\n{2,}', '\n\n', text)

                out.write(text + "\n\n")

            if i % 50 == 0:
                print(f"Processed page {i+1}")

print(" Text extraction complete safely!")