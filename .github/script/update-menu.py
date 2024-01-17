#!/usr/bin/env python3

import os
import shutil
import hashlib
from datetime import datetime

# Get the current and project directories
current_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(current_dir, "../../"))
doc_dir = os.path.join(project_dir, "docs")
tag_dir = os.path.join(project_dir, "tags")
summary_file = os.path.join(project_dir, "SUMMARY.md")

docs= {}

def get_md5(text):
    return hashlib.md5(text.encode()).hexdigest()

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

# Generate SUMMARY file
def create_summary():
    with open(summary_file, "w") as summary:
        summary.write("# Summary\n\n")

# Generate all blogs list
def generate_list():
    with open(summary_file, "a") as summary:
        summary.write("# 列表 - List\n\n")
        for filename, properties in docs:
            timestamp = properties['timestamp']
            formatted_time = datetime.utcfromtimestamp(timestamp).strftime("%Y-%m-%d")
            summary.write(f"  * [{properties['title']}](docs/{filename})\n")

# Generate categories
def generate_categories():
    with open(summary_file, "a") as summary:
        summary.write("# 分类 - Categories\n\n")

    shutil.rmtree(tag_dir)
    os.makedirs(tag_dir)

    tags = set()
    for filename, properties in docs:
        tags = sorted(properties['tags'])
        for tag in tags:
            tag_filename = f"{get_md5(tag)}.md"
            tag_filepath = os.path.join(tag_dir, tag_filename)

            if not os.path.exists(tag_filepath):
                with open(summary_file, "a") as summary:
                    summary.write(f"  * [{tag}](tags/{tag_filename})\n")

                with open(tag_filepath, "w") as tag_file:
                    tag_file.write(f"## {tag}\n\n")

            with open(tag_filepath, "a") as tag_file:
                tag_file.write(f"* [{properties['title']}](../docs/{filename})\n")


def generate_about():
    with open(summary_file, "a") as summary:
        summary.write("* [关于 - About](ABOUT.md)\n")

def separate():
    with open(summary_file, "a") as summary:
        summary.write("\n---\n\n")

if __name__ == "__main__":
    load_markdown_files()
    create_summary()

    generate_about()
    separate()
    generate_list()
    separate()
    generate_categories()
