import os
import requests
import zipfile
import io

# List of Font Awesome icons
icons = [
    "fa-arrow-right", "fa-birthday-cake", "fa-caret-left", "fa-caret-right",
    "fa-chalkboard-teacher", "fa-check", "fa-chevron-down", "fa-chevron-right",
    "fa-circle", "fa-facebook", "fa-glass-cheers", "fa-graduation-cap", 
    "fa-handshake", "fa-linkedin", "fa-map-marker-alt", "fa-moon", "fa-phone", 
    "fa-plus", "fa-seedling", "fa-spinner", "fa-star", "fa-star-half", "fa-sun", 
    "fa-tachometer-alt", "fa-twitter", "fa-user", "fa-youtube"
]

# Map the icons to their correct filenames
icon_map = {icon: icon.replace('fa-', '') for icon in icons}

# Directory to save SVG files
output_dir = "fontawesome_svgs"
os.makedirs(output_dir, exist_ok=True)

# URL of the Font Awesome GitHub repository ZIP file
zip_url = "https://github.com/FortAwesome/Font-Awesome/archive/refs/heads/6.x.zip"

# Download the ZIP file
response = requests.get(zip_url)
if response.status_code == 200:
    print("Downloaded Font Awesome ZIP file.")
    # Extract the ZIP file
    with zipfile.ZipFile(io.BytesIO(response.content)) as z:
        # List all files in the ZIP archive
        all_files = z.namelist()
        for icon, filename in icon_map.items():
            # Look for the SVG file that matches the filename
            svg_path = next((f for f in all_files if f.endswith(f"{filename}.svg") and "/svgs/solid/" in f), None)
            if svg_path:
                try:
                    # Read the SVG file from the ZIP archive
                    with z.open(svg_path) as svg_file:
                        svg_content = svg_file.read()
                        # Save the SVG file to the output directory
                        with open(os.path.join(output_dir, f"{icon}.svg"), "wb") as output_file:
                            output_file.write(svg_content)
                        print(f"Extracted {icon}.svg")
                except KeyError:
                    print(f"SVG not found for {icon}")
            else:
                print(f"SVG not found for {icon}")
else:
    print("Failed to download Font Awesome ZIP file.")
