import re
line="python programming is fun"
matchobj=re.match(r'fun',line)
searchobj=re.search(r'fun',line)
if matchobj:
    print("match found")
else:
    print("match not found")
if searchobj:
    print("match found")
else:
    print("match not found")
