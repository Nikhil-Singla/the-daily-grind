class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()

        playerIndex = 0
        trainerIndex = 0

        matches = 0

        while(playerIndex < len(players) and trainerIndex < len(trainers)):
            if players[playerIndex] <= trainers[trainerIndex]:
                matches += 1
                playerIndex += 1
                trainerIndex += 1
            else:
                trainerIndex += 1

        return matches

        