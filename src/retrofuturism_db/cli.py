from __future__ import annotations

import argparse
import json

from .database import load_default_db


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Retrofuturism reference database")
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("list", help="List available style entries")

    get_parser = subparsers.add_parser("get", help="Fetch one style entry by id")
    get_parser.add_argument("entry_id")

    search_parser = subparsers.add_parser("search", help="Search entries by text")
    search_parser.add_argument("query")

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    db = load_default_db()

    if args.command == "list":
        payload = [entry.id for entry in db.list_entries()]
    elif args.command == "get":
        entry = db.get(args.entry_id)
        payload = entry.__dict__ if entry else None
    elif args.command == "search":
        payload = [entry.__dict__ for entry in db.search(args.query)]
    else:
        raise ValueError(f"Unsupported command: {args.command}")

    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
