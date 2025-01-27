try:
    from typing import Protocol  # type: ignore
except ImportError:
    from typing_extensions import Protocol  # type: ignore


class Data(Protocol):
    def keys(self): ...

    def __getitem__(self, item): ...

    def __contains__(self, item): ...
