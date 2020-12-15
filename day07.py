#   PART ONE    #
class BagGraph () :
    
    def __init__ (self, filepath) :
        self.dict = {} # will store data of form "Parent" : [(quantity, "child 1"), (quantity, "child 2"), ...]
        with open(filepath, "r") as file :
            temp = file.read().split("\n") 
            temp = [line.split(" contain ") for line in temp] #each entry is now ["parent", "child1, child2, etc..."]
            #   Now we format the the children to be tuples (quantity, childname). We also remove plurals and full stops from both parents and children
            for entry in temp :
                #   Remove plural from parents
                if entry[0].endswith("s") :
                    parent = entry[0][:-1]
                else:
                    parent = entry[0]

                #   If there are no children, store an empty list
                if entry[1] == "no other bags." :
                    children = [] # no children, the bag is an end bag
                else: # otherwise, remove plurals and full stops, then format into a tuple.
                    children = entry[1].split(", ")
                    for child in children :
                        quantity = int(child.split(" ")[0])
                        childname = " ".join(child.split(" ")[1:])
                        if childname.endswith(".") :
                            childname = childname[:-1]
                        if childname.endswith("s") :
                            childname = childname[:-1]
                        
                        if parent not in self.dict : # if we havent stored children of parent already
                            self.dict[parent] = [(quantity, childname)]
                        else:
                            self.dict[parent].append((quantity, childname)) # otherwise add to the list of children

    def get_containments (self, start, end, hierachy=[]) :
        hierachy = hierachy + [start]

        if start == end :
            return [hierachy]
        
        #   If the bag is not recognised, it cant have a hierachy
        if start not in self.dict :
            return []

        hierachies = []
        for quantity, childname in self.dict[start] :
            if childname not in hierachy :
                new_hierachy = self.get_containments(childname, end, hierachy)
                for h in new_hierachy :
                    hierachies.append(h)
        
        return hierachies 

    def get_all_containments (self) :
        all_hierachies = []
        for parent1 in self.dict.keys():
            for parent2 in self.dict.keys():
                all_hierachies.append(self.get_containments(parent1, parent2))  

        return all_hierachies

    def get_all_shiny_gold (self) :
        self.shiny_gold_containers = []
        for parent1 in self.dict.keys():
            self.shiny_gold_containers.append(self.get_containments(parent1, "shiny gold bag"))

        return self.shiny_gold_containers

    def count_shiny_gold_containers (self) :
        self.get_all_shiny_gold()
        count = 0
        checked_parents = []
        for parent_containments in self.shiny_gold_containers :
            for hierachy in parent_containments :
                if hierachy[0] in checked_parents :
                    pass
                elif hierachy[0] == "shiny gold bag":
                    pass
                else:
                    checked_parents.append(hierachy[0])
                    count += 1
        return count

part1 = BagGraph("day07input.txt")
print("\n")
print(f"The solution to Part One is {part1.count_shiny_gold_containers()}")


#   PART TWO    #

with open("day07input.txt", "r") as file:
    data = file.read().split("\n")

def get_bag_count(topbag) :
    #   The line of data that tells us what topbag contains, initially empty
    containment = ""

    for line in data :
        if line[:line.index(" bags")] == topbag: # find the line of data that starts with topbag (thus tells us what it contains)
            containment = line

    #   Check if we reached the final bag in the hierachy
    if "no" in containment:
        return 1

    containment = containment[containment.index("contain")+8:].split() # focus on the part of the line that tells us the containment, and then split into a list such that each bag contained takes up 4 indexes

    #   Now let's get the children of each child of topbag
    i = 0
    total_contained = 0

    while i < len(containment) :
        quant = containment[i]
        child = containment[1+i] + " " + containment[2+i] # ignore "bag" or "bags" suffixes

        total_contained += int(quant) * get_bag_count(child)
        

        i += 4

    return total_contained + 1 # +1 to include the topbag

print("The solution to Part Two is ", get_bag_count("shiny gold") - 1) # -1 to remove the very most top bag "shiny gold"

            
        
            
            





