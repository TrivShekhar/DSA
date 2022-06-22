import java.util.Stack;
class Node{
    public Node left = null;
    public Node right =null;
    public int data;
    public Node(int data) {
        this.data = data;
    }
}
class BinaryTree {
    public Node Treeroot=null;
    public void insert(int data,Node root){
        if(root==null){
            Treeroot = new Node(data);
        }
        else{
            if(root.data>data){
                if(root.left==null){
                    root.left = new Node(data);
                    return;
                }
                else{
                    insert(data,root.left);
                }
            }
            if(root.data<data){
                if(root.right==null){
                    root.right = new Node(data);
                    return;
                }
                else{
                    insert(data,root.right);
                }
            }
        }

    }
    public int height(Node root){
        if(root==null){
            return 0;
        }
        else{
            int leheight= height(root.left);
            int riheight= height(root.right);
            if(leheight>riheight){
                return leheight+1;
            }
            else{
                return riheight+1;
            }
        }

    }
    public void inorderTraverse(Node root){
        if(root!=null){
            inorderTraverse(root.left);
            System.out.print(" "+root.data);
            inorderTraverse(root.right);
        }
    }
    
    public void preorderTraverse(Node root){
        if(root!=null){
            
            System.out.print(" "+root.data);
            preorderTraverse(root.left);
            preorderTraverse(root.right);
        }
    }
    
    public void postorderTraverse(Node root){
        if(root!=null){
            postorderTraverse(root.left);
            postorderTraverse(root.right);
            System.out.print(" "+root.data);
        }
    }
    public void iterpreorderTraverse(){
        Stack<Node> nodeStack = new Stack<Node>();
        Node root = Treeroot;
        nodeStack.push(root);
        while(!nodeStack.isEmpty()){
            Node newNode = nodeStack.pop();
            System.out.print(" "+newNode.data);
            if(newNode.right!=null){
                nodeStack.push(newNode.right);
            }
            if(newNode.left!=null){
                nodeStack.push(newNode.left);
            }
        }
    }
    public void iterinorderTraversal(){
        Stack<Node> nodeStack = new Stack<Node>();
        Node curr = Treeroot;
        while(!nodeStack.isEmpty() || curr!=null){
            while(curr!=null){
                nodeStack.push(curr);
                curr=curr.left;
            }
            Node topnode = nodeStack.pop();
            System.out.print(" "+topnode.data);
            if(topnode.right!=null){
                curr=topnode.right;
            }
        }
    }
    public void iterPostorderTraversal(){
        Stack<Node> nodestack = new Stack<Node>();
        Stack<Node> resultstack = new Stack<Node>();
        Node curr;
        nodestack.push(Treeroot);
        while(!nodestack.isEmpty()){
            curr = nodestack.pop();
            resultstack.push(curr);
            if(curr.left!=null){
                nodestack.push(curr.left);
            }
            if(curr.right!=null){
                nodestack.push(curr.right);
            }
        }
        while(!resultstack.isEmpty()){
            System.out.print(" "+resultstack.pop().data);
        }
    }
}
public class Main{
    public static void main(String[] args) {
        BinaryTree tree = new BinaryTree();
        int[] arr ={50,4,55,43,96,32,76,9,1,2,6,57,300};
        for (int a : arr){
            tree.insert(a, tree.Treeroot);
        }
        
        tree.inorderTraverse(tree.Treeroot);
        System.out.println();
        tree.iterinorderTraversal();
        System.out.println();
        tree.iterpreorderTraverse();
        System.out.println();
        tree.preorderTraverse(tree.Treeroot);
        System.out.println();
        tree.postorderTraverse(tree.Treeroot);
        System.out.println();
        tree.iterPostorderTraversal();
    }
}