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
                
    
                
                
            
        