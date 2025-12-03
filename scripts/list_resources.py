import os
import re
import json
import sys
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup


def list_resources(website_url: str):
    """
    Parse the given website URL to identify all required resources (e.g., HTML,
    CSS, JavaScript, images, fonts, etc.).

    Args:
        website_url (str): The URL of the website to parse.

    Returns:
        dict: A dictionary containing lists of resources categorized by type.
    """
    try:
        response = requests.get(website_url)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching the website: {e}")
        return {}

    soup = BeautifulSoup(response.text, 'html.parser')

    resources = {
        'html': [website_url],
        'css': [],
        'js': [],
        'images': [],
        'fonts': [],
        'other': []
    }

    # Find all CSS files
    for link in soup.find_all('link', {'rel': 'stylesheet'}):
        href = link.get('href')
        if href:
            resources['css'].append(urljoin(website_url, href))

    # Find all JavaScript files
    for script in soup.find_all('script', {'src': True}):
        src = script.get('src')
        if src:
            resources['js'].append(urljoin(website_url, src))

    # Find all image files
    for img in soup.find_all('img', {'src': True}):
        src = img.get('src')
        if src:
            resources['images'].append(urljoin(website_url, src))

    # Find all font files (e.g., in style tags or inline CSS)
    for style in soup.find_all('style'):
        font_urls = re.findall(r'url\((.*?)\)', style.text)
        for font_url in font_urls:
            resources['fonts'].append(urljoin(website_url, font_url.strip('"\'')))

    # Find other linked resources
    for tag in soup.find_all(['a', 'iframe', 'embed', 'source'], {'href': True, 'src': True}):
        attr = 'href' if tag.has_attr('href') else 'src'
        url = tag.get(attr)
        if url:
            parsed_url = urlparse(url)
            if not parsed_url.scheme or parsed_url.netloc == urlparse(website_url).netloc:
                resources['other'].append(urljoin(website_url, url))

    return resources


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python list_resources.py <website_url>")
        sys.exit(1)
    website_url = sys.argv[1]
    resources = list_resources(website_url)
    print(json.dumps(resources, indent=2))