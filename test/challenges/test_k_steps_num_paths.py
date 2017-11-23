from src.challenges.k_steps_num_paths import k_steps_num_paths


def test_k_steps_num_paths():
    assert k_steps_num_paths((4, 4), k=4) == 0
    assert k_steps_num_paths((1, 1), k=2) == 2
    assert k_steps_num_paths((1, 2), k=3) == 4
    assert k_steps_num_paths((1, 1), k=1) == 0
    assert k_steps_num_paths((1, 2), k=0) == 0
