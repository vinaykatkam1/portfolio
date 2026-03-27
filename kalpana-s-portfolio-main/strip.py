import sys, re

filepath = r'c:\Users\Vinay\Downloads\kalpana-s-portfolio-main\kalpana-s-portfolio-main\index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove Live Stats section
content = re.sub(r'<!--  LIVE STATS  -->.*?</section>', '', content, flags=re.DOTALL)

# Remove Leetcode / Github heatmaps in scripts
content = re.sub(r'/\*  LIVE STATS — rings \+ heatmap  \*/.*?\)\(\);', '', content, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
