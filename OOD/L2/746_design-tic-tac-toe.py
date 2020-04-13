# 746. 设计井字棋
# 中文English
# 设计井字棋游戏。
#
# 棋盘的尺寸为3
# X 总是先行动走出第一步
# 如果一个位置已经被占，且一名玩家打算占领该位置，一个AlreadyTakenException信息将被抛出
# 如果一名玩家胜利，且有玩家打算继续行动，一个GameEndException信息将被抛出
# 如果所有的地方都已被占领，你需要输出"it's a draw"
# 样例
# 例 1:
#
# 输入:
# move(0, 0) // X 的回合
# move(1, 0) // O 的回合
# move(1, 1) // X 的回合
# move(2, 0) // O 的回合
# move(2, 2) // X 的回合并获得胜利
# move(0, 0)  //抛出 GameEndException
# move(0, 0) // X 的回合
# move(0, 0) // 抛出 AlreadyTakenException
# move(1, 0) // O 的回合
# move(1, 1) // X 的回合
# move(2, 0) // o 的回合
# move(2, 2) // X 的回合并获得胜利
# 输出:
# x player wins!
# x player wins!