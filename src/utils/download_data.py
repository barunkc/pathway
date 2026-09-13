import os
import urllib.request

def download_dataset():
    # An open-source dataset tracking global plastic waste particles
    url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-01-26/plastics.csv"
    
    # Targeting your newly created folder paths
    output_dir = "data/raw"
    output_file = os.path.join(output_dir, "plastic_waste.csv")
    
    # Double-check that directory exists before saving
    os.makedirs(output_dir, exist_ok=True)
    
    print(f"Starting connection to dataset source...")
    try:
        # Stream the file down directly into your target folder
        urllib.request.urlretrieve(url, output_file)
        print(f"Success! Data safely stored at: {output_file}")
        
        # Calculate file size to verify it downloaded cleanly
        file_size = os.path.getsize(output_file) / 1024
        print(f"Verified File Size: {file_size:.2f} KB")
        
    except Exception as e:
        print(f"Pipeline broken. Error downloading data: {e}")

if __name__ == "__main__":
    download_dataset() 