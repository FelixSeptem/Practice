# -*- coding: UTF-8 -*-
import math
import random

class Heap:
    def __init__(self, nums=None, capacity=100):
        self._data = []
        self._capacity = capacity
        if type(nums) == list and len(nums) <= self._capacity:
            for n in nums:
                assert type(n) is int
                self._data.append(n)
        self._length = len(self._data)
        self._heapify()

    def _heapify(self):
        if self._length <= 1:
            return

        # idx of the Last Parent node
        lp = (self._length - 2) // 2

        for i in range(lp, -1, -1):
            self._heap_down(i)

    def _heap_down(self, idx):
        pass

    def insert(self, num):
        pass

    def get_top(self):
        if self._length <= 0:
            return None
        return self._data[0]

    def remove_top(self):
        if self._length <= 0:
            return None

        self._data[0], self._data[-1] = self._data[-1], self._data[0]
        ret = self._data.pop()
        self._length -= 1
        self._heap_down(0)

        return ret

    def get_data(self):
        return self._data

    def get_length(self):
        return self._length

    @staticmethod
    def _draw_heap(data):
        """
        格式化打印
        :param data:
        :return:
        """
        length = len(data)

        if length == 0:
            return 'empty heap'

        ret = ''
        for i, n in enumerate(data):
            ret += str(n)
            # 每行最后一个换行
            if i == 2 ** int(math.log(i + 1, 2) + 1) - 2 or i == len(data) - 1:
                ret += '\n'
            else:
                ret += ', '

        return ret

    def __repr__(self):
        return self._draw_heap(self._data)


class MaxHeap(Heap):
    def _heap_down(self, idx):
        if self._length <= 1:
            return

        lp = (self._length - 2) // 2

        while idx <= lp:
            lc = 2 * idx + 1
            rc = lc + 1

            if rc <= self._length-1:
                tmp = lc if self._data[lc] > self._data[rc] else rc
            else:
                tmp = lc

            if self._data[tmp] > self._data[idx]:
                self._data[tmp], self._data[idx] = self._data[idx], self._data[tmp]
                idx = tmp
            else:
                break

    def insert(self, num):
        if self._length >= self._capacity:
            return False

        self._data.append(num)
        self._length += 1

        nn = self._length - 1
        while nn > 0:
            p = (nn-1) // 2

            if self._data[nn] > self._data[p]:
                self._data[nn], self._data[p] = self._data[p], self._data[nn]
                nn = p
            else:
                break

        return True


class MinHeap(Heap):
    def _heap_down(self, idx):
        if self._length <= 1:
            return

        lp = (self._length - 2) // 2

        while idx <= lp:
            lc = 2 * idx + 1
            rc = lc + 1

            if rc <= self._length-1:
                tmp = lc if self._data[lc] < self._data[rc] else rc
            else:
                tmp = lc

            if self._data[tmp] < self._data[idx]:
                self._data[tmp], self._data[idx] = self._data[idx], self._data[tmp]
                idx = tmp
            else:
                break

    def insert(self, num):
        if self._length >= self._capacity:
            return False

        self._data.append(num)
        self._length += 1

        nn = self._length - 1
        while nn > 0:
            p = (nn-1) // 2

            if self._data[nn] < self._data[p]:
                self._data[nn], self._data[p] = self._data[p], self._data[nn]
                nn = p
            else:
                break

        return True


