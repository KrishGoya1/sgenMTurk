import csv
import os

S3_BASE_URL = "https://sceneprog-nautilus.s3.us-west-1.amazonaws.com/cvpr/"
PATH_MAPPING = {
    'sceneprog': 'sceneprog',
    'nn': 'holodeck'
}

def update_video_urls(input_csv, output_csv):
    """Convert local paths to S3 URLs with proper directory mapping"""
    with open(input_csv, 'r') as infile, open(output_csv, 'w', newline='') as outfile:
        reader = csv.DictReader(infile)
        
        # Verify CSV structure
        print("CSV columns detected:", reader.fieldnames)
        
        writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
        writer.writeheader()
        
        for row in reader:
            # Process video A URL
            original_path = row['video_A_url']
            dir_name, file_name = os.path.split(original_path.replace('./', ''))
            s3_dir = PATH_MAPPING.get(dir_name, dir_name)
            row['video_A_url'] = f"{S3_BASE_URL}{s3_dir}/{file_name}"
            
            # Process video B URL
            original_path = row['video_B_url']
            dir_name, file_name = os.path.split(original_path.replace('./', ''))
            s3_dir = PATH_MAPPING.get(dir_name, dir_name)
            row['video_B_url'] = f"{S3_BASE_URL}{s3_dir}/{file_name}"
            
            writer.writerow(row)

if __name__ == '__main__':
    input_csv = 'scene_data.csv'
    output_csv = 'scene_data_s3.csv'
    update_video_urls(input_csv, output_csv)
    print(f"Updated S3 URLs saved to {output_csv}") 