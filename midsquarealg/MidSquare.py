import math
import time

seed = int(time.time())
seed_size = len(str(seed))
start = math.floor(seed_size/2)
end = start + seed_size
def mid_square():
    global seed
    global start
    global end
    
    seed_number = seed  
    seed_number = int(str(seed_number * seed_number).zfill(seed_size*2)[start:end])
    seed = seed_number
    return seed_number