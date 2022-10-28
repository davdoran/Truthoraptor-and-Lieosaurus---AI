# Project 2
# Davina Doran
# Nicholas Girmes
# Robin Khiv
# Nathan Mayne
from logic import *

ATruthoraptor = Symbol("A is a Truthoraptor")
ALieosaurus = Symbol("A is a Lieosaurus")

BTruthoraptor = Symbol("B is a Truthoraptor")
BLieosaurus = Symbol("B is a Lieosaurus")

CTruthoraptor = Symbol("C is a Truthoraptor")
CLieosaurus = Symbol("C is a Lieosaurus")

# Puzzle 0
# A says "I am both a Truthoraptor and a Lieosaurus."
knowledge0 = And(

    # Info given bye the structure of the problem
    # A cannot be both a Truthoraptor and a Lieosaurus
    Biconditional(ATruthoraptor, Not(ALieosaurus)),
    Biconditional(ALieosaurus, Not(ATruthoraptor)),

    # Info given bye the Dino's
    # If A is Truthoraptor then A is a Lieosaurus
    Implication(ATruthoraptor, ALieosaurus),

    # If A is a Lieosaurus then A is not a Truthoraptor
    Implication(ALieosaurus, Not(ATruthoraptor))

)

# Puzzle 1
# A says "We are both Lieosauruss."
# B says nothing.
knowledge1 = And(

    # Info given bye the structure of the problem
    # A cannot be both a Truthoraptor and a Lieosaurus
    Biconditional(ATruthoraptor, Not(ALieosaurus)),
    Biconditional(ALieosaurus, Not(ATruthoraptor)),

    # B cannot be both a Truthoraptor and a Lieosaurus
    Biconditional(BTruthoraptor, Not(BLieosaurus)),
    Biconditional(BLieosaurus, Not(BTruthoraptor)),

    # Info given bye the Dino's
    # If A is a telling the truth, then both A and B are a Lieosauraus
    Implication(ATruthoraptor, And(ALieosaurus, BLieosaurus)),

    # If A is NOT telling the truth, then A is A Lieousaurs and B is not a Lieosaurus
    Implication(Not(ATruthoraptor), And(ALieosaurus, Not(BLieosaurus)))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(

    # Info given byt the structure of the problem
    # A cannot be both a Truthoraptor and a Lieosaurus
    Biconditional(ATruthoraptor, Not(ALieosaurus)),
    Biconditional(ALieosaurus, Not(ATruthoraptor)),

    # B cannot be both a Truthoraptor and a Lieosaurus
    Biconditional(BTruthoraptor, Not(BLieosaurus)),
    Biconditional(BLieosaurus, Not(BTruthoraptor)),

    # Info given bye the Dino's
    # If A is a Truthoraptor then B is a Trutharaptor
    Implication(ATruthoraptor, BTruthoraptor),

    # If A is a Lieosaurus then B is Not a Lieosaurus
    Implication(ALieosaurus, Not(BLieosaurus)),

    # If B is a Truthoraptor then A is Not a Truthoraptor 
    Implication(BTruthoraptor, Not(ATruthoraptor)),

    # If B is a Lieosaurus then A is a Lieosaurus 
    Implication(BLieosaurus, ALieosaurus)
)

# Puzzle 3
# A says either "I am a Truthoraptor." or "I am a Lieosaurus.", but you don't know which.
# B says "A said 'I am a Lieosaurus'." 
# B says "C is a Lieosaurus."
# C says "A is a Truthoraptor."
knowledge3 = And(

    # Info given bye the structure of the problem
    # A cannot be both a Truthoraptor and a Lieosaurus
    Biconditional(ATruthoraptor, Not(ALieosaurus)),
    Biconditional(ALieosaurus, Not(ATruthoraptor)),

    # B cannot be both a Truthoraptor and a Lieosaurus
    Biconditional(BTruthoraptor, Not(BLieosaurus)),
    Biconditional(BLieosaurus, Not(BTruthoraptor)),

    # C cannot be both a Truthoraptor and a Lieosaurus
    Biconditional(CTruthoraptor, Not(CLieosaurus)),
    Biconditional(CLieosaurus, Not(CTruthoraptor)),


    # Info given bye the Dino's
    # A is either a Truthoraptor or I am a Lieosaurus, but not both
    Or(ATruthoraptor, ALieosaurus),

    # If B Truthoraptor and A Truthoraptor, then A is a Lieosaurus
    Implication(And(BTruthoraptor, ATruthoraptor), ALieosaurus),

    # If B Truthoraptor and A Lieosaurus, then A is Not a Lieosaurus
    Implication(And(BTruthoraptor, ALieosaurus), Not(ALieosaurus)),

    # If B Lieosaurus and A Truthoraptor, then A is Not a Lieosaurus
    Implication(And(BLieosaurus, ATruthoraptor), Not(ALieosaurus)),

    # If B Lieosaurus and A Lieosaurus, then A is a Lieosaurus
    Implication(And(BLieosaurus, ALieosaurus), ALieosaurus),

    # If B Truthoraptor then C is a Lieosaurus
    Implication(BTruthoraptor, CLieosaurus),

    # If B is Lieosaurus then C Not a Lieosaurus
    Implication(BLieosaurus, Not(CLieosaurus)),

    # If C Truthoraptor then A is a Truthoraptor
    Implication(CTruthoraptor, ATruthoraptor),

    # If C is Lieosaurus then C Not a Truthoraptor
    Implication(CLieosaurus, Not(ATruthoraptor))
)


def main():
    symbols = [ATruthoraptor, ALieosaurus, BTruthoraptor, BLieosaurus, CTruthoraptor, CLieosaurus]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
