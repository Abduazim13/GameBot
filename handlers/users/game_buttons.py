from aiogram.dispatcher import FSMContext
from keyboards.inline.games import *
from loader import dp
from aiogram import types
from keyboards.default.user import games_menu, game_menu_back
from aiogram.types import InputFile
from states.user import GameState


@dp.message_handler()
async def games_handler(message: types.Message, state: FSMContext):
    if message.text == "WoT Blitz":
        await state.update_data(game_name='WoT Blitz')
        text = "Choose your company\n\nВыберите компанию\n\nKOmpaniyani tanlang"
        photo = InputFile(path_or_bytesio='./photos/wotblitz.jpg')
        await message.answer_photo(caption=text, reply_markup=three_win_mac_android, photo=photo)
        await GameState.company.set()
    elif message.text == "Pubg":
        await state.update_data(game_name='Pubg')
        text = "Choose your company\n\nВыберите компанию\n\nKOmpaniyani tanlang"
        photo = InputFile(path_or_bytesio='./photos/pubg.jpg')
        await message.answer_photo(caption=text, reply_markup=two_android_app, photo=photo)
        await GameState.company.set()
    elif message.text == "Subway Surf":
        await state.update_data(game_name='Subway Surf')
        text = "Choose your company\n\nВыберите компанию\n\nKOmpaniyani tanlang"
        photo = InputFile(path_or_bytesio='./photos/subway_surf.jpg')
        await message.answer_photo(caption=text, reply_markup=two_android_app, photo=photo)
        await GameState.company.set()
    elif message.text == "Minecraft":
        await state.update_data(game_name='Minecraft')
        text = "Choose your company\n\nВыберите компанию\n\nKOmpaniyani tanlang"
        photo = InputFile(path_or_bytesio='./photos/mincraft.jpg')
        await message.answer_photo(caption=text, reply_markup=three_win_app_android, photo=photo)
        await GameState.company.set()
    elif message.text == "Fortnite":
        await state.update_data(game_name='Fortnite')
        text = "Choose your company\n\nВыберите компанию\n\nKOmpaniyani tanlang"
        photo = InputFile(path_or_bytesio='./photos/fortnite.jpg')
        await message.answer_photo(caption=text, reply_markup=two_android_app, photo=photo)
        await GameState.company.set()
    elif message.text == "Minecraft: Java & Bedrock Edition":
        await state.update_data(game_name='Minecraft: Java & Bedrock Edition')
        text = "Choose your company\n\nВыберите компанию\n\nKOmpaniyani tanlang"
        photo = InputFile(path_or_bytesio='./photos/minecraft_java_bedrock.jpg')
        await message.answer_photo(caption=text, reply_markup=only_windows, photo=photo)
        await GameState.company.set()
    elif message.text == "Discord":
        await state.update_data(game_name='Discord')
        text = "Choose your company\n\nВыберите компанию\n\nKOmpaniyani tanlang"
        photo = InputFile(path_or_bytesio='./photos/disord.jpg')
        await message.answer_photo(caption=text, reply_markup=only_windows, photo=photo)
        await GameState.company.set()
    elif message.text == "Hill Climb":
        await state.update_data(game_name='Hill Climb')
        text = "Choose your company\n\nВыберите компанию\n\nKOmpaniyani tanlang"
        photo = InputFile(path_or_bytesio='./photos/hillclimb.jpg')
        await message.answer_photo(caption=text, reply_markup=three_win_app_android, photo=photo)
        await GameState.company.set()
    elif message.text == "Free Fire":
        await state.update_data(game_name='Free Fire')
        text = "Choose your company\n\nВыберите компанию\n\nKOmpaniyani tanlang"
        photo = InputFile(path_or_bytesio='./photos/free_fire.jpg')
        await message.answer_photo(caption=text, reply_markup=two_android_app, photo=photo)
        await GameState.company.set()
    elif message.text == "Roblox":
        await state.update_data(game_name='Roblox')
        text = "Choose your company\n\nВыберите компанию\n\nKOmpaniyani tanlang"
        photo = InputFile(path_or_bytesio='./photos/roblox.png')
        await message.answer_photo(caption=text, reply_markup=three_win_app_android, photo=photo)
        await GameState.company.set()
    elif message.text == "Among us":
        await state.update_data(game_name='Among us')
        text = "Choose your company\n\nВыберите компанию\n\nKOmpaniyani tanlang"
        photo = InputFile(path_or_bytesio='./photos/amongus.jpg')
        await message.answer_photo(caption=text, reply_markup=two_android_app, photo=photo)
        await GameState.company.set()
    elif message.text == "TLauncher":
        await state.update_data(game_name='TLauncher')
        text = "Choose your company\n\nВыберите компанию\n\nKompaniyani tanlang"
        photo = InputFile(path_or_bytesio='./photos/TL.jpg')
        await message.answer_photo(caption=text, reply_markup=alL_Company, photo=photo)
        await GameState.company.set()
    elif message.text == "Car parking":
        await state.update_data(game_name='Car parking')
        text = "Choose your company\n\nВыберите компанию\n\nKompaniyani tanlang"
        photo = InputFile(path_or_bytesio='./photos/car_parking.jpg')
        await message.answer_photo(caption=text, reply_markup=alL_Company, photo=photo)
        await GameState.company.set()
    elif message.text == "Forza horizon: Demoversion":
        await state.update_data(game_name='Forza horizon: Demoversion')
        text = "Choose your company\n\nВыберите компанию\n\nKOmpaniyani tanlang"
        photo = InputFile(path_or_bytesio='./photos/forza horizon.jpg')
        await message.answer_photo(caption=text, reply_markup=two_win_mac, photo=photo)
        await GameState.company.set()
    elif message.text == "Bow master":
        await state.update_data(game_name='Bow master')
        text = "Choose your company\n\nВыберите компанию\n\nKOmpaniyani tanlang"
        photo = InputFile(path_or_bytesio='./photos/bowmaster.jpg')
        await message.answer_photo(caption=text, reply_markup=two_android_app, photo=photo)
        await GameState.company.set()
    elif message.text == "Counter-Strike 1.6":
        await state.update_data(game_name='Counter-Strike 1.6')
        text = "Choose your company\n\nВыберите компанию\n\nKOmpaniyani tanlang"
        photo = InputFile(path_or_bytesio='./photos/counter.jpg')
        await message.answer_photo(caption=text, reply_markup=two_win_mac, photo=photo)
        await GameState.company.set()
    else:
        await message.answer(text="If you going to go back press button 👇", reply_markup=game_menu_back)


@dp.message_handler(state="*", text="🎮 To Games Menu")
async def to_games_handler(message: types.Message, state: FSMContext):
    await state.finish()
    text = "🎮 Pressed Games Menu\n\nSubscribe To my channel:\nhttps://t.me/carsinvideo"
    await message.answer(text=text, reply_markup=games_menu)


# @dp.callback_query_handler(state=GameState.company)
# async def game_company_handler(call: types.CallbackQuery, state: FSMContext):
#     try:
#         await state.update_data(company=call.data)
#         data = await state.get_data()
#         if data.get('game_name') == "WoT Blitz" and data.get('company') == 'play_market':
#             text = "You can download this game by link:\n"
#         elif data.get('game_name') == "WoT Blitz" and data.get('company') == 'microsoft':
#             text = "You can download this game by link:\n"
#
#
#     except Exception as exc:gigi
#         print(exc)
