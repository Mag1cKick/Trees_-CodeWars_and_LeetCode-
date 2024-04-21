def pre_order(node):
    res = []
    if node:
        res.append(node.data)
        res.extend(pre_order(node.left))
        res.extend(pre_order(node.right))
    return res

def in_order(node):
    res = []
    if node:
        res.extend(in_order(node.left))
        res.append(node.data)
        res.extend(in_order(node.right))
    return res

def post_order(node):
    res = []
    if node:
        res.extend(post_order(node.left))
        res.extend(post_order(node.right))
        res.append(node.data)
    return res
