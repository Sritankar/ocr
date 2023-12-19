import easyocr
import csv
import cv2

reader = easyocr.Reader(['en']) 

image_path = r'C:\Users\srita\Downloads\drdo project\EasyOCR\durf.png'
image = cv2.imread(image_path)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
result = reader.readtext(image_rgb)

csv_filename = 'text_extraction_results.csv'
with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Text'])  # Write the header for the text column only

    # Write only the extracted text to the CSV file
    for detection in result:
        text = detection[1]
        csv_writer.writerow([text])

print(f"Extraction results saved in '{csv_filename}'")
