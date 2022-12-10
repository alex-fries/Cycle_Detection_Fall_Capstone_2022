
"""
Note: some of this code is copy and pasted from:
https://networkx.org/documentation/stable/reference/algorithms/bipartite.html

Converts a networkX bipartite graph into a graph usable by johnsons algoirhtm
"""
import networkx as nx
from networkx.algorithms import bipartite
import random

def graphCorrector(lyst, resourceSet):
    """
    Removes cycles of length 2
    """
    #print("Correcting graph")
    index = 0
    for sublist in lyst:
        for num in sublist:
            if index in lyst[num]: #trying to find cycles of length 2
                #print("Found a cycle less than two")
                #print("Index is " + str(index) + " and num is " + str(num))
                if index in resourceSet:
                    lyst[num].remove(index)
                else:
                    lyst[index].remove(num)

        index+=1

def removeExcessResourcePossessions(lyst, resourceSet):
    """
    Removes resources that are 'assigned' to multiple values
    """
    index = 0
    for sublist in lyst:
        if index in resourceSet:
            if len(sublist) > 1:
                for i in range(len(sublist), 1, -1):
                    sublist.remove(random.sample(sublist, 1)[0])
        index+=1



def generateNXGraph(numberOfProcesses, numberOfResources, edgeProbability):
    """
    Generates a graph to match the format necessary for the johnsonAlgorithm.py

    Returns a list of lists representing the graph, and a list contain verticies in the resource set
    """
    #numberOfProcesses = 5
    #numberOfResources = 5 #resources will have value [bipartite: 1]
    #edgeProbability = .7
    seed = None
    directed = True
    randomGeneratedGraph = bipartite.random_graph(numberOfProcesses, numberOfResources, edgeProbability, seed, directed)

    resourceSet = {n for n, d in randomGeneratedGraph.nodes(data=True) if d["bipartite"] == 1}
    #print(list(resourceSet)) #returns the values in the resource set

    compatableList = []

    index = 0
    for node, bi in randomGeneratedGraph.nodes(data=True):
        #print(randomGeneratedGraph.out_edges(node)) #G.in_edges gives the in-edges
        temporaryList = []
        for orderedPair in randomGeneratedGraph.out_edges(node):
            #returns a tuple
            #print(orderedPair[1])
            temporaryList.append(orderedPair[1])
        compatableList.append(temporaryList)
        #print("End of ordered pair")

    #print(compatableList)
    removeExcessResourcePossessions(compatableList, resourceSet)
    #print(compatableList)
    graphCorrector(compatableList, resourceSet)



    #print(compatableList)
    #print(resourceSet)

    return compatableList, resourceSet




    """
    #prints the nodes and what set they are in
    for n, d in randomGeneratedGraph.nodes(data=True):
        print(n,d)
    """
if __name__ == '__main__':
    generateNXGraph()