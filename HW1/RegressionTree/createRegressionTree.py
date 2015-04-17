from splitData import splitData;
from treeNode import Node;
from getTreeVal import getTreeNodeVal;

def createRegressionTree(traindata, treenode, depth):
    if( len(traindata) == 1 ):
            getTreeNodeVal(traindata, treenode);
            
    elif( treenode.depth <= depth):
            (left, right, treenode_update) = splitData(traindata, treenode);
            
            treenode_update.left = Node();
            treenode_update.left.depth = treenode_update.depth;
            createRegressionTree(left, treenode_update.left, depth);
        
            treenode_update.right = Node();
            treenode_update.right.depth = treenode_update.depth;
            createRegressionTree(right, treenode_update.right, depth);
    elif( len(traindata) > 0 ):
            getTreeNodeVal(traindata, treenode);
