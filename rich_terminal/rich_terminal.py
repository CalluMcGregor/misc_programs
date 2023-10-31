# from rich import print
# print("Hello, [bold magenta]World[/bold magenta]!", ":vampire:")

from rich.console import Console
from rich.panel import Panel

console = Console()

# Create a Panel with a title and content
panel = Panel.fit("this is a colored box with rounded edges!", title="text box example", border_style="blue")

# Display the panel
console.print(panel)


