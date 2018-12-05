# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 17:55:52 2018

@author: Rohit
"""

class Node(object):
    
    def __init__(self, data):
        self.data = data;
        self.leftChild = None;
        self.rightChild = None;
        
class BinarySearchTree(object):
    
    def __init__(self):
        self.rootNode = None;
        
    def Insert(self, data):        
        if not self.rootNode:
            self.rootNode = Node(data);
        else:
            self.InsertNode(data, self.rootNode);
            
    # O(logN) if tree is balanced. Else, O(N)
    def InsertNode(self, data, node):        
        if data < node.data:
            if node.leftChild:
                self.InsertNode(data, node.leftChild);
            else:
                node.leftChild = Node(data);
        else:
            if node.rightChild:
                self.InsertNode(data, node.rightChild);
            else:
                node.rightChild = Node(data); 
                
    # Traverse in order, get the max and min in BST
    # getting the min value
    def GetMin(self):
        if self.rootNode:
            return self.GetMinValue(self.rootNode);
            
    def GetMinValue(self, node):
        if node.leftChild:
            return self.GetMinValue(node.leftChild);
        else:
            return node.data;
    
    # getting the max value
    def GetMax(self):
        if self.rootNode:
            return self.GetMaxValue(self.rootNode);
            
    def GetMaxValue(self, node):
        if node.rightChild:
            return self.GetMaxValue(node.rightChild);
        else:
            return node.data;
        
    # in-order traversal
    def traverseInOrder(self):
        if self.rootNode:
            self.Traverse(self.rootNode);
            
    def Traverse(self, node):
        if node.leftChild:
            self.Traverse(node.leftChild);
            
        print(node.data);
        
        if node.rightChild:
            self.Traverse(node.rightChild);
            
# Testing
            
# with digits            
bst = BinarySearchTree()
bst.Insert(10);
bst.Insert(5);
bst.Insert(15);
bst.Insert(6);

print(bst.GetMin());
print(bst.GetMax());
bst.traverseInOrder();

# =============================================================================
# # with alphabets
# bst.Insert("A");
# bst.Insert("Z");
# bst.Insert("D");
# bst.Insert("H");
# bst.traverseInOrder();            
# =============================================================================
                
                
            
        