def tree_by_levels(node):
    if not node:
        return []
    res = [node]
    prev_res = []
    while True:
        for i in res:
            if i:
                if i.left not in res:
                    if i.left:
                        res.append(i.left)
                if i.right not in res:
                    if i.right:
                        res.append(i.right)
        half_res = [i.value for i in res]
        if half_res == prev_res:
            break
        prev_res = half_res
    return prev_res
