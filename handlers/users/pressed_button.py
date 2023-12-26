from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.default.user import game_menu_back
from loader import dp
from states.user import GameState


@dp.callback_query_handler(state=GameState.company)
async def game_company_handler(call: types.CallbackQuery, state: FSMContext):
    try:
        await state.update_data(company=call.data)
        data = await state.get_data()
        if data.get('game_name') == "WoT Blitz" and data.get('company') == 'play_market':
            text = "You can download this game by link:\n\nhttps://play.google.com/store/apps/details?id=net.wargaming.wot.blitz&hl=en&gl=US&pli=1"
        elif data.get('game_name') == "WoT Blitz" and data.get('company') == 'microsoft':
            text = "You can download this game by link:\n\nhttps://www.microsoft.com/ru-tm/p/world-of-tanks-blitz/9nblggh202h8?activetab=pivot:overviewtab"
        elif data.get('game_name') == "WoT Blitz" and data.get('company') == 'mac_store':
            text = "You can download this game by link:\n\nhttps://apps.apple.com/us/app/world-of-tanks-blitz/id1068932208?mt=12"
        elif data.get('game_name') == "WoT Blitz" and data.get('company') == 'app_store':
            text = "You can download this game by link:\n\nhttps://apps.apple.com/us/app/world-of-tanks-blitz-mobile/id859204347"

        if data.get('game_name') == "Pubg" and data.get('company') == 'play_market':
            text = "You can download this game by link:\n\nhttps://play.google.com/store/apps/details?id=net.wargaming.wot.blitz&hl=en&gl=US&pli=1"
        elif data.get('game_name') == "Pubg" and data.get('company') == 'app_store':
            text = "You can download this game by link:\n\nhttps://apps.apple.com/us/app/pubg-mobile/id1330123889"

        if data.get('game_name') == "Free Fire" and data.get('company') == 'play_market':
            text = "You can download this game by link:\n\nhttps://play.google.com/store/apps/details?id=com.dts.freefireth&hl=en&gl=US"
        elif data.get('game_name') == "Free Fire" and data.get('company') == 'app_store':
            text = "You can download this game by link:\n\nhttps://apps.apple.com/us/app/free-fire-winterlands/id1300146617"

        if data.get('game_name') == "Subway Surf" and data.get('company') == 'play_market':
            text = "You can download this game by link:\n\nhttps://play.google.com/store/apps/details?id=com.kiloo.subwaysurf&hl=en&gl=US"
        elif data.get('game_name') == "Subway Surf" and data.get('company') == 'app_store':
            text = "You can download this game by link:\n\nhttps://apps.apple.com/in/app/subway-surfers/id512939461"

        if data.get('game_name') == "Minecraft" and data.get('company') == 'play_market':
            text = "You can download this game by link:\n\nhttps://play.google.com/store/apps/details?id=com.mojang.minecraftpe&hl=en&gl=US"
        elif data.get('game_name') == "Minecraft" and data.get('company') == 'app_store':
            text = "You can download this game by link:\n\nhttps://apps.apple.com/us/app/minecraft/id479516143"
        elif data.get('game_name') == "Minecraft" and data.get('company') == 'microsoft':
            text = "You can download this game by link:\n\nhttps://www.microsoft.com/en-hu/p/minecraft-for-windows/9nblggh2jhxj?activetab=pivot:overviewtab"

        if data.get('game_name') == "Counter-Strike 1.6" and data.get('company') == 'all':
            text = "You can download this game by link:\n\nhttps://all-cs.ru/?source=gads&creative=650918691821&key=&gclid=Cj0KCQiAm4WsBhCiARIsAEJIEzX8rzoTbKzr5GOm1S-Xx5lrzbOjsFSoHAxnGb7CnFu71LwtKJCKfmYaAtdgEALw_wcB"

        if data.get('game_name') == "Bow master" and data.get('company') == 'play_market':
            text = "You can download this game by link:\n\nhttps://play.google.com/store/apps/details?id=com.playgendary.bowmasters&hl=en&gl=US"
        elif data.get('game_name') == "Bow master" and data.get('company') == 'app_store':
            text = "You can download this game by link:\n\nhttps://apps.apple.com/us/app/bowmasters-multiplayer-game/id1118431695"

        if data.get('game_name') == "Forza horizon: Demoversion" and data.get('company') == 'microsoft':
            text = "You can download this game by link:\n\nhttps://www.microsoft.com/en-gy/p/forza-horizon-4-demo/9p8cp1l72jxs?activetab=pivot:overviewtab"

        if data.get('game_name') == "Car parking" and data.get('company') == 'play_market':
            text = "You can download this game by link:\n\nhttps://play.google.com/store/apps/details?id=com.olzhas.carparking.multyplayer&hl=en&gl=US"
        elif data.get('game_name') == "Car parking" and data.get('company') == 'app_store':
            text = "You can download this game by link:\n\nhttps://apps.apple.com/us/app/car-parking-multiplayer/id1374868881"
        elif data.get('game_name') == "Car parking" and data.get('company') == 'microsoft':
            text = "You can download this game by link:\n\nhttps://www.microsoft.com/en-us/p/car-parking/9ntvt4czgpc4?activetab=pivot:overviewtab"

        if data.get('game_name') == "TLauncher" and data.get('company') == "all":
            text = "You can download this game by link:\n\nhttps://tlauncher.org/en/"

        if data.get('game_name') == "Among us" and data.get('company') == 'play_market':
            text = "You can download this game by link:\n\nhttps://play.google.com/store/apps/details?id=com.innersloth.spacemafia&hl=en&gl=US"
        elif data.get('game_name') == "Among us" and data.get('company') == 'app_store':
            text = "You can download this game by link:\n\nhttps://apps.apple.com/us/app/among-us/id1351168404"
        elif data.get('game_name') == "Among us" and data.get('company') == 'microsoft':
            text = "You can download this game by link:\n\nhttps://www.microsoft.com/en-vg/p/among-us/9ng07qjnk38j"

        if data.get('game_name') == "Roblox" and data.get('company') == 'play_market':
            text = "You can download this game by link:\n\nhttps://play.google.com/store/apps/details?id=com.roblox.client&hl=en&gl=US"
        elif data.get('game_name') == "Roblox" and data.get('company') == 'app_store':
            text = "You can download this game by link:\n\nhttps://apps.apple.com/us/app/roblox/id431946152"
        elif data.get('game_name') == "Roblox" and data.get('company') == 'microsoft':
            text = "You can download this game by link:\n\nhttps://www.microsoft.com/en-id/p/roblox/9nblgggzm6wm"

        if data.get('game_name') == "Discord" and data.get('company') == "all":
            text = "You can download this game by link:\n\nhttps://discord.com/"

        if data.get('game_name') == "Hill Climb" and data.get('company') == 'play_market':
            text = "You can download this game by link:\n\nhttps://play.google.com/store/apps/details?id=com.fingersoft.hillclimb&hl=en&gl=US"
        elif data.get('game_name') == "Hill Climb" and data.get('company') == 'app_store':
            text = "You can download this game by link:\n\nhttps://apps.apple.com/us/app/hill-climb-racing/id564540143"
        elif data.get('game_name') == "Hill Climb" and data.get('company') == 'microsoft':
            text = "You can download this game by link:\n\nhttps://www.microsoft.com/en-us/p/hill-climb-racing/9wzdncrdcwk8"

        if data.get('game_name') == "Fortnite" and data.get('company') == 'play_market':
            text = "You can download this game by link:\n\nhttps://play.google.com/store/apps/details?id=battle.royale.wallpapers.hd&hl=en&gl=US"
        elif data.get('game_name') == "Fortnite" and data.get('company') == 'app_store':
            text = "You can download this game by link:\n\nhttps://apps.apple.com/us/app/companion-for-fortnite/id1267999556"
        elif data.get('game_name') == "Fortnite" and data.get('company') == 'microsoft':
            text = "You can download this game by link:\n\nhttps://apps.microsoft.com/detail/BT5P2X999VH2?hl=en-US&gl=US"

        if data.get('game_name') == "Chess.com" and data.get('company') == 'play_market':
            text = "You can download this game by link:\n\nhttps://play.google.com/store/apps/details?id=com.chess&hl=en_US"
        elif data.get('game_name') == "Chess.com" and data.get('company') == 'app_store':
            text = "You can download this game by link:\n\nhttps://apps.apple.com/us/app/chess-play-learn/id329218549"
        elif data.get('game_name') == "Chess.com" and data.get('company') == 'microsoft':
            text = "You can download this game by link:\n\nhttps://www.microsoft.com/en-us/p/chess-for-windows/9nblggh5jfzq?activetab=pivot:overviewtab"
        await call.message.delete()
        await call.message.answer(text=text, reply_markup=game_menu_back)
    except Exception as exc:
        print(exc)
