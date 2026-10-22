"""Unpacks archives of supporting documents that applicants upload."""

import os
import tarfile
import tempfile
import zipfile


def extract_zip(archive_path: str, target: str) -> list[str]:
    """Extract each member that stays inside target and return the names extracted, e.g. ["id.pdf"]."""
    extracted = []
    root = os.path.realpath(target)
    with zipfile.ZipFile(archive_path) as archive:
        for member in archive.namelist():
            if not os.path.realpath(os.path.join(root, member)).startswith(root + os.sep):
                continue
            archive.extract(member, root)
            extracted.append(member)
    return extracted


def extract_tar(archive_path: str, target: str) -> None:
    """Extract a tar archive into target with the safe "data" filter, e.g. "../x" entries are refused."""
    with tarfile.open(archive_path) as archive:
        archive.extractall(target, filter="data")


def scratch_path(name: str) -> str:
    """Return a unique scratch file path for one upload, e.g. scratch_path("id") gives "/tmp/kyc-id-ab12..."."""
    handle, path = tempfile.mkstemp(prefix=f"kyc-{name}-")
    os.close(handle)
    return path
