# 731. 设计餐馆 II OO Design
# 中文English
# 题目：设计餐馆 II
#
# 不能订外卖
# 能预订座位
# MAX_DINETIME 为 2， 意为占用一桌吃饭的最大时长为2小时
# 如果餐桌被预定，则无法入座
# 餐馆的桌子有不同大小
# 餐馆会优先选择适合当前Party最小的空桌
# 相对设计餐馆 I，Table新增functions 需要实现。相关函数之后会调用restaurantDescription, 来验证你的程序是否正确。
#
# 样例
# meal(10.0)
# meal(13.0)
# meal(15.0)
# table(1, 4)
# table(2, 10)
# party(3)
# reservedDate(6) // Date(2013年1月4日 + 6 * Restaurant.HOUR);
# party(7)
# reservedDate(7) // Date(2013年1月4日 + 7 * Restaurant.HOUR);
# order(1)
# order(2, 3)
# findTableForReservation(1, 1) // 第一个的参数是party的id，第二个参数是reservedDate的id
# findTableForReservation(2, 2)
# Table: 1, table size: 4, isAvailable: true. No current order for this table. Current reservation dates for this table are: 4 Jan 2013 06:00:00 GMT ; .
# Table: 2, table size: 10, isAvailable: true. No current order for this table. Current reservation dates for this table are: .
# *****************************************
#
# Table: 1, table size: 4, isAvailable: true. No current order for this table. Current reservation dates for this table are: 4 Jan 2013 06:00:00 GMT ; .
# Table: 2, table size: 10, isAvailable: true. No current order for this table. Current reservation dates for this table are: 4 Jan 2013 07:00:00 GMT ; .
# *****************************************