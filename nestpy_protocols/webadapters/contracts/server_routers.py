from abc import ABC, abstractmethod
from argparse import ArgumentParser
from typing import List, Any, Callable, ParamSpecKwargs, Optional
from fastapi import APIRouter, FastAPI
from flask_restx import Api, Resource, fields, Namespace
from collections import namedtuple


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
    def add_route(self, name: str, path: str, endpoint: Callable[..., Any], **kwargs: Any) -> None:
        ...

    @abstractmethod
    def get_router(self, router_name: str) -> Any:
        ...
