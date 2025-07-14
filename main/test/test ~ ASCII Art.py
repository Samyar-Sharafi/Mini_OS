
ASCII = open("./assets/ASCII/Octodex.txt", "r")

Octodex = ASCII.read()

print(Octodex)



ASCII = open("./assets/ASCII/tux.txt", "r")
tux = ASCII.read()
print(f"[bold blue]{tux}[/bold blue]")