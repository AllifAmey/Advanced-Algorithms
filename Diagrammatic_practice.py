#just use this to create diagrammic puzzles and solve it for practice
import random
"""
What are not assumptions:
5 types --> MAX.
Arrows to use: -->
Types are represented by : ✪ ♕ ⚝ ☯ ✞
Max routes between each route ( CapitalLetters to CapitalLetters ) is 5.

Assume max amount of letters is 8
Assume lowest amount of letters is 3


Computer will print the equations to solve to get to the final Equation.
User can dictate how many equations can be used.
"""

class Type:
    """
    There a 5 types with 3 types having 2 sub-types.

    Type 1:                                                                           Type 2:
    Re - Remove the first/last letter.                               Swa = Swap the first/last two letters.
    SubTypes:                                                                      SubTypes:
    ReF = Remove the first letter.                                    SwaF = Swap the first two letters.
    ReL = Remove the last letter.                                     SwaL = Swap the last two letters.                               


    Type 3:                                                                           Type 4:
    Dup = Duplicate the first/last two letters.                 Reverse the whole sequence.
    SubTypes:
    DupF = Duplicate the first two letters.                      Type 5:
    DupL = Duplicate the last two letters.                        Add a specific letter start/end.
    """

    def __init__(self):
        pass

    def Type1(self,FrontEquation,Decide):
        #decide has to be random.randint(1,2) to choose between two sub types.
        length = len(FrontEquation)
        if Decide == 1:
            #FirstLetter
            del FrontEquation[0]
        elif Decide == 2:
            #LastLetter
            del FrontEquation[length-1]
        return FrontEquation

    def Type2(self,FrontEquation,Decide):
        length = len(FrontEquation)
        if Decide == 1:
            #FirstLetter
            First_0 = FrontEquation[0]
            First_1 = FrontEquation[1]
            FrontEquation[0] = First_1
            FrontEquation[1] = First_0
        elif Decide == 2:
            #LastLetter
            Last_0 = FrontEquation[length-1]
            Last_1 = FrontEquation[length-2]
            FrontEquation[0] = Last_1
            FrontEquation[1] = Last_0
        return FrontEquation

    def Type3(self,FrontEquation,Decide):
        length = len(FrontEquation)
        if Decide == 1:
            #FirstLetter
            New = FrontEquation[0]
            New_FrontEquation += FrontEquation
            return New_FrontEquation
        elif Decide == 2:
            #LastLetter
            New = FrontEquation[length-1]
            FrontEquation += New
            return FrontEquation
        
    def Type4(self,FrontEquation):
        Count = 0
        length = len(FrontEquation)-1
        New = []
        for letter in list(range(0,length+1)):
            New.extend(FrontEquation[length+Count])
            Count += 1
        return New
        
    def Type5(self,FrontEquation,Decide):
        random_letter = random.randint(0,len(Container)-1)
        Letter_generated = Container[random_letter]
        if Decide == 1:
            #FirstLetter
            New = Letter_generated
            New_FrontEquation = New+FrontEquation
            return New_FrontEquation
        elif Decide == 2:
            #LastLetter
            FrontEquation += Letter_generated
            return FrontEquation

Container = ("abcdefghijklmnopqrstuvwxyz").upper()
Types = "✪ ♕ ⚝ ☯ ✞"
TypesList = Types.split()
Arrow = '-->'
BigString = ""
while True:
    print("How many equations before the final equation?")
    player_input = input()
    if Player_input == 'stop':
        break
    player_input = int(Player_input)
    
    
    Equation_symbols = []
    SymbolList_copy = TypesList
    #establishes what symbols to use and the reason why it is random is so it gives me a far accurate
    #representation of what the test would be like as all symbols do not represent the same type
    #for every equation.
    for iteration in list(range(0,random.randint(3,5))):
        SymbolList_length = len(SymbolList_copy)
        Random_symbol = SymbolList_copy[random.randint(0,SymbolList_length-1)]
        Equation_symbols.extend(Random_symbol)

    Types = Type()
    Type_list = [Type.type1,Type.type2,Type.type3,Type.type4,Type.type5]
    Type_used = []

    #This is the tough part. How many Types relative to the amount of equations would enable the explaination,
    # of all symbols? Assume each equation will explain the equation.
    for iteration in list(range(0,5)):
        pass

            
    #At this point we've established what symbols we're going to use, the type we're going to use.
    #We need to now formulate the equations before the final equation.
    

    Equation_list = {}
    
    #Making sure that every single equation explains each symbol.
    for iteration in list(range(0, player_input)):

        Equation = ''"
        
        Front = random.randint(0,18)
        FrontEquation = Container[Front:Front+random.randint(0,8)]

        
        
        Equation.update({'equation'+str(iteration+1):Equation})
                          
    
    
    
