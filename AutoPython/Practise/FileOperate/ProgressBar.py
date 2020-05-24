import sys, time

# sys.stdout.write('#########################')

for i in range(50):
    sys.stdout.write('#')
    # 可以实时刷新缓存，否则会等满了之后才出现
    sys.stdout.flush()
    time.sleep(0.1)
