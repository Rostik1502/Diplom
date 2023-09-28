# Ростислав Хижняк земля08а  Дипломая работа

import request


def test_create_and_get_order():
    response = request.post_new_order()
    track = response.json()["track"]

    response = request.get_order_by_track(track)
    assert response.status_code == 200