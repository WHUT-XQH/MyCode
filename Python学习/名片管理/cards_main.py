#! /usr/bin/python3
import cards_tools


while True:
    cards_tools.menu()
    choice = input("请输入您的选择： ")
    if choice in ["1", "2", "3"]:
        if choice == "1":
            cards_tools.add()
        elif choice == "2":
            cards_tools.show_all()
        elif choice == "3":
            cards_tools.search()
    elif choice == "0":
        print("欢迎下次使用")
        break
    else:
        print("您的输入有误")
