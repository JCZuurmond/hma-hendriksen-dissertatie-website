import os
import re
import sys
from pathlib import Path

def modify_file(path: Path) -> None:
    """
    Modify a file by removing Gamma-related resources.

    Args:
        file_path (Path): The path to the file to modify.
    """
    try:
        content = path.read_text(encoding="utf-8")

        # Remove Gamma-related resources (scripts, stylesheets, and metadata)
        #updated_content = re.sub(r'<script.*?gammahosted.*?</script>', '', content, flags=re.DOTALL)
        #updated_content = re.sub(r'<link.*?gammahosted.*?>', '', updated_content, flags=re.DOTALL)
        content = re.sub(r'<meta.*?gamma\\.app.*?>', '', content, flags=re.DOTALL)

        path.write_text(content, encoding="utf-8")
        print(f"Modified: {path}")
    except Exception as e:
        print(f"Failed to modify {path}: {e}")


def modify_resources(*html_paths: Path) -> None:
    """
    Modify all HTML files in the given directory to remove Gamma-related
    resources.

    Args:
        html_paths (Path): Paths to HTML files to modify.
    """
    for path in html_paths:
        modify_file(path)


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        html_files = [Path(arg) for arg in sys.argv[1:]]
    else:
        html_files = Path.cwd().rglob("*.html")
    modify_resources(*html_files)