# dialogue-self
<i>code related to dialogue systems</i>

## dialogue-tree
A game similar to '20-questions' where it asks you questions to guess what animal you're thinking of. A binary (Y/N) dialogue system based on a tree, this system asks you a series of questions and if it doesn't get the right answer, it asks additional questions to learn from you so that the next time it knows the answer to the animal. The learned tree will be saved in a pickle file as you exit the system. Sample usage:

<code>python dialogue-tree.py saved_tree.pkl</code>
