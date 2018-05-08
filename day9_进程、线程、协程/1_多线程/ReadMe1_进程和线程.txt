一、什么是进程(process)：
    对各种资源管理的集合

    程序并不能单独运行，只有将程序装载到内存中，系统为它分配资源才能运行，而这种执行的程序就称之为进程。
    程序和进程的区别就在于：程序是指令的集合，它是进程运行的静态描述文本；进程是程序的一次执行活动，属于动态概念。

    在多道编程中，我们允许多个程序同时加载到内存中，在操作系统的调度下，可以实现并发地执行。这是这样的设计，大大提高了CPU的利用率。
    进程的出现让每个用户感觉到自己独享CPU，因此，进程就是为了在CPU上实现多道编程而提出的。

    An executing instance[实例] of a program is called a process.
    程序的执行实例称为进程。
    Each process provides the resources needed to execute a program.
    每个进程都提供执行程序所需的资源。
    A process has a virtual[虚拟的] address space, executable code, open handles to system objects, a security context, a unique [process identifier 进程标识符 pid ], environment variables, a [priority class 优先级类], minimum and maximum working set sizes, and at least one thread of execution.
    进程具有虚拟地址空间，可执行代码，系统对象的打开句柄，安全上下文，唯一进程标识符，环境变量，优先级类别，最小和最大工作集大小以及至少一个执行线程。
    Each process is started with a single thread, often called the primary thread, but can create additional threads from any of its threads.
    每个进程都使用单线程启动，通常称为主线程，但可以从其任何线程创建其他线程。

注意：
    在linux上，每一个进程都是由父进程启动的，windows不详



二、什么是线程(thread):
    线程是操作系统能够进行运算调度的最小单位。是一串指令的集合

    它被包含在进程之中，是进程中的实际运作单位。一条线程指的是进程中一个单一顺序的控制流，一个进程中可以并发多个线程，每条线程并行执行不同的任务

    A thread is an execution[执行] context[上下文], which is all the information a CPU needs to execute a stream of instructions.
    线程是执行上下文，它是CPU执行指令流所需的全部信息。

    Suppose[假设] you're reading a book, and you want to take a break right now, but you want to be able to come back and resume[恢复] reading from the exact[准确的] point where you stopped.
    假设你正在阅读一本书，并且你现在想休息一下，但是你希望能够从停止的确切位置回来并继续阅读。
    One way to achieve[实现] that is by [jotting down 记下来 ] the page number, line number, and word number. So your execution context for reading a book is these 3 numbers.
    实现这一点的一种方法是记下页码，行号和字数。所以你阅读一本书的执行环境就是这3个数字。

    If you have a roommate, and she's using the same technique, she can take the book while you're not using it, and resume reading from where she stopped.
    如果你有一个室友，而且她使用的是同样的技巧，她可以在你不使用的时候拿起这本书，然后从停止的地方继续阅读。
    Then you can take it back, and resume it from where you were.
    然后，(当他不读的时候)您可以将它收回来，然后从您所在的位置恢复。(相当于你们共享阅读了一本书)

    Threads work in the same way.
    线程以相同的方式工作
    A CPU is giving you the illusion[幻觉(因为cpu太快了)] that it's doing multiple computations[运算] at the same time.
    CPU给你的错觉是它正在同时进行多个计算。它通过在每次计算上花费一点时间来做到这一点。
    It does that by spending a bit of time on each computation. It can do that because it has an execution context for each computation.
    它可以这样做，因为它为每个计算都有一个执行上下文(相当于书页行号)。
    Just like you can share a book with your friend, many tasks can share a CPU.
    就像你可以和你的朋友分享一本书一样，许多任务可以共享一个CPU。

    On a more technical level, an execution context (therefore a thread) consists[组合] of the values of the CPU's registers[寄存器].
    在更技术层面上，执行上下文（因此是一个线程）由CPU寄存器的值组成。

    Last: threads are different from processes. A thread is a context of execution, while a process is a bunch[一簇\一堆] of resources associated[相关的] with a computation.
    最后：线程与进程不同。线程是执行的上下文，而进程是与计算相关的一堆资源。
    A process can have one or many threads.
    一个进程可以有一个或多个线程。

    Clarification: the resources associated with a process include memory pages (all the threads in a process have the same view of the memory), file descriptors (e.g., open sockets), and security credentials (e.g., the ID of the user who started the process).
    说明：与进程相关的资源包括内存页面（进程中的所有线程都具有相同的内存视图），文件描述符（例如打开的套接字）和安全证书（例如，启动处理）。

