# 714. 二十一点 OO Design
# 中文English

# 每位玩家起始有1000筹码
# 庄家有10000筹码
# 如果玩家获胜，双倍获得押注的筹码
# 庄家获胜，玩家押注的筹码归庄家
# 点数相同，庄家获胜
# A 可当做 1 或 11

# 样例
# Player(10)
# Player(100)
# Player(500)
# Card([1,4,2,3,1,4,2,3,9,10])
# InitialCards()
# compareResult()
# 输出:
#
# playerid: 1 ;Cards: 1 , 1; Current best value is: 12, current bets: 10, total bets: 990
# playerid: 2 ;Cards: 4 , 4; Current best value is: 8, current bets: 100, total bets: 900
# playerid: 3 ;Cards: 2 , 2; Current best value is: 4, current bets: 500, total bets: 500
# Dealer Cards: 3 , 3; Current best value is: 6, total bets: 10000
# playerid: 1 ;Cards: 1 , 1; Current best value is: 12, current bets: 0, total bets: 1010
# playerid: 2 ;Cards: 4 , 4; Current best value is: 8, current bets: 0, total bets: 1100
# playerid: 3 ;Cards: 2 , 2; Current best value is: 4, current bets: 0, total bets: 500
# Dealer Cards: 3 , 3; Current best value is: 6, total bets: 10390