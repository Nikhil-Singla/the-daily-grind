class Router:
    def __init__(self, memoryLimit: int):
        self.max = memoryLimit
        self.packets = {}
        self.queue = deque()
        self.timestamps = defaultdict(list)

    def _encode(self, source: int, destination: int, timestamp: int) -> int:
        # Encode uniquely into 1 number
        # Only works if destination and timestamp are < 20 bits, or 2^20 ~ 1 million
        return (source << 40) | (destination << 20) | timestamp
        # We OR them as its non destructive 


    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        key = self._encode(source, destination, timestamp)
        
        if key in self.packets:
            return False

        if len(self.queue) >= self.max:
            self.forwardPacket()

        self.queue.append(key)
        self.packets[key] = [source, destination, timestamp]
        self.timestamps[destination].append(timestamp)

        return True

    def forwardPacket(self) -> List[int]:
        if not self.packets:
            return []

        key = self.queue.popleft()
        packet = self.packets.pop(key)

        target = packet[1]
        self.timestamps[target].pop(0)

        return packet

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        possible_times = self.timestamps.get(destination, [])

        if not possible_times:
            return 0

        left = bisect.bisect_left(possible_times, startTime)
        right = bisect.bisect_right(possible_times, endTime)

        return right - left


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)