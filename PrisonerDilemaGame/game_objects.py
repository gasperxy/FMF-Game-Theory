
from typing import List, Callable, Dict, Tuple
from abc import ABC, abstractmethod

# Define payoffs as a matrix
payoffs = [
    [(2,2), (0,5)],
    [(5,0), (1,1)]
]

class Strategy(ABC):
    """
    Abstract class used to implement different strategies.
    """
    @abstractmethod
    def get_action(self, my_moves : List[bool], opponent_moves : List[bool]) -> bool:
        pass
    
    @abstractmethod
    def get_name(self) -> str:
        pass

class Game:
    """
    Class for playing a game between two strategies with given payoffs and number of rounds.
    """
    def __init__(self, 
                 strategy1 : Strategy, 
                 strategy2 : Strategy,  
                 payoffs : List[List[tuple]] = payoffs,
                 rounds : int = 10
                 ):                
      
        self.strategy1 = strategy1
        self.strategy2 = strategy2
        self.payoffs = payoffs
        self.rounds = rounds

        # Lists to store player/stragegy moves.
        # True - defect 
        # False - cooperate
        self.player1 : List[bool] = []
        self.player2 : List[bool] = []

        self.score1 : int = 0
        self.score2 : int = 0

    def play_next_round(self):
        """
        Plays the next round between two strategies.
        """
        move1 = self.strategy1.get_action(self.player1, self.player2)
        move2 = self.strategy2.get_action(self.player2, self.player1)

        payoff1, payoff2 = self.payoffs[move1][move2]

        self.player1.append(move1)
        self.player2.append(move2)
        self.score1 += payoff1
        self.score2 += payoff2

    def play_game(self):
        """
        Play entire game.
        """
        for _ in range(self.rounds):
            self.play_next_round()

        return (self.score1, self.score2)

    def draw(self):
        """
        Izrišemo rezultate igre.
        """
        print(f"player 1: {"|".join(["D" if x else "C" for x in self.player1])}")
        print(f"player 2: {"|".join(["D" if x else "C" for x in self.player2])}")
        print(f"Score player1={self.score1}, player2={self.score2}")

class Tournament:
    """
    Class for round robin tournament between a list of strategies.
    """
    def __init__(self, strategies : List[Strategy], rounds=10, repeat=1):
        self.strategies = strategies       
        self.rounds = rounds
        self.repeat = repeat   

        # Some objects to store the results of all matches (in different formats)
        self.strategy_scores : Dict[str, List[int]] = {strategy.get_name() : [] for strategy in strategies}        
        self.results : List[Tuple[str, float]] = [(strategy.get_name(), 0) for strategy in strategies]     
        self.comparison_results : Dict[str, List[Tuple[str, int]]] = {strategy.get_name() : [] for strategy in strategies}

    def play_tournament(self):
        """
        Plays the round robin tournament and store all results.
        """

        # Construct all games
        games : List[Tuple[str, str, Game]] = []
        for _ in range(self.repeat):
            for strategy1 in self.strategies:
                for strategy2 in self.strategies:
                    games.append(
                        (
                            strategy1.get_name(),
                            strategy2.get_name(), 
                            Game(strategy1, strategy2, rounds=self.rounds)
                        )
                    )

        # Play all games    
        for s1, s2, game in games:
            score1, score2 = game.play_game()
            self.strategy_scores[s1].append(score1)
            self.strategy_scores[s2].append(score2)

            self.comparison_results[s1].append((s2, score1))
            self.comparison_results[s2].append((s1, score2))

        # Create the average for every strategy and sort
        self.results = [(strategy, round(sum(scores)/len(scores) )) for strategy, scores in self.strategy_scores.items()]
        self.results.sort(key=lambda x: -x[1])

    def draw_results(self):
        """
        Print the result of the tournament.
        """
        for stragey, score in self.results:
            print(f"{stragey}: {str(score)}")

    def draw_results_details(self):
        """
        Print results of the tournament in more details. Average number of points
        is displayed for every strategy vs. all other.
        """
        r = dict()
        strats = self.comparison_results.keys()
        for s1 in strats:
            l = []
            for s2 in strats:
                g = [score for x, score in self.comparison_results[s1] if x==s2]
                l.append((s2, round(sum(g)/len(g))))
            r[s1] = l
        
        # Izpišemo:
        for s1 in strats:
            print("")
            print(f"{s1} results:")
            for s2, score in r[s1]:
                print(f"    {str(score)} vs {s2}")



    

