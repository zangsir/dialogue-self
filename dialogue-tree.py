import pickle
import os.path
import sys

class Tree:
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.cargo)

    def __repr__(self):
        return str(self.cargo)


def print_tree_indented(tree, level=0):
    if tree == None: return
    print_tree_indented(tree.right, level + 1)
    print('  ' * level + str(tree.cargo))
    print_tree_indented(tree.left, level + 1)


def yes(ques):
    ans = raw_input(ques).lower()
    return ans[0] == 'y'


def animal(stored_tree):
    # start with a singleton
    if os.path.isfile(stored_tree):
        root = pickle.load(open(stored_tree, 'r'))
    else:
        root = Tree("bird")

    # loop until the user quits
    while True:
        print

        if not yes("Are you thinking of an animal? "):
            tree=root
            pickle.dump(tree, open('saved_tree.pkl','w'))
            print 'bye!see you next time.'
            break

        # walk the tree
        # basically in the first round, the tree is at the root, so root is updated to be the first question that you add, and it keeps it that way. so in later rounds the root will remain the first question you added and it keeps expanding the sub left trees.
        tree = root
        # if you want to see the tree structure at this point, uncomment the next line and it will print tree structure sideways (turn your head 90 degrees left to visualize the tree in upright position)
        # print_tree_indented(tree)
        while tree.left is not None:
            prompt = tree.cargo + "? "
            if yes(prompt):
                tree = tree.right
            else:
                tree = tree.left

        # make a guess
        guess = tree.cargo
        prompt = "Is it a " + guess + "? "
        if yes(prompt):
            print("I rule!")
            continue

        # get new information
        prompt = "What is the animal's name? "
        animal = raw_input(prompt)
        prompt = "What question would distinguish a {0} from a {1}? "
        question = raw_input(prompt.format(animal, guess))

        # add new information to the tree
        tree.cargo = question
        prompt = "If the animal were {0} the answer would be? "
        if yes(prompt.format(animal)):
            tree.left = Tree(guess)
            tree.right = Tree(animal)
        else:
            tree.left = Tree(animal)
            tree.right = Tree(guess)
            # print_tree_indented(tree)


def main():
    stored_tree=sys.argv[1]
    animal(stored_tree)


if __name__ == '__main__':
    main()
