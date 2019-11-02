#
# @lc app=leetcode id=911 lang=python3
#
# [911] Online Election
#
# https://leetcode.com/problems/online-election/description/
#
# algorithms
# Medium (48.14%)
# Likes:    235
# Dislikes: 176
# Total Accepted:    16.6K
# Total Submissions: 34.4K
# Testcase Example:  '["TopVotedCandidate","q","q","q","q","q","q"]\n' +
#  '[[[0,1,1,0,0,1,0],[0,5,10,15,20,25,30]],[3],[12],[25],[15],[24],[8]]'
#
# In an election, the i-th vote was cast for persons[i] at time times[i].
# 
# Now, we would like to implement the following query function:
# TopVotedCandidate.q(int t) will return the number of the person that was
# leading the election at time t.  
# 
# Votes cast at time t will count towards our query.  In the case of a tie, the
# most recent vote (among tied candidates) wins.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: ["TopVotedCandidate","q","q","q","q","q","q"],
# [[[0,1,1,0,0,1,0],[0,5,10,15,20,25,30]],[3],[12],[25],[15],[24],[8]]
# Output: [null,0,1,1,0,0,1]
# Explanation: 
# At time 3, the votes are [0], and 0 is leading.
# At time 12, the votes are [0,1,1], and 1 is leading.
# At time 25, the votes are [0,1,1,0,0,1], and 1 is leading (as ties go to the
# most recent vote.)
# This continues for 3 more queries at time 15, 24, and 8.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= persons.length = times.length <= 5000
# 0 <= persons[i] <= persons.length
# times is a strictly increasing array with all elements in [0, 10^9].
# TopVotedCandidate.q is called at most 10000 times per test case.
# TopVotedCandidate.q(int t) is always called with t >= times[0].
# 
# 
# 
#

# @lc code=start
from bisect import bisect
class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        count = {}
        self.leads = []
        leader, m = None, 0
        for person, time in sorted(zip(persons,times),key=lambda x:x[1]):
            count[person] = count.get(person,0) + 1
            if count[person] >= m:
                if person != leader:
                    leader = person
                    self.leads.append((time, leader))
                
                if count[person] > m:
                    m = count[person]
        
    def q(self, t: int) -> int:
        i = bisect(self.leads,(t,float('inf')))
        return self.leads[i-1][1]

        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
# @lc code=end

