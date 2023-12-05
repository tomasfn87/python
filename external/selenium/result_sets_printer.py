from result_set import ResultSet
from typing import Any, List
import datetime as dt

class ResultSetsPrinter:
    def __init__(self: Any, margin: int):
        if margin < 1:
            self.margin = 2
        else:
            self.margin = margin
        self.num_of_results: int = 0
        self.result_list: List[ResultSet] = []

    def add_results(self: Any, results: ResultSet):
        if results.get_num_of_results():
            self.result_list.append(results)
            self.num_of_results += results.get_num_of_results()

    def get_num_of_results(self: Any) -> int:
        return self.num_of_results

    def get_max_header_length(self: Any) -> int:
        max_header_length: int = 0
        for i in self.result_list:
            header_length = len(i.get_provider()) + len(i.get_title())
            if header_length > max_header_length:
                max_header_length = header_length
        return max_header_length

    def print_all(self: Any):
        print(f"->  {str(dt.datetime.now())[0:19]}")

        padding: int = 0
        r_list = self.result_list

        for r in r_list:
            if r.get_max_key_length() > padding:
                padding = r.get_max_key_length()
        padding += self.margin

        max_header_length: int = self.get_max_header_length()
        header_parts: List[str] = ["    ", " ", "", " ", "    "]
        for p in header_parts:
            max_header_length += len(p)

        for i in range(len(r_list)):
            provider = "{}{}{}".format(
                header_parts[0], r_list[i].get_provider(),
                header_parts[1])
            union = header_parts[2]
            if not len(union) == 1:
                union = union[0] if union else "│"
            title = "{}{}{}".format(
                header_parts[3], r_list[i].get_title(), header_parts[4])
            header = f"{provider}{union}{title}"
            frame = "{}{}{}".format(
                "─" * len(provider), "┬",
                "─" * (max_header_length
                    - (len(provider) + len(union))))

            if i == 0:
                print(frame.replace("─", "═").replace("┬", "╤"), end="")
            else:
                print(frame, end="")
            print("\n{}\n{}".format(
                header, frame.replace("┬", "┴")))

            for j in range(len(r_list[i].results)):
                key   = list(r_list[i].results[j].keys())[0]
                value = list(r_list[i].results[j].values())[0]
                print(f"{key.rjust(padding)}: {value}")
            if i is len(self.result_list) - 1:
                print(f'{"═" * max_header_length}')