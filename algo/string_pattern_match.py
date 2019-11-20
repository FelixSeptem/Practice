# -*- coding:utf-8 -*-
def bf(main, pattern):
    """
    字符串匹配，bf暴搜
    :param main: 主串
    :param pattern: 模式串
    :return:
    """
    n = len(main)
    m = len(pattern)

    if n <= m:
        return 0 if pattern == main else -1

    for i in range(n-m+1):
        for j in range(m):
            if main[i+j] == pattern[j]:
                if j == m-1:
                    return i
                else:
                    continue
            else:
                break
    return -1


def simple_hash(s, start, end):
    """
    计算子串的哈希值
    每个字符取acs-ii码后求和
    :param s:
    :param start:
    :param end:
    :return:
    """
    assert start <= end

    ret = 0
    for c in s[start: end+1]:
        ret += ord(c)
    return ret


def rk(main, pattern):
    n = len(main)
    m = len(pattern)

    if n <= m:
        return 0 if pattern == main else -1

    # 子串哈希值表
    hash_memo = [None] * (n-m+1)
    hash_memo[0] = simple_hash(main, 0, m-1)
    for i in range(1, n-m+1):
        hash_memo[i] = hash_memo[i-1] - simple_hash(main, i-1, i-1) + simple_hash(main, i+m-1, i+m-1)

    # 模式串哈希值
    hash_p = simple_hash(pattern, 0, m-1)

    for i, h in enumerate(hash_memo):
        # 可能存在哈希冲突
        if h == hash_p:
            if pattern == main[i:i+m]:
                return i
            else:
                continue
    return -1



SIZE = 256

def _generate_bad_character_table(pattern):
    bc = [-1] * SIZE
    for i, char in enumerate(pattern):
        bc[ord(char)] = i
    return bc


def _generate_good_suffix_table(pattern):
    m = len(pattern)
    # prefix[k] records whether the last k-character suffix of pattern
    # can match with the first k-character prefix of pattern.
    # suffix[k] records the starting index of the last substring of
    # pattern that can match with the last k-character suffix of pattern.
    prefix, suffix = [False] * m, [-1] * m
    # For each substring patter[:i+1], we find the common suffix with
    # pattern, and the starting index of this common suffix.
    # This way we can re-write previous suffix[k] to record the index
    # as large as possible, hence the last substring.
    for i in range(m - 1):
        j = i  # starting index of the common suffix
        k = 0  # length of the common suffix
        while j >= 0 and pattern[j] == pattern[~k]:
            j -= 1
            k += 1
            suffix[k] = j + 1
        if j == -1: prefix[k] = True
    return (prefix, suffix)


def _move_by_good_suffix(bad_character_index, suffix, prefix):
    k = len(suffix) - 1 - bad_character_index
    if suffix[k] != -1: return bad_character_index - suffix[k] + 1
    # Test from k - 1
    for r, can_match_prefix in enumerate(reversed(prefix[:k]), bad_character_index + 2): 
        if can_match_prefix: return r
    return len(suffix)


def bm(s, pattern):
    bc = _generate_bad_character_table(pattern)
    prefix, suffix = _generate_good_suffix_table(pattern)
    n, m = len(s), len(pattern)
    i = 0
    while i <= n - m:
        j = m - 1  # bad character index in pattern
        while j >= 0: 
            if s[i + j] != pattern[j]: break
            j -= 1
        if j < 0: return i
        
        x = j - bc[ord(s[i + j])]
        y = 0
        if j < m - 1:
            y = _move_by_good_suffix(j, suffix, prefix)
        i += max(x, y)
    return -1


SIZE = 256


def bm(main, pattern):
    """
    BM算法
    匹配规则：
    1. 坏字符规则
    2. 好字符规则
    :param main:
    :param pattern:
    :return:
    """
    assert type(main) is str and type(pattern) is str
    n, m = len(main), len(pattern)

    if n <= m:
        return 0 if main == pattern else -1

    # bc
    bc = [-1] * SIZE
    generate_bc(pattern, m, bc)

    # gs
    suffix = [-1] * m
    prefix = [False] * m
    generate_gs(pattern, m, suffix, prefix)

    i = 0
    while i < n-m+1:
        j = m - 1
        while j >= 0:
            if main[i+j] != pattern[j]:
                break
            else:
                j -= 1

        # pattern整个已被匹配，返回
        if j == -1:
            return i

        # 1. bc规则计算后移位数
        x = j - bc[ord(main[i+j])]

        # 2. gs规则计算后移位数
        y = 0
        if j != m - 1:    # 存在gs
            y = move_by_gs(j, m, suffix, prefix)

        i += max(x, y)

    return -1


def generate_bc(pattern, m, bc):
    """
    生成坏字符哈希表
    :param pattern:
    :param m:
    :param bc:
    :return:
    """
    for i in range(m):
        bc[ord(pattern[i])] = i


