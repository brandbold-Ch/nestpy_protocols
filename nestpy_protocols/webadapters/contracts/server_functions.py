from typing import Any, Callable
from abc import ABC, abstractmethod


class BaseServerFunctions(ABC):

    @abstractmethod
    def add_api_route(self, path: str, endpoint: Callable[..., Any], **kwargs: Any) -> None:
        ...

    @abstractmethod
    def add_api_websocket_route(self, path: str, endpoint: Callable[..., Any], **kwargs: Any) -> None:
        ...

    @abstractmethod
    def websocket(self, path: str, **kwargs: Any) -> None:
        ...

    @abstractmethod
    def include_router_group(self, router: Any, **kwargs: Any) -> None:
        ...

    @abstractmethod
    def trace(self, path: str, **kwargs: Any) -> None:
        ...
