# Blog 

## Content

内容发布到blog.coderwu.com，托管在gitbook。

- **.github**
   - github action和自动生成目录、分类的脚本。
- **docs**
   - 以markdown格式书写文档。
   - **resources**
      - 存放图片等静态资源。
- **about.md**
   - 关于章节，添加联系方式等。
- **W.B.2023**
   - 2023年之前写的文档。
- **tags**
   - 通过脚本生成分类索引
- **SUMMARY.md**
   - 通过脚本动态生成的gitbook目录。



## Markdown格式

markdown文件应包含以下properties注释配置文档属性：

```
<!-- properties
tag: 标签1
tag: 标签2
created: 2023/01/01 00:00:00
-->
```

## 功能点

- [x] 脚本根据tag生成索引目录
- [x] 根据创建时间生成索引，索引按照年、月划分