# finite_automata

Як я писала скінченний автомат для свого дня:
Вирішила, що для кожного стану і івенту створю екземпляр відповідного класу, бо так простіше звертатись до них і їхніх зв'язків (якщо це стан) з іншими станами. В деяких станів і івентів тривалість більша, ніж одна година (я могла б зробити і по одній годині все, але трохи не дуже реалістично, що я сплю годину, потім працюю годину, потім знову сплю годину і так далі). На кількість прийомів їжі стоїть обмеження - мінімум 1 раз на день має викликатись цей стан, але максимум тричі, бо багато їсти теж шкідливо :). Сон має викликатись принаймі один раз, триває чотири години, але після 7 викликатись вже не може - вийнятком є рандомний івент "денний сон".
Ще цікавий момент в івентах: протягом кожної ітерації в чергу додається один з чотирьох івентів (у кожного свій шанс додавання, найбільший у куріння, найменший у денного сну), а далі, якщо рандомний відсоток менший за установлений відсоток викликання події, то з черги дістається цей івент (тоді в години додається тривалість івенту, а не стану, бо вони можуть відрізнятися). З кожною пройденою без івентів годиною ймовірність випадання самого івенту зростає, після випадання події цей шанс скидується до дефолтного.
Вночі не може викликатись стан "їсти", ну, бо я вночі майже ніколи не їм :).
Для черги використовувала вбудовану бібліотеку queue.
Ось моя діаграма станів:
![image](https://github.com/Drakonchyk/finite_automata/assets/63148058/979bc247-02ea-46e9-bcd6-a9fbcc4abac0)
Перший приклад роботи автомату:
![image](https://github.com/Drakonchyk/finite_automata/assets/63148058/b99e5153-86b2-4a73-96c2-26d6cc1a16c2)
![image](https://github.com/Drakonchyk/finite_automata/assets/63148058/834ca59a-a8ac-4d85-bdba-3f3640a6f960)
Другий приклад роботи автомату:
![image](https://github.com/Drakonchyk/finite_automata/assets/63148058/c0f03dc6-e41c-4ac3-8c80-c6d317077673)
![image](https://github.com/Drakonchyk/finite_automata/assets/63148058/76e1eed4-6807-4200-be55-8c9045e546cf)
