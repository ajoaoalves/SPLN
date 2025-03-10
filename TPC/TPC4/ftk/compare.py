import sys
import json
import os

def get_ratio(our_dict, corpus):
    return {word: count / corpus.get(word, 1e-6) for word, count in our_dict.items()}

def read_json(filepath=None):
    if filepath and os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    try:
        return json.loads(input("Digite o JSON: "))
    except json.JSONDecodeError:
        print("Erro: JSON inválido.")
        sys.exit(1)

def main():
    data = read_json(sys.argv[1]) if len(sys.argv) > 1 else read_json()
    corpus = read_json("./corpus/corpus.json")
    print(json.dumps(get_ratio(data, corpus), indent=4, ensure_ascii=False))

if __name__ == "__main__":
    main()
