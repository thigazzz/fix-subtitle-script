import re
from datetime import datetime, timedelta
new = open("data/new.srt", "w")

sync_time = 8

with open("data/example.srt") as wrong_file:
    for line in wrong_file:
        line = line.replace("\n", "")
        if re.search(r"\d{2}:", line):
            begin, final = line.split(" --> ")
            _begin = datetime.strptime(begin, "%H:%M:%S,%f")
            _final = datetime.strptime(final, "%H:%M:%S,%f")

            if _begin.time() < datetime.strptime(str(sync_time), "%S").time():
                if _final.time() < datetime.strptime(str(sync_time), "%S").time():    
                    line = line
            else:
                new_begin = (_begin - timedelta(seconds=sync_time)).time()
                new_final = (_final - timedelta(seconds=sync_time)).time()

                new_begin = new_begin.strftime("%H:%M:%S,%f")[:-3]
                new_final = new_final.strftime("%H:%M:%S,%f")[:-3]
                print(begin, new_begin)
                print(final, new_final)
                line = f"{new_begin} --> {new_final}"
        new.write(line + "\n")
new.close()

