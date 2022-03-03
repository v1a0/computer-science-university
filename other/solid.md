# SOLID

5 принципов

## Принципы 

- [ S ] Single Responsibility principle 
- [ O ] Open-Close principle
- [ L ] Liskov Substitution principle
- [ I ] Interface Segregation principle
- [ D ] Dependency Inversion principle




## Соблюдение гарантирует:

- Расширяемость/поддержка кода =>меньшие затраты
- Увеличивает читаемость кода 
- Упрощает поиск ошибок


# SRP - Single Responsibility principle

Через конкретный класс в процессе разработки должна проходить только одна ось изменений 
(класс должен меняться только по одной причине). 
Поля и методы должны относиться только к конкретному предназначению всего класса. Отвечает только за свои дела.

```
WRONG:
    
    Class
    +-------------+
    |  DateTime   |
    |      +      |
    | Temperature |
    +-------------+
    
    
RIGHT:
    
    Class                Class
    +-------------+      +----------------------+
    |  DateTime   | -----|                      |
    +-------------+      |                      |
                         |                      |
    Class                | DateTime-Temperature |
    +-------------+      |                      |
    | Temperature |------|                      |
    +-------------+      +----------------------+
```

God object - антипаттерн объектно-ориентированного программирования, описывающий объект, 
который хранит в себе «слишком много» или делает «слишком много»




# OCP - Open-Closed principle

Программные сущности (модули, функции и пр.) должны быть открыты для расширения, но закрыты для изменения.

Любой блок кода должен быть "открыт" для того, чтобы в него можно было добавить дополнительную функциональность.

## Принципы:

1. Расширение доступно только по принципу наследования от старшего класса.
2. Клиентский код должен зависть от интерфейса, который НЕИЗМЕННЫЙ!

```

    +-------------+      +-----------+
    |   Client    |----->| Interface |
    +-------------+      +-----------+
                            |    |
        +-------------+     |    |      +-------------+       
        |  Old Code   |<----+    +----->|  New Code   |
        +-------------^                 +-------v-----+
                      |                         |       
                      +--<---------<--------<---+                                                             
```

В чем смысл:
- Если прошлая функциональность не была изменена, в ней не появится новых багов => не нужно проводить полное регрессионное тестирование всего кода
- Исключения bugfix!



# LSP - Liskov Substitution principle

Функции которые используют базовые типы должны иметь возможность использовать подтипы базового типа не зная об этом.

Если есть код в который приходит базовый класс (parent), то в этот же код без каких либо исключений (exceptions) должен 
входить любой его наследник. Если наследник ломает код, то принцип нарушен.

> Пусть q(x) является свойством, верным относительно объектов x некоторого типа T. Тогда q(y) также должно быть верным для объектов y типа S, где S является подтипом типа T.

Поведение наследующих классов не должно противоречит поведению заданному базовым классом.

Подкласс не должен требовать от вызывающего кода больше чем базовый класс, и не должен предоставлять вызывающему коду 
меньше чем базовый класс.


```python
class ParentDB:

    def get_user(self, u_id: int):
        """
        Returns user
        """
        data = ...
        return RealData(data)
        
    def add_user(self, u_id: int, username: str):
        """
        Returns user
        """
        ORM.add_user(u_id, username)
    
# WRONG
class ChildDB(ParentDB):

    def get_user(self, u_id: int, super_new_arg: bool):
        return None
        
    def add_user(self, u_id: int, username: str):
        raise NotImplemented

# RIGHT
class AnotherChildDB(ParentDB):

    def get_user(self, u_id: int, username: str = None):
        if username is None:
            data = super().get_user(u_id)
        else:
            data = ...
        return RealData(data)
        
    def add_user(self, u_id: int, username: str):
        super().get_user(u_id)
```

# Пример реально проблемы

```python
class Rectangular:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b
    
    def set_a(self, val: int):
        self.a = val

    def set_b(self, val: int):
        self.b = val

class Square(Rectangular):
    def __init__(self, a: int):
        super().__init__(a, a)
    
    @property
    def b(self):
        return self.a
        
    def set_a(self, val: int):
        self.a = val

    def set_b(self, val: int):
        raise NotImplemented
```



# ISP - Interface Segregation principle

Много интерфейсов предназначенных для клиента — лучше, чем один интерфейс общего предназначения.

Клиенты не должны зависеть от методов, которые они не используют, 
т.е. если какой-то метод интерфейса не используется клиентом,
то изменение этого метода не должно приводить к необходимости изменений в клиентский код.

```

Class                  Interface
+-----------+          +-----------+
|     X     |----------|     X     |
+-----------+          +-----------+
                         | | | | |
                         | | | | +-----< Сlient_1
                         | | | +-------< Сlient_1, Сlient_2
                         | | +---------< Сlient_2
                         | +-----------< Сlient_3
                         +-------------< Сlient_3

Ну ты понял, нужно чтобы было много разных интерфейсов для разных клиентов, а не 1 большой
```

