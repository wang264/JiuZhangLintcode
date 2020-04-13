# 710. 设计宾馆 OO Design
# 中文English
# 1.Hotel目前有两种房间类型：SINGLE和DOUBLE
# 2.能够支持搜索，输入日期，返回能住的房间
# 3.能够支持预定
# 4.能够取消预定
# 5.使用LRUCache来储存搜索结果, 每次搜索时使用Cache
# 6.Hotel, Room 需要大家实现, 在函数searchRequest和reservationRequest(makeReservation)之后我们会调用printCache来验证程序的正确性。
#
# 样例
# 输入
#
# Hotel(4)
# Room(1, "Single")
# Room(2, "Single")
# Room(3, "Double")
# Room(4, "Double")
# searchRequest("2013-01-01", "2013-10-10")
# roomsNeeded("Single", 1)
# roomsNeeded("Single", 1, "Double", 2)
# roomsNeeded("Single", 1)
# reservationRequest("2013-01-06", "2013-10-10", 2)
# 输出
#
# Printing Cache ...
# Search Request -> Start date is: Jan 1, 2013 12:00:00 AM, End date is: Oct 10, 2013 12:00:00 AM
# Value -> For room type: DOUBLE, available rooms are: 3; 4; . For room type: SINGLE, available rooms are: 1; 2; .
#
# *****************************
#
# Printing Cache ...
# Search Request -> Start date is: Jan 1, 2013 12:00:00 AM, End date is: Oct 10, 2013 12:00:00 AM
# Value -> For room type: DOUBLE, available rooms are: 3; 4; . For room type: SINGLE, available rooms are: 1; 2; .
#
# Search Request -> Start date is: Jan 6, 2013 12:00:00 AM, End date is: Oct 10, 2013 12:00:00 AM
# Value -> For room type: DOUBLE, available rooms are: . For room type: SINGLE, available rooms are: 1; 2; .
#
# *****************************


# NO Python Solution
