import csv
import json

def create_mturk_csv(json_file, output_csv):
    # Load the scene data from JSON
    with open(json_file, 'r') as f:
        scene_data = json.load(f)
    
    # Create CSV file with MTurk template variables
    with open(output_csv, 'w', newline='') as csvfile:
        fieldnames = ['prompt', 'video_A_url', 'video_B_url']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for scene in scene_data:
            # Clean the prompt to remove any problematic characters
            clean_prompt = scene['prompt'].replace('"', '').replace("'", "")
            
            writer.writerow({
                'prompt': clean_prompt,
                'video_A_url': scene['video_A_url'],
                'video_B_url': scene['video_B_url']
            })
    
    print(f"Created MTurk CSV file with {len(scene_data)} rows at {output_csv}")

if __name__ == '__main__':
    create_mturk_csv('scene_data.json', 'mturk_batch.csv') 