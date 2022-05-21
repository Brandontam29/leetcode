// Given an array of integers nums and an integer target,
// return indices of the two numbers such that they add up to target.

// You may assume that each input would have exactly one solution,
// and you may not use the same element twice.

// You can return the answer in any order.

// Example 1:
// Input: nums = [2,7,11,15], target = 9
// Output: [0,1]
// Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

// Example 2:
// Input: nums = [3,2,4], target = 6
// Output: [1,2]

// Example 3:
// Input: nums = [3,3], target = 6
// Output: [0,1]

fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
    for i in 0..nums.len() {
        for j in i + 1..nums.len() {
            if nums[i] + nums[j] == target {
                return vec![i as i32, j as i32];
            }
        }
    }

    unreachable!()
}

use std::collections::HashMap;

fn two_sum_2(nums: Vec<i32>, target: i32) -> Vec<i32> {
    let _len_n = nums.len();
    let mut num_to_idx = HashMap::<i32, usize>::new();
    for (idx, num) in nums.into_iter().enumerate() {
        let expected_sum = target - num;
        match num_to_idx.get(&expected_sum) {
            Some(&prev_idx) => return vec![prev_idx as i32, idx as i32],
            _ => {
                num_to_idx.insert(num, idx);
            }
        }
    }
    unreachable!()
}

fn main() {
    let a1 = vec![2, 7, 11, 15];
    let a2 = vec![3, 2, 4];
    let a3 = vec![3, 3];
    
    // println!("{:?}",two_sum(a1, 9));
    // println!("{:?}",two_sum(a2, 6));
    // println!("{:?}",two_sum(a3, 6));
    
    println!("{:?}",two_sum_2(a1, 9));
    println!("{:?}",two_sum_2(a2, 6));
    println!("{:?}",two_sum_2(a3, 6));
}
