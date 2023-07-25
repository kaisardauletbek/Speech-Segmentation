f = open("f_voices_to_check.txt", "r")
f_new = open("f_voices_to_check_edited.txt", "w")
for line in f:
    splits = line.split("_")
    line = f"{splits[0]}emale_{splits[1]}_00{splits[2]}"
    f_new.write(line)

f = open("m_voices_to_check.txt", "r")
f_new = open("m_voices_to_check_edited.txt", "w")
for line in f:
    splits = line.split("_")
    line = f"{splits[0]}ale_{splits[1]}_00{splits[2]}"
    f_new.write(line)
