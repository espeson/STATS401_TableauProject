import json
import csv

def extract_columns_from_jsonl(file_path, desired_keys):
    extracted_data = []

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            data = json.loads(line)
            # Extract only the desired keys
            filtered_data = {key: data[key] for key in desired_keys if key in data}
            extracted_data.append(filtered_data)

    return extracted_data

def save_to_csv(rows, output_file_path):
    if not rows:
        return
    
    fieldnames = rows[0].keys()  # get column headers from the first row
    with open(output_file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()  # write column headers
        for row in rows:
            writer.writerow(row)

input_file_path = "test_output.jsonl"  # replace with your input JSONL file path
output_file_path = "extracted_output.csv"  # replace with your desired output CSV file path
desired_keys = ['ip_location', 'reposts_count', 'comments_count','attitudes_count','source','content']  # specify the keys you want to extract
    
extracted_data = extract_columns_from_jsonl(input_file_path, desired_keys)
save_to_csv(extracted_data, output_file_path)
print(f"Extracted data saved to {output_file_path}.")
