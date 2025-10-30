from typing import Dict, List, Any
from abc import ABC, abstractmethod


class BaseServerDocs(ABC):

    @abstractmethod
    def set_openapi_url(self, url: str) -> None:
        ...

    @abstractmethod
    def set_openapi_tags(self, tags: List[Dict[str, Any]]) -> None:
        ...

    @abstractmethod
    def set_docs_url(self, url: str) -> None:
        ...

    @abstractmethod
    def set_redoc_url(self, url: str) -> None:
        ...

    @abstractmethod
    def set_swagger_ui_oauth2_redirect_url(self, url: str) -> None:
        ...

    @abstractmethod
    def set_swagger_ui_init_oauth(self, config: Any) -> None:
        ...

    @abstractmethod
    def set_swagger_ui_parameters(self, params: Dict[str, Any]) -> None:
        ...

    @abstractmethod
    def set_swagger_ui_url(self, url: str) -> None:
        ...

    @abstractmethod
    def set_swagger_ui_path(self, path: str) -> None:
        ...

    @abstractmethod
    def set_open_api_version(self, version: str) -> None:
        ...

    @abstractmethod
    def set_api_spec_options(self, spect: dict[str, str]) -> None:
        ...