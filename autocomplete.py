
class Autocomplete:

    def __init__(self):
        self.__directAccess = []
        self.__root = self.TrieElement(None)

    def addFile(self,file,separator=','):
        with open(file,'r') as f:
            lines = f.readlines()
            for line in lines:
                items = line.split(separator)
                for item in items:
                    self.add(item)


    def add(self,item):
        item = item.rstrip('\n')
        if (self.contains(item)): 
            return
        else: 
            tree = self.__root;
            for c in item:
                subtree = tree.getChild(c)
                if subtree == None: 
                    subtree = self.TrieElement(c)
                    tree.addElement(subtree);
                tree = subtree;
            tree.setResult(item);
            self.__directAccess.append(item);   
    

    def contains(self,item):
        return item in self.__directAccess;

    def remove(self,item):
        self.__root.removeFromTree(item);
        self.__directAccess.remove(item)

    def search(self,item = None):
        found = self.__root;
        if (item != None):
            for c in item:
                found = found.getChild(c);
                if (found == None):
                    return None
        return self.__treeTraversal(found)

    def writeToFile(self,file,separator=','):
        with open(file,'w') as f:
            f.write(separator.join(self.__directAccess))

    def __treeTraversal(self,tree):
        leaves = []
        tree.getResultTree(leaves)
        return leaves    

    def __str__(self):
        return self.__directAccess.__str__()

    def __len__(self):
        return len(self.__directAccess)

    def __contains__(self,item):
        return self.contains(item)

    def __iter__(self):
        return self.__directAccess.__iter__()


    class TrieElement:
    
        def __init__(self,c):
            self.map = {}
            self.c = c
            self.result = None

        def addElement(self,child):
            self.map[child.c] = child

        def contains(self,c):
            return c in self.map

        def setResult(self,result):
            self.result = result

        def getResult(self):
            return self.result

        def getResultTree(self,dest): 
            if (self.result != None): 
                dest.append(self.result);
            for c in self.map:
                self.map[c].getResultTree(dest)

        def removeFromTree(self,item):
            for c in self.map:
                if (map[c].result == item):
                    del self.map[c]    

        def getChild(self,c):
            if c in self.map:
                return self.map[c]
            return None
    
