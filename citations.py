@dataclass
class Citation:
    reference: str        # "Source 1"
    chunk_id: UUID
    document_name: str
    page_number: int | None
    content_preview: str  # first 100 chars of cited chunk
