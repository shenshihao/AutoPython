import os


def get_big_file(path, filesize):
    """
    找出path目录下文件大小大于filesize的文件
    :param path:
    :param filesize:
    :return:
    """
    # 遍历指定文件夹及其子文件夹
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            target_file = os.path.join(dirpath, filename)
            # 要判断是否真的是文件,有可能是个链接哦
            if not os.path.isfile(target_file):
                continue
            size = os.path.getsize(target_file)
            if size > filesize:
                size = size // (1024 * 1024)  # 转换兆
                size = '{size}M'.format(size=size)
                print(target_file, size)


if __name__ == '__main__':
    get_big_file('D:\software', 500 * 1024 * 1024)
