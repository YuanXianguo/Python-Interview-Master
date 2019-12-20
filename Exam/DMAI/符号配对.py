def is_bool(str):
    map_ = {"(": ")", "{": "}", "[": "]"}
    stack = list()
    for s in str:
        if s in map_:
            stack.append(s)
        elif stack and s == map_.get(stack[-1], ""):
            stack.pop()
        else:
            return False
    if not stack:
        return True
    return False
