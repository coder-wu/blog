# Blog 

## 内容-Content

[目录-MENU](SUMMARY.md)

## Markdown格式

markdown文件应包含以下properties注释配置文档属性，以便Actions脚本可以自动更新目录和分类。

> markdown files should contains the following comment, so that SUMMARY.md and tag files can be updated automatically.

```
<!-- properties
tag: 标签1
tag: 标签2
created: 2023/01/01 00:00:00
-->
```

## Action flow

```mermaid
graph LR

menu(Update Summary and Tags)
mdbook(Generate static files and publish to Github Pages)

menu ---> mdbook

```