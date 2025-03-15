import csv
import json

def convert_csv_to_json(csv_file, json_file):
    data = []
    with open(csv_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    
    with open(json_file, 'w') as jsonfile:
        json.dump(data, jsonfile, indent=2)
    
    print(f"Converted {len(data)} records from {csv_file} to {json_file}")
    return data

if __name__ == '__main__':
    data = convert_csv_to_json('scene_data_s3.csv', 'scene_data.json')
    
    # Print JavaScript code that can be pasted into the HTML
    js_code = f"const sceneData = {json.dumps(data, indent=2)};"
    print("\nJavaScript code to paste in HTML:")
    print(js_code) 