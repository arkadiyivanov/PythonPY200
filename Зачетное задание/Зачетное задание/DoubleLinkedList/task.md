Двусвязный список на основе односвязного списка.

1. Односвязный список `LinkedList` должен быть унаследован он абстрактного типа `MutableSequence` из модуля `collections.abc`.
   
2. В односвязном списке должны быть реализованы следующие методы:
    - **`__getitem__`**
    - **`__setitem__`**
    - **`__delitem__`**
    - **`__len__`**
    - **`__str__`**
    - **`__repr__`**
    - **`insert`**
    - **`append`**
   
3. Все атрибуты должны быть инкапсулированы.  
   То есть быть либо private или protected по вашему выбору. 
   
4. Двусвязный список `DoubleLinkedList` должен наследоваться от `LinkedList`.  
   Для экземпляров данного класса должны работать все методы базового класса.  
   
   Необязательно все эти методы должны быть перегружены. 
   По максимуму используйте наследование, если поведение списков в контексте реализации указанных метод схоже.  
   С точки зрения наследования по минимуму перегружайте методы.  
   При необходимости рефакторите базовый класс, чтобы локализовать части кода во вспомогательные функции,  
   которые имеют различное поведение в связном и двусвязном списках.
   
   Стремитесь к минимизации кода в дочернем классе.

   
## Дополнительные задания:
Эти задания приветствуются, но оцениваться не будут. Будут вам плюсиком в карму.

Реализовать следующие методы:
   - **`__iter__`**
   - **`__contains__`**
   - **`__reversed__`**

   - **`count`**
   - **`pop`**
   - **`extend`**
   - **`remove`**
   - **`index`**
