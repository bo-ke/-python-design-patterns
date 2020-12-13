# Python Design Patterns

如何写出更好的代码——柯博 2020.07.14

> "Design patterns help you learn from others’ successes instead of your own failures"

设计模式最初发源于 C++/Java 等静态语言，Python 语言本身的很多特性已经覆盖了设计模式，甚至用了都不知道，比如：decorator/metaclass/generator/getattr 等。但是写稍微大型的项目时，还是经常力不从心。就如上面引用的那句话，通过设计模式可以学习前人的智慧，写出更好的代码。

## 设计模式六大原则

1. 单一职责原则

   - 一个类只做一件事情，模块化

2. 里氏替换原则

   - 所有使用父类的地方必须能完全替换为使用其子类
   - 即: 子类可以扩展父类的功能,但不能改变父类原有的功能

3. 依赖倒置原则

   - 高层模块不应该依赖低层模块，二者都应该依赖其抽象
   - 抽象不应该依赖实现；实现应该依赖抽象
   - 面向接口编程，而不是面向实现变成，Duck Type

4. 接口隔离原则

   - 一个类对另一个类依赖的接口越少越好

5. 最小知识原则

   - 一个类对另一个类知道的越少越好

6. 开闭原则 - 类、模块、函数对扩展开放，对修改关闭 - 尽量在不修改源代码的情况下进行扩展

> 其实以上的原则不限于类的设计，很多工程上的系统设计也适用

## 常用设计模式

### 创造模式

- [ ] 单例模式 - _Singleton_
- [ ] 工厂模式 - _Factory_

### 结构模式

- [ ] MVC
- [ ] Proxy
- [ ] Decorator

### 行为模式

- [ ] Template
- [ ] State Machine
- [ ] Iterator
- [ ] Command
- [ ] Chain Of Responsibility
- [ ] Chaining Method
- [ ] Visitor
- [ ] Observer
