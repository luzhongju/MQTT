
# 定义一个函数来找到三个数字中的最大数和最小数
def find_max_min_sum(a, b, c):
    # 找出最大数
    max_num = max(a, b, c)
    # 找出最小数
    min_num = min(a, b, c)
    # 计算最大数和最小数的和
    total_sum = max_num + min_num
    # 打印最大数、最小数和它们的和
    print(f"最大数: {max_num}")
    print(f"最小数: {min_num}")
    print(f"最大数和最小数的和: {total_sum}")

# 示例使用
find_max_min_sum(5, 3, 78)
