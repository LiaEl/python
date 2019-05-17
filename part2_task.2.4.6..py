import os
import os.path

adrs = []
with open ("sample_ans.txt", 'w') as f:
    for current_dir, dirs, files in os.walk("C:\\Users\\User\\Documents\\python_ex\\main"):
        for curdir in dirs:
            for name in files:
                if name.endswith(".py"):
                    adrs.append(current_dir + '\n')
                    break
    for a in adrs:
        f.write(a)
