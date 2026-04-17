import sys

with open(r'd:\New folder\index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_css = """        /* Per Card Styles (Images) */
        .dc-1 { background-image: url('./1.jpg'); }
        .dc-2 { background-image: url('./2.jpg'); }
        .dc-3 { background-image: url('./3.jpg'); }
        .dc-4 { background-image: url('./4.jpg'); }
        .dc-5 { background-image: url('./5.jpg'); }
        .dc-6 { background-image: url('./6.jpg'); }

        .no-image.dc-1 { background-image: linear-gradient(145deg, #1a3329 0%, #0d1f18 40%, #2d5244 100%) !important; }
        .no-image.dc-2 { background-image: linear-gradient(145deg, #0f1a16 0%, #1e3d30 50%, #3E5E51 100%) !important; }
        .no-image.dc-3 { background-image: linear-gradient(145deg, #080f0c 0%, #1a3329 60%, #DCD0C4 100%) !important; }
        .no-image.dc-4 { background-image: linear-gradient(145deg, #1C2B25 0%, #3E5E51 70%, #B8D4C0 100%) !important; }
        .no-image.dc-5 { background-image: linear-gradient(145deg, #0a0f0c 0%, #162019 40%, #4A7A68 100%) !important; }
        .no-image.dc-6 { background-image: linear-gradient(145deg, #0d1a15 0%, #1a3329 50%, #3E5E51 100%) !important; }

        /* Deck Card Layout */
"""

start_idx = -1
end_idx = -1
for i, line in enumerate(lines):
    if "/* Per Card Styles */" in line:
        start_idx = i
    if "/* Deck Card Layout */" in line and start_idx != -1:
        end_idx = i
        break

if start_idx != -1 and end_idx != -1:
    with open(r'd:\New folder\index.html', 'w', encoding='utf-8') as f:
        f.writelines(lines[:start_idx])
        f.write(new_css)
        f.writelines(lines[end_idx+1:])
    print("CSS replaced.")
else:
    print("Could not find CSS blocks.")
