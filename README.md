# Computer Science University

- Algo
    - [Хэш таблицы, коллизии, сложность [RUS]](https://habr.com/ru/post/509220/)

- Python
    - Basic Python
        - LEVEL 0
          - [Corey Schafer - Python Tutorial for Beginners](https://www.youtube.com/watch?v=YYXdXT2l-Gg&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7)
          - [OS Module](https://youtu.be/tJxcKyFMTGo)
          - [Reading and Writing to Files](https://youtu.be/Uh2ebFW8OYM)
          - [venv crib sheet](python/basics/venv.md)
          - [Set the Path, Switch Between Different Versions (Unix)](https://youtu.be/PUIE7CPANfo)
          - [CSV](https://youtu.be/q5uM4VKywbA)
          - [Datetime Module](https://youtu.be/eirjjyP2qcQ)
        - LEVEL 1
            - Syntax and features
                - [Comprehensions](https://www.youtube.com/watch?v=3dt4OGnU5sM)
                - [Generators (yield)](https://www.youtube.com/watch?v=bD05uGo_sVI)
                    - [Examples](python/basics/generators.py)
            - OOP
                - [Classes and Instances #1](https://www.youtube.com/watch?v=ZDa-Z5JzLYM)
                - [Classes and Instances #2](https://www.youtube.com/watch?v=BJ-VvGyQxho)
                - [Classes and Instances #3 🔥](https://www.youtube.com/watch?v=rq8cL2XMM5M)
                - [Inheritance - Creating Subclasses](https://www.youtube.com/watch?v=RSl87lqOXDE)
                - [Magic (Special/Dunder) Methods](https://www.youtube.com/watch?v=3ohzBxoFHAY)
    
    - Python under the hood
        - LEVEL 1
            - About Interpreter 
                - [What is the Python Interpreter? And how does it work.](https://www.youtube.com/watch?v=BkHdmAhapws)
            
            - Mutability
                - [((( notes )))](python/memory/mutable-immutable.md)
                - [Immutable and Mutable Types](https://www.youtube.com/watch?v=Bxr_ZYzC924) 
                - [Programming Terms: Mutable vs Immutable](https://www.youtube.com/watch?v=5qQQ3yzbKp8)
                - [Python List in Memory](https://www.youtube.com/watch?v=fWAf_yFk6A0)
                - [Immutable vs Mutable Objects in Python](https://www.youtube.com/watch?v=p9ppfvHv2Us&t=336s)
            
            - Complexity
               - [Complexity of Python Operations](./python/complexity/complexity.md)
            
            - Memory Management
                - [Garbage Collector (GC)](https://www.youtube.com/watch?v=arxWaw-E8QQ)
                - [GC and GIL in Python](https://www.youtube.com/watch?v=URNdRl97q_0)
            
            -
            
        - LEVEL 2 - Threads, GIL
            - GIL - Global Interpreter Lock
                - [Python's Infamous GIL by Larry Hastings](https://www.youtube.com/watch?v=KVKufdTphKs)
                - [Understanding the GIL](https://www.youtube.com/watch?v=Obt-vMVdM8s) (web: https://dabeaz.com/GIL)
                - [Beating Python's GIL to Max Out Your CPUs (by Andrew Montalenti)](https://www.youtube.com/watch?v=gVBLF0ohcrE)
            -
        - LEVEL 3 - Async/await
            - [Что внутри у питона: откуда быть пошел async](https://www.youtube.com/watch?v=GX7AUAwpQ4I)
            -
          
    - CSC 2015 [RUS]
        - [1. Начало](https://compscicenter.ru/courses/python/2015-autumn/classes/1364/)
            - [notes](./python/csc-2015/1.md)
        - [2. Всё, что вы хотели знать о функциях в Python](https://compscicenter.ru/courses/python/2015-autumn/classes/1386)
            - [notes](./python/csc-2015/2.md)
        - [3. Декораторы и модуль functools](https://compscicenter.ru/courses/python/2015-autumn/classes/1387/)
            - [notes](./python/csc-2015/3.md)
        - [4. Строки, байты, файлы и ввод/вывод](https://compscicenter.ru/courses/python/2015-autumn/classes/1388/)
            - [notes](./python/csc-2015/4.md)
        - [5. Встроенные коллекции и модуль collections](https://compscicenter.ru/courses/python/2015-autumn/classes/1476/)
            - [notes](./python/csc-2015/5.md)
        - [6. Классы](https://compscicenter.ru/courses/python/nsk/2018-autumn/classes/4273/) ?
            - [notes]()
- PostgreSQL
    - [pgexercises.com](https://pgexercises.com)
        - [Simple SQL Queries (Solutions)](./sql/pgexercises.com/basic-sql.md) 
        - [Joins ans Subqueries (Solutions)](./sql/pgexercises.com/joins-and-subqueries.md)
        - [Modifying data (Solutions)](./sql/pgexercises.com/modifying-data.md)

- Development
    - SOLID
        - [RUS] [Solid принципы (by Sergey Nemchinskiy)](https://www.youtube.com/playlist?list=PLmqFxxywkatQNWLG1IZYUhKoQrnuZHqaK)
            - [SRP (Принцип единственной ответственности, Single Responsibility Principle)](https://www.youtube.com/watch?v=O4uhPCEDzSo&list=PLmqFxxywkatQNWLG1IZYUhKoQrnuZHqaK&index=1)
            - [OCP (Открытости/закрытости, Open Closed Principle)](https://www.youtube.com/watch?v=x5OtQiKOG-Q&list=PLmqFxxywkatQNWLG1IZYUhKoQrnuZHqaK&index=2)
            - [LSP (Принцип подстановки Барбары Лисков, The Liskov Substitution Principle)](https://www.youtube.com/watch?v=NqvwYcjrwdw&list=PLmqFxxywkatQNWLG1IZYUhKoQrnuZHqaK&index=3)
            - [ISP (Принцип Разделения Интерфейса, The Interface Segregation Principle)](https://www.youtube.com/watch?v=d9RJqf2o_Sw&list=PLmqFxxywkatQNWLG1IZYUhKoQrnuZHqaK&index=4)
            - [DIP (Принцип инверсии зависимостей, The Dependency Inversion Principle)](https://www.youtube.com/watch?v=Bw6RvCSsETI&list=PLmqFxxywkatQNWLG1IZYUhKoQrnuZHqaK&index=5)
            - [MY NOTES](./other/solid.md)
        
    - KISS
        - [RUS] [Принцип хорошего кода KISS (Keep It Short and Simple/Stupid)](https://www.youtube.com/watch?v=rix-fkrloq4)
    
    - YAGNI
        - [RUS] [Принцип хорошего кода YAGNI (You Aren't Gonna Need It)](https://www.youtube.com/watch?v=rix-fkrloq4)

    - OOP 
        - [RUS] Принципы ООП (by Sergey Nemchinskiy)
            - [1. Инкапсуляция](https://www.youtube.com/watch?v=EvGi6XDgV7w)
            - [2. Наследование](https://www.youtube.com/watch?v=eI0XzQw3V0Q)
            - [3. Полиморфизм](https://www.youtube.com/watch?v=Ay_GwOQWPs8)
    
    - Transactions
        - [Транзакции (Владимир Кузнецов)](https://www.youtube.com/playlist?list=PLmqFxxywkatR3Psg4pz0Br0uDHzjR9Sne)





## Contributors


<a href="https://github.com/iva1010">
<img src="https://avatars.githubusercontent.com/u/58352066?v=4" height="50px">
</a> 
C, Network, Linux/Unix

<br>

<a href="https://github.com/v1a0">
<img src="https://avatars.githubusercontent.com/u/54343363?v=4" height="50px">
</a> 
Python, PostgreSQL
