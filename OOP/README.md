# Object-Oriented Programming (OOP)

## Core Concepts
### Classes & Objects
- Classes as blueprints for objects
- Attributes store data, methods define behaviors
- Constructor (`__init__`) for object initialization

### Inheritance
- Child classes inherit from parent classes
- `Rectangle` and `Circle` inherit from `Shape`
- `Employee` inherits from `Person`

### Polymorphism
- Overriding methods in child classes
- `Dog` and `Cat` override `speak()` from `Animal`
- Same method name, different implementations

### Encapsulation
- Access control: Public, Protected (`_`), Private (`__`)
- BankAccount with private `__balance`
- Car with private `__speed` controlled via `accelerate()`

### Abstraction
- Simplified interfaces hiding complexity
- Abstract `Animal` class with `make_sound()`
- Implementation in concrete classes (`Cat`, `Dog`)

## Practical Exercises
### Shapes Hierarchy
1. `Shape` base class with `area()`
2. `Rectangle` and `Circle` subclasses
3. `print_info()` method showing polymorphism

### Bank Account System
- Private account details with validation
- Deposit/withdraw methods with balance checks
- Getter methods for encapsulated data

### Animal Sounds
- Polymorphic `speak()` method
- `Dog` → "Woof Woof!", `Cat` → "Meow Meow!"
- `animal_speak()` function demonstrating polymorphism

### Car Controller
- Encapsulated speed attribute
- Public `accelerate()` method
- Getter method for controlled access
