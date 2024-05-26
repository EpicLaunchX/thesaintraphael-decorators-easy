from unittest import mock

from pytemplate.entrypoints.cli.main import main


class TestCliEntypoint:
    def test_underage_children(self, capsys):
        with mock.patch("builtins.input", side_effect=["Cars", "5", "6"]):
            main()
            captured = capsys.readouterr()
            assert "Sorry, you are not old enough to watch Cars!" in captured.out

    def test_valid_children_age(self, capsys):
        with mock.patch("builtins.input", side_effect=["Spies in Disguise", "8", "6"]):
            main()
            captured = capsys.readouterr()
            assert "You are allowed to watch Spies in Disguise!" in captured.out

    def test_invalid_age_limit(self, capsys):
        with mock.patch("builtins.input", side_effect=["Spies in Disguise", "8", "90"]):
            main()
            captured = capsys.readouterr()
            assert "Invalid age limit! Please enter 6 or 13 for the age limit" in captured.out

    def test_valid_teen_age(self, capsys):
        with mock.patch("builtins.input", side_effect=["The Matrix", "16", "13"]):
            main()
            captured = capsys.readouterr()
            assert "You are allowed to watch The Matrix!" in captured.out

    def test_invalid_teen_age(self, capsys):
        with mock.patch("builtins.input", side_effect=["The Matrix", "12", "13"]):
            main()
            captured = capsys.readouterr()
            assert "Sorry, you are not old enough to watch The Matrix!" in captured.out
