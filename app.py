import os
import csv
from bs4 import BeautifulSoup

def extract_scene_data(html_path):
    """Extract scene data from a single HTML file"""
    with open(html_path, 'r') as f:
        soup = BeautifulSoup(f, 'html.parser')
        
        # Extract scene ID
        scene_id = soup.find('span', style='color: red; font-size: 60px;').text.strip()
        
        # Extract prompt
        prompt = soup.find('p', style='color: rgb(25, 104, 152); font-size: 30px;').i.text.strip()
        
        # Extract video URLs
        videos = soup.find_all('source')
        video_a = videos[0]['src']
        video_b = videos[1]['src']
        
        return {
            'scene_id': scene_id,
            'prompt': prompt,
            'video_a': video_a,
            'video_b': video_b
        }

def generate_csv(directory, output_file):
    """Process all HTML files in directory and generate CSV"""
    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['scene_id', 'prompt', 'video_A_url', 'video_B_url']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        # Process HTML files in order
        html_files = sorted(
            [f for f in os.listdir(directory) if f.endswith('.html')],
            key=lambda x: int(x.split('.')[0])
        )
        
        for filename in html_files:
            data = extract_scene_data(os.path.join(directory, filename))
            writer.writerow({
                'scene_id': data['scene_id'],
                'prompt': data['prompt'],
                'video_A_url': data['video_a'],
                'video_B_url': data['video_b']
            })

if __name__ == '__main__':
    generate_csv('us4', 'scene_data.csv')
    print("CSV file generated successfully!")