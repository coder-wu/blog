#!/usr/bin/env python3

import os
import hashlib
from datetime import datetime

# Get the current and project directories
current_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(current_dir, "../../"))
doc_dir = os.path.join(project_dir, "docs")
tag_dir = os.path.join(project_dir, "tags")
summary_file = os.path.join(project_dir, "SUMMARY.md")

sorted_docs = []

def get_md5(text):
    return hashlib.md5(text.encode()).hexdigest()

# Generate SUMMARY file
def create_summary():
    with open(summary_file, "w") as summary:
        summary.write("# Summary\n\n")

# Generate all blogs list
def generate_list():
    with open(os.path.join(doc_dir, "list.md"), "w") as list_file:
        list_file.write("## 列表 - List\n")

    docs = []

    for filename in os.listdir(doc_dir):
        if filename.endswith(".md"):
            file_path = os.path.join(doc_dir, filename)

            with open(file_path, "r") as file:
                created = None
                for line in file:
                    if line.startswith("created:"):
                        created = line.split("created:")[1].strip()
                        print(created)
                        break

                if created:
                    try:
                        timestamp = int(datetime.strptime(created,"%Y-%m-%d %H:%M:%S").timestamp())
                    except ValueError:
                        timestamp = int(datetime.strptime(created,"%Y/%m/%d %H:%M:%S").timestamp())
                    docs.append((file_path, timestamp))

    sorted_docs = sorted(docs, key=lambda x: x[1], reverse=True)

    with open(os.path.join(doc_dir, "list.md"), "a") as list_file:
        for file_path, _ in sorted_docs:
            with open(file_path, "r") as file:
                title = file.readline().lstrip("#").strip()
                filename = os.path.basename(file_path)
                list_file.write(f"* [{title} - {created}](./{filename})\n")

# Generate categories
def generate_categories():
    with open(summary_file, "a") as summary:
        summary.write("# 分类 - Categories\n")

    tags = set()

    for filename in os.listdir(doc_dir):
        if filename.endswith(".md"):
            file_path = os.path.join(doc_dir, filename)

            with open(file_path, "r") as file:
                for line in file:
                    if line.startswith("tag:"):
                        tag = line.split(":")[1].strip()
                        tags.add(tag)

    for tag in tags:
        tag_filename = os.path.join(tag_dir, f"{get_md5(tag)}.md")
        with open(tag_filename, "w") as tag_file:
            tag_file.write(f"## {tag}\n")

        with open(tag_filename, "a") as tag_file:
            for filename in os.listdir(doc_dir):
                if filename.endswith(".md"):
                    file_path = os.path.join(doc_dir, filename)

                    with open(file_path, "r") as file:
                        file_tags = [line.split(":")[1].strip() for line in file if line.startswith("tag:")]

                        if tag in file_tags:
                            title = file.readline().lstrip("#").strip()
                            tag_file.write(f"* [{title}](../docs/{filename})\n")

        with open(summary_file, "a") as summary:
            summary.write(f"  * [{tag}](tags/{get_md5(tag)}.md)\n")

def generate_about():
    with open(summary_file, "a") as summary:
        summary.write("* [关于 - About](ABOUT.md)\n")

def separate():
    with open(summary_file, "a") as summary:
        summary.write("\n---\n\n")

if __name__ == "__main__":
    create_summary()
    generate_list()
    separate()
    generate_categories()
    separate()
    generate_about()
