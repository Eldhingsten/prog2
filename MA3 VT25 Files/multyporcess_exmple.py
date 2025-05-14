from time import perf_counter as pc
from time import sleep as pause
#import multiprocessing as mp
import concurrent.futures as future

def runner(n):
    print(f'Performing costly function {n}')
    pause(n)
    print(f'Function {n} complete')

if __name__ == "__main__":
    start = pc()

    with future.ThreadPoolExecutor() as ex:
        p = [5, 4, 3, 2, 1]
        results = ex.map(runner, p)

        for r in results:
            print(r)
end = pc()
print(f"Process took {round(end-start, 2)} seconds")



"""
processes = []
start=pc()
for _ in range(10):
    p = mp.Process(target=runner)
    processes.append(p)
for p in processes:
    p.start()
for p in processes:
    p.join()
stop=pc()
print(f'The process took {round(stop-start,2)} seconds')
"""

