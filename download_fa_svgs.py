import os
import requests
from bs4 import BeautifulSoup

# List of Font Awesome icons
icons = [
    "fa-arrow-right", "fa-birthday-cake", "fa-caret-left", "fa-caret-right",
    "fa-chalkboard-teacher", "fa-check", "fa-chevron-down", "fa-chevron-right",
    "fa-chevron-toggle", "fa-circle", "fa-facebook", "fa-glass-cheers",
    "fa-graduation-cap", "fa-handshake", "fa-lg", "fa-linkedin", "fa-map-marker-alt",
    "fa-moon", "fa-phone", "fa-plus", "fa-pulse", "fa-seedling", "fa-solid",
    "fa-spinner", "fa-star", "fa-star-half", "fa-star-half-o", "fa-sun",
    "fa-tachometer-alt", "fa-twitter", "fa-user", "fa-youtube"
]

# Directory to save SVG files
output_dir = "fontawesome_svgs"
os.makedirs(output_dir, exist_ok=True)

# Base URL for Font Awesome
base_url = "https://fontawesome.com/icons/"

# Function to download an SVG file
def download_svg(icon):
    url = f"{base_url}{icon[3:]}?style=solid"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        svg_tag = soup.find("svg", {"aria-hidden": "true"})
        if svg_tag:
            svg_str = str(svg_tag)
            file_path = os.path.join(output_dir, f"{icon}.svg")
            with open(file_path, "w") as file:
                file.write(svg_str)
            print(f"Downloaded {icon}.svg")
        else:
            print(f"SVG not found for {icon}")
    else:
        print(f"Failed to fetch {icon}")

# Download SVGs for all icons
for icon in icons:
    download_svg(icon)
