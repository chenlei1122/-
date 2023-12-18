# -
ffmpeg 批量视频旋转 

解决 alive_bar 转 exe 后无法运行的问题
一、在你的开发主机上搜索grapheme_break_property.json文件所在的路径，复制到my.py同目录。
二、使用pyinstaller打包的时候添加参数--add-data ".\grapheme_break_property.json;grapheme\data"，问题解决
以下是全部命令的示例
pyinstaller -F --add-data ".\grapheme_break_property.json;grapheme\data"  xuanzhuan.py -n xuanzhuan.exe
