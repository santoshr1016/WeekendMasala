#!/usr/bin/python
# -*- coding: utf-8 -*-

# in-place algorithm that reverses an array in O(N)


def reverse_array(nums):
    # pointer to the first item

    start_index = 0

    # pointer to the last item

    end_index = len(nums) - 1

    # while the end_index is greater than the start_index

    while end_index > start_index:
        # swap the two items

        (nums[start_index], nums[end_index]) = (nums[end_index],
                                                nums[start_index])

        # increment the start_index

        start_index = start_index + 1

        # decrement the end_index

        end_index = end_index - 1

    # the reversed array

    return nums


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]

    print(reverse_array(nums))

