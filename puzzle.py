from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

DKnight = Symbol("D is a Knight")
DKnave = Symbol("D is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # Structural constraints
    Or(AKnight, AKnave),  # A is either a knight or knave
    Not(And(AKnight, AKnave)),  # A is not both
    
    # If A is a knight, then A's statement "I am both knight and knave" is true
    Implication(AKnight, And(AKnight, AKnave)),
    
    # If A is a knave, then A's statement "I am both knight and knave" is false  
    Implication(AKnave, Not(And(AKnight, AKnave)))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # Structural constraints
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),

    # Structural constraints
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),

    # A says "We are both knaves"
    # If A is knight (tells truth), then the statement is true
    Implication(AKnight, And(AKnave, BKnave)),

    # If A is knave (lies), then the statement is false
    Implication(AKnave, Not(And(AKnave, BKnave)))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # Structural constraints for A
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    
    # Structural constraints for B
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    
    # A says "We are the same kind"
    Implication(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    Implication(AKnave, Not(Or(And(AKnight, BKnight), And(AKnave, BKnave)))),
    
    # B says "We are of different kinds"  
    Implication(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight))),
    Implication(BKnave, Not(Or(And(AKnight, BKnave), And(AKnave, BKnight))))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
ASaidKnight = And(Implication(AKnight, AKnight), Implication(AKnave, Not(AKnight)))
ASaidKnave = And(Implication(AKnight, AKnave), Implication(AKnave, Not(AKnave)))
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # Structural constraints for A
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    
    # Structural constraints for B
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),

    # Structural constraints for C
    Or(CKnight, CKnave),
    Not(And(CKnight, CKnave)),

    # Either A said "I am a knight" OR A said "I am a knave"
    Or(ASaidKnight, ASaidKnave),

    # B says "A said 'I am a knave'"
    Implication(BKnight, ASaidKnave),
    Implication(BKnave, ASaidKnight),

    # B says "C is a knave"  
    Implication(BKnight, CKnave),
    Implication(BKnave, CKnight),

    # C says "A is a knight"
    Implication(CKnight, AKnight),
    Implication(CKnave, AKnave)
)

# Puzzle 4
#A says "B is a Knave"
#B says "C is a Knave"
#A says "C is a Knight or I am a Knave"
knowledge4 = And(
    # Structural constraints for A
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    
    # Structural constraints for B
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),

    # Structural constraints for C
    Or(CKnight, CKnave),
    Not(And(CKnight, CKnave)),

    Implication(AKnight, BKnave),
    Implication(AKnave, BKnight),

    Implication(BKnight, CKnave),
    Implication(BKnave, CKnight),

    Implication(AKnight, Or(AKnave, CKnight)),
    Implication(AKnave, Not(Or(AKnave, CKnight)))
)

# Puzzle 5
#A says "B always tells the truth",
#B says "C is a Knight",
#C says "A is truthful",
#D says "C is a Knave and I am a Knave"
knowledge5 = And(
    # Structural constraints for A
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    
    # Structural constraints for B
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),

    # Structural constraints for C
    Or(CKnight, CKnave),
    Not(And(CKnight, CKnave)),

    # Structural constraints for D
    Or(DKnight, DKnave),
    Not(And(DKnight, DKnave)),

    Implication(AKnight, BKnight),
    Implication(AKnave, BKnave),

    Implication(BKnight, CKnight),
    Implication(BKnave, CKnave),

    Implication(CKnight, AKnight),
    Implication(CKnave, AKnave),

    Implication(DKnight, And(CKnave, DKnave)),
    Implication(DKnave, Not(And(CKnave, DKnave)))
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave, DKnight, DKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3),
        ("Puzzle 4", knowledge4),
        ("Puzzle 5", knowledge5)
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
