from typing import Callable, Union, Any, Dict, List, Type, ParamSpecKwargs, Optional
from nestpy_protocols.webadapters import AbstractWebServer
from fastapi import FastAPI, APIRouter
from  flask import  Flask, Blueprint
import threading
from flask_restx import Api, Namespace, Resource


class FastAPIAdapter(AbstractWebServer):

    def __init__(self) -> None:
        super().__init__()
        self.app = FastAPI()
        self.routers = {}

    def add_router_group(
            self,
            prefix: str,
            name: str,
            description: Optional[str] = None,
            tags: Optional[List[str]] = None,
            dependencies: Optional[List[Any]] = None,
            include_in_schema: Optional[bool] = True,
    ) -> None:
        router = APIRouter(
            prefix=prefix,
            tags=tags,
            dependencies=dependencies,
            include_in_schema=include_in_schema
        )
        self.routers[name] = router

    def get_router(self, router_name: str) -> Any:
        return self.routers.get(router_name, None)

    def add_route(self, router_name: str, path: str, endpoint: Callable[..., Any], **kwargs: Any) -> None:
        self.routers[router_name].add_api_route(path=path, endpoint=endpoint, **kwargs)

    def set_title(self, title) -> None:
        self.app.title = title

    def set_prefix(self, prefix: str) -> None:
        self.app.root_path = prefix

    def set_description(self, description: str) -> None:
        self.app.description = description

    def listen(self, host, port):
        for router in self.routers.values():
            self.app.include_router(router=router)

        import uvicorn
        uvicorn.run(self.app, host=host, port=port)

    def set_contact(self, contact: Union[Dict[str, str | Any], Any, None]) -> None:
        self.app.contact = contact

    def set_license(self, license_info: Union[Dict[str, str | Any], Any, None]) -> None:
        self.app.license_info = license_info

    def set_license_url(self, license_url: str) -> None:
        pass

    def set_media_type(self, media_type: str) -> None:
        pass

    def add_middleware(self, middleware_class: Type[Callable], *args, **kwargs) -> None:
        self.app.add_middleware(middleware_class, *args, **kwargs)

    def set_summary(self, summary: str) -> None:
        self.app.summary = summary

    def set_version(self, version: str) -> None:
        self.app.version = version

    def set_terms_of_service(self, terms: str) -> None:
        self.app.terms_of_service = terms

    def set_servers(self, servers: List[Dict[str, Any]]) -> None:
        self.app.servers = servers

    def set_root_path_in_servers(self, enabled: bool) -> None:
        self.app.root_path_in_servers = enabled

    def set_separate_input_output_schemas(self, enabled: bool) -> None:
        self.app.separate_input_output_schemas = enabled

    def set_default_response_class(self, response_class: Any) -> None:
        self.app.default_response_class = response_class

    def set_callbacks(self, callbacks: List[Any]) -> None:
        self.app.callbacks = callbacks

    def set_webhooks(self, webhooks: Any) -> None:
        self.app.webhooks = webhooks

    def set_responses(self, responses: Dict[Any, Dict[str, Any]]) -> None:
        self.app.responses = responses

    def set_extra(self, **extra: Any) -> None:
        self.app.extra = extra

    def set_lifespan(self, lifespan: Any) -> None:
        self.app.lifespan = lifespan

    def add_api_route(self, path: str, endpoint: Callable[..., Any], **kwargs: Any) -> None:
        self.app.add_api_route(path, endpoint, **kwargs)

    def api_route(self, path: str, **kwargs: Any) -> None:
        self.app.api_route(path, **kwargs)

    def add_api_websocket_route(self, path: str, endpoint: Callable[..., Any], **kwargs: Any) -> None:
        self.app.add_api_websocket_route(path, endpoint, **kwargs)

    def websocket(self, path: str, **kwargs: Any) -> None:
        self.app.websocket(path, **kwargs)

    def include_router(self, router: Any, **kwargs: Any) -> None:
        self.app.include_router(router, **kwargs)

    def trace(self, path: str, **kwargs: Any) -> None:
        self.app.trace(path, **kwargs)

    def set_openapi_url(self, url: str) -> None:
        self.app.openapi_url = url

    def set_openapi_tags(self, tags: List[Dict[str, Any]]) -> None:
        self.app.openapi_tags = tags

    def set_docs_url(self, url: str) -> None:
        self.app.docs_url = url

    def set_redoc_url(self, url: str) -> None:
        self.app.redoc_url = url

    def set_swagger_ui_oauth2_redirect_url(self, url: str) -> None:
        self.app.swagger_ui_oauth2_redirect_url = url

    def set_swagger_ui_init_oauth(self, config: Any) -> None:
        self.app.swagger_ui_init_oauth = config

    def set_swagger_ui_parameters(self, params: Dict[str, Any]) -> None:
        self.app.swagger_ui_parameters = params

    def middleware(self, middleware_type: Any) -> None:
        self.app.middleware(middleware_type)

    def exception_handler(self, exc_class_or_status_code: Any) -> None:
        self.app.exception_handler(exc_class_or_status_code)

    def on_event(self, event_type: str) -> None:
        self.app.on_event(event_type)


