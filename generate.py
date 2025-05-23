from config import AI_TOKEN
from openai import AsyncOpenAI

client = AsyncOpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=AI_TOKEN,
)
async def ai_generate(text: str, mode: str):
    completion = await client.chat.completions.create(
        model="deepseek/deepseek-chat",
        messages=[
            {
                "role": "user",
                "content": """### **Идеальный промпт для нейросети с расширенной классификацией запросов**  

**Контекст:**  
На основе опроса среди учеников 9–11 классов был проведён анализ учебных запросов, чтобы определить, какие из них эффективнее решать через **поисковые системы** (Google, Яндекс), а какие — через **нейросети** (ChatGPT, DeepSeek и др.). Результаты исследования были использованы для создания **Telegram-бота**, который автоматически рекомендует пользователю оптимальный способ поиска ответа.  

---

### **Структурированные данные для бота**  

#### **1. Запросы, которые лучше решать через поисковую систему**  
_(Конкретные факты, таблицы, алгоритмы, учебные материалы, тесты, официальные источники)_  

**Основные категории:**  
- **Английский язык**:  
  - Поиск слов, перевод текстов.  
- **Химия**:  
  - Разбор реакций (например, `H₂SO₄ электрическая диссоциация`).  
  - Формулы реакций с концентрированной серной кислотой.  
  - *«Электрохимический ряд напряжений металлов»*  
  - *«Готовые лабораторные работы по химии 10 класс»*  
- **Математика/Геометрия**:  
  - Решение задач по геометрии.  
  - Варианты ОГЭ/ЕГЭ, номера по вероятности и статистике.  
  - Таблицы (Менделеева, квадратов, синусов, дееспособности, интегралов).  
  - *«Решение варианта ЕГЭ по математике 2025»*  
  - *«Готовые ответы на задачи из учебника Мордковича»*  
- **Биология**:  
  - Разбор фотосинтеза (ЕГЭ), варианты ОГЭ/ЕГЭ.  
  - Строение человека, КПД лампы накаливания.  
- **История/Обществознание**:  
  - Сражения при Николае II, Конституция 1918 года.  
  - Повседневная жизнь в СССР, даты по истории.  
  - Права и свободы граждан РФ, виды правоохранительных органов.  
  - *«Даты Второй мировой войны»*  
  - *«Текст Конституции РФ, статья 15»*  
- **Литература/Русский язык**:  
  - Краткие содержания ("Война и мир", "Преступление и наказание", "Герой нашего времени").  
  - Шаблоны сочинений (ОГЭ 13.3), ударения, типы сказуемых.  
  - Стихотворения (например, «Море» Лермонтова).  
  - *«Анализ стихотворения «Парус» Лермонтова»* (если нужен разбор из учебника).  
- **Информатика**:  
  - Команды в Python (циклы `for`, факториал).  
  - Решение задач на сайтах ("Решу ЕГЭ", "Сдам ГИА").  
  - *«Синтаксис цикла for в Python»*  
  - *«Как установить библиотеку Pandas»*  
- **Другие**:  
  - *«Адреса и телефоны учебных заведений»*  
  - *«График проведения ОГЭ 2025»*  

---

#### **2. Запросы, которые лучше решать через нейросеть**  
_(Объяснение концепций, развёрнутые ответы, генерация текстов, решение нестандартных задач)_  

**Основные категории:**  
- **Математика/Физика**:  
  - Формулы (геометрическая прогрессия, Герона, ускорения).  
  - Теоремы (Пифагора, Фалеса, Виета, Бернулли).  
  - Правило буравчика, закон Ома.  
  - *«Объясните, как работает метод математической индукции»*  
  - *«Почему небо синее? Объясните на уровне 9 класса»*  
- **Химия/Биология**:  
  - Алгоритмы решения задач по химии.  
  - *«Почему у крокодила 4-камерное сердце?»*  
  - *«Как предсказать продукты реакции без таблицы растворимости?»*  
- **Программирование**:  
  - Библиотеки Python, разработка алгоритмов.  
  - *«Почему мой код на Python выдаёт ошибку IndexError?»*  
  - *«Объясните разницу между REST и GraphQL»*  
- **Обществознание/Право**:  
  - Определения (правовые отношения, административная ответственность).  
  - *«Сравните причины Французской и Русской революций»*  
  - *«Как объяснить понятие «социальный лифт» простыми словами?»*  
- **Литература/Русский язык**:  
  - Написание сочинений, анализ стихов.  
  - *«Напишите сочинение-рассуждение на тему «Что такое доброта?»»*  
  - *«Как связаны образы Печорина и Онегина?»*  
- **Сложные/творческие вопросы**:  
  - *«Придумайте задачу по физике для 10 класса на тему термодинамики»*  
  - *«Объясните теорию струн так, чтобы понял пятиклассник»*  

---

### **Формат ответа бота**  
Пользователь отправляет учебный запрос → бот анализирует его по ключевым словам и контексту, затем выдаёт рекомендацию:  
- ✅ **«Лучше найти ответ в поисковой системе»** — для точных данных, таблиц, готовых решений.  
- 🤖 **«Лучше найти ответ в нейросети»** — для объяснений, сравнений, генерации текстов.  

**Примеры работы бота:**  
- *«Таблица Менделеева»* → ✅ **Поисковик**.  
- *«Почему в таблице Менделеева элементы расположены именно так?»* → 🤖 **Нейросеть**.  
- *«Как решить уравнение x² + 5x + 6 = 0?»* → ✅ **Поисковик** (если нужен алгоритм).  
- *«Почему квадратные уравнения решаются через дискриминант?»* → 🤖 **Нейросеть**.  

---

### **Правила классификации для бота**  
1. **Поисковая система**, если запрос содержит:  
   - Слова: *«таблица»*, *«вариант ЕГЭ»*, *«конституция»*, *«даты»*, *«как установить»*, *«синтаксис»*.  
   - Запросы на готовые решения, точные данные, официальные источники.  
2. **Нейросеть**, если запрос:  
   - Начинается с *«объясните»*, *«почему»*, *«сравните»*, *«как написать»*.  
   - Требует интерпретации, творческого подхода или решения нестандартной задачи.  

---

### **Итог**  
Объединённый промпт сохраняет все примеры и логику из обоих текстов, дополняя их новыми деталями. Такой подход:  
1. **Упрощает настройку бота** — чёткие критерии для классификации.  
2. **Покрывает больше запросов** — добавлены частые примеры из практики.  
3. **Делает ответы точнее** — минимизирует ошибки в рекомендациях.  
""" if mode == "definder" else "Развёрнуто ответь на поставленный вопрос"
            },
            {
                "role": "user",
                "content": text
            }
        ]
    )
    print(completion)
    return completion.choices[0].message.content
