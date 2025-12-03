# Requirement:  Self-hosting static website.

## Context

The goal is to create a workflow that downloads all assets from a remote static
website and modifies them to host the website locally without any dependency on
the original remote website. This ensures the website can function independently
in a local environment.

## Use Case

A user wants to replicate a static website locally for archival purposes,
offline access, or customization. The workflow should automate the process of
downloading, restructuring, and modifying the website's resources to ensure all
dependencies are local.

## Tasks

### 1. List Resources

- Parse the given website URL to identify all required resources (e.g., HTML,
   CSS, JavaScript, images, fonts, etc.).
- Ensure the list includes all linked assets, such as external scripts,
   stylesheets, and media files.
- Handle dynamic resource loading (e.g., via JavaScript) to ensure completeness.

### 2. Download Resources

- Download all identified resources.
- Maintain the original folder structure of the website where possible.
- Save the resources into a predefined local directory structure.
- Handle potential errors, such as missing or restricted resources.

### 3. Modify Resources

- Update all resource references (e.g., URLs in HTML, CSS, and JavaScript files)
   to point to the local directory structure.
- Ensure that relative paths are used for local resources.
- Remove or replace any dependencies on external services (e.g., analytics
   scripts, CDNs).

### 4. Run Sanity Checks

- Verify that all resources have been downloaded and are accessible locally.
- Check that the modified website functions correctly in a browser.
- Identify and log any missing or broken resources.

## Acceptance Criteria

1. **Resource Listing**
   - All resources required to replicate the website are identified, including
      dynamically loaded assets.

2. **Resource Downloading**
   - All identified resources are downloaded and saved in the correct local
      directory structure.
   - Errors during the download process are logged and handled gracefully.

3. **Resource Modification**
   - All resource references in the website files are updated to point to local
      paths.
   - External dependencies are removed or replaced.

4. **Sanity Checks**
   - The local version of the website is fully functional and visually
      consistent with the original.
   - Any missing or broken resources are logged for review.