class FlaskAdapter(AbstractWebServer):

    def __init__(self) -> None:
        super().__init__()
        self.app = Flask(__name__)
        self.api = Api(self.app)

    def get_router(self, router_name: str) -> Any:
        ...

    def add_router_group(
        self,
        prefix: str,
        name: str,
        description: Optional[str] = None,
        tags: Optional[List[str]] = None,
        dependencies: Optional[List[Any]] = None,
        include_in_schema: Optional[bool] = None,
    ) -> None:
        pass

    def add_route(self, name: str, path: str, endpoint: Callable[..., Any], **kwargs: Any) -> None:
        ...

    def set_title(self, title) -> None:
        self.api.title = title

    def set_description(self, description) -> None:
        self.api.description = description

    def set_prefix(self, prefix: str) -> None:
        self.api.prefix = prefix

    def listen(self, host, port) -> None:
        self.app.run(host=host, port=port)

    def set_contact(self, contact: Union[Dict[str, str | Any], Any, None]) -> None:
        self.api.contact = contact

    def set_license(self, license_info: Union[Dict[str, str | Any], Any, None]) -> None:
        self.api.license = license_info

    def set_license_url(self, license_url: str) -> None:
        self.api.license_url = license_url

    def set_media_type(self, media_type: str) -> None:
        self.api.media_type = media_type

    def add_middleware(self, middleware_class: Type[Callable], *args, **kwargs) -> None:
        ...

    def set_summary(self, summary: str) -> None:
        ...

    def set_version(self, version: str) -> None:
        self.api.version = version

    def set_terms_of_service(self, terms: str) -> None:
        self.api.terms_url = terms

    def set_servers(self, servers: List[Dict[str, Any]]) -> None:
        pass

    def set_root_path_in_servers(self, enabled: bool) -> None:
        pass

    def set_separate_input_output_schemas(self, enabled: bool) -> None:
        pass

    def set_default_response_class(self, response_class: Any) -> None:
        pass

    def set_callbacks(self, callbacks: List[Any]) -> None:
        pass

    def set_webhooks(self, webhooks: Any) -> None:
        pass

    def set_responses(self, responses: Dict[Any, Dict[str, Any]]) -> None:
        pass

    def set_extra(self, **extra: Any) -> None:
        self.app.config.update(**extra)

    def set_lifespan(self, lifespan: Any) -> None:
        pass

    def add_api_route(self, path: str, endpoint: Callable[..., Any], **kwargs: Any) -> None:
        self.app.add_url_rule(rule=path, view_func=endpoint, **kwargs)

    def api_route(self, path: str, **kwargs: Any) -> None:
        pass

    def add_api_websocket_route(self, path: str, endpoint: Callable[..., Any], **kwargs: Any) -> None:
        pass

    def websocket(self, path: str, **kwargs: Any) -> None:
        pass

    def include_router(self, router: Any, **kwargs: Any) -> None:
        pass

    def trace(self, path: str, **kwargs: Any) -> None:
        pass

    def set_openapi_url(self, url: str) -> None:
        self.api.url_scheme = url

    def set_openapi_tags(self, tags: List[Dict[str, Any]]) -> None:
        pass

    def set_docs_url(self, url: str) -> None:
        self.api._doc = url

    def set_redoc_url(self, url: str) -> None:
        pass

    def set_swagger_ui_oauth2_redirect_url(self, url: str) -> None:
        pass

    def set_swagger_ui_init_oauth(self, config: Any) -> None:
        pass

    def set_swagger_ui_parameters(self, params: Dict[str, Any]) -> None:
        pass

    def middleware(self, middleware_type: Any) -> None:
        pass

    def exception_handler(self, exc_class_or_status_code: Any) -> None:
        pass

    def on_event(self, event_type: str) -> None:
        pass


def index():
    return "<h1>Hello World</h1>"


def index2():
    return "<h1>Hello Router</h1>"


app1 = FastAPIAdapter()
app1.set_title("With FastAPI")
app1.set_prefix("/api")
app1.set_description("This server was created in FastAPI")
app1.add_api_route("/", index, tags=["Test Group"])
app1.add_router_group(prefix="/users", name="UserController", tags=["Users Group"])
app1.add_route(router_name="UserController", endpoint=index2, path="/")

app2 = FlaskAdapter()
app2.set_title("With Flask")
app2.set_prefix("/api")
app2.set_docs_url("/docs")
app2.set_description("This server was created in Flask")
app2.add_api_route("/", index)

t1 = threading.Thread(target=app1.listen, args=("127.0.0.1", 8000))
t2 = threading.Thread(target=app2.listen, args=("127.0.0.1", 8001))

t1.start()
t2.start()
