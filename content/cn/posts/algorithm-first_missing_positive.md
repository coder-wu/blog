---
title: 丢失的第一个正整数
date: 2017-05-30
categories: ['算法']
draft: false
---

题目来自LintCode
给出一个无序的正数数组，找出其中没有出现的最小正整数。

样例

如果给出 `[1,2,0]`, return `3`
如果给出 `[3,4,-1,1]`, return `2`

挑战
只允许时间复杂度O(n)的算法，并且只能使用常数级别的空间。

解法：
1.如果A为整数1,2,3…N的随机排列，最小正整数就是N+1。
2.如果A中有<1或者>N的数出现，最小正整数为1到N中的某个数。

```java
int firstMissingPositive(int[] A) {
        //l为左边界，初始值0，表示1到l已经出现过
        //r为右边界，初始值A的长度，当数字大小超过r，则被丢弃
        int l = 0;
        int r = A.length; 
        while(l < r) {
            if(A[l] == l + 1) {
                l++;
            } else if(A[l]> r || A[l] <= l || A[A[l] - 1] == A[l]) {
                A[l] = A[--r];
            } else {
                int temp = A[l];
                A[l] = A[A[l] - 1];
                A[temp - 1] = temp;
            }
        }
        return l + 1;
}
```

时间复杂度O(n)，改变了原数组。 