import json
import random

def read_random_rows_from_jsonl(file_path, num_rows_to_read):
    all_rows = []
    
    # Read all rows from JSONL file
    with open(file_path, 'r',encoding='utf-8') as f:
        for line in f:
            all_rows.append(json.loads(line))
    
    # Randomly select some rows
    selected_rows = random.sample(all_rows, num_rows_to_read)
    
    return selected_rows

def save_to_jsonl(rows, output_file_path):
    with open(output_file_path, 'w',encoding='utf-8') as f:
        for row in rows:
            f.write(json.dumps(row))
            f.write('\n')

    file_path = r"output\tweet_spider_by_keyword_20230905090130.jsonl"  # replace with your JSONL file path
    output_file_path = "test_output.jsonl"  # replace with your desired output file path
    num_rows_to_read = 1000  # replace with the number of rows you want to randomly select
    
    selected_rows = read_random_rows_from_jsonl(file_path, num_rows_to_read)
    
    save_to_jsonl(selected_rows, output_file_path)
    
    print(f"Saved {num_rows_to_read} randomly selected rows to {output_file_path}.")
