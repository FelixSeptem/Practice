# -*- coding:utf-8 -*-
def bag(items_info, capacity):
    """
    固定容量的背包，计算能装进背包的物品组合的最大重量
    :param items_info: 每个物品的重量
    :param capacity: 背包容量
    :return: 最大装载重量
    """
    n = len(items_info)
    memo = [[-1]*(capacity+1) for i in range(n)]
    memo[0][0] = 1
    if items_info[0] <= capacity:
        memo[0][items_info[0]] = 1

    for i in range(1, n):
        for cur_weight in range(capacity+1):
            if memo[i-1][cur_weight] != -1:
                memo[i][cur_weight] = memo[i-1][cur_weight]   # 不选
                if cur_weight + items_info[i] <= capacity:    # 选
                    memo[i][cur_weight + items_info[i]] = 1

    for w in range(capacity, -1, -1):
        if memo[-1][w] != -1:
            return w


def bag_with_max_value(items_info, capacity):
    """
    固定容量的背包，计算能装进背包的物品组合的最大价值
    :param items_info: 物品的重量和价值
    :param capacity: 背包容量
    :return: 最大装载价值
    """
    n = len(items_info)
    memo = [[-1]*(capacity+1) for i in range(n)]
    memo[0][0] = 0
    if items_info[0][0] <= capacity:
        memo[0][items_info[0][0]] = items_info[0][1]

    for i in range(1, n):
        for cur_weight in range(capacity+1):
            if memo[i-1][cur_weight] != -1:
                memo[i][cur_weight] = memo[i-1][cur_weight]
                if cur_weight + items_info[i][0] <= capacity:
                    memo[i][cur_weight + items_info[i][0]] = max(memo[i][cur_weight + items_info[i][0]],
                                                                 memo[i-1][cur_weight] + items_info[i][1])
    return max(memo[-1])


def knapsack01(weights, values, capacity):
    # Denote the state as (i, c), where i is the stage number,
    # and c is the capacity available. Denote f(i, c) to be the
    # maximum value when the capacity available is c, and Item 0
    # to Item i-1 are to be packed.
    # The goal is to find f(n-1, W), where W is the total capacity.
    # Then the DP functional equation is:
    #   f(i, c) = max(xᵢvᵢ + f(i-1, c-xᵢwᵢ)), xᵢ ∈ D, i ≥ 0,
    #   f(-1, c) = 0, 0 ≤ c ≤ W,
    # where
    #                  /  {0},    if wᵢ > c
    #   D = D(i, c) = 
    #                  \  {0, 1}, if wᵢ ≤ c

    prev = [0] * (capacity + 1)
    for w, v in zip(weights, values):
        prev = [c >= w and max(prev[c], prev[c-w] + v) for c in range(capacity + 1)]
    return prev[-1]


Layer_nums = List[int]


def yh_triangle(nums):
    """
    从根节点开始向下走，过程中经过的节点，只需存储经过它时最小的路径和
    :param nums:
    :return:
    """
    assert len(nums) > 0
    n = len(nums)   # 层数
    memo = [[0]*n for i in range(n)]
    memo[0][0] = nums[0][0]

    for i in range(1, n):
        for j in range(i+1):
            # 每一层首尾两个数字，只有一条路径可以到达
            if j == 0:
                memo[i][j] = memo[i-1][j] + nums[i][j]
            elif j == i:
                memo[i][j] = memo[i-1][j-1] + nums[i][j]
            else:
                memo[i][j] = min(memo[i-1][j-1] + nums[i][j], memo[i-1][j] + nums[i][j])
    return min(memo[n-1])


def yh_triangle_space_optimization(nums):
    assert len(nums) > 0
    n = len(nums)
    memo = [0] * n
    memo[0] = nums[0][0]

    for i in range(1, n):
        for j in range(i, -1, -1):
            if j == i:
                memo[j] = memo[j-1] + nums[i][j]
            elif j == 0:
                memo[j] = memo[j] + nums[i][j]
            else:
                memo[j] = min(memo[j-1] + nums[i][j], memo[j] + nums[i][j])
    return min(memo)


def yh_triangle_bottom_up(nums):
    assert len(nums) > 0
    n = len(nums)
    memo = nums[-1].copy()

    for i in range(n-1, 0, -1):
        for j in range(i):
            memo[j] = min(memo[j] + nums[i-1][j], memo[j+1] + nums[i-1][j])
    return memo[0]


def min_dist(weights):
    """Find the minimum weight path from the weights matrix."""
    m, n = len(weights), len(weights[0])
    table = [[0] * n for _ in range(m)]
    # table[i][j] is the minimum distance (weight) when
    # there are i vertical moves and j horizontal moves
    # left.
    table[0] = list(accumulate(reversed(weights[-1])))
    for i, v in enumerate(accumulate(row[-1] for row in reversed(weights))):
        table[i][0] = v
    for i in range(1, m):
        for j in range(1, n):
            table[i][j] = weights[~i][~j] + min(table[i - 1][j], table[i][j - 1])
    return table[-1][-1]


