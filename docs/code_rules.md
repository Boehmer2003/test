Code Rules RvIHH
========================================

-  Header Boilerplate
    - Alle bronbestanden (.hpp en .cpp) moeten de voorgeschreven header bevatten.
    -	De header moet de volgende velden bevatten: bestandsnaam, product of subsysteem, originele auteur en een korte beschrijving.

```cpp
  // ---------------------------------------------------------------------
  //                                                                     
  // Filename:                                                           
  //   <filename>.hhp                                                    
  //                                                                     
  // Product or product-subsystem:                                       
  //   <name of the end-product or module that this file belongs to>     
  //                                                                     
  // Original author:                                                    
  //   <original author>                                                 
  //                                                                     
  // Description:                                                        
  //   <a very brief description of the contents of the file>            
  //                                                                     
  // ---------------------------------------------------------------------
```

- Indentation
    -   Gebruik twee spaties voor inspringing.
    -   Het gebruik van tabs is verboden.

```
void Loop(int loops) { 
  int result = 0; // twee spaties
    result += 5; // vier spaties
} 
```

- Single Line Comments
    -   Gebruik // voor opmerkingen, in plaats van /* ... */.
    -   Voor grote stukken code: gebruik precompiler-voorwaarden (#ifdef of #if).

- Curly Braces
    - Opening accolade op dezelfde regel als de voorgaande statement.
    - Sluitende accolade op een nieuwe regel.
    - Voor if-else: else op dezelfde regel als de sluitende accolade van if.
```cpp
void Foo() {
  if (i < 10) {
    i += 10;
  } else {
    i -= 2;
  }
}
```

- Curly Braces for Single-Line Blocks
    -   Gebruik altijd accolades, ook voor enkelvoudige regels code binnen een loop of voorwaardelijke statement.

``
if (0 == nrOfItems) {
  AddNewItem();
}
``

- Multiple Conditions
    -   Bij meerdere condities in één statement moeten de condities in haakjes worden gezet.

```cpp
if ((value == 5) || (stopped)) {
  DoSomeThing();
}
```

- Switch Cases
    -   Gebruik een switch-case om over een volledige enum te itereren.

```cpp
int foo(ExampleKey_e key) {
    switch(key) {
        case ExampleKey_e::A: return 1;
        case ExampleKey_e::B: return 2;
        case ExampleKey_e::C: return 3;
        case ExampleKey_e::END_OF_ENUM: return 4;
    }
    return 5; // Unreachable, maar nodig om waarschuwingen te voorkomen
}
```

- Implicit Casts
    -   Gebruik -casts zoals static_cast<>(). Vermijd C-stijl casts zoals (int)x.
    -   Gebruik (void) casts om aan te geven dat een variabele of argument niet wordt gebruikt.

- Pointer and Reference Declaration
    -   Plaats het * of & symbool bij het type, niet bij de variabelenaam.

  ```cpp
  int* intExample;
  bool& boolExample;
  ```

- Class/Struct Access Modifiers
    -   De toegangsmodifiers (public, protected, private) worden gerangschikt van public naar private.
    -   Methoden en ledenvariabelen worden gescheiden.

```cpp
class Device {
public:
    int publicMember {42};


protected:
    int protectedMember {120};


private:
    const double PI {3.14159265358979};
};
```

```cpp
methoden en ledenvariable gescheiden
class Example {
    public:
        def GetName(){
            return name
        }
        def SetName(string newName){
            name = newNaam
        }
    private:
        string name
}
```

- Member Variable Order
    -   Ordening van ledenvariabelen: built-ins eerst, dan custom types.
    -   de variable moeten ook op grooten geordend worden(bool, char, int, float, double)

```cpp
class Device {
private:
  bool m_b {false};
  std::uint8_t m_u8 {0};
  CustomClass m_class;
};
```
 
- Member Variable Initialization
    -   Initialiseer variabelen via constructorargumenten, inline in de member definitie of via -   configuratievariabelen.
    -   Gebruik brace-initializers voor variabelen.

```cpp
class Counter {
public:
  explicit Counter(unsigned int repeatFor = 1) : m_repeatFor{repeatFor} {}

private:
  unsigned int m_repeatFor {};
};
```

- Include "" vs <>
    -   Bibliotheekbestanden worden opgenomen met < >.
    -   Applicatiebestanden worden opgenomen met " ".

```cpp
include "Buzzer.h"
include <driver/ledc.h>
```

- Naming: Multiple Words

    -   Variabelen beginnen met een kleine letter. (camelCase)
    -   Functies ,classes en structs beginnen met een hoofdletter(PascalCase).

```cpp
int roomTemperature;
double drivingSpeed;
char GetDefaultCharacter();
```

- Member Variables Prefix
    -   Klasseleden krijgen de prefix m_.

```cpp
class Test {
private:
  int m_value {};
};
```

- Interface Names
    -   Interfacenamen worden voorafgegaan door de hoofdletter I_.

```cpp
class I_Test {
public:
  virtual void FunctionToBeImplementedByDerivedClass() = 0;
};
```

- File Names
    -   Bestandsnamen zijn gelijk aan de klasse die geïmplementeerd wordt.

```cpp
Type bestand Bestandsnaam
Interface bestand I_MotorController.hpp
Header bestand MotorController.hpp
Source bestand MotorController.cpp
```

- Custom Types Naming
    -   Custom structs eindigen op t, custom enumerations op e.

```cpp
enum class MyEnum_e { VALUE_1, VALUE_2 };
struct MyStruct_t { int m_member1 {}; };
```

- Constant Values
    -   Constante waarden worden in hoofdletters geschreven, met underscores tussen woorden.

```cpp
const double BRAKING_FORCE = 12.1123;
constexpr int MAX_ENTRIES = 5;
```

- Template Parameters
    -   Templateparameters die constanten zijn, volgen de regels voor constante waarden.

```cpp
template<typename FuncType, int MAX_HANDLERS>
class InterruptHandler {
private:
  std::array<FuncType, MAX_HANDLERS> m_handlers {};
};
```