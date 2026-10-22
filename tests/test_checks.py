"""Tests for document naming, storage, and check records. None of them touch the network."""

import os
import tempfile
import unittest
from unittest import mock

from kyc import documents, store


class GeneratedNameTests(unittest.TestCase):
    def test_keeps_allowed_extension_in_lowercase(self) -> None:
        self.assertTrue(documents.generated_name("passport.PDF").endswith(".pdf"))

    def test_rejects_other_extensions(self) -> None:
        with self.assertRaises(ValueError):
            documents.generated_name("script.sh")


class SaveDocumentTests(unittest.TestCase):
    def test_writes_under_upload_dir_with_generated_name(self) -> None:
        with tempfile.TemporaryDirectory() as folder, mock.patch.object(documents, "UPLOAD_DIR", folder):
            path = documents.save_document("passport.pdf", b"%PDF-1.4 test")
            self.assertEqual(os.path.dirname(path), folder)
            with open(path, "rb") as f:
                self.assertEqual(f.read(), b"%PDF-1.4 test")

    def test_rejects_files_over_the_limit(self) -> None:
        with self.assertRaises(ValueError):
            documents.save_document("passport.pdf", b"x" * (documents.MAX_BYTES + 1))


class StoreTests(unittest.TestCase):
    def setUp(self) -> None:
        self.conn = store.connect(":memory:")

    def test_new_check_starts_pending_and_takes_a_status(self) -> None:
        check_id = store.add_check(self.conn, "Ada", "uploads/a.pdf")
        self.assertEqual(store.get_check(self.conn, str(check_id)), (check_id, "Ada", "pending"))
        store.set_status(self.conn, check_id, "approved")
        self.assertEqual(store.get_check(self.conn, str(check_id))[2], "approved")

    def test_unknown_id_returns_none(self) -> None:
        self.assertIsNone(store.get_check(self.conn, "999"))


if __name__ == "__main__":
    unittest.main()