注意：
    1、进程本身不可以执行
    2、进程要操作cpu，必须要创建一个线程(进程至少要有一个线程)
    3、所有在同一个进程的线程的是共享同一块内存空间的( 所以线程同时修改同一份数据时必须加锁 mutex互斥锁 )

三、有了进程为什么还要线程？
    进程有很多优点，它提供了多道编程，让我们感觉我们每个人都拥有自己的CPU和其他资源，可以提高计算机的利用率。很多人就不理解了，既然进程这么优秀，为什么还要线程呢？
    其实，仔细观察就会发现进程还是有很多缺陷的，主要体现在两点上：
        进程只能在一个时间干一件事，如果想同时干两件事或多件事，进程就无能为力了。
        进程在执行的过程中如果阻塞，例如等待输入，整个进程就会挂起，即使进程中有些工作不依赖于输入的数据，也将无法执行。

    例如，我们在使用qq聊天， qq做为一个独立进程如果同一时间只能干一件事，那他如何实现在同一时刻 即能监听键盘输入、又能监听其它人给你发的消息、同时还能把别人发的消息显示在屏幕上呢？
    你会说，操作系统不是有分时么？但我的亲，分时是指在不同进程间的分时呀， 即操作系统处理一会你的qq任务，又切换到word文档任务上了，每个cpu时间片分给你的qq程序时，你的qq还是只能同时干一件事呀。

再直白一点， 一个操作系统就像是一个工厂，工厂里面有很多个生产车间，不同的车间生产不同的产品，每个车间就相当于一个进程，且你的工厂又穷，供电不足，同一时间只能给一个车间供电，为了能让所有车间都能同时生产，你的工厂的电工只能给不同的车间分时供电，但是轮到你的qq车间时，发现只有一个干活的工人，结果生产效率极低，为了解决这个问题，应该怎么办呢？。。。。没错，你肯定想到了，就是多加几个工人，让几个人工人并行工作，这每个工人，就是线程！


四、进程和线程的区别
    1、Threads share the address space of the process that created it; processes have their own address space.
        线程共享创建它的进程的地址空间; 进程拥有自己的地址空间(进程是独立的)。
    2.Threads have direct access to the data segment of its process; processes have their own copy of the data segment of the parent process.
        线程可以直接访问其进程的数据段; 进程拥有父进程的数据段的自己的副本( 子进程共享父进程资源，但是子进程之间数据不共享，甚至不能访问，完全独立)。
    3.Threads can directly communicate[直接] with other threads of its process; processes must use interprocess(中间进程) communication to communicate with sibling processes.
        线程可以直接与其进程的其他线程通信( 同一个进程的线程之间可以直接交流 ); 进程必须使用进程间通信与兄弟进程进行通信。(两个进程想要通信，必须通过一个中间代理来实现 )
    4.New threads are easily created; new processes require duplication of the parent process.
        新线程很容易创建; 新进程需要重复父进程(创建新进程需要对其父进程进行一次克隆，如果父进程有2个G，创建的新进程也有2个G)。
    5.Threads can exercise considerable control over threads of the same process; processes can only exercise control over child processes.
        线程可以对同一进程的线程进行相当程度的控制和操作; 进程只能对子进程进行控制和操作。
    6.Changes to the main thread (cancellation[取消], priority change, etc.) may affect the behavior of the other threads of the process; changes to the parent process does not affect child processes.
        对主线程的更改（取消，优先级更改等）可能会影响进程其他线程的行为; 对父进程的更改不会影响子进程。


问题一：进程快还是线程快？(忽悠题)
    这个问题本身就有问题，进程和线程本身没有可比性，因为进程是资源的集合，线程是真正执行任务的，进程他要想执行任务也要通过线程
    所以本质上问的是两个线程哪个快

问题二：启动一个线程快还是进程快？
    启动一个线程快
    启动一个进程相当于建一个屋子，它需要各种各样的东西需要跟操作系统申请，启动一个线程相当于拉一个人进来，线程就是一堆指令，咔嚓就出来了
    但是启动之后一运行，都是一样的，因为进程也是线程来运行的
、
问题注意：
    # 线程过多唯一的不好就是：导致CPU切换过于频繁，导致系统过慢
    # 但是如果进程过多就会容易把系统搞瘫