
from loader import dp
from aiogram import types
import asyncio
from typing import Union

from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.dispatcher import FSMContext
from states import Form_zakaz, Form_publik
from loader import bot


ADMIN_CHAT_ID =   # Замени на актуальный ID чата администратора
BARAHOLKA_CHAT_ID =   # Замени на актуальный ID чата барахолки

@dp.message_handler(text='огурец')
async def answer_kukumber_command(message: types.Message):
    await message.answer(text=f'ага! огурец!')
    
@dp.message_handler(text='Правила чата')
async def answer_ruls_command(message: types.Message):
    await message.reply(text=f'правила канала\nПросим обратить внимание, что для рекламы выделен 1 рекламный день в неделю!\nПлатно!\n♦️ чат/канал содан для покупки и продажи б/у товаров в г.Нови Сад\n♦️ ваше объявление должно содержать:\n- запрос на товар или предложение товара\n- фото и  описание\n- условия самовывоза (указать район самовывоза) или доставки (лично или курьером)\n-цену (как и ее отстутствие)\nЕсли вы хотите выставить несколько фото одного товара, вы должны выложить их одним общим сообщением, иначе остальные фото будут удалены без предупреждения\n♦️ повторная публикация одного и того же предложения возможна не чаще чем раз в 5 дней\n♦️ если ваш товар продан или запрос выполнен, вы должны удалить свое сообщение, если товар в брони, указать это, пока телеграм дает редактировать сообщение.\nУчастники чата могут просить удалить других участников неактульные предложения\n♦️ каждый месяц, 1-го числа автоматически удаляются все сообщения, поэтому просто перезалейте ваш пост на следующий день\n✅♦️ в чате запрещены:\n-продажа/ дарение любого вида электронных билетов/ товаров/ услуг реализуемых через какой то электронный билет или сертификат и тп. (только типографские с фото билета)\n♦️ в чате недопустимы:\n⚠️разговоры на посторонние темы\n⚠️обсуждения и оценка товаров и их стоимости\n⚠️бронирование ( все в личку)\n⚠️все дополнительные вопросы вы можете задать автору в личные сообщения\n⚠️все остальное удаляется без предупреждения\n♦️ ссылки на другие чаты, сайты, а так же сообщения без ссылок об оказании любого рода услуг, несущих финансовую или любую иную выгоду считаются рекламой и немедленно удаляются без предупреждения.\n✅\n♦️ все предложения о продаже авто/ мото техники , недвижимости и бизнеса относятся к рекламным!!!\nРекламный день в группе - воскресенье. Реклама в чате платная и согласовывается с админами заранее в личку. Так же возможны любые предложения о взаиморекламе ( Олеся - @MrsKapelac Саша - @aradosh \n♦️ участники, игнорирующие правила первый раз, получают предупреждение, за повторное нарушение - бан\n✅♦️все вопросы по правилам чата и иным моментам выясняются с админами лично в личных сообщениях. Если происходит какой-то спорный/ требующий времени для решения/согласования момент и админы пишут,  что вопрос отложен и будет решен в такой то срок, после этого сообщения запрещено настаивать на ответе,  требовать разъяснений,  подсылать группу поддержки и вести прочую переписку,  кроме предоставления новых , не известных на момент переписки  и имеющих важное значение в решении ситуации фактов. За нарушение- автоматический бан ,   в том числе и группы поддержки.\n♦️ ссылка на группу - https://t.me/+dzYBVRHKtPdhMjZk\nУдачных всем покупок и пристроя!💰')
    

@dp.message_handler(text='Заявка на рекламу')
async def answer_reklama_command(message: types.Message, state: FSMContext):
    await message.answer('Как могу к Вам обращаться?..')
    await Form_zakaz.Name.set()
    
@dp.message_handler(state = Form_zakaz.Name)
async def answer_name_funk(message: types.Message, state: FSMContext):
    name = message.text
    if '@' not in name:
        await message.reply('Пожалуйста, введите ваше имя с использованием @. Например, @JohnDoe')
        return

    await state.update_data(name=name)
    await message.answer('Мне нужно Ваше telegram-имя через @..')
    await Form_zakaz.Surname.set()
    
