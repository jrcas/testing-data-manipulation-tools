import difflib

req = open("requirements.txt")
current = open("old_req.txt")

diff = difflib.ndiff(req.readlines(), current.readlines())
delta = "".join([x for x in diff if x.startswith("-")])

print(delta)
