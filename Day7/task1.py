f = open('input.txt',mode='r')
data = f.readlines()

class Node():
    def __init__(self,letter):
        self.letter = letter
        self.fathers = []
        self.sons = []
        self.available = False
        self.done = False

all_nodes = []
for d in data:
    earlier_letter = d[5]
    later_letter = d[-13]
    print(earlier_letter, later_letter)
    father_exist = False
    for i in range(len(all_nodes)):
        if all_nodes[i].letter == earlier_letter:# father node exist
            all_nodes[i].sons.append(later_letter)
            father_exist = True
            break
    if not father_exist:# father node does not exist
        tmp_nodeA = Node(earlier_letter)
        tmp_nodeA.sons.append(later_letter)
        all_nodes.append(tmp_nodeA)
    son_exist = False
    for i in range(len(all_nodes)):
        if all_nodes[i].letter == later_letter:# son node exist
            all_nodes[i].fathers.append(earlier_letter)
            son_exist = True
            break
    if not son_exist:
        tmp_nodeB = Node(later_letter)
        tmp_nodeB.fathers.append(earlier_letter)
        all_nodes.append(tmp_nodeB)
class Tree():
    def __init__(self):
        self.nodes = {}
        self.root = ""
        self.top = ""
        self.available_list = []
tree = Tree()

for node in all_nodes:
    tree.nodes[node.letter] = node
    if len(node.fathers)==0:
        tree.root = node.letter
        tree.nodes[tree.root].available = True
    if len(node.sons)==0:
        tree.top = node.letter
# tree done
final_list = ""

def update_available_list(tree):
    for node in tree.nodes:
        all_fathers_done = True
        for father in tree.nodes[node].fathers:
            if not tree.nodes[father].done:
                all_fathers_done = False
        if all_fathers_done and not tree.nodes[node].done:
            tree.nodes[node].available = True
            if node not in tree.available_list:
                tree.available_list.append(node)
    return tree
while True:
    tree = update_available_list(tree)
    print('len:',len(tree.available_list),tree.available_list)
    if len(tree.available_list) == 0:
        break
    tree.available_list.sort()
    final_list+=tree.available_list[0]
    tree.nodes[tree.available_list[0]].done = True
    del tree.available_list[0]

print(final_list)