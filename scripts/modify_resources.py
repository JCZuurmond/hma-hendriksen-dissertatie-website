import os
import re
import sys
from pathlib import Path

def modify_file(path: Path, app_folder: Path) -> None:
    """
    Modify a file by removing Gamma-related resources and replacing them with local resources.

    Args:
        path (Path): The path to the file to modify.
        app_folder (Path): The path to the local `_app` folder containing JavaScript files.
    """
    try:
        content = path.read_text(encoding="utf-8")

        # Remove Gamma-related resources (scripts, stylesheets, and metadata)
        #content = re.sub(r'<script.*?gammahosted.*?</script>', '', content, flags=re.DOTALL)
        #content = re.sub(r'<link.*?gammahosted.*?>', '', content, flags=re.DOTALL)
        #updated_contentcontent = re.sub(r'<meta.*?gamma\\.app.*?>', '', content, flags=re.DOTALL)

        # Replace remote JavaScript references with local ones from the `_app` folder
        content = re.sub(
            r'<script.*?src="https://assets\.gammahosted\.com/.*?/(_next/static/chunks/.*?)".*?></script>',
            lambda match: f'<script src="{app_folder / match.group(1)}" defer></script>',
            content
        )

        path.write_text(content, encoding="utf-8")
        print(f"Modified: {path}")
    except Exception as e:
        print(f"Failed to modify {path}: {e}")


def modify_resources(app_folder: Path, *html_paths: Path) -> None:
    """
    Modify all HTML files to remove Gamma-related resources and use local resources.

    Args:
        app_folder (Path): The path to the local `_app` folder containing JavaScript files.
        html_paths (Path): Paths to HTML files to modify.
    """
    for path in html_paths:
        modify_file(path, app_folder)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python modify_resources.py <app_folder> <html_file1> [<html_file2> ...]")
        sys.exit(1)

    app_folder = Path(sys.argv[1])
    html_files = [Path(arg) for arg in sys.argv[2:]]

    if not app_folder.is_dir():
        print(f"Error: {app_folder} does not exist or is not a directory.")
        sys.exit(1)

    modify_resources(app_folder, *html_files)