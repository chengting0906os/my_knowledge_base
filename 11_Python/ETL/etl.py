"""
ETL Practice — JSONPlaceholder Posts
-------------------------------------
Extract  : fetch posts from a public REST API
Transform: filter short posts, compute word_count
Load     : upsert into SQLite via SQLAlchemy
"""

import httpx
from sqlalchemy.orm import Session
from models import Post, get_engine, init_db


API_URL = "https://jsonplaceholder.typicode.com/posts"
MIN_WORD_COUNT = 20   # filter threshold


# ---------------------------------------------------------------------------
# Extract
# ---------------------------------------------------------------------------

def extract(url: str = API_URL) -> list[dict]:
    response = httpx.get(url, timeout=10)
    response.raise_for_status()
    return response.json()


# ---------------------------------------------------------------------------
# Transform
# ---------------------------------------------------------------------------

def transform(raw: list[dict]) -> list[dict]:
    result = []
    for item in raw:
        word_count = len(item["body"].split())

        if word_count < MIN_WORD_COUNT:   # drop very short posts
            continue

        result.append({
            "id":         item["id"],
            "user_id":    item["userId"],
            "title":      item["title"].strip().capitalize(),
            "body":       item["body"].strip(),
            "word_count": word_count,
        })
    return result


# ---------------------------------------------------------------------------
# Load
# ---------------------------------------------------------------------------

def load(records: list[dict], engine) -> int:
    """Upsert records; returns number of rows written."""
    with Session(engine) as session:
        for data in records:
            post = session.get(Post, data["id"])
            if post is None:
                post = Post(**data)
                session.add(post)
            else:
                for key, value in data.items():
                    setattr(post, key, value)
        session.commit()
    return len(records)


# ---------------------------------------------------------------------------
# Pipeline
# ---------------------------------------------------------------------------

def run_pipeline() -> None:
    engine = get_engine()
    init_db(engine)

    print("Extracting ...")
    raw = extract()
    print(f"  fetched {len(raw)} records")

    print("Transforming ...")
    records = transform(raw)
    print(f"  {len(records)} records passed filter (word_count >= {MIN_WORD_COUNT})")

    print("Loading ...")
    written = load(records, engine)
    print(f"  {written} rows upserted into DB")

    print("Done.")


if __name__ == "__main__":
    run_pipeline()
