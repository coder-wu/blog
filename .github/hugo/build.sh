#!/bin/bash

current_dir=$(dirname "$0")
current_dir=$(cd "${current_dir}" && pwd)
readonly current_dir

readonly build_dir="${current_dir}/build"

if [ -d "${build_dir}" ]; then
  rm -rf "${build_dir}"
fi
mkdir "${build_dir}"

cd "${build_dir}" || exit 1
hugo new site blog --format yaml

cd blog || exit 1
git clone https://github.com/adityatelange/hugo-PaperMod themes/PaperMod --depth=1

cp "${current_dir}/custom/hugo.yaml" ./
cp "${current_dir}/custom/favicon.ico" "${build_dir}/blog/static/"
cp "${current_dir}/custom/extend_head.html" "${build_dir}/blog/themes/PaperMod/layouts/partials/extend_head.html"

cd "${current_dir}" || exit 1
./generate-content.py

cd "${build_dir}/blog" || exit 1
hugo --minify