def generate_gs(pattern, m, suffix, prefix):
    """
    好后缀预处理
    :param pattern:
    :param m:
    :param suffix:
    :param prefix:
    :return:
    """
    for i in range(m-1):
        k = 0   # pattern[:i+1]和pattern的公共后缀长度
        for j in range(i, -1, -1):
            if pattern[j] == pattern[m-1-k]:
                k += 1
                suffix[k] = j
                if j == 0:
                    prefix[k] = True
            else:
                break


def move_by_gs(j, m, suffix, prefix):
    """
    通过好后缀计算移动值
    需要处理三种情况：
    1. 整个好后缀在pattern仍能找到
    2. 好后缀里存在 *后缀子串* 能和pattern的 *前缀* 匹配
    3. 其他
    :param j:
    :param m:
    :param suffix:
    :param prefix:
    :return:
    """
    k = m - 1 - j           # j指向从后往前的第一个坏字符，k是此次匹配的好后缀的长度

    if suffix[k] != -1:             # 1. 整个好后缀在pattern剩余字符中仍有出现
        return j - suffix[k] + 1
    else:
        for r in range(j+2, m):     # 2. 后缀子串从长到短搜索
            if prefix[m-r]:
                return r
        return m                    # 3. 其他情况


def kmp(s: int, pattern: int) -> int:
    m = len(pattern)
    partial_match_table = _get_partial_match_table(pattern)
    j = 0
    for i in range(len(s)):
        while j >= 0 and s[i] != pattern[j]:
            j = partial_match_table[j]
        j += 1
        if j == m:
            return i - m + 1
    return -1


def _get_partial_match_table(pattern: int) -> List[int]:
    # Denote πᵏ(i) as π applied to i for k times,
    # i.e., π²(i) = π(π(i)).
    # Then we have the result:
    #    π(i) = πᵏ(i-1) + 1,
    # where k is the smallest integer such that
    # pattern[πᵏ(i-1)+1] == pattern[i].

    # The value of π means the maximum length
    # of proper prefix/suffix.
    # The index of π means the length of the prefix
    # considered for pattern.
    # For example, π[2] means we are considering the first 2 characters
    # of the pattern.
    # If π[2] == 1, it means for the prefix of the pattern, P[0]P[1],
    # it has a maximum length proper prefix of 1, which is also the
    # suffix of P[0]P[1].
    # We also add a π[0] == -1 for easier handling of boundary
    # condition.
    
    m = len(pattern)
    π = [0] * (m + 1)
    π[0] = k = -1  # We use k here to represent πᵏ(i)
    for i in range(1, m + 1):
        while k >= 0 and pattern[k] != pattern[i - 1]:
            k = π[k]
        k += 1
        π[i] = k
    return π


def kmp(main, pattern):
    """
    kmp字符串匹配
    :param main:
    :param pattern:
    :return:
    """
    assert type(main) is str and type(pattern) is str

    n, m = len(main), len(pattern)

    if m == 0:
        return 0
    if n <= m:
        return 0 if main == pattern else -1

    # 求解next数组
    next = get_next(pattern)

    j = 0
    for i in range(n):
        # 在pattern[:j]中，从长到短递归去找最长的和后缀子串匹配的前缀子串
        while j > 0 and main[i] != pattern[j]:
            j = next[j-1] + 1   # 如果next[j-1] = -1，则要从起始字符取匹配

        if main[i] == pattern[j]:
            if j == m-1:
                return i-m+1
            else:
                j += 1
    return -1


def get_next(pattern):
    """
    next数组生成
    注意：
    理解的难点在于next[i]根据next[0], next[1]…… next[i-1]的求解
    next[i]的值依赖于前面的next数组的值，求解思路：
    1. 首先取出前一个最长的匹配的前缀子串，其下标就是next[i-1]
    2. 对比下一个字符，如果匹配，直接赋值next[i]为next[i-1]+1，因为i-1的时候已经是最长
    *3. 如果不匹配，需要递归去找次长的匹配的前缀子串，这里难理解的就是递归地方式，next[i-1]
        是i-1的最长匹配前缀子串的下标结尾，则 *next[next[i-1]]* 是其次长匹配前缀子串的下标
        结尾
    *4. 递归的出口，就是在次长前缀子串的下一个字符和当前匹配 或 遇到-1，遇到-1则说明没找到任
        何匹配的前缀子串，这时需要找pattern的第一个字符对比
    ps: next[m-1]的数值其实没有任何意义，求解时可以不理。网上也有将next数组往右平移的做法。
    :param pattern:
    :return:
    """
    m = len(pattern)
    next = [-1] * m

    next[0] = -1

    # for i in range(1, m):
    for i in range(1, m-1):
        j = next[i-1]       # 取i-1时匹配到的最长前缀子串
        while j != -1 and pattern[j+1] != pattern[i]:
            j = next[j]     # 次长的前缀子串的下标，即是next[next[i-1]]

        # 根据上面跳出while的条件，当j=-1时，需要比较pattern[0]和当前字符
        # 如果j!=-1，则pattern[j+1]和pattern[i]一定是相等的
        if pattern[j+1] == pattern[i]:  # 如果接下来的字符也是匹配的，那i的最长前缀子串下标是next[i-1]+1
            j += 1
        next[i] = j

    return next