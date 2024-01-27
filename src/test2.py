from musicpy import *

c_minor = scale('C', 'minor')
dsharp_minor = scale('D#', 'minor')
fsharp_minor = scale('F#', 'minor')
asharp_minor = scale('A', 'minor')

# chords = []

with open('output.txt', 'w') as file:
    for note1 in c_minor.notes:
        if c_minor.notes.index(note1) == 7: continue
        for note2 in dsharp_minor.notes:
            if dsharp_minor.notes.index(note2) == 7: continue
            for note3 in fsharp_minor.notes:
                if fsharp_minor.notes.index(note3) == 7: continue
                for note4 in asharp_minor.notes:
                    if asharp_minor.notes.index(note4) == 7: continue
                    chord_tmp = chord([note1, note2, note3, note4], 1)
                    chord_name = alg.detect(chord_tmp)
                    text = '[' + str(note1) + ', ' + str(note2) + ', ' + str(note3) + ', ' + str(note4) + ']: ' + chord_name + '\n'
                    file.write(text)
                    # chords.append(chord_tmp)

print('Done!')

# combined_chord = concat(chords, '|')

# play(combined_chord, bpm=100, instrument=1, wait=True)