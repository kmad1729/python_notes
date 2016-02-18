#!/usr/bin/env python3
'implementation of basic priority queue using heapq data structure'

import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._order = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._order, item))
        self._order += 1

    def pop(self):
        return heapq.heappop(self._queue)[2]

pq = PriorityQueue()
pq.push("wash clothes", 20)
pq.push("iron clothes", 15)
pq.push("buy clothes", 4)
pq.push("go to market", 21)
pq.push("buy milk", 20)
pq.push("eat food", 22)

for i in range(6):
    print(pq.pop())

