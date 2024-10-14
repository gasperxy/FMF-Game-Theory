## Iterated prisoner's dilemma game between multiple players

### Game description
Two players are playing the following game. In any round the player can either **defect(D)** or **cooperate(C)**. Based on the outcome, player are given different amount of points:
* If both play C, then they gain 3 points
* If both play D, then they gain 1 point
* If one plays C and other plays D, then defector (the one that played D) gain 5 points and the other gains 0 points.

If there is only one game played and the number of round is fixed, the best strategy is always to defect. However, if there are more than two players (sometimes called strategies) playing round robin tournament (against each other and the copy of itself) then it is sometimes better to cooperate. To find more about this read wikipedia article [Prisoner's dilemma](https://en.wikipedia.org/wiki/Prisoner%27s_dilemma).

### Game simulation
The Python code in this repository simulates the game described above, where new strategies can be quickly implemented and their effectiveness tested against others.
The main objects for game simulation are implemented in `game_objects.py` file. To implement the new strategy, implement new abstract class `Strategy` in file `strategies.py`. 

To implement new strategy you need to implement two functions:
* `get_action(my_moves, opponent_moves) -> bool`
* `get_name() -> str`

An example of a basic defector strategy is implemented as 
```python
from game_objects import Strategy
from typing import List

class DefectorStrategy(Strategy):
    def get_action(self, my_moves: List[bool], opponent_moves: List[bool]) -> bool:
        return True
    def get_name(self) -> str:
        return "defector"
```

To play the torunament or a single game check `game_runner.py` file.