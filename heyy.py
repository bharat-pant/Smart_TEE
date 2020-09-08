from time import sleep
import multiprocessing as mp


def foo(x):
    print('foo')
    for i in range(5):
        print('Process {}: in foo {}'.format(x, i))
        sleep(0.5)


if __name__ == '__main__':
    pool = mp.Pool()

    jobs = []
    for i in range(4):
        job = pool.apply_async(foo, args=[i])
        jobs.append(job)

    for job in jobs:
        job.wait()
