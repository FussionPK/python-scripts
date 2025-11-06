def cat(a):
    with open(a, "r") as file: 
        print(file.read())

cat("openme.txt")

