queue队列    -------> 存放数据的容器   --------->  解耦，使得程序直接实现松耦合( 提高效率 )
queue is especially useful in threaded programming when information must be exchanged safely between multiple threads.
当信息必须在多个线程之间安全地交换时，队列在线程编程中特别有用。(记住是同一个进程下的多个线程，不同进程不能使用)
class queue.Queue(maxsize=0) #先入先出 FIFO			# maxsize = 队列允许存放的最大值，如果存放多于maxsize，线程阻塞
	方法：put()、get()、qsize()、empty(),full()
class queue.LifoQueue(maxsize=0) #last in fisrt out(后进先出，栈)     LIFO
class queue.PriorityQueue(maxsize=0) #存储数据时可设置优先级的队列

Constructor for a priority queue.
优先队列的构造函数。
 maxsize is an integer that sets the upperbound limit on the number of items that can be placed in the queue.
maxsize是一个整数，用于设置可以放入队列中的项目数的上限。
Insertion will block once this size has been reached, until queue items are consumed. If maxsize is less than or equal to zero, the queue size is infinite.
一旦达到此大小，插入将会阻塞，直到消耗队列项目。如果maxsize小于或等于零，则队列大小是无限的。

The lowest valued entries are retrieved first (the lowest valued entry is the one returned by sorted(list(entries))[0]).
首先检索最低值的条目（最低值条目是由排序（列表（条目））[0]返回的条目）。
A typical pattern for entries is a tuple in the form: (priority_number, data).
条目的典型模式是以下形式的元组：（priority_number，data）。

exception queue.Empty
Exception raised when non-blocking get() (or get_nowait()) is called on a Queue object which is empty.
在空队列对象上调用非阻塞get（）（或get_nowait（））时引发异常。

exception queue.Full
Exception raised when non-blocking put() (or put_nowait()) is called on a Queue object which is full.
在已满的Queue对象上调用非阻塞put（）（或put_nowait（））时引发异常。

Queue.qsize()
Queue.empty() #return True if empty
Queue.full() # return True if full
Queue.put(item, block=True, timeout=None)
Put item into the queue. If optional args block is true and timeout is None (the default), block if necessary until a free slot is available. If timeout is a positive number, it blocks at most timeout seconds and raises the Full exception if no free slot was available within that time. Otherwise (block is false), put an item on the queue if a free slot is immediately available, else raise the Full exception (timeout is ignored in that case).

Queue.put_nowait(item)
Equivalent to put(item, False).

Queue.get(block=True, timeout=None)			block = True 默认取不到值就阻塞卡住，timeout = 阻塞等待时间
Remove and return an item from the queue.
将项目放入队列中。
If optional args block is true and timeout is None (the default), block if necessary until an item is available.
如果可选参数块为真，并且超时值为无（默认值），则在需要时禁止，直到有空闲插槽可用。
If timeout is a positive number, it blocks at most timeout seconds and raises the Empty exception if no item was available within that time.
如果超时时间为正数，则在最长超时秒数内阻塞，如果在该时间内没有空闲插槽可用，则会引发全例外。
Otherwise (block is false), return an item if one is immediately available, else raise the Empty exception (timeout is ignored in that case).
否则（块为假），如果空闲插槽立即可用，则在队列中放置一个项目，否则引发Full异常（在这种情况下超时被忽略）。

Queue.get_nowait()
Equivalent to get(False).
相当于put（item，False）

Two methods are offered to support tracking whether enqueued tasks have been fully processed by daemon consumer threads.
提供了两种方法来支持跟踪入队任务是否已完全由守护进程消费者线程处理。

Queue.task_done()
Indicate that a formerly enqueued task is complete. Used by queue consumer threads.
表明以前排队的任务已完成。由队列消费者线程使用。
For each get() used to fetch a task, a subsequent call to task_done() tells the queue that the processing on the task is complete.
对于用于获取任务的每个get（），随后对task_done（）的调用会告知队列该任务的处理已完成。

If a join() is currently blocking, it will resume when all items have been processed (meaning that a task_done() call was received for every item that had been put() into the queue).
如果join（）当前处于阻塞状态，则在处理完所有项目后（即，为每个已放入队列的项目收到task_done（）调用）它将继续。

Raises a ValueError if called more times than there were items placed in the queue.
如果调用的次数多于放入队列中的项目，则引发ValueError

Queue.join() block直到queue被消费完毕