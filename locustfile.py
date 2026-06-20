class QueryUser(HttpUser):
    weight = 7
    @task
    def query_pipeline(self):
        self.client.post("/query", json={"query": random.choice(SAMPLE_QUERIES), ...})

class IngestUser(HttpUser):
    weight = 2
    @task
    def ingest_document(self):
        self.client.post("/ingest", files={"file": open(random.choice(TEST_DOCS), "rb")})

class AdminUser(HttpUser):
    weight = 1
    @task
    def check_evaluations(self):
        self.client.get("/evaluations")
