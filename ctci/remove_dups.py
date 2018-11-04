def remove_dups(ll):
    unique = set()
    new_ll = []
    for ele in ll:
        if ele not in unique:
            unique.add(ele)
            new_ll.append(ele)
    return new_ll

"""
with ll lib installed

def remove_dups(head)
    unique = set()
    temp = head
    prev = None
    
    while temp != None:
        if temp in unique:
            prev.next = temp.next
        else:
            unique.add(temp)
            prev = temp 
            #prev only changes if we're not removing! b/c
            #when removing, the prev is not the one we just removed b/c it 
            #is non-existent
 
        temp = temp.next
"""

if __name__ == "__main__":
    ll = [4,5,1,2,2,4,4,7]
    ll = remove_dups(ll)
    print(ll)