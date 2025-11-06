# x = "aaabbbbcccddeee"
# i = 0
# while (i< len(x)):
#     count = 0
#     end = len(x)
#     for j in range(i+1,len(x)):
#         if x[i] == x[j]:
#             c = c + 1
#         else:
#             end = j
#             break
#     print(i,x[i], count, sep='|', end=' - ')
#     i = end
    

# seasons = 5
# episodes = 10
# episodeTime_season1 = 2735
# episodeTime_rest = 2115

# # Season 1 time
# TotalSeason1Time = episodeTime_season1 * episodes
# print(f"The total time in season one is {TotalSeason1Time} seconds")

# # Seasons 2–5 time (4 seasons)
# TotalRestTime = episodeTime_rest * episodes * (seasons - 1)
# print(f"The total time in the rest of the seasons is {TotalRestTime} seconds")

# # Total show time
# TotalShowTime = TotalSeason1Time + TotalRestTime
# print(f"The whole show is {TotalShowTime} seconds long")

# # Convert to hhmmss
# Hours = TotalShowTime // 3600
# remaining = TotalShowTime % 3600
# minutes = remaining // 60
# seconds = remaining % 60

# print(f"Total Time: {Hours}h {minutes}m {seconds}s")


# # Your code here
# IP = input("Please input your IP: ")
# Method = str(input("What method do you want to use: "))
# Path = str(input("What is the desired path: "))
# Status = int(input("What is the status code: "))
# Bytes = int(input("What is the size in bytes: "))

# print(f"{IP} - \"{Method} {Path}\" {Status} {Bytes}")

from pathlib import Path
p = Path("/usr/local/bin/python.exe")
print(f"\n{p.name}")
print(p.suffix)
print(p.suffixes)
print(p.stem)
print(p.parent)
print(list(p.parents))
print(p.anchor)
print(p.root)
print(p.drive)