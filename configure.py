from pathlib import Path
from enum import Enum


class MODE(Enum):
    DEV = "dev"
    PRO = "pro"


g_mode: MODE = MODE.PRO


class MakeConfig:
    class _BaseConf:
        title = "项目名称"

    class _DevConf(_BaseConf):
        url = "dev url"

    class _ProConf(_BaseConf):
        url = "pro url"

    def __init__(self, _mode: MODE):
        self._config = None
        self._use(_mode)

    def _use(self, _mode: MODE):
        if _mode == MODE.DEV:
            self._config = self._DevConf()
        else:
            self._config = self._ProConf()

    @property
    def url(self):
        return self._config.url

    @property
    def title(self):
        return self._config.title

    @property
    def mode(self):
        return g_mode


__all__ = ["MODE", "MakeConfig"]
