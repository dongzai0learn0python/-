# ID=input("请输入用户名：")
# print(ID)
# MM=input("请输入密码：")
# print(MM)
# print("1234\"12121\"5677")
# admin = "sb"
# print(admin[0]+admin[1])
# ID = input("请输入用户名：")
# MM = input("请输入密码：")
#
# # print(ID, int(ID) + int(MM))
# SJ = int(ID) + int(MM)
# print("您的用户名为{}\n您的随机密码为{}".format(ID, SJ))
# print (not 1)

# XG = input("你回家路上是否有西瓜摊：（请输入 是 或 否 ）")
# if XG == a:
#     print("你买到了两个西瓜回家并挨了揍")
# else:
#     XG = input("任意键重新开始")
# XG = ''
# while XG != a:
#     XG = input("你回家路上是否有西瓜摊：（请输入 是 或 否 ）")
#     if XG == a:
#         print("你买到了两个西瓜回家并挨了揍")
#     else:
#         print("任意键重新开始")
# XZ = input("虽然没有找到西瓜摊，但是想到女朋友想要你买水果回去，你决定买点：（苹果 或 车厘子）")
# if XZ == c:
#     print("你暗暗下定决心，选择去买一个{},结果因为过于直男只买了一个，回家挨了骂，还被赶出了门")
# a = "是"
# b = "否"
# c = '苹果'
# d = '车厘子'
# XG = input("你回家路上是否有西瓜摊：（请输入 是 或 否 ）")
# while XG == a:
#     if XG == a:
#         print("你买到了两个西瓜回家并挨了揍\n你失败了，重新开始")
#         XG = input("你回家路上是否有西瓜摊：（请输入 是 或 否 ）")
#     else:
#         break
# JG = input("虽然没有找到西瓜摊，但是想到女朋友想要你买水果回去，你决定买点：（苹果 或 车厘子）")
# #
# if JG == c:
#     print("你暗暗下定决心，选择去买一个{},结果因为过于直男只买了一个，回家挨了骂，还被赶出了门".format(c))
#     while JG == c:
#         JG = input("虽然没有找到西瓜摊，但是想到女朋友想要你买水果回去，你决定买点：（苹果 或 车厘子）")
#         if JG == d:
#             print("你暗暗下定决心，选择去买一袋{},老婆很高兴，当场给你了100块零花钱，但是买车厘子用了95块，苦逼男人\n不过今天也是成功的活了下去，你成功了".format(d))
#         elif JG == c:
#             print("你暗暗下定决心，选择去买一个{},结果因为过于直男只买了一个，回家挨了骂，还被赶出了门".format(c))
#         else:
#             print("啥都不买？？？你没了!!!")
# elif JG == d:
#     print("你暗暗下定决心，选择去买一袋{},老婆很高兴，当场给你了100块零花钱，但是买车厘子用了95块，苦逼男人\n不过今天也是成功的活了下去，你成功了".format(d))
#
# else:
#     print("啥都不买？？？你没了!!!")
a = 0
while a < 100:
    a = a + 1
    if a % 7 == 0:
        continue
    elif a % 10 == 7 or a // 10 == 7 :
    # if a // 10 == 7:
        continue
    print(a)

# while a % 7 == 0:
