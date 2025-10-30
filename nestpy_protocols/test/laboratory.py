"""
from typing import Callable, Union, Any, Dict, List, Type, Optional, Sequence
from nestpy_protocols.webadapters import AbstractWebServer
from fastapi import FastAPI, APIRouter
from  flask import  Flask
import threading
from flask_smorest import Api, Blueprint


class FastAPIAdapter(AbstractWebServer):

    def get_router_groups(self) -> List[Any] | Dict[Any, Any] | Sequence[Any]:
        return self.routers

    def set_global_url_prefix(self, prefix: str) -> None:
        self.app.root_path = prefix

    def set_swagger_ui_url(self, url: str) -> None:
        pass

    def set_swagger_ui_path(self, path: str) -> None:
        pass

    def set_open_api_version(self, version: str) -> None:
        pass

    def set_api_spec_options(self, spect: dict[str, str]) -> None:
        pass

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

    def get_router_group(self, router_name: str) -> Any:
        return self.routers.get(router_name, None)

    def add_route_in_router_group(self, router_name: str, path: str, endpoint: Callable[..., Any], **kwargs: Any) -> None:
        self.routers[router_name].add_api_route(path=path, endpoint=endpoint, **kwargs)

    def set_title(self, title) -> None:
        self.app.title = title

    def set_description(self, description: str) -> None:
        self.app.description = description

    def listen(self, host: str, port: Union[str, int]) -> None:
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

    def add_api_websocket_route(self, path: str, endpoint: Callable[..., Any], **kwargs: Any) -> None:
        self.app.add_api_websocket_route(path, endpoint, **kwargs)

    def websocket(self, path: str, **kwargs: Any) -> None:
        self.app.websocket(path, **kwargs)

    def include_router_group(self, router: Any, **kwargs: Any) -> None:
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

    def set_global_url_prefix(self, prefix: str) -> None:
        ...

    def set_swagger_ui_url(self, url: str) -> None:
        self.flask_app.config["OPENAPI_SWAGGER_UI_URL"] = url

    def set_swagger_ui_path(self, path: str) -> None:
        self.flask_app.config["OPENAPI_SWAGGER_UI_PATH"] = path

    def set_open_api_version(self, version: str) -> None:
        self.flask_app.config["OPENAPI_VERSION"] = version

    def set_api_spec_options(self, spect: dict[str, str]) -> None:
        pass

    def __init__(self) -> None:
        super().__init__()
        self.flask_app = Flask(__name__)
        self.api: Optional[Api] = None
        self.blueprints = {}

    def get_router_groups(self) -> List[Any] | Dict[Any, Any] | Sequence[Any]:
        return self.blueprints

    def get_router_group(self, router_name: str) -> Any:
        return self.blueprints.get(router_name, None)

    def add_router_group(
        self,
        prefix: str,
        name: str,
        description: Optional[str] = None,
        tags: Optional[List[str]] = None,
        dependencies: Optional[List[Any]] = None,
        include_in_schema: Optional[bool] = None,
    ) -> None:
        bl = Blueprint(url_prefix=prefix, name=name, description=description, import_name=name)
        self.blueprints[name] = bl

    def add_route_in_router_group(self, name: str, path: str, endpoint: Callable[..., Any], **kwargs: Any) -> None:
        self.blueprints[name].add_url_rule(endpoint=name, rule=path, view_func=endpoint, **kwargs)

    def set_title(self, title) -> None:
        self.flask_app.config["API_TITLE"] = title

    def set_description(self, description: str) -> None:
        ...

    def listen(self, host: str, port: Union[str, int]) -> None:
        self.api = Api(self.flask_app)

        for bl in self.blueprints.values():
            self.api.register_blueprint(bl)

        self.flask_app.run(host=host, port=port)

    def set_contact(self, contact: Union[Dict[str, str | Any], Any, None]) -> None:
        ...

    def set_license(self, license_info: Union[Dict[str, str | Any], Any, None]) -> None:
        ...

    def set_license_url(self, license_url: str) -> None:
        ...

    def set_media_type(self, media_type: str) -> None:
        ...

    def add_middleware(self, middleware_class: Type[Callable], *args, **kwargs) -> None:
        ...

    def set_summary(self, summary: str) -> None:
        ...

    def set_version(self, version: str) -> None:
        self.flask_app.config["API_VERSION"] = version

    def set_terms_of_service(self, terms: str) -> None:
        ...

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
        self.flask_app.config.update(**extra)

    def set_lifespan(self, lifespan: Any) -> None:
        pass

    def add_api_route(self, path: str, endpoint: Callable[..., Any], **kwargs: Any) -> None:
        self.flask_app.add_url_rule(rule=path, view_func=endpoint, **kwargs)

    def add_api_websocket_route(self, path: str, endpoint: Callable[..., Any], **kwargs: Any) -> None:
        pass

    def websocket(self, path: str, **kwargs: Any) -> None:
        pass

    def include_router_group(self, router: Any, **kwargs: Any) -> None:
        pass

    def trace(self, path: str, **kwargs: Any) -> None:
        pass

    def set_openapi_url(self, url: str) -> None:
        self.flask_app.config["OPENAPI_URL"] = url
        ...

    def set_openapi_tags(self, tags: List[Dict[str, Any]]) -> None:
        pass

    def set_docs_url(self, url: str) -> None:
        self.flask_app.config["OPENAPI_URL_PREFIX"] = url

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


def get_status():
    return {"status": "ok", "message": "Servidor funcionando correctamente"}


def get_user():
    return {"id": 1, "name": "Alice", "role": "admin"}


def about():
    return "Esta es una API de ejemplo creada con Flask-RESTX."


def get_products():
    return {
        "products": [
            {"id": 1, "name": "Laptop", "price": 1200},
            {"id": 2, "name": "Mouse", "price": 25},
            {"id": 3, "name": "Teclado", "price": 45}
        ]
    }


app1 = FastAPIAdapter()
app1.set_title("With FastAPI")
app1.set_global_url_prefix("/api")
app1.set_description("This server was created in FastAPI")
app1.add_api_route("/", get_products, tags=["Products Group"])
app1.add_router_group(prefix="/users", name="UserController", tags=["Users Group"])
app1.add_route_in_router_group(router_name="UserController", endpoint=get_user, path="/")
app1.add_route_in_router_group(router_name="UserController", endpoint=about, path="/about")

app2 = FlaskAdapter()
app2.set_title("With Flask")
app2.set_version("1.0.0")
app2.set_swagger_ui_url("https://cdn.jsdelivr.net/npm/swagger-ui-dist/")
app2.set_open_api_version("3.0.3")
app2.set_docs_url("/")
app2.set_swagger_ui_path("/docs")
app2.add_api_route("/products", get_products)
app2.add_api_route("/users/user", get_user)
app2.add_router_group(prefix="/users", name="UserController", description="Endpoints flask-smorest")
app2.add_route_in_router_group(name="UserController", endpoint=get_status, path="/")
app2.add_route_in_router_group(name="UserController", endpoint=get_products, path="/products")

t1 = threading.Thread(target=app1.listen, args=("127.0.0.1", 8000))
t2 = threading.Thread(target=app2.listen, args=("127.0.0.1", 8001))

t1.start()
t2.start()

"""