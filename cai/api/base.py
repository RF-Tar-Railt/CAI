from cai.client.session import Session


class BaseAPI:
    session: Session

    async def _executor(
        self, func_name: str, *args, uncaught_error=False, **kwargs
    ):
        if not hasattr(self.session, func_name):
            raise AttributeError(f"client has no attribute '{func_name}'")
        try:
            return await getattr(self.session, func_name)(*args, **kwargs)
        except Exception:
            if uncaught_error:
                await self.session.close()
            raise
