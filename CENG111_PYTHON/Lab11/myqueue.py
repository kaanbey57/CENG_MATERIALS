def createQueue():
    return []
def enqueue(item, queue):
    queue.append(item)
def dequeue(queue):
    return queue.pop(0)
def isEmpty(queue):
    return queue==[]