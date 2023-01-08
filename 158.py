def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
	key = [keysPressed[0]]
	max_dur = releaseTimes[0]

	for i in range(1, len(releaseTimes)):
		if releaseTimes[i] - releaseTimes[i - 1] == max_dur:
			key.append(keysPressed[i])

		if releaseTimes[i] - releaseTimes[i - 1] > max_dur:
			max_dur = releaseTimes[i] - releaseTimes[i - 1]
			key = [keysPressed[i]]


	return max(key)
