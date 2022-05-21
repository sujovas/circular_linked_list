class Node:
    def __init__(self, dat = None, nxt_node = None):

        #self.dat = None
        #self.nxt_node = None 

        self.dat = dat
        self.nxt_node = nxt_node
        

class CLR:

    def __init__(self, head = None, end = None):

        self.head = head
        self.end = end
        #self.size = 0 nope..
       

    def move(self):
        #  first node - current node
        c_node = self.head

### circle linked loop 1st time use

        while c_node.nxt_node:
            #print dat
            print(c_node.dat)
            c_node = c_node.nxt_node
            #through loop back to the head then break
            if c_node == self.head:
                break

## counter
    def move_count(self):
        #  first node
        c_node = self.head
        counter=0

        while c_node.nxt_node:
            c_node = c_node.nxt_node
            counter=counter+1
            if c_node == self.head:
                print(counter)
                break

#insert to the begginning fcn
    def ins_beg(self, dat):
        new_node = Node(dat)
        new_node.nxt_node = self.head
        c_node = self.head

        #if empty list
        if c_node == None:
            self.head = new_node
            self.end = new_node
            self.head.nxt_node = new_node
            return

        #if non empty list
        if self.end != None:
            self.end.nxt_node = new_node
            new_node.nxt_node = self.head
            self.head = new_node
            return

#insert to the end fcn
    def ins_end(self, dat):
        new_node = Node(dat)

        #if empty
        if self.head == None:
            self.head = new_node
            self.head.nxt_node = new_node
            self.end = new_node
            return

        #if not empty
        if self.end != None:
            self.end.nxt_node = new_node
            new_node.nxt_node = self.head
            self.end = new_node
            return


#delete head - 1.st            
    def del_beg(self):
        #  first node
        c_node = self.head
#        print('Head node:')
#        print(c_node)
#        print(c_node.dat)
#        print('2nd node:')
#        print(c_node.nxt_node)
#        print(c_node.nxt_node.dat)
        print('Deleting head node:')
        print('New head node:')
        self.head=c_node.nxt_node
#       print(self.head)
        print(self.head.dat)
        self.end.nxt_node=self.head

 #delete end - Last             -  so much fun...
    def del_end(self):
        #  first node
        c_node = self.head
        
        while c_node.nxt_node:
            c_node = c_node.nxt_node
            c_node1 = c_node.nxt_node
            
            #through loop back to the head then break
            if c_node1 == self.end:
                self.end=c_node
                self.end.nxt_node=self.head
                break


        print('Deleting end node:')
        print('New end node:')
#       print(self.end)
        print(self.end.dat)
      


#test in terminal - insert 5 nodes, print list, delete head, new head, new list, delete end, new end, new list...
def main():
    circ_lst = CLR()

#insert 5 nodes
    circ_lst.ins_beg (20)
    circ_lst.ins_beg (30)
    circ_lst.ins_beg (40)
    circ_lst.ins_beg (50)
    circ_lst.ins_end (100)

#terminal print of initial circular linked list
    print('Circular linked list')
    circ_lst.move()
    print('Count of mebers')
    circ_lst.move_count()
#deleting head and terminal print of deleting head of circular linked list    
    circ_lst.del_beg()
    print('New Circular linked list')
    circ_lst.move()
    print('Count of mebers')
    circ_lst.move_count()
#deleting end and terminal print of deleting head of curcular linked list
    circ_lst.del_end()
    print('New Circular linked list')
    circ_lst.move()
    print('Count of mebers')
    circ_lst.move_count()


if __name__=="__main__":
    main()