from googlesearch import search
import asyncio

async def search_google_free(query: str, num_results: int = 5) -> list[str]:
    """Возвращает URL топ-N результатов из Google (бесплатно)."""
    try:
        loop = asyncio.get_event_loop()
        results = await loop.run_in_executor(
            None,
            lambda: list(
                search(
                    query,
                    num_results=num_results,
                    lang="ru",  # Язык — русский
                )
            ),
        )
        return results
    except Exception as e:
        print(f"Ошибка поиска: {e}")
        return []