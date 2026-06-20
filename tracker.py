import mlflow

def start_training_job(job_id: UUID, pairs: list[TrainingPair]) -> str:
    with mlflow.start_run(run_name=f"finetune-{job_id}") as run:
        mlflow.log_params({
            "base_model": base_model,
            "training_pair_count": len(pairs),
            "avg_quality_score": mean([p.quality_score for p in pairs]),
            "date_range": f"{min_date} to {max_date}"
        })
        
        # Log training data as artifact
        mlflow.log_artifact(f"training_data/{job_id}.jsonl")
        
        return run.info.run_id
