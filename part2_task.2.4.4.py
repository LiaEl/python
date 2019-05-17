lines = []
with open("file_r.txt") as r, open("file_w.txt", "w") as w:
    for line in r:
        lines.append((line).rstrip())
    lines_str = "\n".join(lines[::-1])
    w.write(lines_str)
