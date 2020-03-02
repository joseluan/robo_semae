import _thread
from SEMAE import SEMAE
from queue import Queue
import time

semae = SEMAE()
queue = Queue()

try:    
    _thread.start_new_thread(semae.run, (queue, 100, 200,))
    _thread.start_new_thread(semae.run, (queue, 200, 300,))
    _thread.start_new_thread(semae.run, (queue, 300, 400,))
    
    _thread.start_new_thread(semae.showTitles, (queue,))
except Exception as e:
    print(e)
    print('Algo deu errado nas threads...')

while 1:
    pass