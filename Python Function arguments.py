#python Functions
def greet(name, msg):
    """This function greets to
    the person with the provided message"""
    print("hi", name + ', ' + msg)
greet("Kiran", "Good morning!")
greet("Kiran","Good morning")
#greet()
def greet(name, msg="True friends are rare!"):
    """
    This function greets the friends nature
    If the message is not provided,
    it defaults to "Good
    morning!"
    """
    print("Hello", name + ', ' + msg)
greet("kiran")
greet("kiran","True friends are rare")
greet(name="Kiran", msg = "True friends are rare!" )


