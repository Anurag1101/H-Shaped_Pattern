# pyramid printing using text alignment in string.

# Get the thickness (height of the letter H) from the user
thickness = int(input("Enter the thickness of the letter H: "))

# The character used to draw the H
c = 'H'

# Top vertical bars of the H (two sides of H)
for i in range(thickness):
    # Print the left vertical bar, center H, and right vertical bar
    print((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))

# Upper horizontal bar of the H (top crossbar)
for i in range(thickness + 1):
    # Print the two horizontal bars side by side
    print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

# Middle horizontal bar of the H (the longest crossbar)
for i in range((thickness + 1) // 2):
    # Print the wide horizontal bar in the center
    print((c * thickness * 5).center(thickness * 6))

# Lower horizontal bar of the H (bottom crossbar)
for i in range(thickness + 1):
    # Print the two horizontal bars side by side again
    print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

# Bottom vertical bars of the H (mirroring the top section)
for i in range(thickness):
    # Print the left vertical bar, center H, and right vertical bar, mirrored
    print(((c * (thickness - i - 1)).rjust(thickness) + c + (c * (thickness - i - 1)).ljust(thickness)).rjust(thickness * 6))