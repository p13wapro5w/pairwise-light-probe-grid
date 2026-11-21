import math

def lerp(a, b, t):
    """插值。"""
    raise NotImplementedError("TODO: lerp")

def probe_visible(occluded):
    """探针可见性。"""
    raise NotImplementedError("TODO: probe_visible")

def blend(weights, values):
    """多探针混合。"""
    raise NotImplementedError("TODO: blend")

def sh_directional(dc, dir_z, scale):
    """球谐方向项。"""
    raise NotImplementedError("TODO: sh_directional")

def update_interval(importance, base):
    """更新间隔。"""
    raise NotImplementedError("TODO: update_interval")

def cull_probe(occluded):
    """遮挡剔除。"""
    raise NotImplementedError("TODO: cull_probe")

def expand_bounds(bounds, margin):
    """边界扩展。"""
    raise NotImplementedError("TODO: expand_bounds")

def normalize_weights(weights):
    """权重归一。"""
    raise NotImplementedError("TODO: normalize_weights")

def specular_pick(diffuse, glossy):
    """镜面探针。"""
    raise NotImplementedError("TODO: specular_pick")

def hdr_store(value, maximum):
    """HDR 存储。"""
    raise NotImplementedError("TODO: hdr_store")

def weight_sum(weights):
    """权重和。"""
    raise NotImplementedError("TODO: weight_sum")

def inside(pos, low, high):
    """体积内判定。"""
    raise NotImplementedError("TODO: inside")

def grid_index(pos, size):
    """网格索引。"""
    raise NotImplementedError("TODO: grid_index")

def probe_key(seed, index):
    """探针键。"""
    raise NotImplementedError("TODO: probe_key")

def is_lit(energy):
    """能量判定。"""
    raise NotImplementedError("TODO: is_lit")
