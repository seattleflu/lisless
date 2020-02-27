"""
Command-line entrypoints.
"""

def main():
    """
    Entrypoint for the ``lisless`` command.
    """
    from lisless.server import Server
    Server().serve_forever()

if __name__ == "__main__":
    # Invoked via `python -m lisless`.
    main()
