
"""
Firestore Caching Layer

This module provides simple get/set functions for a time-to-live (TTL)
cache using Google Firestore in Datastore mode.

It relies on the `gcloud` environment being set up correctly for authentication.
For local development, this is typically achieved via:
`gcloud auth application-default login`

The cache uses a dedicated collection and stores expiration timestamps
to manage TTL.
"""

import os
from datetime import datetime, timedelta, timezone
from google.cloud import firestore

# Initialize Firestore client. It will automatically use the credentials
# set up in the environment (e.g., via `gcloud auth application-default login`).
try:
    db = firestore.Client()
    # Use a specific collection for cache entries to keep them separate.
    CACHE_COLLECTION = "aeronewsfra_cache"
except Exception as e:
    db = None
    CACHE_COLLECTION = None
    print(f"Warning: Firestore client could not be initialized. Caching will be disabled. Error: {e}")

def set_in_cache(key: str, value: dict, ttl_seconds: int = 60):
    """
    Saves a value to the Firestore cache with a specific TTL.

    Args:
        key (str): The unique key for the cache entry.
        value (dict): The dictionary value to cache.
        ttl_seconds (int): The time-to-live for the cache entry in seconds.
    """
    if not db:
        return

    try:
        expires_at = datetime.now(timezone.utc) + timedelta(seconds=ttl_seconds)
        doc_ref = db.collection(CACHE_COLLECTION).document(key)
        doc_ref.set({
            'value': value,
            'expires_at': expires_at
        })
    except Exception as e:
        print(f"Error setting cache for key '{key}': {e}")


def get_from_cache(key: str) -> dict | None:
    """
    Retrieves a value from the Firestore cache if it exists and has not expired.

    Args:
        key (str): The key to look up in the cache.

    Returns:
        dict | None: The cached value if found and valid, otherwise None.
    """
    if not db:
        return None

    try:
        doc_ref = db.collection(CACHE_COLLECTION).document(key)
        doc = doc_ref.get()

        if not doc.exists:
            return None

        data = doc.to_dict()
        expires_at = data.get('expires_at')

        # Ensure expires_at is a timezone-aware datetime object for comparison
        if isinstance(expires_at, datetime) and expires_at.tzinfo is None:
             expires_at = expires_at.replace(tzinfo=timezone.utc)


        if expires_at and expires_at > datetime.now(timezone.utc):
            return data.get('value')
        else:
            # The entry has expired, so we can delete it (optional cleanup)
            doc_ref.delete()
            return None
    except Exception as e:
        print(f"Error getting cache for key '{key}': {e}")
        return None
