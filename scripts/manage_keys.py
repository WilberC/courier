#!/usr/bin/env python
"""CLI for managing per-user API keys.

Usage:
    uv run python scripts/manage_keys.py create --user-id 1 --name "backup-job"
    uv run python scripts/manage_keys.py list --user-id 1
    uv run python scripts/manage_keys.py revoke --key-id 3
    uv run python scripts/manage_keys.py users
"""
from __future__ import annotations

import argparse
import sys

from sqlmodel import Session

from app.db.api_keys import create_key, list_user_keys, revoke_key
from app.db.session import get_engine
from app.db.users import get_by_id, list_users
from app.db.init_db import init_db


def cmd_create(args: argparse.Namespace) -> None:
    engine = get_engine()
    init_db(engine)
    with Session(engine) as session:
        user = get_by_id(session, args.user_id)
        if user is None:
            print(f"Error: user {args.user_id} not found.", file=sys.stderr)
            sys.exit(1)
        key_record, raw_key = create_key(session, args.user_id, args.name)
    print(f"Created API key [{key_record.id}] for user {args.user_id} ({args.name})")
    print(f"Key prefix : {key_record.key_prefix}...")
    print(f"Raw key    : {raw_key}")
    print("Store this key safely — it will not be shown again.")


def cmd_list(args: argparse.Namespace) -> None:
    engine = get_engine()
    with Session(engine) as session:
        keys = list_user_keys(session, args.user_id)
    if not keys:
        print(f"No API keys for user {args.user_id}.")
        return
    print(f"API keys for user {args.user_id}:")
    for k in keys:
        status = "active" if k.is_active else "revoked"
        print(f"  [{k.id}] {k.name!r}  prefix={k.key_prefix}...  {status}  last_used={k.last_used_at}")


def cmd_revoke(args: argparse.Namespace) -> None:
    engine = get_engine()
    with Session(engine) as session:
        ok = revoke_key(session, args.key_id)
    if ok:
        print(f"Key {args.key_id} revoked.")
    else:
        print(f"Key {args.key_id} not found.", file=sys.stderr)
        sys.exit(1)


def cmd_users(_args: argparse.Namespace) -> None:
    engine = get_engine()
    with Session(engine) as session:
        users = list_users(session, active_only=False)
    if not users:
        print("No users found.")
        return
    for u in users:
        status = "active" if u.is_active else "inactive"
        print(f"  [{u.id}] tg={u.telegram_user_id}  @{u.username}  role={u.role}  {status}  last_seen={u.last_seen_at}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Courier API key manager")
    sub = parser.add_subparsers(dest="command", required=True)

    p_create = sub.add_parser("create", help="Create a new API key for a user")
    p_create.add_argument("--user-id", type=int, required=True)
    p_create.add_argument("--name", required=True)

    p_list = sub.add_parser("list", help="List API keys for a user")
    p_list.add_argument("--user-id", type=int, required=True)

    p_revoke = sub.add_parser("revoke", help="Revoke an API key by ID")
    p_revoke.add_argument("--key-id", type=int, required=True)

    sub.add_parser("users", help="List all users")

    args = parser.parse_args()
    {"create": cmd_create, "list": cmd_list, "revoke": cmd_revoke, "users": cmd_users}[
        args.command
    ](args)


if __name__ == "__main__":
    main()
