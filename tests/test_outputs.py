import json
import re
from collections import Counter
from pathlib import Path


REPORT_PATH = Path("/app/report.json")
LOG_PATH = Path("/app/access.log")


def test_report_exists():
    """
    Verifies instruction criterion:
    "/app/report.json is created."
    """
    assert REPORT_PATH.exists()


def test_report_matches_access_log():
    """
    Verifies instruction criterion:
    "Analyze the access log and summarize request count,
    clients involved, and popular pages."
    """

    with LOG_PATH.open() as f:
        lines = [
            line.strip()
            for line in f
            if line.strip()
        ]

    expected_total = len(lines)

    expected_ips = set()
    paths = Counter()

    for line in lines:
        expected_ips.add(line.split()[0])

        match = re.search(
            r'"(?:GET|POST|PUT|DELETE|HEAD|PATCH) (\S+) ',
            line,
        )

        if match:
            paths[match.group(1)] += 1

    expected_unique_ips = len(expected_ips)
    expected_top_path = paths.most_common(1)[0][0]

    with REPORT_PATH.open() as f:
        report = json.load(f)

    assert report["total_requests"] == expected_total
    assert report["unique_ips"] == expected_unique_ips
    assert report["top_path"] == expected_top_path