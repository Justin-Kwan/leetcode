# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # optimal iterative merge sort approach
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        # keep merging lists until only final merged linked list remaining
        while len(lists) > 1:
            mergedLists = []

            # merge pairs of original or partially merged lists at current "tree level"
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = None if i + 1 >= len(lists) else lists[i + 1]
                mergedLists.append(self.mergeTwoLists(list1, list2))

            # replace list of linked lists with merged lists at current "tree level"
            # (number of merged lists reduces by half each time)
            lists = mergedLists

        return lists[0]

    def mergeTwoLists(self, list1: List[Optional[ListNode]], list2: List[Optional[ListNode]]) -> Optional[ListNode]:
        mergedHead = curHead = ListNode(-1)

        # keep merging while both lits still have nodes
        while list1 and list2:
            if list1.val < list2.val:
                curHead.next = list1
                list1 = list1.next
            else:
                curHead.next = list2
                list2 = list2.next

            curHead = curHead.next

        # add rest of a list's nodes to merged list once other is exhausted
        # since they're larger (usual case of one node left in one list)
        curHead.next = list2 if not list1 else list1
        return mergedHead.next

    # # optimal recursive merge sort approach
    # def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    #     if not lists:
    #         return None

    #     return self.mergeLists(lists, 0, len(lists) - 1)

    # def mergeLists(self, lists: List[Optional[ListNode]], startPos: int, endPos: int) -> Optional[ListNode]:
    #     # reached single list of nodes after splitting, return it to be merged
    #     if startPos == endPos:
    #         return lists[startPos]

    #     # partition to get partially merged left and right linked lists nodes from
    #     # subtrees and merge here
    #     middlePos = (startPos + endPos) // 2
    #     mergedLeftNodes = self.mergeLists(lists, startPos, middlePos)
    #     mergedRightNodes = self.mergeLists(lists, middlePos + 1, endPos)

    #     return self.mergeTwoLists(mergedLeftNodes, mergedRightNodes)

    # # min heap approach
    # def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    #     # order current layer of list heads to compare and find minimum
    #     sortedNodeLayer = []

    #     # load first layer of linked list heads into min heap to reach all
    #     # nodes in all lists (node value by index of list it's head of)
    #     for i in range(len(lists)):
    #         if lists[i]:
    #             heapq.heappush(sortedNodeLayer, (lists[i].val, i))

    #     # merged linked list pointer starts at dummy head
    #     mergedHead = curHead = ListNode(-1)

    #     # keep comparing nodes in layer and adding their next ones until all
    #     # list of nodes are exhausted
    #     while sortedNodeLayer:
    #         # pop next minimum node in current layer of comparison
    #         _, nodeListPos = heapq.heappop(sortedNodeLayer)
    #         minLayerNode = lists[nodeListPos]

    #         if minLayerNode.next:
    #             heapq.heappush(sortedNodeLayer, (minLayerNode.next.val, nodeListPos))
    #             # make minimum's next node the head of list at index, used once
    #             # popped later
    #             lists[nodeListPos] = minLayerNode.next

    #         curHead.next = minLayerNode
    #         curHead = curHead.next

    #     curHead.next = None
    #     return mergedHead.next