class BinaryHeap:
    """
    大顶堆
    """
    def __init__(self, data=None, capacity=100):
        self._data = []
        self._capacity = capacity
        if type(data) is list:
            if len(data) > self._capacity:
                raise Exception('Heap oversize, capacity:{}, data size:{}'.format(self._capacity, len(data)))
            self._type_assert(data)
            self._data = data

        self._length = len(self._data)

    def heapify(self):
        """
        堆化
        :return:
        """
        self._heapify(self._data, self._length-1)

    def _heapify(self, data, tail_idx):
        """
        堆化内部实现
        :param data: 需要堆化的数据
        :param tail_idx: 尾元素的索引
        :return:
        """
        # heapify data[:tail_idx+1]
        if tail_idx <= 0:
            return

        # idx of the Last Parent node
        lp = (tail_idx - 1) // 2

        for i in range(lp, -1, -1):
            self._heap_down(data, i, tail_idx)

    @staticmethod
    def _heap_down(data, idx, tail_idx):
        """
        将指定的位置堆化
        :param data: 需要堆化的数据
        :param idx: data: 中需要堆化的位置
        :param tail_idx: 尾元素的索引
        :return:
        """
        assert type(data) is list

        lp = (tail_idx - 1) // 2
        # top-down
        while idx <= lp:
            # Left and Right Child index
            lc = 2 * idx + 1
            rc = lc + 1

            # right child exists
            if rc <= tail_idx:
                tmp = lc if data[lc] > data[rc] else rc
            else:
                tmp = lc

            if data[tmp] > data[idx]:
                data[tmp], data[idx] = data[idx], data[tmp]
                idx = tmp
            else:
                break

    def insert(self, num):
        """
        插入
        :param num:
        :return:
        """
        if self._length < self._capacity:
            if self._insert(self._data, num):
                self._length += 1
                return True
        return False

    @staticmethod
    def _insert(data, num):
        """
        堆中插入元素的内部实现
        :param data:
        :param num:
        :return:
        """
        assert type(data) is list
        assert type(num) is int

        data.append(num)
        length = len(data)

        # idx of New Node
        nn = length - 1
        # bottom-up
        while nn > 0:
            p = (nn-1) // 2
            if data[nn] > data[p]:
                data[nn], data[p] = data[p], data[nn]
                nn = p
            else:
                break

        return True

    def get_top(self):
        """
        取堆顶
        :return:
        """
        if self._length <= 0:
            return None
        return self._data[0]

    def remove_top(self):
        """
        取堆顶
        :return:
        """
        ret = None
        if self._length > 0:
            ret = self._remove_top(self._data)
            self._length -= 1
        return ret

    @staticmethod
    def _remove_top(data):
        """
        取堆顶内部实现
        :param data:
        :return:
        """
        assert type(data) is list

        length = len(data)
        if length == 0:
            return None

        data[0], data[-1] = data[-1], data[0]
        ret = data.pop()
        length -= 1

        # length == 0 or == 1, return
        if length > 1:
            BinaryHeap._heap_down(data, 0, length-1)

        return ret

    @staticmethod
    def _type_assert(nums):
        assert type(nums) is list
        for n in nums:
            assert type(n) is int

    @staticmethod
    def _draw_heap(data):
        """
        格式化打印
        :param data:
        :return:
        """
        length = len(data)

        if length == 0:
            return 'empty heap'

        ret = ''
        for i, n in enumerate(data):
            ret += str(n)
            # 每行最后一个换行
            if i == 2**int(math.log(i+1, 2)+1) - 2 or i == len(data) - 1:
                ret += '\n'
            else:
                ret += ', '

        return ret

    def __repr__(self):
        return self._draw_heap(self._data)


