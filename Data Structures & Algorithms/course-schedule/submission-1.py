class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        pre_req_map = {i:[] for i in range(numCourses)}
        for course, pre in prerequisites:
            pre_req_map[course].append(pre)
        visiting= set()

        def dfs(course):
            if course in visiting:
                return False
            if pre_req_map[course] == []:
                return True
            visiting.add(course)
            for pre in pre_req_map[course]:
                if not dfs(pre):
                    return False
            visiting.remove(course)
            pre_req_map[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
        