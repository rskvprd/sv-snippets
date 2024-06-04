"""Read all snippets files and concatenate to one systemverilog.json file"""

import os
result_file = "systemverilog.json"

snippets_string = []

# Read all .json files
for file in os.listdir():
    if file[-5:] == '.json' and file != result_file:
        with open(file) as f:
            snippets_string.append(''.join(f.readlines())[1:-1])

# Write files content (separate file content by comma)
with open(result_file, 'w') as f:
    f.write('{' + ','.join(snippets_string) + '}\n')
