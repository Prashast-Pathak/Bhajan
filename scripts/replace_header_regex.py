import os
import re
import glob

# First, extract the components from bhajan.html
with open('bhajan.html', 'r', encoding='utf-8') as f:
    bhajan = f.read()

# 1. Extract CSS
# Let's find the exact block in bhajan.html between <style> and </style>
# Wait, bhajan.html just has one <style> block? Let's check!
