# Sherrill Ford French Drains - Deployment Guide

## Quick Start

Your site has been completely restructured and is ready to deploy! Here's everything you need to know.

---

## What's Been Done ✅

### Site Structure
- ✅ 17 HTML pages created (6 main, 3 service, 7 service area, 1 blog post)
- ✅ Navigation with dropdown menus implemented
- ✅ All pages use consistent Sherrill Ford branding (red/coral #FF5A5F, Poppins font)
- ✅ SEO files added (robots.txt, sitemap.xml, llms.txt)
- ✅ Forms migrated to Formspree
- ✅ Responsive design with Tailwind CSS

### Pages Created
1. **Main:** index.html, about.html, services.html, blog.html, contact.html, privacy.html, terms.html
2. **Services:** french-drain-installation.html, trench-drains.html, drain-cleaning-maintenance.html
3. **Service Areas:** 7 location pages (Sherrill's Ford, Mooresville, Denver, Lake Norman, Huntersville, Cornelius, Charlotte)

---

## Before You Deploy

### 1. Set Up Formspree (5 minutes)

Your forms currently use a placeholder Formspree endpoint. Set up your real endpoint:

1. Go to https://formspree.io
2. Sign up for a free account
3. Create a new form
4. Get your form endpoint (looks like: `https://formspree.io/f/xxxxxxxx`)
5. Update all forms:

```bash
cd /root/sherrills-ford-french-drains

# Replace placeholder with your real endpoint
find . -name "*.html" -type f -exec sed -i 's|https://formspree.io/f/mkogdqaz|https://formspree.io/f/YOUR_ENDPOINT|g' {} \;
```

6. Configure email forwarding in Formspree to: `contact@sherrillfordfrenchdrains.com`

### 2. Update Contact Information

Replace placeholder contact info with your real details:

**Current placeholders:**
- Phone: (704) 555-0123
- Email: info@sherrillfordfrenchdrains.com

**Update with:**
```bash
# Replace phone number
find . -name "*.html" -type f -exec sed -i 's|(704) 555-0123|YOUR_REAL_PHONE|g' {} \;

# Replace email
find . -name "*.html" -type f -exec sed -i 's|info@sherrillfordfrenchdrains.com|YOUR_REAL_EMAIL|g' {} \;
```

### 3. Update Domain (if different)

If your domain is NOT `sherrillfordfrenchdrains.com`, update:

```bash
# Update sitemap.xml
sed -i 's|sherrillfordfrenchdrains.com|YOUR_DOMAIN.com|g' sitemap.xml

# Update any canonical URLs
find . -name "*.html" -type f -exec sed -i 's|sherrillfordfrenchdrains.com|YOUR_DOMAIN.com|g' {} \;
```

---

## Deployment Options

### Option 1: Netlify (Recommended - Easiest)

1. **Push to GitHub first:**
```bash
cd /root/sherrills-ford-french-drains
git init
git add .
git commit -m "Initial deployment of Sherrill Ford French Drains"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/sherrills-ford-french-drains.git
git push -u origin main
```

2. **Deploy to Netlify:**
   - Go to https://netlify.com
   - Sign up/Login
   - Click "Add new site" → "Import an existing project"
   - Connect to GitHub
   - Select your repository
   - Click "Deploy site"
   - Done! Your site is live in ~2 minutes

3. **Custom Domain:**
   - In Netlify dashboard: Domain settings → Add custom domain
   - Follow DNS instructions
   - Enable HTTPS (automatic with Netlify)

### Option 2: Vercel

```bash
# Install Vercel CLI
npm install -g vercel

# Deploy
cd /root/sherrills-ford-french-drains
vercel --prod
```

### Option 3: GitHub Pages

```bash
# Push to GitHub
cd /root/sherrills-ford-french-drains
git init
git add .
git commit -m "Initial deployment"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/sherrills-ford-french-drains.git
git push -u origin main

# Enable GitHub Pages
# Go to repository Settings → Pages
# Source: Deploy from branch "main"
# Folder: / (root)
```

Your site will be at: `https://YOUR_USERNAME.github.io/sherrills-ford-french-drains/`

---

## Post-Deployment Checklist

### Immediate (Day 1)
- [ ] Test all forms - submit test entries
- [ ] Check all navigation links work
- [ ] Verify mobile responsiveness
- [ ] Test on different browsers (Chrome, Firefox, Safari)
- [ ] Verify contact information displays correctly

### Week 1
- [ ] Set up Google Analytics
- [ ] Set up Google Search Console
- [ ] Submit sitemap to Google: `https://your-domain.com/sitemap.xml`
- [ ] Set up Google My Business
- [ ] Add social media links to footer

### Month 1
- [ ] Add more blog posts (aim for 1-2 per week)
- [ ] Add customer testimonials
- [ ] Add service/project photos
- [ ] Monitor form submissions and respond promptly
- [ ] Check Google Analytics for traffic insights

---

## Adding Content

### Add a New Blog Post

1. Create new HTML file in `blog/` directory:
```bash
cd blog
cp complete-guide-to-french-drain-installation-in-she.html new-post-title.html
```

2. Edit the new file:
   - Update title, description, content
   - Keep the navigation structure
   - Keep the Sherrill Ford branding

3. Add to blog.html listing:
   - Add a new blog card with link to your new post

4. Update sitemap.xml:
   - Add new URL entry for the blog post

### Add a New Service

1. Edit `generate_all_pages.py`
2. Add new service to SERVICES array
3. Run: `python3 generate_all_pages.py`
4. Update navigation in all pages
5. Update sitemap.xml

### Add a New Service Area

1. Edit `generate_all_pages.py`
2. Add new area to SERVICE_AREAS array
3. Run: `python3 generate_all_pages.py`
4. Update dropdown navigation in all pages
5. Update sitemap.xml

---

## Monitoring & Maintenance

### Weekly
- Check form submissions
- Monitor Google Analytics traffic
- Respond to customer inquiries
- Check for broken links

### Monthly
- Review and respond to reviews (Google, Yelp, etc.)
- Publish new blog content
- Update service area pages with local news
- Check site speed and performance
- Review SEO rankings

### Quarterly
- Refresh testimonials
- Update service photos
- Review and update pricing if needed
- Audit for broken links
- Update contact information if changed

---

## SEO Optimization

### Google Search Console Setup
1. Go to https://search.google.com/search-console
2. Add property: your-domain.com
3. Verify ownership (via HTML file or DNS)
4. Submit sitemap: `https://your-domain.com/sitemap.xml`
5. Monitor search performance

### Local SEO
1. Claim Google My Business listing
2. Add schema.org markup for LocalBusiness
3. Get listed in local directories:
   - Yelp
   - Angie's List
   - HomeAdvisor
   - Thumbtack
4. Encourage customer reviews

### Content SEO
- Blog regularly (1-2 posts per week)
- Use keywords: "French drain installation Sherrill Ford NC", "drainage solutions Lake Norman", etc.
- Add alt tags to all images
- Internal linking between service and area pages

---

## Support & Resources

### Documentation
- See `RESTRUCTURE_SUMMARY.md` for detailed structure
- Original repo: https://github.com/tiegebentley/sherrill-ford-french-drain-installation-2026-01-14-73676
- Template reference: Denver NC Drainage Pros

### Tools & Services
- **Forms:** https://formspree.io
- **Analytics:** https://analytics.google.com
- **Search Console:** https://search.google.com/search-console
- **Domain:** https://namecheap.com or https://domains.google
- **Hosting:** https://netlify.com or https://vercel.com

### Quick Commands

```bash
# Navigate to site directory
cd /root/sherrills-ford-french-drains

# Regenerate all service/area pages
python3 generate_all_pages.py

# Update navigation on all pages
python3 update_navigation.py

# Update forms
./update_forms_to_formspree.sh

# List all pages
ls -1 *.html

# Check for broken links (install linkchecker first)
linkchecker index.html
```

---

## Troubleshooting

### Forms not working?
- Check Formspree endpoint is correct
- Verify email is set up in Formspree dashboard
- Test with a real submission
- Check browser console for errors

### Navigation dropdowns not working?
- Check JavaScript is loaded (view page source)
- Verify dropdown CSS is present in `<style>` section
- Check browser console for JavaScript errors

### Pages not loading?
- Verify all file names match exactly (case-sensitive)
- Check for broken links with browser dev tools
- Ensure all `href` attributes are correct

### Mobile menu not working?
- Current implementation is a placeholder (shows alert)
- Enhance with a proper slide-out menu
- See "Recommended Enhancements" in RESTRUCTURE_SUMMARY.md

---

## Next Steps

1. **Complete pre-deployment checklist above**
2. **Deploy to Netlify/Vercel**
3. **Set up Formspree and test forms**
4. **Configure Google Analytics and Search Console**
5. **Start adding blog content**
6. **Gather customer testimonials**
7. **Add professional photos**

---

## Success Metrics to Track

### Week 1
- Site is live and accessible
- Forms are working and receiving submissions
- Google Analytics is tracking visitors
- All pages load correctly on mobile and desktop

### Month 1
- 100+ visitors to the site
- 5+ form submissions
- 2-3 blog posts published
- Google Search Console shows site being indexed

### Month 3
- 500+ visitors per month
- 20+ form submissions per month
- Ranking for local keywords in Google
- 5+ customer reviews on Google My Business

---

**Your site is ready to launch! 🚀**

Good luck with Sherrill Ford French Drains!
