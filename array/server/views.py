from aiohttp import web
import tasks


async def clean_array_handler(request):
    content = await request.json()
    job = await tasks.pool.enqueue_job('clean_array_avg_task', content)
    result = await job.result()
    return web.json_response(result)


def init_routes(app, cors):
    app.router.add_route('POST', '/clean_array_avg', clean_array_handler)

    for route in list(app.router.routes()):
        cors.add(route)
