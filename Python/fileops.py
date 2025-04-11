p = "/DSA/DSA_NOTES/Python/a_test.txt"
with open(p, 'r') as f:   #r is the file permission / f can be used as alias to perform file operations
    print(f.readlines())