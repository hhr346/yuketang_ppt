# README

## 准备工作

下载和自己的Chrome浏览器对应的chromedriver并放置在根目录。

参考[Downloads  | ChromeDriver  | Chrome for Developers](https://developer.chrome.com/docs/chromedriver/downloads) 

## 爬取图片

运行`py crawl_ppt.py` 将会打开chrome，需要手动扫码登录雨课堂，并点击相应课程的ppt，显示出ppt的预览格式的时候在命令行里单击回车进行下一步。

程序会自动爬取当前页面下的所有图片，并将其保存至fig文件夹里。

爬取完当前界面的图片后，会询问你是否继续。若需要继续，则同样转到下一个课程的ppt详情页，再次点击回车继续处理。程序会自动为课程进行编号。

> 注意：如果多次运行文件，而fig里保存了之前爬取的内容，需要手动修改初始号码变量`ppt_no`，防止图片被覆盖。

## 整合PPT

在整理完图片后，运行`py ppt_create.py`文件，将图片整合为同一个纯图ppt文件。不同的ppt序号对应不同的ppt文件。

