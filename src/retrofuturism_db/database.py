from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


@dataclass(frozen=True)
class StyleEntry:
    id: str
    era: str
    title: str
    summary: str
    influences: list[str]
    visual_cues: list[str]
    color_palette: list[str]
    materials: list[str]
    architecture: list[str]
    fashion: list[str]
    prompt_tokens: list[str]
    negative_tokens: list[str]
    source_notes: list[str]


class RetrofuturismDB:
    def __init__(self, entries: Iterable[dict]):
        self._entries = [StyleEntry(**entry) for entry in entries]
        self._by_id = {entry.id: entry for entry in self._entries}

    def list_entries(self) -> list[StyleEntry]:
        return sorted(self._entries, key=lambda entry: entry.id)

    def get(self, entry_id: str) -> StyleEntry | None:
        return self._by_id.get(entry_id)

    def search(self, query: str) -> list[StyleEntry]:
        query_lower = query.lower().strip()
        if not query_lower:
            return self.list_entries()

        matches: list[StyleEntry] = []
        for entry in self._entries:
            haystack = " ".join(
                [
                    entry.id,
                    entry.era,
                    entry.title,
                    entry.summary,
                    *entry.influences,
                    *entry.visual_cues,
                    *entry.prompt_tokens,
                ]
            ).lower()
            if query_lower in haystack:
                matches.append(entry)
        return matches


def _default_data_path() -> Path:
    return Path(__file__).resolve().parents[2] / "data" / "retrofuturism_entries.json"


def load_default_db() -> RetrofuturismDB:
    with _default_data_path().open("r", encoding="utf-8") as file:
        data = json.load(file)
    return RetrofuturismDB(data)
