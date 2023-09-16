---
title: 闲来无事写个知乎爬虫
date: 2017-04-25
categories: ['PHP']
draft: false
---

知乎刷多了，就想做点好玩的......
可以爬知乎某个问题下的所有回答中所包含的图片。
错误没有完全处理，容错性可能不太好。
代码：

```php
<?php

/**
 * Created by PhpStorm.
 * User: Jehu
 * Date: 2017/4/25
 * Time: 18:06
 */

class Zhihu {

    private $hasDone = 0;

    private $question;

    function __construct(string $question) {
        $this->question = $question;
        if (!file_exists("image/" . $this->question)) {
            mkdir ("image/" . $this->question);
        }
    }

    public function getHasDone(): int{
        return $this->hasDone;
    }

    public function setHasDone(int $hasDone){
        $this->hasDone = $hasDone;
    }

    public function saveImg(array $content) {
        if (isset($content['data'])) {
            foreach ($content['data'] as $key => $value) {
                preg_match_all("/<img.*?>/", $value['content'], $result);
                if (count($result[0]) > 0) {
                    foreach ($result[0] as $k => $v) {
                        preg_match("/src=\".*?\"/", $v, $result);
                        $result = str_replace('src=', "", $result[0]);
                        $imgUrl = str_replace('"', "", $result);
                        if ($imgUrl != "//zhstatic.zhihu.com/assets/zhihu/ztext/whitedot.jpg") {
                            preg_match('((?<=(com/))[\w\W]*)', $imgUrl, $imgName);
                            $imgName = $imgName[0];
                            $filePath = "image/" . $this->question . "/" . $imgName;
                            if (!file_exists($filePath)) {
                                file_put_contents($filePath, file_get_contents($imgUrl));
                            }
                        }
                    }
                }
            }

        }
    }

    public function doIt(string $url) : string {
        $cookie = "";//设置成自己账号登陆知乎的Cookie
        $ch = curl_init();
        curl_setopt_array($ch, array(
            CURLOPT_URL => $url,
            CURLOPT_HTTPHEADER => [
                "accept:application/json, text/plain, */*",
                "Accept-Encoding:gzip, deflate, sdch, br",
                "Accept-Language:zh-CN,zh;q=0.8",
                "authorization:Bearer         Mi4wQUJBS0xDVVdXd2dBUU1KMmw3eVZDeGNBQUFCaEFsVk5CN2tTV1FDNVFOV196cTVVUmVGWTFEVy1nbGk3Q2hVakx3|1493118236|3fa676b476d335125e9b4990da0f0137dc2d99ba",
                "Connection:keep-alive",
                "User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
                "x-udid:AEDCdpe8lQuPTqqIYSLrMvJpCdXgRVxt_Pw=",
            ],
            CURLOPT_COOKIE => $cookie,
            CURLOPT_FOLLOWLOCATION => 1,
            CURLOPT_RETURNTRANSFER => 1,
            CURLOPT_HEADER => 0,
            CURLOPT_SSL_VERIFYPEER => false,
            CURLOPT_SSL_VERIFYHOST => false,
            CURLOPT_ENCODING => "gzip"
        ));
        $content = curl_exec($ch);
        curl_close($ch);
        return $content;
    }
}

$question = 56999743;//问题ID
$total = 1;//初始总回答数
if (isset($question) && !empty($question)) {
    $zhihu = new Zhihu($question);
    while ($zhihu->getHasDone() < $total) {
        $url = "https://www.zhihu.com/api/v4/questions/" . $question . "/answers?include=data%5B*%5D.is_normal%2C" .
            "is_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2C" .
            "voteup_count%2Creshipment_settings%2Ccomment_permission%2Cmark_infos%2Ccreated_time%2Cupdated_time%2C" .
            "relationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2C" .
            "upvoted_followees%3Bdata%5B*%5D.author.badge%5B%3F(type%3Dbest_answerer)%5D.topics&" .
            "offset=" . $zhihu->getHasDone() . "&limit=20&sort_by=default";
        $content = $zhihu->doIt($url);
        $content = json_decode($content, true);
        $total = $content['paging']['totals'];
        if (isset($content['data'])) {
            $zhihu->saveImg($content);
        }
        $zhihu->setHasDone($zhihu->getHasDone() + 20);
        var_dump($zhihu->getHasDone() . "/" . $content['paging']['totals']);
    }
}
```