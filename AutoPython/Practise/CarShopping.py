product_list = [
    ('Iphone', 8000),
    ('Mac Pro', 5000),
    ('Bike', 800),
    ('zxh Python', 800),
    ('coffee', 30)

]
shopping_list = []
salary = input("input your salary:")
# 判断是否是整数
if salary.isdigit():
    salary = int(salary)
    while True:
        for index, item in enumerate(product_list):
            print(index, item)
        user_choice = input('选择买什么》》：')
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice < len(product_list) and user_choice >= 0:
                p_item = product_list[user_choice]
                if p_item[1] <= salary:
                    print('买得起')
                    salary -= p_item[1]
                    shopping_list.append(p_item)

                    print(
                        'added %s into shooping cart,your salary balance is \033[31;1m%s\033[0m' % (p_item, salary))
                else:
                    print("\033[41;1mYour current salary only have [%s],还买个毛线啊\033[0m" % salary)
            else:
                print('product code [%s] is not exists' % user_choice)
        elif user_choice == 'q':
            print("--------------------------shopping List---------------------")
            for p in shopping_list:
                print(p)
                print('Your Current salary:', salary)
                exit()
        else:
            print('invalid option')
else:
    print('非法字符，请核对账户')
