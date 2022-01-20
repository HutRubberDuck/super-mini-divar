from starlette.middleware.cors import CORSMiddleware


class AppCORSMiddleware(CORSMiddleware):
    allow_origins = ["*"]
    allow_methods = ["*"]
    allow_headers = ["*"]
    allow_credentials = True
