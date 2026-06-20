async def retrieve(query: str, k: int = 20) -> list[RetrievalResult]:
    results = await asyncio.gather(
        self._dense_retrieval(query, k),
        self._sparse_retrieval(query, k),
        self._metadata_retrieval(query, k)
    )
    return self._fuse(results)
