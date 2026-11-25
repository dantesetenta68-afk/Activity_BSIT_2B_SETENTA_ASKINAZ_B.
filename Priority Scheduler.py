
import heapq

class PriorityScheduler:

    def __init__(self):
        self.queue = []

    def add_job(self, job, priority):
        heapq.heappush(self.queue, (-priority, job))

    # Release the highest priority job
    def release_job(self):
        if len(self.queue) == 0:
            return None

        priority, job = heapq.heappop(self.queue)

        return job

    def is_empty(self):
        return len(self.queue) == 0


scheduler = PriorityScheduler()

scheduler.add_job("Job A", 2)
scheduler.add_job("Job B", 5)
scheduler.add_job("Job C", 3)
scheduler.add_job("Job D", 8)

release_order = []

print("Releasing Jobs:")

while not scheduler.is_empty():

    job = scheduler.release_job()

    release_order.append(job)

    print(job)

print("\nRelease Order:")
print(release_order)
