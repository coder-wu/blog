#!/bin/bash

current_dir=$(dirname "$1")
project_dir=$(cd "$current_dir/../../" && pwd)

function get_md5() {
	echo $1 | openssl md5 -r | cut -d' ' -f1
}

doc_dir="$project_dir/docs/"
tag_dir="$project_dir/tags/"
menu_dir="$project_dir/"

summary_file="$menu_dir/SUMMARY.md"
echo "# Summary" >$summary_file

echo "" >>"$summary_file"
echo "* 最新" >>$summary_file
# 遍历所有 markdown 文件
docs=()
for file in $doc_dir/*.md; do
	if [ ! -f $file ]; then
		continue
	fi
	# 从 markdown 文件中提取创建时间
	created=$(grep -oE 'created:[[:space:]]*(.*)$' "$file" | sed -E 's/created:[[:space:]]*//')

	# 将创建时间转换为 Unix 时间戳
	timestamp=$(date -d "$created" +"%s")

	# 将文档名和创建时间保存到数组中
	docs+=("$file,$timestamp")
done

# 按照创建时间排序文档名
IFS=$'\n' sorted_docs=($(sort -t, -k2 -rn <<<"${docs[*]}"))

# 生成索引文件
for line in "${sorted_docs[@]}"; do
	# 从排序后的行中提取文档名和创建时间
	file=$(cut -d, -f1 <<<"$line")
	created=$(cut -d, -f2 <<<"$line")

	# 从 markdown 文件中提取一级标题
	title=$(sed -n 's/^# *//p' "$file" | head -n1)

	filename=$(basename "$file")
	# 将文档名和标题添加到索引文件中
	echo "  * [$title](docs/$filename)" >>$summary_file
done

# Get all unique tags
rm -rf "$tag_dir"
mkdir "$tag_dir"

tags=()
for file in $doc_dir/*.md; do
	while read -r line; do
		if [[ $line == "tag:"* ]]; then
			tag=$(echo $line | awk '{print $2}')
			if [[ ! " ${tags[@]} " =~ " ${tag} " ]]; then
				tags+=($tag)
			fi
		fi
	done <"$file"
done

for tag in "${tags[@]}"; do
	tag_filename="$tag_dir/$(get_md5 $tag).md"
	for file in $doc_dir/*.md; do
		file_tags=()
		while read -r line; do
			if [[ $line == "tag:"* ]]; then
				file_tag=$(echo $line | awk '{print $2}')
				file_tags+=($file_tag)
			fi
		done <"$file"
		if [[ " ${file_tags[@]} " =~ " ${tag} " ]]; then
			title=$(grep "^# " "$file" | head -n1 | sed 's/^# //')
			filename=$(basename "$file")
			echo "* [$title](../docs/$filename)" >>"$tag_filename"
		fi
	done
done

echo "" >>"$summary_file"
echo "* 分类" >>"$summary_file"
for tag in "${tags[@]}"; do
	echo "  * [$tag](tags/$(get_md5 $tag).md)" >>"$summary_file"
done

echo "" >>"$summary_file"
echo "* [关于](about.md)" >>"$summary_file"
