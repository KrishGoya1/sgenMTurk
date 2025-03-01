import csv
import os

def update_video_paths(input_csv, output_csv):
    """Update video paths in CSV to reflect new directory structure"""
    with open(input_csv, 'r') as infile, open(output_csv, 'w', newline='') as outfile:
        reader = csv.DictReader(infile)
        
        # Verify CSV structure
        print("CSV columns detected:", reader.fieldnames)
        
        writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
        writer.writeheader()
        
        for row in reader:
            # Update paths for both video columns
            row['video_A_url'] = row['video_A_url'].replace('../', './', 1)
            row['video_B_url'] = row['video_B_url'].replace('../', './', 1)
            writer.writerow(row)

if __name__ == '__main__':
    input_csv = 'scene_data.csv'
    output_csv = 'scene_data_updated.csv'
    update_video_paths(input_csv, output_csv)
    print(f"Updated CSV created: {output_csv}") 