from browser_search import search_google_free
from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from generate import ai_generate

router = Router()


class DialogStates(StatesGroup):
    waiting_for_query = State()  # Ожидание вопроса
    waiting_for_confirmation = State()  # Ожидание подтверждения
    waiting_for_additional_info = State()  # Ожидание уточнений


@router.message(DialogStates.waiting_for_query)
async def handle_query(message: Message, state: FSMContext):
    query = message.text.strip()

    await state.update_data(user_query=query)

    response = await ai_generate(
        f"Определи, где искать ответ на вопрос: '{query}'. "
        "Ответь только 'браузер' или 'нейросеть'.", mode="definder"
    )

    if response.lower() not in ("браузер", "нейросеть"):
        await message.answer(
            "Не могу определить. Попробуй уточнить вопрос.",
            parse_mode="Markdown"
        )
        return

    await state.update_data(answer_type=response.lower())

    await message.answer(
        f"Я рекомендую искать через *{response}*.\n"
        "Точно ищем? (Да/Уточнить)",
        parse_mode="Markdown"
    )
    await state.set_state(DialogStates.waiting_for_confirmation)


@router.message(DialogStates.waiting_for_confirmation)
async def handle_confirmation(message: Message, state: FSMContext):
    user_choice = message.text.lower()
    data = await state.get_data()
    query = data.get("user_query", "")

    if user_choice == "да":
        if data.get("answer_type") == "браузер":
            await message.answer(
                f"🔍 Ищу в браузере: '{query}'...",
                parse_mode="Markdown"
            )

            urls = await search_google_free(query)

            if not urls:
                await message.answer(
                    "Ничего не найдено. Попробуй уточнить запрос.",
                    parse_mode="Markdown"
                )
                return

            response = "Вот что я нашел:\n\n" + "\n".join(
                [f"{i + 1}. [{url}]({url})" for i, url in enumerate(urls[:5])]
            )
            await message.answer(response, parse_mode="Markdown")

        else:
            await message.answer(
                "Генерирую ответ...",
                parse_mode="Markdown"
            )
            response = await ai_generate(query, mode="answer")
            await message.answer(response, parse_mode="Markdown")

        await state.set_state(DialogStates.waiting_for_query)

    elif user_choice == "уточнить":
        await message.answer(
            "Что именно уточнить? Опиши детальнее.",
            parse_mode="Markdown"
        )
        await state.set_state(DialogStates.waiting_for_additional_info)

    else:
        await state.set_state(DialogStates.waiting_for_query)


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await message.answer(
        "Привет! Я помогу тебе найти ответ.\n"
        "Задай вопрос, и я скажу, где лучше искать — в *браузере* или *нейросети*.\n\n"
        "Примеры:\n"
        "- «Где купить билеты на поезд?» → браузер\n"
        "- «Напиши стих» → нейросеть",
        parse_mode="Markdown"
    )
    await state.set_state(DialogStates.waiting_for_query)


@router.message(DialogStates.waiting_for_additional_info)
async def handle_additional_info(message: Message, state: FSMContext):
    additional_info = message.text.strip()
    data = await state.get_data()
    original_query = data.get("user_query", "")

    new_query = f"{original_query}. Уточнение: {additional_info}"
    await state.update_data(user_query=new_query)

    await message.answer(
        "Перепроверяю...",
        parse_mode="Markdown"
    )
    await handle_query(message, state)


@router.message()
async def fallback_handler(message: Message):
    await message.answer(
        "Пожалуйста, используйте команду /start для начала работы.",
        parse_mode="Markdown"
    )
