#!/usr/bin/env python3
import sys
sys.path.append('../script') 

import os
import shutil
import hashlib
import re
import common
from datetime import datetime

hugo_blog_dir = os.path.abspath(os.path.join(common.project_dir, ".github/hugo/build/blog"))

def generate_content():
    hugo_content_path = os.path.join(hugo_blog_dir, "content")
    shutil.copy(common.project_dir + "/ABOUT.md", hugo_content_path)
    shutil.copytree(common.doc_dir + "/resources", hugo_content_path + "/resources")

    for filename, properties in common.docs:
        language = properties['language'] if 'language' in properties else "zh"
        hugo_language_path = os.path.join(hugo_content_path, language)
        if not os.path.exists(hugo_language_path):
            os.makedirs(hugo_language_path)

        created_time = datetime.fromtimestamp(properties['timestamp'])
        formatted_time = created_time.strftime("%Y-%m-%d %H:%M:%S")

        doc_path = os.path.join(common.doc_dir, filename)
        with open(doc_path, 'r') as doc_file:
            doc_file.readline()
            doc_content = doc_file.read()
            # 替换resources的路径
            doc_content = re.sub("resources/", "/resources/", doc_content)

        hugo_doc_path = os.path.join(hugo_language_path, filename)
        with open(hugo_doc_path, "w") as hugo_doc_file:
            hugo_doc_file.write("---\n")
            hugo_doc_file.write("title: " + properties['title'] + "\n")
            hugo_doc_file.write("date: \"" + formatted_time + "\"\n")
            hugo_doc_file.write("tags: " + str(list(properties['tags'])) + "\n")
            hugo_doc_file.write("---\n")
            hugo_doc_file.write(doc_content)

if __name__ == "__main__":
    common.load_markdown_files()
    generate_content()
