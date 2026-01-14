#!/usr/bin/env python3
"""
Update navigation in existing Sherrill Ford French Drains pages
"""

import re
import os

# Navigation HTML with Sherrill Ford style
NAVIGATION_HTML = '''    <!-- Header -->
    <header class="sticky top-0 z-50 bg-white shadow-md">
        <nav class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4 flex items-center justify-between">
            <a href="index.html" class="flex items-center gap-2">
                <i class="fas fa-water text-3xl text-primary"></i>
                <span class="text-xl font-bold">Sherrill Ford French Drains</span>
            </a>

            <div class="hidden lg:flex items-center gap-6">
                <a href="index.html" class="text-gray-700 hover:text-primary transition-colors font-medium">Home</a>

                <div class="relative services-link">
                    <button class="services-dropdown-btn text-gray-700 hover:text-primary transition-colors font-medium flex items-center gap-1">
                        Services <i class="fas fa-chevron-down text-xs"></i>
                    </button>
                    <div class="dropdown-menu services-dropdown">
                        <a href="french-drain-installation.html" class="dropdown-item">French Drain Installation</a>
                        <a href="trench-drains.html" class="dropdown-item">Trench Drains</a>
                        <a href="drain-cleaning-maintenance.html" class="dropdown-item">Drain Cleaning & Maintenance</a>
                    </div>
                </div>

                <div class="relative service-areas-link">
                    <button class="areas-dropdown-btn text-gray-700 hover:text-primary transition-colors font-medium flex items-center gap-1">
                        Service Areas <i class="fas fa-chevron-down text-xs"></i>
                    </button>
                    <div class="dropdown-menu areas-dropdown">
                        <a href="service-area-sherrills-ford-nc.html" class="dropdown-item">Sherrill's Ford</a>
                        <a href="service-area-mooresville-nc.html" class="dropdown-item">Mooresville</a>
                        <a href="service-area-denver-nc.html" class="dropdown-item">Denver</a>
                        <a href="service-area-lake-norman-nc.html" class="dropdown-item">Lake Norman</a>
                        <a href="service-area-huntersville-nc.html" class="dropdown-item">Huntersville</a>
                    </div>
                </div>

                <a href="about.html" class="text-gray-700 hover:text-primary transition-colors font-medium">About</a>
                <a href="blog.html" class="text-gray-700 hover:text-primary transition-colors font-medium">Blog</a>
                <a href="contact.html" class="btn-primary">Get Free Quote</a>
            </div>

            <button class="lg:hidden text-gray-700" id="mobile-menu-btn">
                <i class="fas fa-bars text-2xl"></i>
            </button>
        </nav>
    </header>'''

# Dropdown CSS to add to style section
DROPDOWN_CSS = '''        .dropdown-menu {
            display: none;
            position: absolute;
            top: 100%;
            left: 0;
            background: white;
            border: 1px solid #e5e7eb;
            border-radius: 0.5rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            min-width: 200px;
            z-index: 40;
            margin-top: 0.5rem;
        }
        .dropdown-menu.active { display: block; }
        .dropdown-item {
            display: block;
            padding: 12px 16px;
            color: #374151;
            text-decoration: none;
            transition: all 300ms ease-out;
            border-bottom: 1px solid #e5e7eb;
        }
        .dropdown-item:last-child { border-bottom: none; }
        .dropdown-item:hover {
            background-color: #fef2f2;
            color: #FF5A5F;
            padding-left: 20px;
        }'''

# JavaScript for dropdown functionality
DROPDOWN_JS = '''        // Dropdown functionality
        document.querySelector('.services-dropdown-btn')?.addEventListener('click', function(e) {
            e.stopPropagation();
            document.querySelector('.services-dropdown').classList.toggle('active');
            document.querySelector('.areas-dropdown')?.classList.remove('active');
        });

        document.querySelector('.areas-dropdown-btn')?.addEventListener('click', function(e) {
            e.stopPropagation();
            document.querySelector('.areas-dropdown').classList.toggle('active');
            document.querySelector('.services-dropdown')?.classList.remove('active');
        });

        document.addEventListener('click', function() {
            document.querySelectorAll('.dropdown-menu').forEach(menu => menu.classList.remove('active'));
        });

        // Mobile menu
        document.getElementById('mobile-menu-btn')?.addEventListener('click', function() {
            alert('Mobile menu coming soon!');
        });'''

FILES_TO_UPDATE = ['index.html', 'contact.html', 'blog.html', 'services.html', 'privacy.html', 'terms.html']

def update_file(filename):
    """Update a file with new navigation"""
    if not os.path.exists(filename):
        print(f"⚠ Skipping {filename} - file not found")
        return

    with open(filename, 'r') as f:
        content = f.read()

    # Replace old header/nav with new navigation
    # Match from <header to </header> or <nav to </nav>
    nav_pattern = r'<header[^>]*>.*?</header>'
    content = re.sub(nav_pattern, NAVIGATION_HTML, content, flags=re.DOTALL)

    # If no header found, try nav
    if '<header' not in content and '<nav' in content:
        nav_pattern = r'<nav[^>]*>.*?</nav>'
        content = re.sub(nav_pattern, NAVIGATION_HTML.replace('<header', '<nav').replace('</header>', '</nav>'), content, flags=re.DOTALL)

    # Add dropdown CSS if not present
    if 'dropdown-menu' not in content and '</style>' in content:
        content = content.replace('</style>', DROPDOWN_CSS + '\n    </style>')

    # Add dropdown JS if not present
    if 'services-dropdown-btn' not in content and '</script>' in content:
        content = content.replace('</script>', DROPDOWN_JS + '\n    </script>')
    elif 'services-dropdown-btn' not in content and '</body>' in content:
        content = content.replace('</body>', f'    <script>\n{DROPDOWN_JS}\n    </script>\n</body>')

    with open(filename, 'w') as f:
        f.write(content)

    print(f"✓ Updated {filename}")

if __name__ == "__main__":
    print("Updating navigation in existing pages...")
    for filename in FILES_TO_UPDATE:
        update_file(filename)
    print("\n✅ Navigation updates complete!")
