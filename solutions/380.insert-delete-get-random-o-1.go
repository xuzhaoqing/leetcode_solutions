/*
 * @lc app=leetcode id=380 lang=golang
 *
 * [380] Insert Delete GetRandom O(1)
 *
 * https://leetcode.com/problems/insert-delete-getrandom-o1/description/
 *
 * algorithms
 * Medium (48.07%)
 * Likes:    2890
 * Dislikes: 176
 * Total Accepted:    276.3K
 * Total Submissions: 574.3K
 * Testcase Example:  '["RandomizedSet","insert","remove","insert","getRandom","remove","insert","getRandom"]\n' +
  '[[],[1],[2],[2],[],[1],[2],[]]'
 *
 * Implement the RandomizedSet class:
 *
 *
 * bool insert(int val) Inserts an item val into the set if not present.
 * Returns true if the item was not present, false otherwise.
 * bool remove(int val) Removes an item val from the set if present. Returns
 * true if the item was present, false otherwise.
 * int getRandom() Returns a random element from the current set of elements
 * (it's guaranteed that at least one element exists when this method is
 * called). Each element must have the same probability of being returned.
 *
 *
 * Follow up: Could you implement the functions of the class with each function
 * works in average O(1) time?
 *
 *
 * Example 1:
 *
 *
 * Input
 * ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove",
 * "insert", "getRandom"]
 * [[], [1], [2], [2], [], [1], [2], []]
 * Output
 * [null, true, false, true, 2, true, false, 2]
 *
 * Explanation
 * RandomizedSet randomizedSet = new RandomizedSet();
 * randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was
 * inserted successfully.
 * randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
 * randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now
 * contains [1,2].
 * randomizedSet.getRandom(); // getRandom() should return either 1 or 2
 * randomly.
 * randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now
 * contains [2].
 * randomizedSet.insert(2); // 2 was already in the set, so return false.
 * randomizedSet.getRandom(); // Since 2 is the only number in the set,
 * getRandom() will always return 2.
 *
 *
 *
 * Constraints:
 *
 *
 * -2^31 <= val <= 2^31 - 1
 * At most 10^5 calls will be made to insert, remove, and getRandom.
 * There will be at least one element in the data structure when getRandom is
 * called.
 *
 *
*/
package randomizedset

import "math/rand"

// @lc code=start
type RandomizedSet struct {
	array   []int
	hashmap map[int]int
}

/** Initialize your data structure here. */
func Constructor() RandomizedSet {
	return RandomizedSet{array: []int{}, hashmap: make(map[int]int)}
}

/** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
func (this *RandomizedSet) Insert(val int) bool {
	if _, ok := this.hashmap[val]; ok {
		return false
	}
	this.hashmap[val] = len(this.array)
	this.array = append(this.array, val)
	return true
}

/** Removes a value from the set. Returns true if the set contained the specified element. */
func (this *RandomizedSet) Remove(val int) bool {
	idx, ok := this.hashmap[val]
	if !ok {
		return false
	}
	last_idx := len(this.array) - 1
	this.array[last_idx], this.array[idx] = this.array[idx], this.array[last_idx]
	this.hashmap[this.array[idx]] = idx
	this.array = this.array[:last_idx]
	delete(this.hashmap, val)
	return true
}

/** Get a random element from the set. */
func (this *RandomizedSet) GetRandom() int {
	idx := rand.Intn(len(this.array))
	return this.array[idx]
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Insert(val);
 * param_2 := obj.Remove(val);
 * param_3 := obj.GetRandom();
 */
// @lc code=end
