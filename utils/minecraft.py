from mcstatus import MinecraftServer


def server_stats() -> str:
    response = ''
    server = MinecraftServer.lookup('92.249.127.225:25565')
    try:
        status = server.status()
    except TimeoutError:
        response = 'Press F to pay respect to KPI Craft'
        return response
    response += f'На КПИ Крафте {status.players.online} Стивов\n'
    latency = round(server.ping())
    response += f'Пинг: {latency} мс\n'
    # query = server.query()
    # response += (f"Играют в кубики : {', '.join(query.players.names)}") # нужна двойная кавычка
    response += 'Тут должен быть список игроков, но у них запросы к серваку отключены :('
    return response
