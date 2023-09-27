c_major = ['C' ,'D'  ,'E'  ,'F'  ,'G' , 'A',  'B']
e_major = ['E' , 'F#', 'G#', 'A' , 'B' , 'C#', 'D#']
gflat_major = ['G#', 'A#', 'C' , 'C#', 'D#', 'F',  'G']

chords_count = 0

for note1 in c_major:
    for note2 in e_major:
        for note3 in gflat_major:
            print(note1 + '-' + note2 + '-' + note3)
            chords_count += 1

print(chords_count)