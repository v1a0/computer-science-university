

```c

class SomeClass {

  private int someAttribute; // <-- Attribute (declaration)

  public void setSomeAttribute( int attrValue /* <-- Parameter (declaration) */ ) {
    int twice = attrValue * 2; // (local) variable
    this.someAttribute = twice;
  }

  public void doSomethingElse() {
    int x; // (local) variable
    x = 1;
    setSomeAttribute(x); // the value of x is the argument
    setSomeAttribute(999); // 999 is the argument
  }
}

```