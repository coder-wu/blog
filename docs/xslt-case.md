# 接口适配

[EN](#interface-adaptation)

<!-- properties
tag: 软件工程
tag: 案例
created:  2023-12-02 22:08:58
-->

## 背景

某个WebService接口在实现框架替换后，WSDL和请求响应报文中XML的格式与原实现存在差异，比如namespace别名定义，字段顺序，层级（是否应该带有in0之类的层级）等。因为接口被广泛使用，所以需要保证新的接口和原接口一摸一样。

## 解决方案

1. 通过拦截器或能实现类似效果的截面层对请求和响应报文做适配，对于每个接口定义一个单独的实现类。

2. 引入XSLT，定义两个拦截器引用两个XSLT文件分别处理请求和响应报文，具体格式转换在XSLT中定义实现。

## 总结

最终采用引入XSLT的方案实现，这种修改对系统侵入性小且灵活。

> Finally, XSLT is chosen, because it has minimal intrusion to the system and is more flexible.

在业务系统中保证功能实现的前提下也要考虑可扩展性，可维护性。通过XSLT实现，当新增、修改接口时仅需要修改XSLT中代码。而且XSLT是纯文本，不涉及编译重新部署的麻烦，扩展和维护都很方便。


---

# Interface Adaptation

## Background

After replacing the implementation framework for a WebService interface, request-response messages is different with the original implementation, such as namespace alias definitions, field order, hierarchy (whether it should have levels like in0), etc. Because the interface is widely used, it is necessary to ensure that the new interface is exactly the same as the original one.

## Solution

1. Reassemble message through interceptors or aspects, one implementation class for on interface.

2. Use XSLT, define two interceptors that references to two XSLT files to process request and response requests, and implement specific format conversions in XSLT.

## Conclusion

Finally, XSLT is chosen, because it has minimal intrusion to the system and is more flexible.

While implementing functions in business system, extension and maintenance are also should be considered. With XSLT, after adding or modifying interfaces, only XSLT code should be changed. Because XSLT code is plain text and doesn't require compilation, it's convenient to modify and deploy.

