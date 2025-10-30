from abc import ABC, abstractmethod
from typing import List, Any, Callable, Optional


class BaseServerRouter(ABC):

    @abstractmethod
    def add_router_group(
        self,
        prefix: str,
        name: str,
        description: Optional[str] = None,
        tags: Optional[List[str]] = None,
        dependencies: Optional[List[Any]] = None,
        include_in_schema: Optional[bool]  = True
    ) -> None:
        ...

    @abstractmethod
    def add_route_in_router_group(self, name: str, path: str, endpoint: Callable[..., Any], **kwargs: Any) -> None:
        ...

    @abstractmethod
    def get_router_group(self, router_name: str) -> Any:
        ...
