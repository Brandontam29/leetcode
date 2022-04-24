<?php

/**
 * @param int[] $nums
 * @param int $target
 * @return int[]
 */
function twoSum($nums, $target)
{
    $map = array();

    foreach ($nums as $key => $value) {
        $targetItem = $target - $value;
        if (isset($map[$targetItem])) {
            return array($key, $map[$targetItem]);
        }
        $map[$value] = $key;
    }
    return array(0, 0);
}

print_r(twoSum([2, 11, 7, 15], 9)); // 0 2
print_r(twoSum([1234, 4356, 8925, 23457, 14, 78, 30, 10, 4, 12346, 84, 123, 40, 23452, 8648, 12304, 6345, 89678], 98603)); //2 17
