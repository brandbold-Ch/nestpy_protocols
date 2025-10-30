from abc import ABC, abstractmethod
from typing import Any, Union


class BaseServerMiddlewares(ABC):
    
    @abstractmethod
    def middleware(self, middleware_type: Any) -> None:
        ...

    @abstractmethod
    def exception_handler(self, exc_class_or_status_code: Any) -> None:
        ...
        
    @abstractmethod
    def listen(self, host: str, port: Union[str, int]) -> None:
        ...
