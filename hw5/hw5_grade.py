import os
import hashlib
import json

def hash_file(s: str) -> str:
    sorted_s_bytes = "_".join(sorted(s.split("\n"))).encode("utf-8")
    return hashlib.sha256(sorted_s_bytes).hexdigest()

if __name__ == "__main__":

    res = {}
    report = {}
    solution = None
    

    with open("solution.json", "r") as f:
        solution = json.loads(f.read())
    
    for file in os.listdir("./"):
        if ".res" in file:
            with open(file, "r") as f:
                ans = f.read()
                tag = file.split(".")[0]
                res[tag] = hash_file(ans)
    
    for q in solution:
        if q not in res:
            report[q] = 0
        else:
            if "q2" in q:
                report[q] = 5 if res[q] == solution[q] else 2
            if "q3" in q:
                report[q] = 7.5 if res[q] == solution[q] else 2
    
    with open("score.res", "w") as f:
        tags = sorted(solution.keys())
        for tag in tags:
            f.write("{t}:{s}\n".format(t=tag, s=str(report[tag])))
    