@dp.message_handler(state = Form_zakaz.Surname)
async def answer_surname_funk(message: types.Message, state: FSMContext):
    surname = message.text
    await state.update_data(surname=surname)
    await message.reply('Спасибо!')
    
    data = await state.get_data()
    name = data.get('name')
    surname = data.get('surname')

    await bot.send_message(ADMIN_CHAT_ID, f'Новая заявка на рекламу:\nИмя: {name}\n Фамилия: {surname}')

    await state.finish()
    
    

@dp.message_handler(text='Разместить свое объявление')
async def answer_razmestit_command(message: types.Message, state: FSMContext):
    await message.reply("Заполните, пожалуйста, форму.")
    await message.reply("Текст Вашего объявления. Не забудьте указать район города, если у Вас самовывоз.")
    await Form_publik.Text_ob.set()

@dp.message_handler(state=Form_publik.Text_ob)
async def answer_razm_name_funk(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data(text=text)
    await message.answer('Мне нужно Ваше telegram-имя через @..')
    await Form_publik.Name.set()

@dp.message_handler(state=Form_publik.Name)
async def answer_razm_photo_funk(message: types.Message, state: FSMContext):
    name = message.text
    if '@' not in name:
        await message.reply('Пожалуйста, введите ваше имя с использованием @. Например, @JohnDoe')
        return

    await state.update_data(name=name)
    await message.answer('Прикрепите фото. Пожалуйста, минимум 2 шт. Я умею публиковать только альбомом..')
    await Form_publik.Photo.set()

 




class AlbumMiddleware(BaseMiddleware):

    album_data: dict = {}

    def __init__(self, latency: Union[int, float] = 0.01):
        self.latency = latency
        super().__init__()

    async def on_process_message(self, message: types.Message, data: dict):
        if not message.media_group_id:
            return

        try:
            self.album_data[message.media_group_id].append(message)
            raise CancelHandler() 
        except KeyError:
            self.album_data[message.media_group_id] = [message]
            await asyncio.sleep(self.latency)

            message.conf["is_last"] = True
            data["album"] = self.album_data[message.media_group_id]

    async def on_post_process_message(self, message: types.Message, result: dict, data: dict):
        if message.media_group_id and message.conf.get("is_last"):
            del self.album_data[message.media_group_id]


@dp.message_handler(content_types=types.ContentType.PHOTO, state=Form_publik.Photo)
async def handle_photo(message: types.Message, state: FSMContext, *args, **kwargs):

    await state.update_data(photo=message.photo[-1].file_id)

    data = await state.get_data()
    name = data.get('name')
    text = data.get('text')
    photo = data.get('photo')


    media_group = types.MediaGroup()
    album = kwargs.get('album', [])
    for obj in album:
        if obj.photo:
            file_id = obj.photo[-1].file_id
        else:
            file_id = obj[obj.content_type].file_id

        try:
            media_group.attach({"media": file_id, "type": obj.content_type})
        except ValueError:
            return await message.answer("This type of album is not supported by aiogram.")
    try:
    # await message.answer_media_group(media_group)
        await bot.send_media_group(chat_id=BARAHOLKA_CHAT_ID, media=media_group)

        message_text = f"Новое объявление:\nИмя: {name}\nТекст объявления: {text}"
        await bot.send_message(chat_id=BARAHOLKA_CHAT_ID, text=message_text)
        await message.reply('Ваше объявление опубликовано')

        await state.finish()
    except:
        await message.reply('Вы прикрепили меньше фотографий, чем я просил. Попробуйте заново')
        await state.finish()
    


@dp.message_handler(text='Условия рекламы')
async def answer_uslovija_command(message: types.Message):
    await message.reply(text=f'Рекламный день- ВОСКРЕСЕНЬЕ\n🌟Категория "товары"\nОдин пост - 1000 дин\nС закрепом на месяц +2000 дин\n🌟Категория "не товары" (недвижимость, машина/яхта/мотоцикл и тд, фирма)\nОдин пост - 1500 дин\nС закрепом на месяц +3000 дин\n🌟Категория "услуги"(в т.ч. реклама чатов и каналов)\nОдин пост -2000 дин\nС закрепом на месяц+ 4000дин')
    
@dp.message_handler(text='отмена')
async def cancel_handler0(message: types.Message, state: FSMContext):
    await state.finish()
    await message.reply('ОК')
    
@dp.message_handler(text='Отмена')
async def cancel_handler1(message: types.Message, state: FSMContext):
    await state.finish()
    await message.reply('ОК')
