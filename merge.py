class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key= lambda x: x[0])
        new = []
        l,r = intervals[0][0],intervals[0][1]
        appended = False
        for i in range(1,len(intervals)):
            # if appended:
            #     l,r = intervals[i][0],intervals[i][1]
            #     appended = False
                
            if intervals[i][0] <= r :
                r = max(intervals[i][1],r)
            else:
                appended = True
                new.append([l,r])
                l,r = intervals[i][0],intervals[i][1]
            # print(i,l,r)
        new.append([l,r])
        return new