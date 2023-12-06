from typing import Any, Dict, List

class ResultSet:
    def __init__(self: Any,
        provider: str="Result set provider", title: str="Result set title"):

        self.title: str = title.strip()
        self.provider: str = provider.strip()
        self.num_of_results: int = 0
        self.results: List[Dict[str, str]] = []

    def add_key_value(self: Any, key: str, value: str) -> bool:
        if (not any(list(i.keys())[0] == key for i in self.results) \
            and key.strip() and value.strip()):
            self.results.append({key: value})
            self.num_of_results += 1
            return True
        else:
            print("Resultado não foi adicionado ", end="")
            print(f"(chave: {key}, valor: {value}).")
            return False

    def get_provider(self: Any) -> str:
        return self.provider

    def get_title(self: Any) -> str:
        return self.title

    def get_num_of_results(self: Any) -> int:
        return self.num_of_results

    def get_max_key_length(self: Any) -> int:
        max_key_length: int = 0
        for i in range(len(self.results)):
            key: str = list(self.results[i].keys())[0]
            if len(key) > max_key_length:
                max_key_length = len(key)
        return max_key_length
