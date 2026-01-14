#!/usr/bin/env python3
"""
Generate all service pages and service area pages for Sherrill Ford French Drains
while preserving the unique Sherrill Ford style (red/coral colors, Poppins font)
"""

import os

# Service pages configuration
SERVICES = [
    {
        "filename": "french-drain-installation.html",
        "title": "French Drain Installation | Sherrill Ford French Drains",
        "h1": "Professional French Drain Installation",
        "subtitle": "Permanent solutions to protect your property from water damage",
        "icon": "fa-water",
        "description": "Expert French drain installation services in Sherrill Ford, NC. Stop flooding, protect your foundation, and eliminate standing water with our professional drainage solutions.",
        "content": {
            "intro": "French drains are the gold standard for managing water problems on your property. Our expert installation creates a permanent solution that redirects water away from your foundation, preventing costly damage and protecting your investment.",
            "benefits": [
                {"icon": "fa-shield-alt", "title": "Foundation Protection", "desc": "Prevent water from damaging your home's foundation"},
                {"icon": "fa-home", "title": "Basement Waterproofing", "desc": "Keep your basement dry and mold-free"},
                {"icon": "fa-chart-line", "title": "Property Value", "desc": "Increase your home's value with proper drainage"},
                {"icon": "fa-leaf", "title": "Landscape Protection", "desc": "Preserve your landscaping and prevent erosion"}
            ],
            "process": [
                {"step": "1", "title": "Free Consultation", "desc": "We assess your property and identify drainage issues"},
                {"step": "2", "title": "Custom Design", "desc": "We create a drainage plan tailored to your property"},
                {"step": "3", "title": "Professional Installation", "desc": "Our team installs your French drain system"},
                {"step": "4", "title": "Quality Assurance", "desc": "We test the system and ensure proper function"}
            ]
        }
    },
    {
        "filename": "trench-drains.html",
        "title": "Trench Drain Installation | Sherrill Ford French Drains",
        "h1": "Trench Drain Installation & Repair",
        "subtitle": "Heavy-duty drainage for driveways, patios, and commercial properties",
        "icon": "fa-road",
        "description": "Professional trench drain installation in Sherrill Ford, NC. Perfect for driveways, patios, and areas with heavy water flow. Durable, effective, and built to last.",
        "content": {
            "intro": "Trench drains are ideal for managing large volumes of water in specific areas. Whether it's your driveway, patio, or commercial property, our trench drain systems provide superior water management and protection.",
            "benefits": [
                {"icon": "fa-car", "title": "Driveway Protection", "desc": "Prevent water pooling and ice formation on driveways"},
                {"icon": "fa-industry", "title": "Commercial Solutions", "desc": "Heavy-duty systems for parking lots and loading areas"},
                {"icon": "fa-swimming-pool", "title": "Pool & Patio", "desc": "Keep pool decks and patios dry and safe"},
                {"icon": "fa-wrench", "title": "Custom Solutions", "desc": "Tailored to your specific drainage needs"}
            ],
            "process": [
                {"step": "1", "title": "Site Evaluation", "desc": "We analyze water flow patterns and problem areas"},
                {"step": "2", "title": "System Design", "desc": "We design a trench drain system for optimal performance"},
                {"step": "3", "title": "Installation", "desc": "Professional installation with quality materials"},
                {"step": "4", "title": "Testing", "desc": "We verify proper function and water flow"}
            ]
        }
    },
    {
        "filename": "drain-cleaning-maintenance.html",
        "title": "Drain Cleaning & Maintenance | Sherrill Ford French Drains",
        "h1": "Drain Cleaning & Maintenance Services",
        "subtitle": "Keep your drainage system flowing freely year-round",
        "icon": "fa-broom",
        "description": "Professional drain cleaning and maintenance in Sherrill Ford, NC. Regular maintenance prevents clogs and ensures your drainage system operates at peak efficiency.",
        "content": {
            "intro": "Regular maintenance is essential to keep your drainage system working properly. Our comprehensive cleaning and maintenance services prevent clogs, remove debris, and extend the life of your drainage system.",
            "benefits": [
                {"icon": "fa-clock", "title": "Prevent Problems", "desc": "Regular maintenance prevents costly repairs"},
                {"icon": "fa-tint", "title": "Optimal Flow", "desc": "Keep drains flowing at maximum capacity"},
                {"icon": "fa-calendar-check", "title": "Scheduled Service", "desc": "Annual or seasonal maintenance plans available"},
                {"icon": "fa-tools", "title": "Expert Care", "desc": "Professional cleaning and inspection"}
            ],
            "process": [
                {"step": "1", "title": "Inspection", "desc": "We inspect your drainage system for issues"},
                {"step": "2", "title": "Cleaning", "desc": "We remove debris, sediment, and blockages"},
                {"step": "3", "title": "Testing", "desc": "We test water flow and system performance"},
                {"step": "4", "title": "Recommendations", "desc": "We provide maintenance tips and future planning"}
            ]
        }
    }
]

