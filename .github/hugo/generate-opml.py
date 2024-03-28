#!/usr/bin/env python3
import sys
sys.path.append('../script') 

import common
import os
import xml.etree.ElementTree as ET

opml_md_file_path = os.path.join(common.project_dir + "/OPML.md")
output_opml_file_path = os.path.join(common.project_dir, 
                                     ".github/hugo/build/blog/content/resources/subscriptions.opml")

opml = ET.Element("opml", version="1.0")

head = ET.SubElement(opml, "head")
title = ET.SubElement(head, "title")
title.text = "Wu's subscriptions"

body = ET.SubElement(opml, "body")

with open(opml_md_file_path, "r") as file:
    for line in file:
        parts = line.split("- ")
        blank, title, type, url = parts
        outline = ET.SubElement(body, "outline", text=title.strip(),
                                title=title.strip(), type=type.strip(),
                                xmlUrl=url.strip())

tree = ET.ElementTree(opml)
with open(output_opml_file_path, "wb") as file:
    tree.write(file, encoding="utf-8", xml_declaration=True)