class BinaryHeapSort(BinaryHeap):
    def __init__(self):
        super(BinaryHeapSort, self).__init__()

    def sort(self, nums):
        """
        排序
        1. 堆化，大顶堆
        2. 排序，从后往前遍历，首尾元素互换，子数组堆化
        :param nums:
        :return:
        """
        assert type(nums) is list
        length = len(nums)

        if length <= 1:
            return

        self._type_assert(nums)

        # heapify
        self._heapify(nums, length-1)

        # sort
        for i in range(length-1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            self._heap_down(nums, 0, i-1)

        return


class QueueNode:
    def __init__(self, priority, data=None):
        assert type(priority) is int and priority >= 0
        self.priority = priority
        self.data = data

    def __repr__(self):
        return str((self.priority, self.data))


class PriorityQueue:
    def __init__(self, capacity=100):
        self._capacity = capacity
        self._q = []
        self._length = 0

    def enqueue(self, priority, data=None):
        if self._length >= self._capacity:
            return False

        new_node = QueueNode(priority, data)
        self._q.append(new_node)
        self._length += 1

        # update queue
        nn = self._length - 1
        while nn > 0:
            p = (nn - 1) // 2
            if self._q[nn].priority < self._q[p].priority:
                self._q[nn], self._q[p] = self._q[p], self._q[nn]
                nn = p
            else:
                break

        return True

    def dequeue(self):
        if self._length <= 0:
            raise Exception('the queue is empty....')

        self._q[0], self._q[-1] = self._q[-1], self._q[0]
        ret = self._q.pop()
        self._length -= 1

        if self._length > 1:
            # update queue
            lp = (self._length - 2) // 2
            idx = 0

            while idx <= lp:
                lc = 2 * idx + 1
                rc = lc + 1

                if rc <= self._length - 1:
                    tmp = lc if self._q[lc].priority < self._q[rc].priority else rc
                else:
                    tmp = lc

                if self._q[tmp].priority < self._q[idx].priority:
                    self._q[tmp], self._q[idx] = self._q[idx], self._q[tmp]
                    idx = tmp
                else:
                    break
        return ret

    def get_length(self):
        return self._length

    @staticmethod
    def _draw_heap(data):
        """
        格式化打印
        :param data:
        :return:
        """
        length = len(data)

        if length == 0:
            return 'empty'

        ret = ''
        for i, n in enumerate(data):
            ret += str(n)
            # 每行最后一个换行
            if i == 2 ** int(math.log(i + 1, 2) + 1) - 2 or i == len(data) - 1:
                ret += '\n'
            else:
                ret += ', '

        return ret

    def __repr__(self):
        def formater(node):
            assert type(node) is QueueNode
            return node.priority, node.data

        data = list(map(formater, self._q))
        return self._draw_heap(data)


def top_k(nums, k):
    """
    返回数组的前k大元素
    :param nums:
    :param k:
    :return:
    """
    if len(nums) <= k:
        return nums

    min_h = MinHeap(nums[:k], k)
    for i in range(k, len(nums)):
        tmp = min_h.get_top()
        if nums[i] > tmp:
            min_h.remove_top()
            min_h.insert(nums[i])

    return min_h.get_data()


class MaxHeap:
    def __init__(self, capacity: int):
        self._data = [0] * (capacity + 1)
        self._capacity = capacity
        self._count = 0
    
    @classmethod
    def _parent(cls, child_index: int) -> int:
        """The parent index."""
        return child_index // 2
    
    @classmethod
    def _left(cls, parent_index: int) -> int:
        """The left child index."""
        return 2 * parent_index
    
    @classmethod
    def _right(cls, parent_index: int) -> int:
        """The right child index."""
        return 2 * parent_index + 1

    def _siftup(self) -> None:
        i, parent = self._count, Heap._parent(self._count)
        while parent and self._data[i] > self._data[parent]:
            self._data[i], self._data[parent] = self._data[parent], self._data[i]
            i, parent = parent, Heap._parent(parent)

    @classmethod
    def _siftdown(cls, a: List[int], count: int, root_index: int = 1) -> None:
        i = larger_child_index = root_index
        while True:
            left, right = cls._left(i), cls._right(i)
            if left <= count and a[i] < a[left]:
                larger_child_index = left
            if right <= count and a[larger_child_index] < a[right]:
                larger_child_index = right
            if larger_child_index == i: break
            a[i], a[larger_child_index] = a[larger_child_index], a[i]
            i = larger_child_index

    def insert(self, value: int) -> None:
        if self._count >= self._capacity: return
        self._count += 1
        self._data[self._count] = value
        self._siftup()

    def remove_max(self) -> Optional[int]:
        if self._count:
            result = self._data[1]
            self._data[1] = self._data[self._count]
            self._count -= 1
            Heap._siftdown(self._data, self._count)
            return result

    @classmethod
    def build_heap(cls, a: List[int]) -> None:
        """Data in a needs to start from index 1."""
        for i in range((len(a) - 1)//2, 0, -1):
            cls._siftdown(a, len(a) - 1, i)
    
    @classmethod
    def sort(cls, a: List[int]) -> None:
        """Data in a needs to start from index 1."""
        cls.build_heap(a)
        k = len(a) - 1
        while k > 1:
            a[1], a[k] = a[k], a[1]
            k -= 1
            cls._siftdown(a, k)

    def __repr__(self):
        return self._data[1 : self._count + 1].__repr__()


class MinHeap:
    '''
    索引从0开始的小顶堆
    参考: https://github.com/python/cpython/blob/master/Lib/heapq.py
    author: Ben
    '''

    def __init__(self, nums):
        self._heap = nums

    def _siftup(self, pos):
        '''
        从上向下的堆化
        将pos节点的子节点中的最值提升到pos位置
        '''
        start = pos
        startval = self._heap[pos]
        n = len(self._heap)
        # 完全二叉树特性
        child = pos * 2 + 1
        # 比较叶子节点
        while child < n:
            right = child + 1
            # 平衡二叉树的特性, 大的都在右边
            if right < n and not self._heap[right] > self._heap[child]:
                child = right
            self._heap[pos] = self._heap[child]
            pos = child
            child = pos * 2 + 1
        self._heap[pos] = startval

        # 此时只有pos是不确定的
        self._siftdown(start, pos)

    def _siftdown(self, start, pos):
        '''
        最小堆: 大于start的节点, 除pos外已经是最小堆
        以pos为叶子节点, start为根节点之间的元素进行排序. 将pos叶子节点交换到正确的排序位置
        操作: 从叶子节点开始, 当父节点的值大于子节点时, 父节点的值降低到子节点
        '''
        startval = self._heap[pos]
        while pos > start:
            parent = (pos - 1) >> 1
            parentval = self._heap[parent]
            if parentval > startval:
                self._heap[pos] = parentval
                pos = parent
                continue
            break
        self._heap[pos] = startval

    def heapify(self):
        '''
        堆化: 从后向前(从下向上)的方式堆化, _siftup中pos节点的子树已经是有序的,
        这样要排序的节点在慢慢减少
        1. 因为n/2+1到n的节点是叶子节点(完全二叉树的特性), 它们没有子节点,
        所以, 只需要堆化n/2到0的节点, 以对应的父节点为根节点, 将最值向上筛选,
        然后交换对应的根节点和查找到的最值
        2. 因为开始时待排序树的根节点还没有排序, 为了保证根节点的有序,
        需要将子树中根节点交换到正确顺序
        '''
        n = len(self._heap)
        for i in reversed(range(n // 2)):
            self._siftup(i)

    def heappop(self):
        '''
        弹出堆首的最值 O(logn)
        '''
        tail = self._heap.pop()
        # 为避免破环完全二叉树特性, 将堆尾元素填充到堆首
        # 此时, 只有堆首是未排序的, 只需要一次从上向下的堆化
        if self._heap:
            peak = self._heap[0]
            self._heap[0] = tail
            self._siftup(0)
            return peak
        return tail

    def heappush(self, val):
        '''
        添加元素到堆尾 O(logn)
        '''
        n = len(self._heap)
        self._heap.append(val)
        # 此时只有堆尾的节点是未排序的, 将添加的节点迭代到正确的位置
        self._siftdown(0, n)

    def __repr__(self):
        vals = [str(i) for i in self._heap]
        return '>'.join(vals)
