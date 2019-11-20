# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-
picks = []
picks_with_max_value = []


def bag(capacity, cur_weight, items_info, pick_idx):
    """
    回溯法解01背包，穷举
    :param capacity: 背包容量
    :param cur_weight: 背包当前重量
    :param items_info: 物品的重量和价值信息
    :param pick_idx: 当前物品的索引
    :return:
    """
    # 考察完所有物品，或者在中途已经装满
    if pick_idx >= len(items_info) or cur_weight == capacity:
        global picks_with_max_value
        if get_value(items_info, picks) > \
                get_value(items_info, picks_with_max_value):
            picks_with_max_value = picks.copy()
    else:
        item_weight = items_info[pick_idx][0]
        if cur_weight + item_weight <= capacity:    # 选
            picks[pick_idx] = 1
            bag(capacity, cur_weight + item_weight, items_info, pick_idx + 1)

        picks[pick_idx] = 0                         # 不选
        bag(capacity, cur_weight, items_info, pick_idx + 1)


def get_value(items_info, pick_items):
    values = [_[1] for _ in items_info]
    return sum([a*b for a, b in zip(values, pick_items)])


# 棋盘尺寸
BOARD_SIZE = 8

solution_count = 0
queen_list = [0] * BOARD_SIZE


def eight_queens(cur_column: int):
    """
    输出所有符合要求的八皇后序列
    用一个长度为8的数组代表棋盘的列，数组的数字则为当前列上皇后所在的行数
    :return:
    """
    if cur_column >= BOARD_SIZE:
        global solution_count
        solution_count += 1
        # 解
        print(queen_list)
    else:
        for i in range(BOARD_SIZE):
            if is_valid_pos(cur_column, i):
                queen_list[cur_column] = i
                eight_queens(cur_column + 1)


def is_valid_pos(cur_column: int, pos: int) -> bool:
    """
    因为采取的是每列放置1个皇后的做法
    所以检查的时候不必检查列的合法性，只需要检查行和对角
    1. 行：检查数组在下标为cur_column之前的元素是否已存在pos
    2. 对角：检查数组在下标为cur_column之前的元素，其行的间距pos - QUEEN_LIST[i]
       和列的间距cur_column - i是否一致
    :param cur_column:
    :param pos:
    :return:
    """
    i = 0
    while i < cur_column:
        # 同行
        if queen_list[i] == pos:
            return False
        # 对角线
        if cur_column - i == abs(pos - queen_list[i]):
            return False
        i += 1
    return True


is_match = False


def rmatch(r_idx: int, m_idx: int, regex: str, main: str):
    global is_match
    if is_match:
        return

    if r_idx >= len(regex):     # 正则串全部匹配好了
        is_match = True
        return

    if m_idx >= len(main) and r_idx < len(regex):   # 正则串没匹配完，但是主串已经没得匹配了
        is_match = False
        return

    if regex[r_idx] == '*':     # * 匹配1个或多个任意字符，递归搜索每一种情况
        for i in range(m_idx, len(main)):
            rmatch(r_idx+1, i+1, regex, main)
    elif regex[r_idx] == '?':   # ? 匹配0个或1个任意字符，两种情况
        rmatch(r_idx+1, m_idx+1, regex, main)
        rmatch(r_idx+1, m_idx, regex, main)
    else:                       # 非特殊字符需要精确匹配
        if regex[r_idx] == main[m_idx]:
            rmatch(r_idx+1, m_idx+1, regex, main)


permutations_list = []  # 全局变量，用于记录每个输出


def permutations(nums, n, pick_count):
    """
    从nums选取n个数的全排列
    回溯法，用一个栈记录当前路径信息
    当满足n==0时，说明栈中的数已足够，输出并终止遍历
    :param nums:
    :param n:
    :param pick_count:
    :return:
    """
    if n == 0:
        print(permutations_list)
    else:
        for i in range(len(nums) - pick_count):
            permutations_list[pick_count] = nums[i]
            nums[i], nums[len(nums) - pick_count - 1] = nums[len(nums) - pick_count - 1], nums[i]
            permutations(nums, n-1, pick_count+1)
            nums[i], nums[len(nums) - pick_count - 1] = nums[len(nums) - pick_count - 1], nums[i]
