import importlib


def _load_translations(locale: str) -> dict:
    try:
        return importlib.import_module(f"otterwiki.translations.{locale}").translations
    except ModuleNotFoundError:
        from otterwiki.translations.en import translations
        return translations


def get_locale(key: str) -> str:
    from otterwiki.server import app
    locale = app.config.get("SITE_LANG", "en")
    _t = _load_translations(locale)
    if key in _t:
        return _t[key]
    from otterwiki.translations.en import translations as _en
    return _en.get(key, key)
