# This file should not exist…
f = open("testing_file.txt", "x")
f.close()

# We created this file earlier…
f = open("test_file.txt", "x")
f.close()