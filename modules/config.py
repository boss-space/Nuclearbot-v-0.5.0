settings = {
    'id': 781404915142492171,
    'prefix': '!',
    'link': 'https://discord.com/api/oauth2/authorize?client_id=781404915142492171&permissions=8&redirect_uri=https%3A%2F%2Fnuclearbot.ga%2F&scope=bot',
    'server': 'https://discord.gg/WFX5ukJj2F',
    'channel': 782584270694776852,
    'logs':782584276314488832,
    'site': 'https://nuclearbot.ga/',
    'token': 'NzgxNDA0OTE1MTQyNDkyMTcx.X79KCQ.vcdevmaaRYCADgMagz0iAJX7VTo'
}

__ver__ = '4'

print (f': {__name__}.py {__ver__}')
await bot.get_channel (settings ['logs']).send (f'file ready: {__name__}.py {__ver__}')
