from musicpy import *

c_major = scale('C', 'major')
e_major = scale('E', 'major')
gsharp_major = scale('G#', 'major')

chords = []

for note1 in c_major.notes:
    if c_major.notes.index(note1) == 7: continue
    for note2 in e_major.notes:
        if e_major.notes.index(note2) == 7: continue
        for note3 in gsharp_major.notes:
            if gsharp_major.notes.index(note3) == 7: continue
            chord_tmp = chord([note1, note2, note3], 1)
            print(alg.detect(chord_tmp))
            chords.append(chord_tmp)

# combined_chord = concat(chords, '|')

# play(combined_chord, bpm=100, instrument=1, wait=True)