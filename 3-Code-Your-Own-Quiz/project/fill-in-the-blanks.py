TEXT_EASY = "Computer __1__ is a process that leads from an original formulation\nof a computing problem to executable computer programs. __1__ involves\nactivities such as analysis, developing understanding, generating __2__,\nverification of requirements of __2__ including their correctness and\nresources consumption, and implementation (commonly referred to as coding) of\n__2__ in a target __1__ language. Source __3__ is written in one or\nmore __1__ languages. The purpose of __1__ is to find a sequence of\ninstructions that will automate performing a specific task or solving a given\nproblem. The process of __1__ thus often requires expertise in many different\nsubjects, including knowledge of the application domain, specialized __2__,\nand formal __4__."
TEXT_MEDIUM = "__1__ science, also known as __1__-driven science, is an interdisciplinary field\nabout scientific methods, processes, and systems to extract knowledge or insights\nfrom __1__ in various forms, either structured or unstructured, similar to __1__ mining.\n__1__ science is a \"concept to unify statistics, __1__ analysis and their related methods\"\nin order to \"understand and analyze actual phenomena\" with __1__. It employs techniques\nand theories drawn from many fields within the broad areas of __2__, statistics,\ninformation science, and computer science, in particular from the subdomains of __3__\nlearning, classification, cluster analysis, __1__ mining, __1__bases, and visualization.\nTuring award winner Jim Gray imagined __1__ science as a \"fourth paradigm\" of science\n(empirical, theoretical, computational and now __1__-driven) and asserted that \"everything\nabout science is changing because of the impact of information __4__\" and the __1__\ndeluge."    
TEXT_HARD = "Modern __1__ learning provides a powerful framework for supervised learning.By adding more\n__2__s and more units within a __2__, a __1__ network can representfunctions of increasing\ncomplexity. Most tasks that consist of mapping an input __3__ to an output __3__, and that\nare easy for a person to do rapidly, can be accomplished via __1__ learning, given sufficiently\nlarge models and sufficiently large datasets of labeled __4__ examples. Other tasks, that\ncannot be described as associating one __3__ to another, or that are difficult enough that a\nperson would require time to think and reflect in order to accomplish the task, remain beyond\nthe scope of __1__ learning for now\nIn summary, __1__ learning is an approach to __5__ learning that has drawn heavily on our\nknowledge of the human __6__, statistics and applied math as it developed over the past several\ndecades. In recent years, __1__ learning has seen tremendous growth in its popularity and usefulness,\nlargely as the result of more powerful computers, larger __7__ and techniques to train __1__er\nnetworks. The years ahead are full of challenges and opportunities to improve __1__ learning\nevenfurther and to bring it to new frontiers."
    
TEXTS = {
    "easy": TEXT_EASY,
    "medium": TEXT_MEDIUM,
    "hard": TEXT_HARD}

LEVELS = ["easy", "medium", "hard"]
TRIES = 5
BLANKS = {
    "easy":["__1__", "__2__", "__3__", "__4__"],
    "medium": ["__1__", "__2__", "__3__", "__4__"],
    "hard": ["__1__", "__2__", "__3__", "__4__", "__5__", "__6__", "__7__"]}

ANSWERS = {
    "easy": ["programming", "algorithms", "code", "logic"],
    "medium": ["data", "mathematics", "machine", "technology"],
    "hard": ["deep", "layer", "vector", "training", "machine", "brain", "datasets"]}    
        
def update_text(text, blank, ans):    
    """update text with provided answer
    
    This function updates the text by replacing the blank (like "__3__") with the 
    correct ans (like "vector")
    
    arguments:
        text: string, a long string of the text
        blank: string, a short string representing the numbered blank like "__3__"
        ans: string, a short string representing the correct answer for the blank
    return:
        string, the updated text
    """
    replaced = []
    text = text.split()
    for word in text:
        if blank in word:
            replaced.append(word.replace(blank, ans))
        else:
            replaced.append(word)
    return " ".join(replaced)
    
def get_user_level():
    user_level = input("Please select a game difficulty by typing it in!\nPossible choices include easy, medium, and hard.\n")
    while user_level not in LEVELS:
        user_level = input("That's not an option!\nPlease select a game difficulty by typing it in!\nPossible choices include easy, medium, and hard.\n")
    print("You've Chosen " + user_level + "!\n\n" + "You will get " + str(TRIES) + " guesses per problem")
    return user_level
    
def play_game():
    """play the game of guessing words
    
    This function plays the game of guessing words. The player first chooses
    from three levels (easy, medium, hard), then start to guess. If correct,
    then start to guess next word, otherwise try to guess the word again.
    """
    user_level = get_user_level()
    blanks, text, answer = BLANKS[user_level], TEXTS[user_level], ANSWERS[user_level]
    not_finish, tries_left, current_number = True, TRIES, 1
    while not_finish and tries_left > 0:
        print("The current paragraph reads as such:\n" + text + "\n\n")
        user_input = input("What should be substituted in for" + blanks[current_number-1] + "?")
        if user_input.lower() == answer[current_number-1].lower():
            print("Correct!\n\n")
            text = update_text(text, blanks[current_number-1], answer[current_number-1])
            current_number += 1
            if current_number == len(blanks) + 1:
                print(text)
                not_finish = False
        else:
            tries_left -= 1
            print("That isn't the correct answer! Let's try again; you have " + str(tries_left) +" trys left!\n\n")
    print("The answer is " + " ".join(answer))
    
if __name__ == "__main__":
    play_game()