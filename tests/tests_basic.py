def test_imports():
    # Make sure modules load.
    import app
    import app.net
    import app.server
    import app.client
    assert True