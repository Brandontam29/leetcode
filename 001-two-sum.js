var twoSum = function (nums, target) {
    prevSet = new Map();
    index1 = -1;
    index2 = -1;
    for (let i = 0; i < nums.length; i++) {
        if (prevSet.has(target - nums[i])) {
            index2 = i;
            index1 = prevSet.get(target - nums[i]);
            return [index1, index2];
        }
        prevSet.set(nums[i], i);
    }
};
