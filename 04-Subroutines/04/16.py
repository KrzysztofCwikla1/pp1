def difference_between_largest_and_smallest(n1, n2, n3):
    max_num = max(n1, n2, n3)
    min_num = min(n1, n2, n3)
    return max_num - min_num

# main program
nums1 = (7, 4, 9)
nums2 = (2, 12, 8)

print(f"f{nums1} returns {difference_between_largest_and_smallest(*nums1)}")  # 5
print(f"f{nums2} returns {difference_between_largest_and_smallest(*nums2)}")  # 10