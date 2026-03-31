import asyncio


def section(title: str) -> None:
    print()
    print("=" * 72)
    print(title)


async def asyncio_edge_cancellation_demo() -> None:
    section("asyncio edge cancellation demo")
    task = asyncio.current_task()
    assert task is not None

    print("[asyncio] calling task.cancel() once")
    task.cancel()

    try:
        print("[asyncio] first await")
        await asyncio.sleep(0)
    except asyncio.CancelledError:
        print("[asyncio] caught CancelledError once")

    try:
        print("[asyncio] second await")
        await asyncio.sleep(0)
        print("[asyncio] second await succeeds (cancellation was not re-injected)")
    except asyncio.CancelledError:
        print("[asyncio] second await cancelled again")


async def anyio_level_cancellation_demo() -> None:
    section("AnyIO level cancellation demo")
    try:
        import anyio
    except ModuleNotFoundError:
        print("[anyio] not installed. Install with: python3 -m pip install anyio")
        return

    cancelled_exc = anyio.get_cancelled_exc_class()

    with anyio.CancelScope() as scope:
        print("[anyio] cancel scope now")
        scope.cancel()

        try:
            print("[anyio] first await in cancelled scope")
            await anyio.sleep(0)
        except cancelled_exc:
            print("[anyio] first await cancelled")

        try:
            print("[anyio] second await in cancelled scope")
            await anyio.sleep(0)
            print("[anyio] second await unexpectedly succeeded")
        except cancelled_exc:
            print("[anyio] second await cancelled again (level cancellation)")

    print("[anyio] outside cancelled scope, awaits work again")
    await anyio.sleep(0)
    print("[anyio] completed")


async def main() -> None:
    await asyncio_edge_cancellation_demo()
    await anyio_level_cancellation_demo()


if __name__ == "__main__":
    asyncio.run(main())
