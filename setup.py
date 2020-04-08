import os

include_files = []

for root, dirs, files in os.walk('./assets'):
    for file in files:
        include_files.append(os.path.join(root, file))

print(include_files)