def min_dist_recur(weights):
    m, n = len(weights), len(weights[0])
    table = [[0] * n for _ in range(m)]
    def min_dist_to(i: int, j: int) -> int:
        if i == j == 0: return weights[0][0]
        if table[i][j]: return table[i][j]
        min_left = float("inf") if j - 1 < 0 else min_dist_to(i, j - 1)
        min_up = float("inf") if i - 1 < 0 else min_dist_to(i - 1, j)
        return weights[i][j] + min(min_left, min_up)
    return min_dist_to(m - 1, n - 1)


def coins_dp(values, target) -> int:
    # memo[i]表示target为i的时候，所需的最少硬币数
    memo = [0] * (target+1)
    # 0元的时候为0个
    memo[0] = 0

    for i in range(1, target+1):
        min_num = 999999
        # 对于values中的所有n
        # memo[i]为 min(memo[i-n1], memo[i-n2], ...) + 1
        for n in values:
            if i >= n:
                min_num = min(min_num, 1 + memo[i-n])
            else:   # values中的数值要从小到大排序
                break
        memo[i] = min_num

    # print(memo)
    return memo[-1]


min_num = 999999
def coins_backtracking(values, target, cur_value, coins_count):
    if cur_value == target:
        global min_num
        min_num = min(coins_count, min_num)
    else:
        for n in values:
            if cur_value + n <= target:
                coins_backtracking(values, target, cur_value+n, coins_count+1)

def levenshtein_dp(s, t):
    m, n = len(s), len(t)
    table = [[0] * (n) for _ in range(m)]

    for i in range(n):
        if s[0] == t[i]:
            table[0][i] = i - 0
        elif i != 0:
            table[0][i] = table[0][i - 1] + 1
        else:
            table[0][i] = 1

    for i in range(m):
        if s[i] == t[0]:
            table[i][0] = i - 0
        elif i != 0:
            table[i][0] = table[i - 1][0] + 1
        else:
            table[i][0] = 1

    for i in range(1, m):
        for j in range(1, n):
            table[i][j] = min(1 + table[i - 1][j], 1 + table[i][j - 1], int(s[i] != t[j]) + table[i - 1][j - 1])

    print(table)
    return table[-1][-1]


def common_substring_dp(s, t):
    m, n = len(s), len(t)
    table = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            table[i][j] = max(table[i - 1][j], table[i][j - 1], int(s[i - 1] == t[j - 1]) + table[i - 1][j - 1])
    return table[-1][-1]


def longest_increasing_subsequence(nums):
    """
    最长子上升序列的一种DP解法，从回溯解法转化，思路类似于有限物品的背包问题
    每一次决策都算出当前可能的lis的长度，重复子问题合并，合并策略是lis的末尾元素最小
    时间复杂度：O(n^2)
    空间复杂度：O(n^2)，可优化至O(n)
    没leetcode上的参考答案高效，提供另一种思路作为参考
    https://leetcode.com/problems/longest-increasing-subsequence/solution/
    :param nums:
    :return:
    """
    if not nums:
        return 0

    n = len(nums)
    # memo[i][j] 表示第i次决策，长度为j的lis的 最小的 末尾元素数值
    # 每次决策都根据上次决策的所有可能转化，空间上可以类似背包优化为O(n)
    memo = [[-1] * (n+1) for _ in range(n)]

    # 第一列全赋值为0，表示每次决策都不选任何数
    for i in range(n):
        memo[i][0] = 0
    # 第一次决策选数组中的第一个数
    memo[0][1] = nums[0]

    for i in range(1, n):
        for j in range(1, n+1):
            # case 1: 长度为j的lis在上次决策后存在，nums[i]比长度为j-1的lis末尾元素大
            if memo[i-1][j] != -1 and nums[i] > memo[i-1][j-1]:
                memo[i][j] = min(nums[i], memo[i-1][j])

            # case 2: 长度为j的lis在上次决策后存在，nums[i]比长度为j-1的lis末尾元素小/等
            if memo[i-1][j] != -1 and nums[i] <= memo[i-1][j-1]:
                memo[i][j] = memo[i-1][j]

            if memo[i-1][j] == -1:
                # case 3: 长度为j的lis不存在，nums[i]比长度为j-1的lis末尾元素大
                if nums[i] > memo[i-1][j-1]:
                    memo[i][j] = nums[i]
                # case 4: 长度为j的lis不存在，nums[i]比长度为j-1的lis末尾元素小/等
                break

    for i in range(n, -1, -1):
        if memo[-1][i] != -1:
            return i