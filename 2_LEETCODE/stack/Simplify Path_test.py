class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        paths = path.split("/")

        for cur in paths:
            if cur == "..":
                if stack:
                    stack.pop()
            elif cur != "" and cur != ".":
                stack.append(cur)

        return "/" + "/".join(stack)


if __name__ == "__main__":
    tests = [
        ("/neetcode/practice//...///../courses", "/neetcode/practice/courses"),
        ("/..//", "/"),
        ("/..//_home/a/b/..///", "/_home/a"),
    ]

    for path, expected in tests:
        ans = Solution().simplifyPath(path)
        assert ans == expected, f"Expected {expected}, got {ans}"
