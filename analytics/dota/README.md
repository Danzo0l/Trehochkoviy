Возвращаемые значения метода start()
============
Словарь с полями:

* "score" - Общая оценка командности игрока
* "role" - позиция, на которой играет игрок ( role <= 60 - Core, role > 60 - Support)
* "comparing_skill" - показатели в сравнении с другими игроками ( если < 50, то хуже чем игроки это рейтинга, если > 50, то лучше)
* "benefit" - Польза игрока для игры (если < 50, то набирает меньше чем игроки это рейтинга, если > 50, то больше)
* "frequency_fight" - процент участия в командных убийствах