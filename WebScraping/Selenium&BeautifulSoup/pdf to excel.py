import pandas as pd
import tabula

# Specify the actual path to the PDF file using double backslashes
pdf_path = "C:\\Users\\rs561\\Downloads\\Excel Practice.pdf"

# Read PDF into a DataFrame
df = tabula.read_pdf(pdf_path, pages='all', multiple_tables=True)

# Display the DataFrame
print(df)
df.
