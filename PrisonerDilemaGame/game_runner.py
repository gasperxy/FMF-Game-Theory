from game_objects import Game, Tournament
from strategies import *

# Create a list of the strategies
strategies = [
    TitForTat(),
    GrimTrigger(),    
    CooperateStrategy(), 
    TitForTwoTat(), 
    TwoTitForTat(), 
    FirmButFair(retaliate=2), 
    DefectorStrategy(), 
    Prober(),
    Spoiler(),
    Joss(temperature=0.1),     
    Bully(retaliate=3),          
    RandomStrategy(), 
    # RandomStrategy(temperature=0.75), 
    # RandomStrategy(temperature=0.25)
    ]


# Play the tournament and display results
tournament = Tournament(strategies, rounds=200, repeat=5)
tournament.play_tournament()
tournament.draw_results()
tournament.draw_results_details()


# Play a single game between two strategies
game = Game(DefectorStrategy(), TitForTat(), rounds=20)
game.play_game()
game.draw()