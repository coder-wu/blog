---
title: 模拟微信发送消息的一个Demo
date: 2016-12-24
categories: ['PHP']
draft: false
---

模拟在微信客户端发送信息到后台的过程用来微信测试，只有部分信息类型，其他的可以根据需求模仿例子添加，Demo可以直接粘贴使用

示例代码：

```php
<?php
/**
 * Created by PhpStorm.
 * User: Jehu
 * Date: 2016/12/24
 * Time: 11:47
 */
class WeChatPost{
    private $event = "";
    private $content = "";
    private $time;

    /**
     * WeChatPost constructor.
     * @param $event String 事件类型
     * @param $url String 链接
     * @param $content array("标签名" => "内容")
     * 发送的内容
     * 例发送地理位置
     * array("Location_X" => 1.29290, "Location_Y" => 1.29290, "Scale" => 20, "Label" => "位置信息")
     * 发送文字
     * array("Content" => "text")
     */
    public function __construct($event, $url, $content){
        $this->event = $event;
        $this->url = $url;
        $this->content = $content;
        $this->time = time();
    }
    
    /**
     * 把要发送的内容处理为微信可识别的xml数据
     * @return string 处理完的xml数据
     */
    private  function xml(){
        $xml = "<xml>
                    <ToUserName>100012</ToUserName>
                    <FromUserName>100012</FromUserName>
                    <CreateTime>{$this->time}</CreateTime>
                    <MsgType>{$this->event}</MsgType>
                    {$this->content()}
                    <MsgId>1234567890123456</MsgId>
            </xml>";
        return $xml;
    }

    /**
     * 根据信息类型处理剩余的信息
     * @return null|string
     */
    private function content() {
        switch ($this->event) {
            case "text" :
                return "<Content>{$this->content["Content"]}</Content>";
            case "image" :
                return "<PicUrl>{$this->content["PicUrl"]}</PicUrl>";
            case "link" :
                return "<Title>{$this->content["Title"]}</Title>
                        <Description>{$this->content["Description"]}</Description>
                        <Url>{$this->content["Url"]}</Url>";
            case "location" :
                return "<Location_X>{$this->content["Location_X"]}</Location_X>
                        <Location_Y>{$this->content["Location_Y"]}</Location_Y>
                        <Scale>{$this->content["Scale"]}</Scale>
                        <Label>{$this->content["Label"]}</Label>";
            case "event" :
                return "<Event>{$this->content["Event"]}</Event>";
            default :
                return null;
        }
    }

    /**
     * 模拟post过程
     * @return mixed
     */
    private function post(){
        $ch = curl_init();
        curl_setopt_array($ch, array(
            CURLOPT_URL => $this->url,
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_HTTPHEADER => [
                "Content-type: text/xml"
            ],
            CURLOPT_POST => true,
            CURLOPT_POSTFIELDS => $this->xml()
        ));
        $result = curl_exec($ch);
        if (curl_errno($ch)) {
            print curl_error($ch);
        }
        curl_close($ch);
        return $result;
    }

    /**
     * 接收返回的信息，并处理为字符串
     * @return string
     */
    public function response(){
        $response = '';
        $postObj = simplexml_load_string($this->post(), 'SimpleXMLElement', LIBXML_NOCDATA);
        foreach ((array)$postObj as $key => $value) {
            $response .= $key . '=>' . $value . "<br>";
        }
        return $response;
    }
}
$postData = array(
    "Content" => "Hello World"
);
$weChat = new WeChatPost("text", "http://www.wechatexample.com", $postData);
echo $weChat->response();
```
