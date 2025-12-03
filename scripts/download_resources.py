import json
import os
import sys
from pathlib import Path
from urllib.parse import urlparse

import requests


def download_file(url: str, path: Path) -> None:
    """
    Download a file from a URL and save it to the specified output directory.

    Args:
        url (str): The URL of the file to download.
        path (Path): The file or directory where the file will be saved.
    """
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        if path.is_dir():
            parsed_url = urlparse(url)
            path = path / Path(parsed_url.path.lstrip("/"))
            path.parent.mkdir(parents=True, exist_ok=True)

        with open(path, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        print(f"Downloaded: {url} -> {path}")
    except requests.RequestException as e:
        print(f"Failed to download {url}: {e}")


def download_resources(
    resources: dict[str, list[str]], 
    output_dir: Path, 
    *, 
    resource_types: tuple[str, ...] | None = None
) -> None:
    """
    Download HTML, CSS, and image resources from the given resource dictionary.

    Args:
        resources (dict): A dictionary containing categorized resource URLs.
        output_dir (Path): The directory where resources will be saved.
        resource_types (tuple[str, ...] | None): A tuple of resource types to download.
            If None, all resource types will be downloaded.
    """
    resource_types = resource_types or tuple(resources.keys())
    for resource_type in resource_types:
        path = output_dir
        if resource_type == "html":
            path = output_dir / "index.html" 
        for url in resources.get(resource_type, []):
            download_file(url, path)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python download_resources.py <resources.json> <output_dir>")
        sys.exit(1)

    resources_file = Path(sys.argv[1])
    output_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else Path.cwd()
    output_dir.mkdir(parents=True, exist_ok=True)

    if not resources_file.is_file():
        print(f"Error: {resources_file} does not exist or is not a file.")
        sys.exit(1)

    resources = json.loads(resources_file.read_text())
    download_resources(
        resources, 
        output_dir, 
        resource_types=("html", "js")
    )