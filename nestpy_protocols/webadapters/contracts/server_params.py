from abc import ABC, abstractmethod
from typing import Any, Dict, List, Type, Callable, Union


class BaseServerParams(ABC):

    @abstractmethod
    def set_contact(self, contact: Union[Dict[str, str | Any], str, None]) -> None:
        ...

    @abstractmethod
    def set_license(self, license_info: Union[Dict[str, str | Any], str, None]) -> None:
        ...

    @abstractmethod
    def set_license_url(self, license_url: str) -> None:
        ...

    @abstractmethod
    def set_media_type(self, media_type: str) -> None:
        ...

    @abstractmethod
    def add_middleware(self, middleware_class: Type[Callable], *args, **kwargs) -> None:
        ...

    @abstractmethod
    def set_title(self, title: str) -> None:
        ...

    @abstractmethod
    def set_summary(self, summary: str) -> None:
        ...

    @abstractmethod
    def set_description(self, description: str) -> None:
        ...

    @abstractmethod
    def set_version(self, version: str) -> None:
        ...

    @abstractmethod
    def set_terms_of_service(self, terms: str) -> None:
        ...

    @abstractmethod
    def set_servers(self, servers: List[Dict[str, Any]]) -> None:
        ...

    @abstractmethod
    def set_root_path_in_servers(self, enabled: bool) -> None:
        ...

    @abstractmethod
    def set_prefix(self, prefix: str) -> None:
        ...

    @abstractmethod
    def set_separate_input_output_schemas(self, enabled: bool) -> None:
        ...

    @abstractmethod
    def set_default_response_class(self, response_class: Any) -> None:
        ...

    @abstractmethod
    def set_callbacks(self, callbacks: List[Any]) -> None:
        ...

    @abstractmethod
    def set_webhooks(self, webhooks: Any) -> None:
        ...

    @abstractmethod
    def set_responses(self, responses: Dict[Any, Dict[str, Any]]) -> None:
        ...

    @abstractmethod
    def set_extra(self, **extra: Any) -> None:
        ...

    @abstractmethod
    def set_lifespan(self, lifespan: Any) -> None:
        ...
