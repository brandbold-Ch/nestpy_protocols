from abc import ABC, abstractmethod


class BaseServerEvents(ABC):
    
    @abstractmethod
    def on_event(self, event_type: str) -> None:
        ...
