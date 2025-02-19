/* 
In an exam room, there are N seats in a single row, numbered 0, 1, 2, ..., N-1.

When a student enters the room, they must sit in the seat that maximizes the distance to the closest person.  If there are multiple such seats, they sit in the seat with the lowest number.  (Also, if no one is in the room, then the student sits at seat number 0.)

Return a class ExamRoom(int N) that exposes two functions: ExamRoom.seat() returning an int representing what seat the student sat in, and ExamRoom.leave(int p) representing that the student in seat number p now leaves the room.  It is guaranteed that any calls to ExamRoom.leave(p) have a student sitting in seat p.

 

Example 1:

Input: ["ExamRoom","seat","seat","seat","seat","leave","seat"], [[10],[],[],[],[],[4],[]]
Output: [null,0,9,4,2,null,5]
Explanation:
ExamRoom(10) -> null
seat() -> 0, no one is in the room, then the student sits at seat number 0.
seat() -> 9, the student sits at the last seat number 9.
seat() -> 4, the student sits at the last seat number 4.
seat() -> 2, the student sits at the last seat number 2.
leave(4) -> null
seat() -> 5, the student​​​​​​​ sits at the last seat number 5.
​​​​​​​

Note:

1 <= N <= 10^9
ExamRoom.seat() and ExamRoom.leave() will be called at most 10^4 times across all test cases.
Calls to ExamRoom.leave(p) are guaranteed to have a student currently sitting in seat number p.
===================================================================
*/
// 2018-8-30
// 855. Exam Room
// https://leetcode.com/problems/exam-room/description/

class ExamRoom {
public:
    int last_seat;
    set<int> room_seat;
    ExamRoom(int N) {
        last_seat = N - 1;
    }
    
    int seat() {
        if(room_seat.size() == 0){
            room_seat.insert(0);
            return 0;
        }
        int i = 0;
        auto it = room_seat.begin();
        int pre_seat = *it;
        // 如果位置0被移除了,则最大距离就是 pre_seat - i。 若没有被移除则距离为0
        int distance = pre_seat - i;
        for(; it != room_seat.end(); it++){
            if((*it - pre_seat) / 2 > distance) {
                    distance = (*it - pre_seat) / 2;
                    i = pre_seat + distance;
                }
            pre_seat = *it;
        }
        // 最后一个位置没有坐人的情况则distance不会超过 last_seat - pre_seat
        if(last_seat - pre_seat > distance) i = last_seat;
        room_seat.insert(i);
        return i;
    }
    
    void leave(int p) {
        room_seat.erase(p);
    }
};

/**
 * Your ExamRoom object will be instantiated and called as such:
 * ExamRoom obj = new ExamRoom(N);
 * int param_1 = obj.seat();
 * obj.leave(p);
 */