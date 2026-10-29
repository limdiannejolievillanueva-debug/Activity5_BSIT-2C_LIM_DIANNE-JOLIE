# Print Queue Simulation using LinkedQueue
from linked_queue import LinkedQueue


class PrintJob:
    def __init__(self, job_id, pages):
        self.job_id = job_id
        self.pages = pages

    def __repr__(self):
        return f"[Job ID: {self.job_id}, Pages: {self.pages}]"


def simulate_print_queue():
    print_queue = LinkedQueue()
    jobs = [("Job1", 5), ("Job2", 12), ("Job3", 2)]

    print("--- Enqueuing Print Jobs ---")
    for job_id, pages in jobs:
        job = PrintJob(job_id, pages)
        print_queue.enqueue(job)
        print(f"Enqueued: {job}")

    print("\n--- Processing Print Jobs (FIFO) ---")
    order = 1
    while not print_queue.is_empty():
        job = print_queue.dequeue()
        print(f"Wait Position {order}: Printing {job}")
        order += 1


if __name__ == "__main__":
    simulate_print_queue()
