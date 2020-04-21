"""
Draw/model out enqueuing into a queue that uses a linked list as its underlying storage structure.

Draw/model out dequeuing from a queue that uses a linked list as its underlying storage structure.
"""

# enqueuing into a queue that uses a linked list as its underlying storage structure.
"""
- Create an linked list with one node.
- Create a function that adds new entries.  New entries will be the head of the linked list, new_value.next will point to the former_head.  The former_head.prev will point to the new_value, the former.head.next will point to None - it is the new tail.
"""

# dequeuing from a queue that uses a linked list as its underlying storage structure.
"""
- Create an linked list with two or more nodes.
- Create a function that removes the latest entries.  New entries will be removed from the head of the linked list, new_value.prev will point None, new_value.prev will point to None.  The former_head.prev will point to None (as the new head), the former.head.next will point to the entry after it.  The last_entry.next will point to None as the new tail.
"""