class StationaryItems:

    def __init__(self,item1,item2=None,item3=None):
        self.Item1 = item1
        self.Item2 = item2
        self.Item3 = item3

    def display_info(self):
        print("Stationary item_1: " + self.Item1)
        print("Stationary item_2: " + self.Item2)
        print("Stationary item_3: " + self.Item3)

Items = StationaryItems("Pencil","Pen","NoteBook")

Items.display_info()

