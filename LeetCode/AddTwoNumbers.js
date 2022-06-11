/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */

//위 조건에 주어진 대로 ListNode를 사용해야한다. 반환 값도 ListNode 형태로 반환해야함

var addTwoNumbers = function(l1, l2) {
    const node = new ListNode();
    let tmp = node;
    let carry = 0;
    
    while (l1 || l2 || carry){
        tmp.next = new ListNode();
        tmp = tmp.next;
        const left = l1?l1.val:0;
        const right = l2?l2.val:0;
        let sum = left+right+carry;
        const value = sum<10?sum:sum%10;
        carry = sum<10?0:1;
        tmp.val = value;
        l1 = l1?l1.next:null;
        l2 = l2?l2.next:null;
    }
    return node.next;
};
