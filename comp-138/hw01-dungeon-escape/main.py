# node class for a binary tree
class Node:
	def __init__(self, name):
		self.name = name
		self.left = None
		self.right = None

# I ordered the rooms in a way so they would appear in the proper order for appearing sequentially in a preorder traverse
rooms = {
	"A1": "\nA1: You are in a dark cave with only your wits to guide you...",
	"B1": "\nB1: You are standing in a shallow stream with glowing eels circling your heels. \nA breeze is coming from the left, but it smells horrible...",
	"C1": "\nC1: The ceiling here glows near the right exit.  It is beautiful, but something in the right tunnel is moving. CLOSER...",
	"D1": "\nD1: You see an opening. A possible escape?? Nooooo - the floor falls away into a dark abyss. \nAs your foot loses its grip, you wonder..should I perhaps have turned right?...\nYou have DIED.",
	"D2": "\nD2: Your tour guide emerges from the shadows, angry because the bus was supposed to leave 10 minutes ago... \nYou are SAVED!",
	"C2": "\nC2: There's a smell of sulfur here. And a distant booming drum beat. But which tunnel is it coming from?...",
	"D3": "\nD3: Orcs!!!!  You try to turn back, but they have blocked your escape.  At least you will not have to turn in your next assignment...\nYou have DIED.",
	"D4": "\nD4: The source of the booming reveals itself.  A cave troll beats its club against the wall and the ceiling above you collapses on your head.  If only you had worn that helmet...\nYou have DIED.",
	"B2": "\nB2: You suddenly feel intense hunger.  There's a skeleton here with a note.  It says: Avoid the Fish on Tuesdays...",
	"C3": "\nC3: A dark pool lies in the center of the cave.  As you aim your lantern into its depths, a giant tentacle wraps around your leg and pulls you down...\nYou have DIED.",
	"D5": None,
	"D6": None,
	"C4": "\nC4: You have entered a slanted room.  The floor tilts down to the left.  As if the cave WANTS you to go that way...",
	"D7": "\nD7: You slip onto a water slide that catapults out of the caverns to a sunlit river below.... \nYou are SAVED!",
	"D8": "\nD8: You have been climbed into a chamber of vampire bats.  You should have listened to the cave...\nYou have DIED."
}

roomNames = list(rooms.keys())

index = 0
# use preorder traversal to fill tree with room names
def create_tree(depth):
	global index
	if depth == 0:
		return
	node = Node(roomNames[index])
	index += 1
	node.left = create_tree(depth - 1)
	node.right = create_tree(depth - 1)
	return node

# start with root node
room = create_tree(4)
print("--- Dungeon Escape ---")

# keep taking user input until there are no nodes remaining
while room.left != None and room.right != None:
	if room.name == "C3": 
		break
	print(rooms[room.name])
	response = input("\nWhich way would you like to go (left or right)? ").lower()
	# validate user input
	while response != "left" and response != "right":
		response = input("Invalid input, only enter 'left' or 'right'. Try again... ")
	print("\nYou went " + response + "...")
	# traverse down the tree in the chosen direction
	if response == "left":
		room = room.left
	else:
		room = room.right

print(rooms[room.name])
