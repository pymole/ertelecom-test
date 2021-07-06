from aiohttp import web
import aiohttp_cors
import views


app = web.Application()

cors = aiohttp_cors.setup(app, defaults={
    "*": aiohttp_cors.ResourceOptions(
        allow_credentials=True,
        expose_headers="*",
        allow_headers="*",
    )
})

views.init_routes(app, cors)


if __name__ == '__main__':
    web.run_app(app)
