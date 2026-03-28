from __future__ import annotations

import time
from collections import defaultdict, deque


class FixedWindowRateLimiter:
    def __init__(self, limit: int, window_seconds: int = 60):
        self.limit = limit
        self.window_seconds = window_seconds
        self._events: dict[str, deque[float]] = defaultdict(deque)

    def allow(self, key: str) -> bool:
        now = time.time()
        window_start = now - self.window_seconds
        queue = self._events[key]

        while queue and queue[0] < window_start:
            queue.popleft()

        if len(queue) >= self.limit:
            return False

        queue.append(now)
        return True

    def reset(self) -> None:
        self._events.clear()
