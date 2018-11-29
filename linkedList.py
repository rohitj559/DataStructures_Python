# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 18:33:40 2018

@author: Rohit
"""
# distinct class for nodes in the linkedlist
class Node(object):
    
    def __init__(self, data):
        self.data = data;
        self.nextNode = None;
        
class LinkedList(object):
    
    def __init__(self):
        self.head = None;
        self.size = 0;
        
    def insertStart(self, data):
        self.size = self.size + 1;
        newNode = Node(data);
        
        # if head is None(Null)
        if not self.head:
            self.head = newNode;
        else:
            newNode.nextNode = self.head;
            self.head = newNode;
            
    def remove(self, data):
        
        if self.head is None:
            return;
            
        self.size = self.size - 1;
        
        currentNode = self.head;
        previousNode = None;
        
        while currentNode.data != data:
            previousNode = currentNode;
            currentNode = currentNode.nextNode;
            
        if previousNode is None:
            self.head = currentNode.nextNode;
        else:
            previousNode.nextNode = currentNode.nextNode;           
        
            
    def size1(self):
        
        return self.size;
    
    def size2(self):
        
        actualNode = self.head;
        size = 0;
        
        while actualNode is not None:
            size+=1;
            actualNode = actualNode.nextNode;
            
        return size
            
    def insertEnd(self, data):
        
        self.size = self.size + 1;
        newNode = Node(data);
        actualNode = self.head;
        
        while actualNode.nextNode is not None:
            actualNode = actualNode.nextNode;
            
        actualNode.nextNode = newNode;
        
    def traverseList(self):
        
        actualNode = self.head;
        
        while actualNode is not None:
            print("%d" % actualNode.data);
            actualNode = actualNode.nextNode;
            
linkedlist = LinkedList();

linkedlist.insertStart(12);
linkedlist.insertStart(122);
linkedlist.insertStart(3);
linkedlist.insertStart(31);

linkedlist.insertEnd(5);

linkedlist.traverseList();

print(linkedlist.size1());

linkedlist.remove(31);
linkedlist.remove(3);
linkedlist.remove(122);
linkedlist.remove(12);

print(linkedlist.size1());

linkedlist.remove(5);

print(linkedlist.size1());