# Service areas configuration
SERVICE_AREAS = [
    {
        "filename": "service-area-sherrills-ford-nc.html",
        "city": "Sherrill's Ford",
        "state": "NC",
        "description": "Professional French drain installation and drainage solutions in Sherrill's Ford, NC. Local experts serving our home community.",
        "local_info": "As a locally-based company, Sherrill's Ford is our home. We understand the unique drainage challenges of our area, from clay soil to seasonal flooding. Our team provides fast, reliable service to our neighbors and friends."
    },
    {
        "filename": "service-area-mooresville-nc.html",
        "city": "Mooresville",
        "state": "NC",
        "description": "Expert French drain installation in Mooresville, NC. Protecting Race City properties from water damage with professional drainage solutions.",
        "local_info": "Serving Mooresville with pride, we understand the drainage challenges unique to this growing community. From historic downtown to new developments, we provide reliable drainage solutions."
    },
    {
        "filename": "service-area-denver-nc.html",
        "city": "Denver",
        "state": "NC",
        "description": "Professional drainage solutions in Denver, NC. French drain installation, trench drains, and maintenance services for Lincoln County properties.",
        "local_info": "Denver residents trust us for expert drainage solutions. We're familiar with the local terrain and soil conditions, ensuring your drainage system is designed for maximum effectiveness."
    },
    {
        "filename": "service-area-lake-norman-nc.html",
        "city": "Lake Norman",
        "state": "NC",
        "description": "Lake Norman drainage solutions - French drains, waterfront property protection, and expert installation. Serving all Lake Norman communities.",
        "local_info": "Lake Norman properties require special attention to drainage. We specialize in waterfront and lakeside drainage solutions that protect your property while preserving the natural beauty of the area."
    },
    {
        "filename": "service-area-huntersville-nc.html",
        "city": "Huntersville",
        "state": "NC",
        "description": "French drain installation in Huntersville, NC. Professional drainage solutions for residential and commercial properties in North Mecklenburg.",
        "local_info": "Huntersville's rapid growth brings unique drainage challenges. We provide professional solutions for new construction and existing properties throughout North Mecklenburg County."
    },
    {
        "filename": "service-area-cornelius-nc.html",
        "city": "Cornelius",
        "state": "NC",
        "description": "Expert drainage solutions in Cornelius, NC. French drain installation, trench drains, and maintenance for Lake Norman area properties.",
        "local_info": "Cornelius homeowners and businesses rely on our expertise for comprehensive drainage solutions. We understand the local landscape and provide tailored systems for every property."
    },
    {
        "filename": "service-area-charlotte-nc.html",
        "city": "Charlotte",
        "state": "NC",
        "description": "Professional French drain installation in Charlotte, NC. Serving greater Charlotte with expert drainage solutions and foundation protection.",
        "local_info": "As Charlotte continues to grow, proper drainage is more important than ever. We serve all Charlotte neighborhoods with fast, professional drainage solutions."
    }
]

