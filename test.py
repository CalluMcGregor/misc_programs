from rich.progress import track
import time

def do_step(step):
    time.sleep(1)

for step in track(range(100)):
    do_step(step)