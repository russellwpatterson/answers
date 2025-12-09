import pytest

from solution import Solution


@pytest.mark.parametrize(
    "test_case, expected_count",
    [
        ("a", 1),
        ("cac", 2),
        ("zab", 6),
        ("russell", 5),
        ("yzabcdefghijklmnopqrstuvwx" * 20, 13195),
        ("abcdefghijklmnopqrstuvwxyz" * 3846, 2599571),
    ],
)
def test_solution(test_case: str, expected_count: int):
    sol = Solution()
    assert sol.findSubstringInWraproundString(test_case) == expected_count
