import os
import re
import sys
import json
from pathlib import Path

def load_resources(resources_file: Path) -> dict:
    """
    Load the resources from the JSON file.

    Args:
        resources_file (Path): The path to the resources JSON file.

    Returns:
        dict: A dictionary containing the resources categorized by type.
    """
    try:
        with resources_file.open("r", encoding="utf-8") as file:
            return json.load(file)
    except Exception as e:
        print(f"Failed to load resources file {resources_file}: {e}")
        sys.exit(1)

def modify_file(path: Path, resources: dict) -> None:
    """
    Modify a file by replacing specific HTTPS references with local references.

    Args:
        path (Path): The path to the file to modify.
        resources (dict): A dictionary containing the resources to replace.
    """
    try:
        content = path.read_text(encoding="utf-8")

        # Replace specific links in the content based on the resources file
        for _, links in resources.items():
            for link in links:
                local_reference = f"./{Path(link).name}"
                content = content.replace(link, local_reference)

        path.write_text(content, encoding="utf-8")
        print(f"Modified: {path}")
    except Exception as e:
        print(f"Failed to modify {path}: {e}")

def modify_resources(resources_file: Path, *html_paths: Path) -> None:
    """
    Modify all HTML files to replace specific HTTPS references with local references.

    Args:
        resources_file (Path): The path to the resources JSON file.
        html_paths (Path): Paths to HTML files to modify.
    """
    resources = load_resources(resources_file)
    for path in html_paths:
        modify_file(path, resources)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python modify_resources.py <resources_file> <html_file1> [<html_file2> ...]")
        sys.exit(1)

    resources_file = Path(sys.argv[1])
    html_files = [Path(arg) for arg in sys.argv[2:]]

    if not resources_file.is_file():
        print(f"Error: {resources_file} does not exist or is not a file.")
        sys.exit(1)

    modify_resources(resources_file, *html_files)