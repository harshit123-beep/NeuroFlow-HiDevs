async def submit_finetune_job(jsonl_path: str, base_model: str) -> str:
    client = AsyncOpenAI()
    file_resp = await client.files.create(file=open(jsonl_path, "rb"), purpose="fine-tune")
    job = await client.fine_tuning.jobs.create(training_file=file_resp.id, model=base_model)
    return job.id
