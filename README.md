# 使用方法

## 1. 申请Google API Key

参考链接 [youtube api overview](https://developers.google.com/youtube/v3/getting-started)

## 2. 环境配置单

建议使用python 3.7以上，需要安装mongoDB, 谷歌搜mongodb安装跟着教程走就可以了，装完了之后装个mongoDB compass用来可视化检阅数据。mongoDB作为非关系型数据库很适合用来存放json数据，如果你很抗拒数据库也可以存excel，可以参考pandas官方文档怎么把json转成dataframe再存excel，但我不建议你这样做，第一这样很麻烦，而且数据量大了之后不好合表和拆表，第二这样也很不酷。

需要安装的库有requests，pandas，matplotlib，wordcloud，如果报错提示你需要其他的库，按照提示的要求安装就行了。

## 3. 配置代码

首先需要把代码中的{yourapikey}更换成你在第一步申请的api key，然后再videos列表里填上你需要的videoID

![](/assets/videoID.png)

v=后面的那一串就是videoID，这个脚本支持多个视频批量抓取评论，多个videoID之间用逗号隔开即可。

除此之外，由于一些众所周知的原因，你还需要配置代理，通常来说你的代理应该都是走的socks5，所以只需要在proxy里填上你对应的socks代理端口即可

以上全部配置完成之后直接运行即可把所有数据打入数据库了，之后你可以通过mongodb compass 查看，也可以通过 dataAnalyse.py 导出excel和词频统计
