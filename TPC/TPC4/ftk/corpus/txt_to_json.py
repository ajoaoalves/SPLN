import json

file = "corpus.txt"

data = {}

with open(file, "r", encoding="utf-8") as f:
    for line in f:
        try:
            value, key = line.strip().split("\t")
            if int(value) > 2:
                data[key] = int(value)
        except ValueError:
            print(f"Error: {line}")

result = json.dumps(data, indent=4, ensure_ascii=False)

with open("corpus.json", "w", encoding="utf-8") as f_json:
    f_json.write(result)