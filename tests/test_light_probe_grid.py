import pytest
import math
from render import light_probe_grid as mod

CASES = [
    ("lerp", 'm.lerp(0, 10, 0.5) == approx(5.0)'),
    ("visible", 'm.probe_visible(False) is True'),
    ("blend", 'm.blend([1, 1], [2, 4]) == approx(3.0)'),
    ("sh", 'm.sh_directional(1, 1, 2) == approx(7)'),
    ("interval", 'm.update_interval(2, 8) == 4'),
    ("cull", 'm.cull_probe(True) is False'),
    ("bounds", 'm.expand_bounds((1, 2, 3, 4), 1) == (0, 1, 5, 6)'),
    ("norm", 'm.normalize_weights([1, 3]) == approx([0.25, 0.75])'),
    ("spec", 'm.specular_pick(1, 2) == 2'),
    ("hdr", 'm.hdr_store(1200, 1000) == 1000'),
    ("wsum", 'm.weight_sum([1, 2, 3]) == 6'),
    ("inside", 'm.inside(2, 0, 3) is True'),
    ("grid", 'm.grid_index(3, 2) == 1'),
    ("key", 'm.probe_key(3, 2) == "3:2"'),
    ("lit", 'm.is_lit(0.5) is True')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx, "math": math})
