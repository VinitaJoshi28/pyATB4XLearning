import time

def time_dec(func):
    def wrapper():
        start_time = time.time()
        print(f"start time: {start_time}")
        func()
        end_time = time.time()
        print(f"end time: {end_time}")

        time_taken=end_time-start_time
        print(f"total time taken is :{time_taken}")

    return wrapper()






@time_dec
def time_ui():
    print("added a time function:")
    time.sleep(2)
@time_dec
def time_ui2():
        print("added a time function:")
        time.sleep(5)