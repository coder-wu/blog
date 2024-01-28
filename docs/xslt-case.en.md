# Interface Adaptation

<!-- properties
language: en
tag: 软件工程
tag: 案例
created:  2023-12-02 22:08:58
-->

## Background

After replacing the implementation framework for a WebService interface, request-response messages is different with the original implementation, such as namespace alias definitions, field order, hierarchy (whether it should have levels like in0), etc. Because the interface is widely used, it is necessary to ensure that the new interface is exactly the same as the original one.

## Solution

1. Reassemble message through interceptors or aspects, one implementation class for on interface.

2. Use XSLT, define two interceptors that references to two XSLT files to process request and response requests, and implement specific format conversions in XSLT.

## Conclusion

Finally, XSLT is chosen, because it has minimal intrusion to the system and is more flexible.

While implementing functions in business system, extension and maintenance are also should be considered. With XSLT, after adding or modifying interfaces, only XSLT code should be changed. Because XSLT code is plain text and doesn't require compilation, it's convenient to modify and deploy.

