from typing import List
from game_objects import Strategy
from random import random

class CooperateStrategy(Strategy):
    def get_action(self, my_moves: List[bool], opponent_moves: List[bool]) -> bool:
        return False
    def get_name(self) -> str:
        return "cooperator"
    
class DefectorStrategy(Strategy):
    def get_action(self, my_moves: List[bool], opponent_moves: List[bool]) -> bool:
        return True
    def get_name(self) -> str:
        return "defector"
    
class RandomStrategy(Strategy):
    def __init__(self, temperature=0.5) -> None:
        super().__init__()
        self.temperature = temperature
    def get_action(self, my_moves: List[bool], opponent_moves: List[bool]) -> bool:
        r = random()
        return r <  self.temperature        
    def get_name(self) -> str:
        return f"random {str(self.temperature)}"
    
class TitForTat(Strategy):
    def get_action(self, my_moves: List[bool], opponent_moves: List[bool]) -> bool:
        return False if len(my_moves) == 0 else opponent_moves[-1]
    def get_name(self) -> str:
        return "tit for tat"
    
class TitForTwoTat(Strategy):
    def get_action(self, my_moves: List[bool], opponent_moves: List[bool]) -> bool:
        return False if len(my_moves) in [0, 1] else opponent_moves[-1] and opponent_moves[-2]
    def get_name(self) -> str:
        return "tit for two tats"
    
class TwoTitForTat(Strategy):
    def get_action(self, my_moves: List[bool], opponent_moves: List[bool]) -> bool:
        return False if len(my_moves) in [0, 1] else opponent_moves[-1] or opponent_moves[-2]
    def get_name(self) -> str:
        return "two tit for tat"
    
class ReverseTitForTat(Strategy):
    def get_action(self, my_moves: List[bool], opponent_moves: List[bool]) -> bool:
        return False if len(my_moves) == 0 else False if opponent_moves[-1] else True
    def get_name(self) -> str:
        return "reverse tit for tat"
    
class Joss(Strategy):
    def __init__(self, temperature=0.05) -> None:
        super().__init__()
        self.temperature = temperature 
    def get_action(self, my_moves: List[bool], opponent_moves: List[bool]) -> bool:
        r = random()
        if r < self.temperature:
            return True
        
        # Otherwise play tit for tat
        return False if len(my_moves) == 0 else opponent_moves[-1]
    def get_name(self) -> str:
        return f"joss {str(self.temperature)}"
    
class FirmButFair(Strategy):
    def __init__(self, retaliate=2) -> None:
        super().__init__()
        self.retaliate = retaliate
    def get_action(self, my_moves: List[bool], opponent_moves: List[bool]) -> bool:
        if len(opponent_moves) == 0:
            return False
        
        if opponent_moves[-1] and not my_moves[-1]:
            return True
        
        # Oterwise get the number of recent retaliations
        n = len(my_moves) - 1
        i = 0
        while n > 0:
            if my_moves[n]:
                # We have retaliated
                n -=1
                i +=1
            else:
                break
        
        if  0 < i < self.retaliate:
            return True
        
        return False        
       
    def get_name(self) -> str:
        return f"firm but fair {self.retaliate}"    
    

    
class GrimTrigger(Strategy):
    def get_action(self, my_moves: List[bool], opponent_moves: List[bool]) -> bool:
        has_defected = len([x for x in opponent_moves if x]) > 0
        return  has_defected
    def get_name(self) -> str:
        return "grim trigger"
    
class Bully(Strategy):
    def __init__(self, retaliate=2) -> None:
        super().__init__()
        self.retaliate = retaliate

    def get_action(self, my_moves: List[bool], opponent_moves: List[bool]) -> bool:
        # Defect for some first rules
        if len(my_moves) <= self.retaliate:
            return True
        
        # Else check oponent last move
        return opponent_moves[-1]
    
    def get_name(self) -> str:
        return f"bully {str(self.retaliate)}"
    
class Prober(Strategy):
    def get_action(self, my_moves: List[bool], opponent_moves: List[bool]) -> bool:
        if len(my_moves) == 0:
            # First round always defect to probe the opponent
            return True
        
        if my_moves[-1] and opponent_moves[-1]:
            # Oponent reacted with deflection, then start to cooperate
            return False 
        
        # If we didnt deflect the last round just play tit for tat.
        return opponent_moves[-1]      
        
    
    def get_name(self) -> str:
        return "prober"
    
class Spoiler(Strategy):
    def get_action(self, my_moves: List[bool], opponent_moves: List[bool]) -> bool:
        if len(my_moves) == 0:
            # First round always defect to probe the opponent
            return True
        
        if my_moves[-1] and not opponent_moves[-1]:
            # As long as oponent didnt respond to our probing, spoil this behaviour
            return True 
        
        # else copy oponent strategy
        return  opponent_moves[-1]
        
    
    def get_name(self) -> str:
        return "spoiler"


