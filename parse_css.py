import re

files = ['index.html', 'oscp-journey.html', 'evilrdp.html', 'siem.html']

all_blocks = []
for file in files:
    with open(file, 'r') as f:
        content = f.read()
        match = re.search(r'<style>\s*(.*?)\s*</style>', content, re.DOTALL)
        if match:
            all_blocks.append(match.group(1))

def extract_blocks_raw(css):
    blocks = []
    current_block = ""
    brace_level = 0
    in_comment = False
    i = 0
    while i < len(css):
        if css[i:i+2] == '/*' and not in_comment:
            in_comment = True
            current_block += '/*'
            i += 2
            continue
        if css[i:i+2] == '*/' and in_comment:
            in_comment = False
            current_block += '*/'
            i += 2
            continue

        char = css[i]
        current_block += char

        if not in_comment:
            if char == '{':
                brace_level += 1
            elif char == '}':
                brace_level -= 1
                if brace_level == 0:
                    blocks.append(current_block.strip())
                    current_block = ""
        i += 1
    return blocks

file_blocks = [extract_blocks_raw(css) for css in all_blocks]

from collections import defaultdict

selector_to_contents = defaultdict(set)
content_to_files = defaultdict(list)

def get_selector(block_str):
    return block_str.split('{', 1)[0].strip()

for f_idx, blocks in enumerate(file_blocks):
    for b in blocks:
        sel = get_selector(b)
        selector_to_contents[sel].add(b)
        content_to_files[b].append(f_idx)

common_css = []
specific_css = [[] for _ in range(len(files))]

for sel, contents in selector_to_contents.items():
    if len(contents) == 1:
        common_css.append(list(contents)[0])
    else:
        for b in contents:
            for f_idx in content_to_files[b]:
                specific_css[f_idx].append(b)

common_css_ordered = []
for b in file_blocks[0]:
    if b in common_css:
        common_css_ordered.append(b)
        common_css.remove(b)

common_css_ordered.extend(common_css)

with open('style.css', 'w') as f:
    f.write('\n\n'.join(common_css_ordered) + '\n')

for i, file in enumerate(files):
    with open(file, 'r') as f:
        html = f.read()

    if specific_css[i]:
        style_content = '\n\n        '.join(specific_css[i])
        style_content = style_content.replace('\n', '\n        ')
        replacement = f'<link rel="stylesheet" href="style.css">\n    <style>\n        {style_content}\n    </style>'
    else:
        replacement = f'<link rel="stylesheet" href="style.css">'

    new_html = re.sub(r'<style>\s*(.*?)\s*</style>', replacement, html, flags=re.DOTALL)

    with open(file, 'w') as f:
        f.write(new_html)

print("Extraction completed cleanly.")
