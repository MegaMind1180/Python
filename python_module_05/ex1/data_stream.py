import typing
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    @abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        self.name = "Numeric Processor"
        self.total_processed = 0
        self.remaining = 0
        self._items = []

    def validate(self, data: typing.Any) -> bool:
        return (isinstance(data, list) and all(isinstance(x, (int, float)) for x in data)) or isinstance(data, (int, float))

    def ingest(self, data: typing.Any) -> None:
        self._items.append(data)
        self.total_processed += 1
        self.remaining += 1

    def consume(self, count: int) -> None:
        self.remaining = max(0, self.remaining - count)


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        self.name = "Text Processor"
        self.total_processed = 0
        self.remaining = 0
        self._items = []

    def validate(self, data: typing.Any) -> bool:
        return isinstance(data, str) or (isinstance(data, list) and all(isinstance(x, str) for x in data))

    def ingest(self, data: typing.Any) -> None:
        self._items.append(data)
        self.total_processed += 1
        self.remaining += 1

    def consume(self, count: int) -> None:
        self.remaining = max(0, self.remaining - count)


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        self.name = "Log Processor"
        self.total_processed = 0
        self.remaining = 0
        self._items = []

    def validate(self, data: typing.Any) -> bool:
        return isinstance(data, list) and len(data) > 0 and all(isinstance(x, dict) for x in data)

    def ingest(self, data: typing.Any) -> None:
        self._items.append(data)
        self.total_processed += 1
        self.remaining += 1

    def consume(self, count: int) -> None:
        self.remaining = max(0, self.remaining - count)


class DataStream:
    def __init__(self) -> None:
        self._processors = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        for item in stream:
            processed = False
            for proc in self._processors:
                if proc.validate(item):
                    proc.ingest(item)
                    processed = True
                    break
            if not processed:
                print(f"DataStream error - Can't process element in stream: {item}")

    def print_processors_stats(self) -> None:
        if not self._processors:
            print("No processor found, no data")
            return
        for proc in self._processors:
            print(f"{proc.name}: total {proc.total_processed} items processed, remaining {proc.remaining} on processor")


if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===")
    print("Initialize Data Stream...")
    stream = DataStream()

    print("== DataStream statistics ==")
    stream.print_processors_stats()

    print("Registering Numeric Processor")
    num_proc = NumericProcessor()
    stream.register_processor(num_proc)

    batch = [
        'Hello world',
        [3.14, -1, 2.71],
        [{'log_level': 'WARNING', 'log_message': 'Telnet access! Use ssh instead'}, {'log_level': 'INFO', 'log_message': 'User wil is connected'}],
        42,
        ['Hi', 'five']
    ]

    print(f"Send first batch of data on stream: {batch}")
    stream.process_stream(batch)

    print("== DataStream statistics ==")
    stream.print_processors_stats()

    print("Registering other data processors")
    text_proc = TextProcessor()
    log_proc = LogProcessor()
    stream.register_processor(text_proc)
    stream.register_processor(log_proc)

    print("Send the same batch again")
    stream.process_stream(batch)

    print("== DataStream statistics ==")
    stream.print_processors_stats()

    print("Consume some elements from the data processors: Numeric 3, Text 2, Log 1")
    num_proc.consume(3)
    text_proc.consume(2)
    log_proc.consume(1)

    print("== DataStream statistics ==")
    stream.print_processors_stats()