def generate_service_page(service):
    """Generate a service page HTML file"""
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{service['description']}">
    <meta name="keywords" content="French drain, drainage solutions, Sherrill Ford NC, {service['h1']}">
    <title>{service['title']}</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        * {{ font-family: 'Poppins', sans-serif; }}
        html {{ scroll-behavior: smooth; }}
        .text-primary {{ color: #FF5A5F; }}
        .bg-primary {{ background-color: #FF5A5F; }}
        .border-primary {{ border-color: #FF5A5F; }}
        .text-accent {{ color: #FFD166; }}
        .bg-accent {{ background-color: #FFD166; }}
        .btn-primary {{
            background-color: #FF5A5F;
            color: white;
            padding: 12px 24px;
            border-radius: 4px;
            font-weight: 600;
            transition: all 0.3s ease-in-out;
            display: inline-block;
            border: 2px solid #FF5A5F;
        }}
        .btn-primary:hover {{
            background-color: white;
            color: #FF5A5F;
            transform: scale(1.05);
            box-shadow: 0 4px 12px rgba(255, 90, 95, 0.3);
        }}
        .dropdown-menu {{
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
        }}
        .dropdown-menu.active {{ display: block; }}
        .dropdown-item {{
            display: block;
            padding: 12px 16px;
            color: #374151;
            text-decoration: none;
            transition: all 300ms ease-out;
            border-bottom: 1px solid #e5e7eb;
        }}
        .dropdown-item:last-child {{ border-bottom: none; }}
        .dropdown-item:hover {{
            background-color: #fef2f2;
            color: #FF5A5F;
            padding-left: 20px;
        }}
    </style>
</head>
<body class="bg-white text-gray-900">
    <!-- Header -->
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
    </header>

    <!-- Hero Section -->
    <section class="bg-gradient-to-br from-gray-900 to-gray-800 text-white py-20">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center">
                <i class="fas {service['icon']} text-6xl mb-6 text-accent"></i>
                <h1 class="text-4xl md:text-5xl font-bold mb-6">{service['h1']}</h1>
                <p class="text-xl text-gray-300 max-w-3xl mx-auto mb-8">
                    {service['subtitle']}
                </p>
                <a href="contact.html" class="btn-primary text-lg px-8 py-4">
                    Get Your Free Estimate
                </a>
            </div>
        </div>
    </section>

    <!-- Introduction -->
    <section class="py-16">
        <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
            <p class="text-lg text-gray-600 leading-relaxed">
                {service['content']['intro']}
            </p>
        </div>
    </section>

    <!-- Benefits -->
    <section class="py-16 bg-gray-50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <h2 class="text-3xl font-bold text-center mb-12">Benefits of Our Service</h2>
            <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-8">
                {"".join([f'''
                <div class="bg-white p-6 rounded-lg shadow-md text-center">
                    <i class="fas {benefit['icon']} text-4xl text-primary mb-4"></i>
                    <h3 class="text-xl font-bold mb-3">{benefit['title']}</h3>
                    <p class="text-gray-600">{benefit['desc']}</p>
                </div>
                ''' for benefit in service['content']['benefits']])}
            </div>
        </div>
    </section>

    <!-- Process -->
    <section class="py-16">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <h2 class="text-3xl font-bold text-center mb-12">Our Process</h2>
            <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-8">
                {"".join([f'''
                <div class="text-center">
                    <div class="w-16 h-16 bg-primary text-white rounded-full flex items-center justify-center text-2xl font-bold mx-auto mb-4">
                        {step['step']}
                    </div>
                    <h3 class="text-xl font-bold mb-3">{step['title']}</h3>
                    <p class="text-gray-600">{step['desc']}</p>
                </div>
                ''' for step in service['content']['process']])}
            </div>
        </div>
    </section>

    <!-- CTA Section -->
    <section class="py-16 bg-primary text-white">
        <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
            <h2 class="text-3xl md:text-4xl font-bold mb-6">Ready to Get Started?</h2>
            <p class="text-xl mb-8">Contact us today for a free, no-obligation estimate!</p>
            <a href="contact.html" class="inline-block bg-white text-primary px-8 py-4 rounded font-bold text-lg hover:bg-gray-100 transition-colors">
                Get Your Free Quote
            </a>
        </div>
    </section>

    <!-- Footer -->
    <footer class="bg-gray-900 text-white py-12">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid md:grid-cols-4 gap-8">
                <div>
                    <h3 class="text-lg font-bold mb-4">Sherrill Ford French Drains</h3>
                    <p class="text-gray-400">Professional drainage solutions for the Lake Norman area.</p>
                </div>
                <div>
                    <h4 class="text-lg font-bold mb-4">Services</h4>
                    <ul class="space-y-2">
                        <li><a href="french-drain-installation.html" class="text-gray-400 hover:text-white">French Drain Installation</a></li>
                        <li><a href="trench-drains.html" class="text-gray-400 hover:text-white">Trench Drains</a></li>
                        <li><a href="drain-cleaning-maintenance.html" class="text-gray-400 hover:text-white">Drain Cleaning & Maintenance</a></li>
                    </ul>
                </div>
                <div>
                    <h4 class="text-lg font-bold mb-4">Quick Links</h4>
                    <ul class="space-y-2">
                        <li><a href="about.html" class="text-gray-400 hover:text-white">About</a></li>
                        <li><a href="blog.html" class="text-gray-400 hover:text-white">Blog</a></li>
                        <li><a href="contact.html" class="text-gray-400 hover:text-white">Contact</a></li>
                    </ul>
                </div>
                <div>
                    <h4 class="text-lg font-bold mb-4">Contact</h4>
                    <ul class="space-y-2 text-gray-400">
                        <li><i class="fas fa-phone mr-2"></i> (704) 555-0123</li>
                        <li><i class="fas fa-envelope mr-2"></i> info@sherrillfordfrenchdrains.com</li>
                        <li><i class="fas fa-map-marker-alt mr-2"></i> Sherrill's Ford, NC</li>
                    </ul>
                </div>
            </div>
            <div class="border-t border-gray-800 mt-8 pt-8 text-center text-gray-400">
                <p>&copy; 2026 Sherrill Ford French Drains. All rights reserved.</p>
                <div class="mt-4 space-x-4">
                    <a href="privacy.html" class="hover:text-white">Privacy Policy</a>
                    <a href="terms.html" class="hover:text-white">Terms of Service</a>
                </div>
            </div>
        </div>
    </footer>

    <script>
        // Dropdown functionality
        document.querySelector('.services-dropdown-btn')?.addEventListener('click', function(e) {{
            e.stopPropagation();
            document.querySelector('.services-dropdown').classList.toggle('active');
            document.querySelector('.areas-dropdown').classList.remove('active');
        }});

        document.querySelector('.areas-dropdown-btn')?.addEventListener('click', function(e) {{
            e.stopPropagation();
            document.querySelector('.areas-dropdown').classList.toggle('active');
            document.querySelector('.services-dropdown').classList.remove('active');
        }});

        document.addEventListener('click', function() {{
            document.querySelectorAll('.dropdown-menu').forEach(menu => menu.classList.remove('active'));
        }});

        // Mobile menu
        document.getElementById('mobile-menu-btn')?.addEventListener('click', function() {{
            alert('Mobile menu coming soon!');
        }});
    </script>
</body>
</html>"""

    with open(service['filename'], 'w') as f:
        f.write(html)
    print(f"✓ Created {service['filename']}")

def generate_service_area_page(area):
    """Generate a service area page HTML file"""
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{area['description']}">
    <meta name="keywords" content="French drain {area['city']}, drainage solutions {area['city']} {area['state']}, french drain installation">
    <title>French Drain Installation {area['city']}, {area['state']} | Sherrill Ford French Drains</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        * {{ font-family: 'Poppins', sans-serif; }}
        html {{ scroll-behavior: smooth; }}
        .text-primary {{ color: #FF5A5F; }}
        .bg-primary {{ background-color: #FF5A5F; }}
        .border-primary {{ border-color: #FF5A5F; }}
        .text-accent {{ color: #FFD166; }}
        .bg-accent {{ background-color: #FFD166; }}
        .btn-primary {{
            background-color: #FF5A5F;
            color: white;
            padding: 12px 24px;
            border-radius: 4px;
            font-weight: 600;
            transition: all 0.3s ease-in-out;
            display: inline-block;
            border: 2px solid #FF5A5F;
        }}
        .btn-primary:hover {{
            background-color: white;
            color: #FF5A5F;
            transform: scale(1.05);
            box-shadow: 0 4px 12px rgba(255, 90, 95, 0.3);
        }}
        .dropdown-menu {{
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
        }}
        .dropdown-menu.active {{ display: block; }}
        .dropdown-item {{
            display: block;
            padding: 12px 16px;
            color: #374151;
            text-decoration: none;
            transition: all 300ms ease-out;
            border-bottom: 1px solid #e5e7eb;
        }}
        .dropdown-item:last-child {{ border-bottom: none; }}
        .dropdown-item:hover {{
            background-color: #fef2f2;
            color: #FF5A5F;
            padding-left: 20px;
        }}
    </style>
</head>
<body class="bg-white text-gray-900">
    <!-- Header -->
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
    </header>

    <!-- Hero Section -->
    <section class="bg-gradient-to-br from-gray-900 to-gray-800 text-white py-20">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center">
                <i class="fas fa-map-marker-alt text-6xl mb-6 text-accent"></i>
                <h1 class="text-4xl md:text-5xl font-bold mb-6">French Drain Installation in {area['city']}, {area['state']}</h1>
                <p class="text-xl text-gray-300 max-w-3xl mx-auto mb-8">
                    Professional drainage solutions for {area['city']} properties
                </p>
                <a href="contact.html" class="btn-primary text-lg px-8 py-4">
                    Get Your Free Estimate
                </a>
            </div>
        </div>
    </section>

    <!-- Local Info -->
    <section class="py-16">
        <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
            <h2 class="text-3xl font-bold mb-6">Serving {area['city']}, {area['state']}</h2>
            <p class="text-lg text-gray-600 leading-relaxed mb-8">
                {area['local_info']}
            </p>
        </div>
    </section>

    <!-- Services in Area -->
    <section class="py-16 bg-gray-50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <h2 class="text-3xl font-bold text-center mb-12">Our Services in {area['city']}</h2>
            <div class="grid md:grid-cols-3 gap-8">
                <div class="bg-white p-6 rounded-lg shadow-md">
                    <i class="fas fa-water text-4xl text-primary mb-4"></i>
                    <h3 class="text-xl font-bold mb-3">French Drain Installation</h3>
                    <p class="text-gray-600 mb-4">Permanent solutions for water management and foundation protection.</p>
                    <a href="french-drain-installation.html" class="text-primary font-semibold hover:underline">Learn More →</a>
                </div>
                <div class="bg-white p-6 rounded-lg shadow-md">
                    <i class="fas fa-road text-4xl text-primary mb-4"></i>
                    <h3 class="text-xl font-bold mb-3">Trench Drains</h3>
                    <p class="text-gray-600 mb-4">Heavy-duty drainage for driveways, patios, and commercial properties.</p>
                    <a href="trench-drains.html" class="text-primary font-semibold hover:underline">Learn More →</a>
                </div>
                <div class="bg-white p-6 rounded-lg shadow-md">
                    <i class="fas fa-broom text-4xl text-primary mb-4"></i>
                    <h3 class="text-xl font-bold mb-3">Drain Cleaning & Maintenance</h3>
                    <p class="text-gray-600 mb-4">Keep your drainage system flowing freely year-round.</p>
                    <a href="drain-cleaning-maintenance.html" class="text-primary font-semibold hover:underline">Learn More →</a>
                </div>
            </div>
        </div>
    </section>

    <!-- Why Choose Us -->
    <section class="py-16">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <h2 class="text-3xl font-bold text-center mb-12">Why {area['city']} Chooses Us</h2>
            <div class="grid md:grid-cols-3 gap-8">
                <div class="text-center">
                    <i class="fas fa-map-marked-alt text-4xl text-primary mb-4"></i>
                    <h3 class="text-xl font-bold mb-3">Local Experts</h3>
                    <p class="text-gray-600">We understand {area['city']}'s unique drainage challenges</p>
                </div>
                <div class="text-center">
                    <i class="fas fa-clock text-4xl text-primary mb-4"></i>
                    <h3 class="text-xl font-bold mb-3">Fast Response</h3>
                    <p class="text-gray-600">Same-day service available for emergencies</p>
                </div>
                <div class="text-center">
                    <i class="fas fa-shield-alt text-4xl text-primary mb-4"></i>
                    <h3 class="text-xl font-bold mb-3">Lifetime Warranty</h3>
                    <p class="text-gray-600">Your investment is protected forever</p>
                </div>
            </div>
        </div>
    </section>

    <!-- CTA Section -->
    <section class="py-16 bg-primary text-white">
        <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
            <h2 class="text-3xl md:text-4xl font-bold mb-6">Ready to Solve Your {area['city']} Drainage Problems?</h2>
            <p class="text-xl mb-8">Contact us today for a free, no-obligation estimate!</p>
            <a href="contact.html" class="inline-block bg-white text-primary px-8 py-4 rounded font-bold text-lg hover:bg-gray-100 transition-colors">
                Get Your Free Quote
            </a>
        </div>
    </section>

    <!-- Footer -->
    <footer class="bg-gray-900 text-white py-12">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid md:grid-cols-4 gap-8">
                <div>
                    <h3 class="text-lg font-bold mb-4">Sherrill Ford French Drains</h3>
                    <p class="text-gray-400">Professional drainage solutions for the Lake Norman area.</p>
                </div>
                <div>
                    <h4 class="text-lg font-bold mb-4">Services</h4>
                    <ul class="space-y-2">
                        <li><a href="french-drain-installation.html" class="text-gray-400 hover:text-white">French Drain Installation</a></li>
                        <li><a href="trench-drains.html" class="text-gray-400 hover:text-white">Trench Drains</a></li>
                        <li><a href="drain-cleaning-maintenance.html" class="text-gray-400 hover:text-white">Drain Cleaning & Maintenance</a></li>
                    </ul>
                </div>
                <div>
                    <h4 class="text-lg font-bold mb-4">Quick Links</h4>
                    <ul class="space-y-2">
                        <li><a href="about.html" class="text-gray-400 hover:text-white">About</a></li>
                        <li><a href="blog.html" class="text-gray-400 hover:text-white">Blog</a></li>
                        <li><a href="contact.html" class="text-gray-400 hover:text-white">Contact</a></li>
                    </ul>
                </div>
                <div>
                    <h4 class="text-lg font-bold mb-4">Contact</h4>
                    <ul class="space-y-2 text-gray-400">
                        <li><i class="fas fa-phone mr-2"></i> (704) 555-0123</li>
                        <li><i class="fas fa-envelope mr-2"></i> info@sherrillfordfrenchdrains.com</li>
                        <li><i class="fas fa-map-marker-alt mr-2"></i> Sherrill's Ford, NC</li>
                    </ul>
                </div>
            </div>
            <div class="border-t border-gray-800 mt-8 pt-8 text-center text-gray-400">
                <p>&copy; 2026 Sherrill Ford French Drains. All rights reserved.</p>
                <div class="mt-4 space-x-4">
                    <a href="privacy.html" class="hover:text-white">Privacy Policy</a>
                    <a href="terms.html" class="hover:text-white">Terms of Service</a>
                </div>
            </div>
        </div>
    </footer>

    <script>
        // Dropdown functionality
        document.querySelector('.services-dropdown-btn')?.addEventListener('click', function(e) {{
            e.stopPropagation();
            document.querySelector('.services-dropdown').classList.toggle('active');
            document.querySelector('.areas-dropdown').classList.remove('active');
        }});

        document.querySelector('.areas-dropdown-btn')?.addEventListener('click', function(e) {{
            e.stopPropagation();
            document.querySelector('.areas-dropdown').classList.toggle('active');
            document.querySelector('.services-dropdown').classList.remove('active');
        }});

        document.addEventListener('click', function() {{
            document.querySelectorAll('.dropdown-menu').forEach(menu => menu.classList.remove('active'));
        }});

        // Mobile menu
        document.getElementById('mobile-menu-btn')?.addEventListener('click', function() {{
            alert('Mobile menu coming soon!');
        }});
    </script>
</body>
</html>"""

    with open(area['filename'], 'w') as f:
        f.write(html)
    print(f"✓ Created {area['filename']}")

if __name__ == "__main__":
    print("Generating service pages...")
    for service in SERVICES:
        generate_service_page(service)

    print("\nGenerating service area pages...")
    for area in SERVICE_AREAS:
        generate_service_area_page(area)

    print("\n✅ All pages generated successfully!")
