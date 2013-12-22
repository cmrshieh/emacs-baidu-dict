A English-Chinese dictionary for emacs .

python env:python3

# 配置

1. 修改dict.el中的第9行`~/path/bdict.py`为bdict.py文件的路径.
2. 将dict.el放到emacs可以引用的地方.比如说.emacs.d文件夹,或你使用`(add-to-list 'load-path "~/xxx")`指定的文件夹.
3. 添加`(require 'dict)` 到你的~/.emacs文档.

# 使用

选中一个英文单词,C-c d 即可
