import math

def lerp(a, b, t):
    """插值。"""
    return a + (b - a) * t

def probe_visible(occluded):
    """探针可见性。"""
    return not occluded

def blend(weights, values):
    """多探针混合。"""
    total = sum(weights)
    if total == 0:
        return 0.0
    return sum(w * v for w, v in zip(weights, values)) / total

def sh_directional(dc, dir_z, scale):
    """球谐方向项。"""
    return dc + 3.0 * dir_z * scale

def update_interval(importance, base):
    """更新间隔。"""
    if importance <= 0:
        return base
    return base // importance

def cull_probe(occluded):
    """遮挡剔除。"""
    return not occluded

def expand_bounds(bounds, margin):
    """边界扩展。"""
    x, y, width, height = bounds
    return (x - margin, y - margin, width + 2 * margin, height + 2 * margin)

def normalize_weights(weights):
    """权重归一。"""
    total = sum(weights)
    if total == 0:
        return [0.0 for _ in weights]
    return [w / total for w in weights]

def specular_pick(diffuse, glossy):
    """镜面探针。"""
    return glossy

def hdr_store(value, maximum):
    """HDR 存储。"""
    return min(value, maximum)

def weight_sum(weights):
    """权重和。"""
    return sum(weights)

def inside(pos, low, high):
    """体积内判定。"""
    return low <= pos <= high

def grid_index(pos, size):
    """网格索引。"""
    return int(pos // size)

def probe_key(seed, index):
    """探针键。"""
    return f"{seed}:{index}"

def is_lit(energy):
    """能量判定。"""
    return energy > 0
