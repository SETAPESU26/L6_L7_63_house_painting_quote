"""Lab 6: statement and branch coverage for the house painting quote module."""

import pytest
from house_painting_quote import painting_quote, paint_litres, crew_days


@pytest.mark.parametrize(('paint', 'area', 'coats', 'exterior', 'expected'), [
    ('enamel', 500, 2, True, 32500),
    ('emulsion', 100, 1, False, 5000),  # Minimum quote applies.
    ('distemper', 500, 1, False, 6000),
    ('emulsion', 2001, 1, False, 36018),  # Large-job discount.
    ('enamel', 2001, 1, True, 63032),  # Exterior fee and discount.
    ('emulsion', 2000, 1, False, 40000),  # Boundary: no discount.
])
def test_painting_quote_valid(paint, area, coats, exterior, expected):
    assert painting_quote(paint, area, coats, exterior) == expected


@pytest.mark.parametrize(('paint', 'area', 'coats', 'exterior', 'message'), [
    ('watercolour', 500, 1, False, 'unknown paint'),
    ('emulsion', 0, 1, False, 'invalid job'),
    ('emulsion', -10, 1, False, 'invalid job'),
    ('emulsion', 100, 0, False, 'invalid job'),
    ('distemper', 100, 1, True, 'distemper is for interiors only'),
])
def test_painting_quote_invalid(paint, area, coats, exterior, message):
    with pytest.raises(ValueError, match=message):
        painting_quote(paint, area, coats, exterior)


@pytest.mark.parametrize(('area', 'coats', 'surface', 'expected'), [
    (200, 1, 'smooth', 2),
    (201, 1, 'smooth', 3),  # Rounds up remainder.
    (120, 1, 'rough', 2),
    (121, 1, 'rough', 3),
    (50, 2, 'smooth', 1),
])
def test_paint_litres_valid(area, coats, surface, expected):
    assert paint_litres(area, coats, surface) == expected


def test_paint_litres_invalid_surface():
    with pytest.raises(ValueError, match='unknown surface'):
        paint_litres(100, 1, 'uneven')


@pytest.mark.parametrize(('area', 'painters', 'wallpaper', 'expected'), [
    (800, 2, False, 1),  # Exact daily capacity.
    (801, 2, False, 2),  # Partial day rounds up.
    (800, 2, True, 3),  # Wallpaper removal adds two days.
    (801, 2, True, 4),
])
def test_crew_days_valid(area, painters, wallpaper, expected):
    assert crew_days(area, painters, wallpaper) == expected


@pytest.mark.parametrize('painters', [0, -1])
def test_crew_days_invalid_painters(painters):
    with pytest.raises(ValueError, match='need at least one painter'):
        crew_days(800, painters, False)
