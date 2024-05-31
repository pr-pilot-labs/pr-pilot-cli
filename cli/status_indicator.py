from rich.console import Console
from yaspin import yaspin


class StatusIndicator:

    def __init__(self, spinner=True, messages=True, console=None):
        self.spinner = yaspin("Let's go", timer=True)
        self.visible = spinner
        self.messages = messages
        self.console = console if console else Console()

    def update(self, text):
        if self.visible:
            self.spinner.text = text
        elif self.messages:
            self.console.print(f"[bold]>[/bold] {text}")

    def success(self):
        if self.visible:
            self.spinner.ok("✅ ")
            self.spinner.start()

    def fail(self):
        if self.visible:
            self.spinner.fail("❌ ")
            self.spinner.stop()

    def start(self):
        if self.visible:
            self.spinner.start()

    def stop(self):
        if self.visible:
            self.spinner.stop()