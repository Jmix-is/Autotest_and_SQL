# Настя Симакова, 28-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request

def test_orders_track():
    response = sender_stand_request.get_orders_track()
    assert response.status_code == 200
