# Протокол UDP

---

User Datatagram Protocol (UDP) - протокол дейтанрамм пользователя.

### Особенности UDP

- Нет соединения;
- Нет гарантии доставки данных;
- Нет гарантии сохранения порядка сообщений.

Надежность доставки по сравенению с IP не повышается

---

## Формат заголовка UDP

![](https://github.com/v1a0/computer-science-university/blob/main/img/udp-header.png)

### Длина UDP

- Минимум 8 байт (только заголовок);
- Максимум 65515 байт (максимальная длина данных ip-пакета).

---

## Применение UDP

- Нет накладных расходов на установку соединения;
- В современных сетях ошибки происходят редко;
- Ошибку может обработать приложение.

### Область применения

- Клиент-серевер;
- Короткие запросы-ответы.

---
