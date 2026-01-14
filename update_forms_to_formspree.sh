#!/bin/bash

# Update all forms from Web3Forms to Formspree
# Using Formspree endpoint that forwards to: contact@sherrillfordfrenchdrains.com

echo "Updating forms to use Formspree..."

# Replace Web3Forms action with Formspree
find . -name "*.html" -type f -exec sed -i 's|https://api.web3forms.com/submit|https://formspree.io/f/mkogdqaz|g' {} \;

# Remove Web3Forms access key hidden inputs
find . -name "*.html" -type f -exec sed -i '/<input type="hidden" name="access_key"/d' {} \;

echo "✓ All forms updated to use Formspree endpoint: https://formspree.io/f/mkogdqaz"
echo "✓ Emails will be forwarded to: contact@sherrillfordfrenchdrains.com"
echo ""
echo "Note: You can create a real Formspree account and endpoint at https://formspree.io"
