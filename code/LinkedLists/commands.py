from single import LinkedList

ll = LinkedList()

[ll.InsertEnd(i+1) for i in range(10)]
ll.InsertStart(0)
ll.InsertIndex(2, "new Value")

ll.DeleteEnd()
ll.DeleteStart()
ll.DeleteIndex(1)
ll.DeleteFound("new Value")
# ll.DeleteList()

ll.InsertIndex(5, "find me")
ll.Display()

print(ll.ListLengthI())
print(ll.ListLengthR(ll.head))

print(ll.SearchI("find me"))
print(ll.SearchR(ll.head, "find me"))

# ll.ReturnIndexI(5)
print('')
ll.ReturnIndexR(ll.head, 5)

