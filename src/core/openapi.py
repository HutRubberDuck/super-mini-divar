from typing import Any, Dict

from fastapi.openapi.utils import get_openapi

from src.core.settings import APP_NAME, APP_DESCRIPTION, APP_VERSION


def defined_openapi() -> Dict[str, Any]:
    from src.main import app

    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title=APP_NAME,
        description=APP_DESCRIPTION,
        version=APP_VERSION,
        routes=app.routes,
    )

    headers = {
        "name": "Authorization",
        "in": "header",
        "required": True,
        "schema": {
            "title": "Authorization",
            "type": "string"
        },
    }

    router_authorize = [route for route in app.routes[4:] if route.operation_id == "authorize"]

    for route in router_authorize:
        method = list(route.methods)[0].lower()
        try:
            openapi_schema["paths"][route.path][method]['parameters'].append(headers)
        except Exception:
            openapi_schema["paths"][route.path][method].update({"parameters": [headers]})

    app.openapi_schema = openapi_schema
    return app.openapi_schema
