import itertools

# class Skeleton:
#     def __init__(self, var1, var2):
#         self.var1 = var1
#         self.var2 = var2
    
#     def some_function(self):
#         # Add your function logic here
#         pass

# C C# D D# E F F# G G# A A# B

c_minor = ['C' ,'D'  ,'D#'  ,'F'  ,'G' , 'G#',  'A#']
dsharp_minor = ['D#', 'E#', 'F#' , 'G#', 'A#', 'B' , 'C#' ]
gflat_major = ['G#', 'A#', 'C' , 'C#', 'D#', 'F',  'G']

chords_count = 0

for note1 in c_minor:
    for note2 in dsharp_minor:
        for note3 in gflat_major:
            print(note1 + '-' + note2 + '-' + note3)
            chords_count += 1

print(chords_count)