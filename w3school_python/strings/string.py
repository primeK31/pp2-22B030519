print("Hello")
print('Hello')

a = "Hello"
print(a)

# Multiline Strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# or

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

# as arrays
a = "Hello, World!"
print(a[1])  # outp: "e"

# Looping Through a String
for x in "banana":
    print(x)
    # outp:
    # b
    # a
    # n
    # a
    # n
    # a

# length
a = "Hello, World!"
print(len(a))  # out: "13"

# Check String(in)
txt = "The best things in life are free!"
print("free" in txt)  # outp: true

txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")

txt = "The best things in life are free!"
print("expensive" not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")