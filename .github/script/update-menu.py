#!/usr/bin/env python3
import os
import shutil
import hashlib
import common
from datetime import datetime


def get_md5(text):
    return hashlib.md5(text.encode()).hexdigest()

# Generate SUMMARY file
def create_summary():
    with open(common.summary_file, "w") as summary:
        summary.write("# Summary\n\n")

# Generate all blogs list
def generate_list():
    with open(common.summary_file, "a") as summary:
        summary.write("# 列表 - List\n\n")
        for filename, properties in common.docs:
            timestamp = properties['timestamp']
            formatted_time = datetime.utcfromtimestamp(timestamp).strftime("%Y-%m-%d")
            summary.write(f"  * [{properties['title']}](docs/{filename})\n")

def generate_about():
    with open(common.summary_file, "a") as summary:
        summary.write("* [关于 - About](ABOUT.md)\n")

def separate():
    with open(common.summary_file, "a") as summary:
        summary.write("\n---\n\n")

if __name__ == "__main__":
    common.load_markdown_files()
    create_summary()

    generate_list()
    separate()
    generate_about()
