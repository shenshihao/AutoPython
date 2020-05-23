data = {
    '北京市': {
        '东城区': {
            'aa': {'xx', 'll'},
            'bb': {'dd', 'cc'},
        },
        '西城区': {
            'cc',
            'dd',
        },
    },
    '天津市': {
        '和平区': {
            'ee',
            'ff',
        },
        '河东区': {
            'gg',
            'hh',
        },
    },
    '河北省': {
        '石家庄市': {
            '长安区': {
                'jj',
                'kk',
            },
            '桥西区': {
                'll',
                'mm',
            }
        },
        '唐山市': {
            '路南区',
            '路北区',
        },
    }
}
exit_flag = False
while not exit_flag:
    # 打印第一层
    for key in data:
        print(key)
    # 选择进入
    choice = input("选择进入1")
    if choice in data:
        while not exit_flag:
            for i2 in data[choice]:
                print("\t", i2)
            choice2 = input("选择进入2")
            if choice2 in data[choice]:
                while not exit_flag:
                    for i3 in data[choice][choice2]:
                        print("\t\t", i3)
                    choice3 = input("选择进入3")
                    if choice3 in data[choice][choice2]:
                        for i4 in data[choice][choice2][choice3]:
                            print("\t\t", i4)
                        choice4 = input("最后一层，按B返回")
                        if choice4 == 'b':
                            pass
                        elif choice4 == 'q':
                            exit_flag = True
                    if choice3 == 'b':
                        break
            if choice2 == 'b':
                break
            elif choice4 == 'q':
                exit_flag = True