### Для чего:

- Безопаснее, дает клиентам только те возможности, что им нужны
- Интерфейс должен являться принадлежностью КЛИЕНТА, а поэтому клиент (, а не сервер) определяет интерфейс. Backend must to, так сказать.
- Чем проще и минималистичнее интерфейс, тема менее ресурсоёмкое является его реализация в новых классах и тем меньше причин его модификации (SRP)




# Dependency Inversion principle

Модули верхних уровней не должны зависеть от модулей нижних уровней. Оба типа модулей должны зависеть от абстракций.

Абстракции не должны зависеть от абстракций. Детали должны зависеть от абстракций.

Использовать классы рекомендуется исключительно через интерфейсы. Позволяет в любое место системы встроить дополнительный функционал.



----
----
----


# Ещё раз

# SOLID

- Single Responsibility
- Open-Closed
- Liskov
- Interfaces segregation
- Dependency inversion


# Single responsibility principle
## Принцип единственной ответственности

У модуля должна быть только одна причина для изменения (не очень)

Класс должен отвечать только за какую-то единственную задачу, 
так чтобы в случае изменения задействовать наименьшее количество модулей.

Также говорят об оси изменений, в процессе разработки она должна проходить только через один класс.


```python

"""
Bad example
"""

class Car:
    def __init__(self, color=None, name=None, code=None, id=None):
        pass
    
    def order_car(self):
        pass
    
    def get_cars_from_db(self, color=None, name=None, code=None):
        pass
    
    def get_all_cars(self):
        pass
```

```python

"""
Good example
"""

class Buyer:
    def order_car(self):
        pass

class Database:
    def get_cars(self, color=None, name=None, code=None):
        pass
    
    def get_all_cars(self):
        pass

class Car:
    def __init__(self, color=None, name=None, code=None):
        pass

```



# Open-Closed

## Принцип Открытости и Закрытости

Модуль должен быть открыт для расширения, но закрыт для изменения.

Абстракция — интерфейс реализации классов потомков (?)

```python

"""
Bad Example
"""

class Car:
    def __init__(self, brand: str):
        self.brand = brand
    
    @property
    def price(self):
        if self.brand == 'BMW':
            return 2_000_000
        elif self.brand == 'Honda':
            return 1_000_000
        else:
            return 0
```


```python
from abc import abstractmethod

"""
Good Example
"""

@abstractmethod
class Car:
    @property
    @abstractmethod
    def price(self):
        pass

class BMW(Car):
    @property
    def price(self):
        return 2_000_000

class Honda(Car):
    @property
    def price(self):
        return 1_000_000
```



# Lickov substitution

## Принцип подстановки Барбары Лисков

Необходимо, чтобы подклассы могли служить для замены своих super-классов.

Функции использующие базовый тип должны иметь возможность использовать его подтипы.

Но в реальности (из-за дополнительных проверок логики) лучше 
для обоих классов лучше использовать общий интерфейс, а не наследовать
один класс от другого.

```python
"""
BAD EXAMPLE
"""

class Rectangle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
    
    def set_width(self, width: float):
        self.width = width
    
    def set_height(self, height: float):
        self.height = height


class Square(Rectangle):
    def __init__(self, size: float):
        super().__init__(size, size)

    def set_width(self, width: float):
        self.width = width
        self.height = width
    
    def set_height(self, height: float):
        self.height = height
        self.width = height

def make_fit(figure: Rectangle):
    """
    figure fit it it's have 20x50 form
    """
    figure.set_width(20)
    figure.set_height(50)
    
    # expected figure 20x50 

my_rec = Rectangle(10, 15)
my_sq = Square(15)

make_fit(my_rec) # 20x50
make_fit(my_sq) # 50x50
```

В общем не стоило переопределять метод родительского класса.
На крайняк тогда уж стоило делать абстрактный класс Figure,
с абстр. методами изменения высоты и ширины, а от него уже
наследовать все последующие.

Это помогает выявлять проблемные абстракции и скрытые связи
между сущностями, делать модули предсказуемыми.


# Interface segregation

## Принцип разделения (декомпозиции) интерфейсов

Сущности не должны зависеть от интерфейсов, которые они используют.

В общем нужно смотреть, чтобы класс потомок не получал херову тучу ненужной функциональности. 
Поэтому нужно эти родительские классы декомпозировать, а не склеивать в один Бого-класс



# Dependency inversion

## Принцип инверсии зависимостей

Модули высших уровней не должны зависеть от модулей низких уровней.
Оба должны зависеть от абстракций.

Абстракции не должны зависеть от деталей, детали должны зависеть от абстракций.

Иначе:

Верхне-уровневые сущности не должны зависеть от нижне-уровневых
реализаций, а любые зависимости лучше всего выносить в абстракции.

(цель: уменьшение межмодульных зависимостей)
(как итог: читаемость, понятность, тестируемость)



https://www.youtube.com/watch?v=A6wEkG4B38E