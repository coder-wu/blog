#!/usr/bin/env python3
import os
from datetime import datetime

# Get the current and project directories
current_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(current_dir, "../../"))
doc_dir = os.path.join(project_dir, "docs")
tag_dir = os.path.join(project_dir, "tags")
summary_file = os.path.join(project_dir, "README.md")
docs= {}

# Read all markdown files and sort order by create time
def load_markdown_files():
    global docs

    for filename in os.listdir(doc_dir):
        if not filename.endswith(".md"):
            continue

        doc = {}
        doc['tags'] = set()

        file_path = os.path.join(doc_dir, filename)
        with open(file_path, "r") as file:
            title = file.readline().lstrip("#").strip()
            doc['title'] = title

            created = None
            for line in file:
                if line.startswith("created:"):
                    created = line.split("created:")[1].strip()
                if line.startswith("language:"):
                    language = line.split("language:")[1].strip()
                    doc['language'] = language
                if line.startswith("tag:"):
                    tag = line.split(":")[1].strip()
                    doc['tags'].add(tag)
                if line.startswith("-->"):
                    break

            if created:
                try:
                    timestamp = int(datetime.strptime(created,"%Y-%m-%d %H:%M:%S").timestamp())
                except ValueError:
                    timestamp = int(datetime.strptime(created,"%Y/%m/%d %H:%M:%S").timestamp())
                doc['timestamp'] = timestamp
                docs[filename] = doc

    docs = sorted(docs.items(), key=lambda x: x[1]['timestamp'], reverse=True)