from abc import ABC, abstractmethod
from typing import Any, List, Union, Dict

class DataProcessor(ABC):
    def __init__(self) -> None:
        self._storage: List[tuple[int, str]] = []
        self._rank_counter: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> List[tuple[int, str]]:
        return self._storage

class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)) and not isinstance(data, bool):
            return True
        if isinstance(data, list):
            return all(isinstance(x, (int, float)) and not isinstance(x, bool) for x in data)
        return False

    def ingest(self, data: Union[int, float, List[Union[int, float]]]) -> None:
        if not self.validate(data):
            raise ValueError("Invalid data type for NumericProcessor")
        items = data if isinstance(data, list) else [data]
        for item in items:
            self._rank_counter += 1
            self._storage.append((self._rank_counter, str(item)))

class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(x, str) for x in data)
        return False

    def ingest(self, data: Union[str, List[str]]) -> None:
        if not self.validate(data):
            raise ValueError("Invalid data type for TextProcessor")
        items = data if isinstance(data, list) else [data]
        for item in items:
            self._rank_counter += 1
            self._storage.append((self._rank_counter, item))

class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        def is_valid_dict(d: Any) -> bool:
            return isinstance(d, dict) and all(isinstance(k, str) and isinstance(v, str) for k, v in d.items())

        if is_valid_dict(data):
            return True
        if isinstance(data, list):
            return all(is_valid_dict(d) for d in data)
        return False

    def ingest(self, data: Union[Dict[str, str], List[Dict[str, str]]]) -> None:
        if not self.validate(data):
            raise ValueError("Invalid data type for LogProcessor")
        items = data if isinstance(data, list) else [data]
        for item in items:
            self._rank_counter += 1
            self._storage.append((self._rank_counter, str(item)))

num_proc = NumericProcessor()
num_proc.ingest(42)
num_proc.ingest([10, 20.5, 30])

text_proc = TextProcessor()
text_proc.ingest("Hallo Welt")
text_proc.ingest(["Python", "Programmieren"])

log_proc = LogProcessor()
log_proc.ingest({"status": "OK", "message": "System läuft"})

print("Zahlen-Speicher:", num_proc.output())
print("Text-Speicher:", text_proc.output())
print("Log-Speicher:", log_proc.output())
