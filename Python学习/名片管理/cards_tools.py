cards_list = []


def menu():
    print("*" * 50)
    print("欢迎使用【名片管理系统】")
    print("1.新增名片")
    print("2.查看全部")
    print("3.查询名片")
    print("0.退出系统")
    print("*" * 50)


def add():
    print("-" * 50)
    name = input("请输入要添加的姓名： ")
    phone = input("请输入要添加的电话： ")
    qq = input("请输入要添加的qq号： ")
    cards_list.append({"name": name,
                       "phone": phone,
                       "qq": qq})
    print("添加%s成功！" % name)


def show_all():
    print("-" * 50)
    if len(cards_list) == 0:
        print("还未添加任何名片，请返回添加！")
        return
    for name in ["姓名", "电话", "qq"]:
        print(name, end="\t\t")
    print("")
    print("=" * 50)
    for key in cards_list:
        print("%s\t\t%s\t\t%s" % (key["name"],
                                  key["phone"],
                                  key["qq"]))


def search():
    print("-" * 50)
    find_name = input("请输入要查找的姓名： ")
    for key in cards_list:
        if key["name"] == find_name:
            for name in ["姓名", "电话", "qq"]:
                print(name, end="\t\t")
            print("")
            print("%s\t\t%s\t\t%s" % (key["name"],
                                      key["phone"],
                                      key["qq"]))
            while True:
                action = input("您还可以继续操作："
                               "按[1]修改名片  "
                               "按[2]删除名片  "
                               "按[0]返回上级界面")
                if action == "1":
                    key["name"] = input_pro(key["name"], "姓名： ")
                    key["phone"] = input_pro(key["phone"], "电话： ")
                    key["qq"] = input_pro(key["qq"], "qq: ")
                    print("修改完成！")
                elif action == "2":
                    cards_list.remove(key)
                    print("删除成功！")
                elif action == "0":
                    break
            break

    else:
        print("查无此人")


def input_pro(key, message):
    value = input(message)
    if len(value) > 0:
        return value
    else:
        return key
