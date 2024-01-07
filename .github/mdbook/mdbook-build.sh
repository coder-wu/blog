#!/bin/bash

current_dir=$(dirname "$0")
readonly current_dir

project_dir=$(cd "${current_dir}/../../" && pwd)
readonly project_dir

mdbook_dir="${project_dir}/mdbook"
readonly mdbook_dir

# Copy files to mdbook directory.
if [ -d "${mdbook_dir}" ]; then
  rm -rf "${mdbook_dir}"
fi
mkdir "${mdbook_dir}"

cp -rf "${project_dir}/docs" "${mdbook_dir}/"
cp -rf "${project_dir}/tags" "${mdbook_dir}/"

cp "${project_dir}/SUMMARY.md" "${mdbook_dir}/"
cp "${project_dir}/ABOUT.md" "${mdbook_dir}/"
cp "${current_dir}/book.toml" "${mdbook_dir}/"

for file in "${mdbook_dir}/docs/"*.md; do
  echo "<!-- toc -->" > temp.md
  cat "${file}" >> temp.md
  mv temp.md "${file}"
done

mdbook-mermaid install "${mdbook_dir}"

cd "${mdbook_dir}" || exit 1
mdbook build