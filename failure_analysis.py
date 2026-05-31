def classify_failure(stderr):

    if not stderr:
        return "unknown"

    if "AssertionError" in stderr:
        return "assertion_error"

    if "SyntaxError" in stderr:
        return "syntax_error"

    if "ImportError" in stderr:
        return "import_error"

    if "ModuleNotFoundError" in stderr:
        return "import_error"

    return "runtime_error"