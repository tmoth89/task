import json
from pathlib import Path


REPORT_PATH = Path("/app/report.json")


def test_report_exists():
    """
    Verifies instruction criterion:
    "Create the output report file at /app/report.json."
    """
    assert REPORT_PATH.exists(), "Missing /app/report.json"


def test_report_is_valid_json_with_required_fields():
    """
    Verifies instruction criterion:
    "The report must contain a summary of request count,
    clients involved, and popular pages."
    """
    with REPORT_PATH.open() as f:
        report = json.load(f)

    assert isinstance(report, dict)

    assert "total_requests" in report
    assert "unique_ips" in report
    assert "top_path" in report


def test_report_field_formats():
    """
    Verifies instruction criterion:
    "The report contains correctly formatted summary values."
    """
    with REPORT_PATH.open() as f:
        report = json.load(f)

    assert isinstance(report["total_requests"], int)
    assert isinstance(report["unique_ips"], int)
    assert isinstance(report["top_path"], str)