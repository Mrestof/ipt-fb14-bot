from mcstatus import MinecraftServer


def server_stats() -> str:
    response = ''
    server = MinecraftServer.lookup('92.249.127.225:25565')
    try:
        status = server.status()
    except TimeoutError:
        response = 'Press F to pay respect to KPI Craft'
        return response
    players = status.players.online
    # max amount of players on the server is 20, so we can simplify the following block
    if players == 1:
        response += f'На КПІ Крафті {status.players.online} Стив\n'
    elif players == 2 or players == 3 or players == 4:
        response += f'На КПІ Крафті {status.players.online} Стива\n'
    else:
        response += f'На КПІ Крафті {status.players.online} Стивів\n'
    latency = round(server.ping())
    response += f'Пинг: {latency} мс\n'
    # query = server.query()
    # response += (f'Грають у кубиики : {", ".join(query.players.names)}')
    # response += 'Тут має бути список гравців, але в них запити до серверу вимкнені :('
    return response
