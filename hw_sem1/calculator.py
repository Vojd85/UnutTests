import numbers

def calculate_discount(order_value, discount_value):
    if not isinstance(order_value, numbers.Number) or not isinstance(discount_value, numbers.Number):
        raise ArithmeticError('Значения должны быть числами')
    if order_value < 0:
        raise ArithmeticError('Сумма покупки не может быть меньше нуля')
    if discount_value < 0:
        raise ArithmeticError('Скидка не может быть меньше нуля')
    if discount_value > 100:
        raise ArithmeticError('Скидка не может быть больше 100%')
    return order_value - discount_value / 100 * order_value