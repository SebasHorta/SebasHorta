import PyPDF2
import os

merger = PyPDF2.PdfMerger()
output_filename = "MergedDocs.pdf"  # Initialize the output filename

for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        print(file)
        merger.append(file)

# Construct a new filename based on the input filenames
input_pdf_files = [file for file in os.listdir(os.curdir) if file.endswith(".pdf")]
if input_pdf_files:
    # Extract the base filenames (without extensions) and join them with underscores
    merged_filename = "_".join(os.path.splitext(file)[0] for file in input_pdf_files) + ".pdf"
    output_filename = merged_filename

merger.write(output_filename)
merger.close()

print(f"Merged PDF saved as '{output_filename}'")