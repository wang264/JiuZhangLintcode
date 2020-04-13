# 748. 设计kindle OO Design
# 中文English
# 设计一个可以打开三种文件格式的Kindle，文件格式分别为：PDF, MOBI , EPUB。
#
# 尝试使用 ENUM 处理文件格式。
# 尝试使用 simple factory 设计模式为每种格式创建用户。
# 样例
# 输入:
#
# readBook("EPUB")
# readBook("PDF")
# readBook("MOBI")
# 输出:
#
# Using EPUB reader, book content is: epub
# Using PDF reader, book content is: pdf
# Using MOBI reader, book content is: mobi