# Static website hosting

This project hosts a static website using GitHub Pages. 

The website content is automatically updated by [a GitHub Actions
workflow](.github/workflows/update-website.yml), which downloads a webpage and
publishes it to GitHub Pages.

## Repository Structure

``` tree
|- .github/workflows/update-website.yml     -- The workflow that updates the website
|- index.html                               -- The static website
```
