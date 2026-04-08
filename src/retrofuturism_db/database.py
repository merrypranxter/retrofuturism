from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable


@dataclass(frozen=True)
class StyleEntry:
    id: str
    era: str
    title: str
    summary: str
    influences: list[str] = field(default_factory=list)
    visual_cues: list[str] = field(default_factory=list)
    color_palette: list[str] = field(default_factory=list)
    materials: list[str] = field(default_factory=list)
    architecture: list[str] = field(default_factory=list)
    fashion: list[str] = field(default_factory=list)
    shape_language: list[str] = field(default_factory=list)
    pattern_systems: list[str] = field(default_factory=list)
    ornament_logic: list[str] = field(default_factory=list)
    symbol_systems: list[str] = field(default_factory=list)
    composition_rules: list[str] = field(default_factory=list)
    lighting_atmosphere: list[str] = field(default_factory=list)
    typography_graphics: list[str] = field(default_factory=list)
    common_subjects: list[str] = field(default_factory=list)
    regional_variants: list[str] = field(default_factory=list)
    historical_context: list[str] = field(default_factory=list)
    modern_reinterpretation: list[str] = field(default_factory=list)
    adjacent_styles: list[str] = field(default_factory=list)
    prompt_tokens: list[str] = field(default_factory=list)
    negative_tokens: list[str] = field(default_factory=list)
    usage_notes: list[str] = field(default_factory=list)
    source_notes: list[str] = field(default_factory=list)

    @classmethod
    def from_dict(cls, payload: dict[str, Any]) -> "StyleEntry":
        list_fields = {
            "influences",
            "visual_cues",
            "color_palette",
            "materials",
            "architecture",
            "fashion",
            "shape_language",
            "pattern_systems",
            "ornament_logic",
            "symbol_systems",
            "composition_rules",
            "lighting_atmosphere",
            "typography_graphics",
            "common_subjects",
            "regional_variants",
            "historical_context",
            "modern_reinterpretation",
            "adjacent_styles",
            "prompt_tokens",
            "negative_tokens",
            "usage_notes",
            "source_notes",
        }
        normalized = dict(payload)
        for field_name in list_fields:
            normalized[field_name] = list(normalized.get(field_name, []))
        return cls(**normalized)


class RetrofuturismDB:
    def __init__(self, entries: Iterable[dict[str, Any]]):
        self._entries = [StyleEntry.from_dict(entry) for entry in entries]
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
                    *entry.pattern_systems,
                    *entry.symbol_systems,
                    *entry.typography_graphics,
                    *entry.common_subjects,
                    *entry.adjacent_styles,
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
