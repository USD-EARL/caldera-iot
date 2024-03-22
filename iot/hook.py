from app.utility.base_world import BaseWorld
from plugins.iot.app.iot_gui import IotGUI
from plugins.iot.app.iot_api import IotAPI

name = 'Iot'
description = 'Emulated Mirai abilities'
address = '/plugin/iot/gui'
access = BaseWorld.Access.RED


async def enable(services):
    app = services.get('app_svc').application
    iot_gui = IotGUI(services, name=name, description=description)
    app.router.add_static('/iot', 'plugins/iot/static/', append_version=True)
    app.router.add_route('GET', '/plugin/iot/gui', iot_gui.splash)

    iot_api = IotAPI(services)
    # Add API routes here
    app.router.add_route('POST', '/plugin/iot/mirror', iot_api.mirror)

