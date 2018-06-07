from django import template

register = template.Library()


@register.filter
def formatru(endings, number):
    endings = endings.split(",")
    if number % 100 // 10 == 1:
        return endings[2]
    if number % 10 == 1:
        return endings[0]
    if 2 <= number % 10 <= 4:
        return endings[1]
    return endings[2]
