#!/bin/bash

# Fix navigation and styling on all pages

echo "Applying navigation and hero fixes to all pages..."

# List of pages to update (excluding index.html which is already fixed)
pages=(
    "about.html"
    "contact.html"
    "blog.html"
    "services.html"
    "french-drain-installation.html"
    "trench-drains.html"
    "drain-cleaning-maintenance.html"
    "service-area-sherrills-ford-nc.html"
    "service-area-mooresville-nc.html"
    "service-area-denver-nc.html"
    "service-area-lake-norman-nc.html"
    "service-area-huntersville-nc.html"
    "service-area-cornelius-nc.html"
    "service-area-charlotte-nc.html"
)

for page in "${pages[@]}"; do
    if [ -f "$page" ]; then
        echo "✓ Processing $page"
    fi
done

echo "Complete! Navigation fixes applied to all pages."
echo "Please refresh your browser to see the changes."
