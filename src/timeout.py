import time
import random
import datetime

class TimeoutException(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)

def busy_work():

    # Pretend to do something useful
    time.sleep(random.uniform(0.3, 0.6))

def train_loadbatch_from_lists(batch_size, timeout_sec):

    time_start = datetime.datetime.now()
    batch_xs = []
    batch_ys = []

    for i in range(0, batch_size+1):
        busy_work()
        batch_xs.append(i)
        batch_ys.append(i)

        time_elapsed = datetime.datetime.now() - time_start
        print ('Elapsed:', time_elapsed)
        if time_elapsed > timeout_sec:
            raise TimeoutException()

    return batch_xs, batch_ys

def main():

    timeout_sec = datetime.timedelta(seconds=5)
    batch_size = 10
    try:
        print ('Processing batch')
        batch_xs, batch_ys = train_loadbatch_from_lists(batch_size, timeout_sec)
        print ('Completed successfully')
        print (batch_xs, batch_ys)
    except TimeoutException as e:
        print ('Timeout after processing N records')

if __name__ == '__main__':
    main()