# 712. 自动售货机 OO Design
# 中文English
# 1.Vending Machine一共有三种状态：NoSelection, HasSelection, InsertedMoney
# 2.Vending Machine一共卖三种饮料：Coke, Sprite和MountainDew
# 3.要求Vending Machine在正确的状态要有正确的输出
# 样例
# 输入：
#
# select("Coke")
# select("Sprite")
# insert(500)
# execTrans()
# 输出:
#
# Current selection is: Coke, current inserted money: 0, current state is : HasSelection
# Current selection is: Sprite, current inserted money: 0, current state is : HasSelection
# Current selection is: Sprite, current inserted money: 500, current state is : InsertedMoney
# Current selection is: null, current inserted money: 0, current state is : NoSelection