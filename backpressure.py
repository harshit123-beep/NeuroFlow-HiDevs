async with circuit_breaker("openai"):
    result = await provider.complete(messages)
