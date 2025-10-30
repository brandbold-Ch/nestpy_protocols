from nestpy_protocols.webadapters.contracts import BaseServerDocs, BaseServerParams, BaseServerRouter, BaseServerMiddlewares, BaseServerFunctions, BaseServerEvents
from abc import ABC


class AbstractWebServer(
    BaseServerParams,
    BaseServerFunctions,
    BaseServerDocs,
    BaseServerMiddlewares,
    BaseServerEvents,
    BaseServerRouter,
    ABC
):
    ...
    