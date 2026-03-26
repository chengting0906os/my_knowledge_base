# Anyio vs asyncio

## Biggest Difference: Structured Concurrency vs Fire-and-Forget

The biggest practical gap is task lifecycle control.

- `AnyIO` pushes you toward structured concurrency (`create_task_group()`).
- Plain `asyncio` makes it easy to do fire-and-forget (`create_task(...)` and move on).

## Why This Matters

- With structured concurrency, child tasks are tied to the parent scope.
- You cannot accidentally leave orphan/background tasks running forever.
- Errors and cancellation are propagated in a predictable way.

## AnyIO Style (Preferred)

```python
import anyio

async def worker(name):
    await anyio.sleep(1)
    print(name)

async def main():
    async with anyio.create_task_group() as tg:
        tg.start_soon(worker, "A")
        tg.start_soon(worker, "B")
```

All child tasks must finish (or fail/cancel) before leaving the task group.

## asyncio Fire-and-Forget Risk

```python
import asyncio

async def worker():
    await asyncio.sleep(10)
    print("done")

async def main():
    asyncio.create_task(worker())  # fire-and-forget
    await asyncio.sleep(1)
```

`main()` can exit while `worker()` is still running.  
This is convenient, but easy to misuse in production.

## Note

`asyncio` also has `TaskGroup` (Python 3.11+), which provides structured concurrency.
So the real difference is often team discipline and default coding style, not raw capability.

## Cancellation Model (Most Important)

Both sides raise a cancellation exception.
The key difference is when and how many times cancellation is delivered.

### asyncio: Edge Cancellation

- `cancel()` schedules one cancellation injection.
- You usually get one `CancelledError`.
- If code catches and swallows it, execution can continue.

```python
import asyncio

async def demo():
    task = asyncio.current_task()
    task.cancel()

    try:
        await asyncio.sleep(0)
    except asyncio.CancelledError:
        print("caught once")

    await asyncio.sleep(0)  # continues
    print("still running")
```

### AnyIO/Trio: Level Cancellation

- `cancel_scope.cancel()` puts execution into a cancelled state.
- As long as you stay inside that cancelled scope, each checkpoint (`await`) gets cancelled again.
- Catching once does not clear cancellation state.

```python
import anyio

async def demo():
    cancelled_exc = anyio.get_cancelled_exc_class()
    with anyio.CancelScope() as scope:
        scope.cancel()
        try:
            await anyio.sleep(0)
        except cancelled_exc:
            print("cancelled at first await")
        try:
            await anyio.sleep(0)
        except cancelled_exc:
            print("cancelled again at second await")
```

### Quick Comparison

| Topic | asyncio | AnyIO / Trio |
| --- | --- | --- |
| Cancellation model | Edge | Level |
| How many times cancellation is raised | Usually once per cancel request | Repeatedly at checkpoints inside cancelled scope |
| If cancellation is swallowed | Task can continue | Next `await` is cancelled again (inside scope) |
| Risk of hidden half-cancelled work | Higher | Lower |

### Why It Matters in Production

- Request timeout handling
- Graceful shutdown
- Cancelling background work
- Preventing resource leaks from half-cancelled tasks

## Runnable Test

See `11_Python/anyio_vs_asyncio_cancellation_test.py` for a side-by-side demo.
