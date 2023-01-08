			class Solution:
				def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
					ans =0
					time=0
					for i in timeSeries:
						ans += i + duration - max(i, time)
						time = i + duration
					return ans
