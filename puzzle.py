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
    # TODO
    # A cannot be both a Truthoraptor and a Lieosaurus, therefore they must be a Lieosaurus
    Symbol(ALieosaurus)
)

# Puzzle 1
# A says "We are both Lieosauruss."
# B says nothing.
knowledge1 = And(
    # TODO
    # Since A is a Lieosaurus then the statement "We are both Lieosauruss" cannot be true, therefore -(A^B)
    Implication(Symbol(ALieosaurus), Not(Symbol(BLieosaurus)))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # TODO
    # Since A is a Lieosaurus then they cannot be the same
    Or(Symbol(ALieosaurus), Symbol(BLieosaurus)), 
    Or(Symbol(ATruthoraptor), Symbol(BTruthoraptor))
)

# Puzzle 3
# A says either "I am a Truthoraptor." or "I am a Lieosaurus.", but you don't know which.
# B says "A said 'I am a Lieosaurus'." (If A is lie, and B cannot be the same as A, then B is truth, but this statement does not make sense with that logic?)
# B says "C is a Lieosaurus."
# C says "A is a Truthoraptor."
knowledge3 = And(
    # TODO
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