import sys
import subprocess

if len(sys.argv) > 1:
    repo_input = sys.argv[1].strip()
    branch = None
    folder = None

    if "/tree/" in repo_input:
        parts = repo_input.split("/tree/")
        repo = parts[0]
        branch = parts[1].split("/")[0]
        folder = repo.split("/")[-1] + "-" + branch
    else:
        repo = repo_input

    url = f"{repo}.git"

    command = ["git", "clone"]
    if branch:
        command += ["--branch", branch, "--single-branch"]
    command.append(url)
    if folder:
        command.append(folder)

    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        print(f"\n✔ Cloned: {url}" + (f" (branch: {branch})" if branch else ""))
        print(result.stdout.strip())
    except subprocess.CalledProcessError as e:
        print(f"\n✖ Failed to clone: {url}" + (f" (branch: {branch})" if branch else ""))
        print(e.stderr.strip())
else:
    from textual.app import App, ComposeResult
    from textual.containers import Vertical, Horizontal
    from textual.widgets import Static, Input, Button, Footer
    from textual.binding import Binding
    from textual.reactive import reactive

    class GitCloneApp(App):
        BINDINGS = [
            Binding(key="q", action="quit", description="Quit the app"),
            Binding(
                key="question_mark",
                action="show_code",
                description="Show/hide the code",
                key_display="?",
            ),
        ]
        CSS_PATH = "app.tcss"
        repo_name = reactive("")

        def compose(self) -> ComposeResult:
            with Vertical():
                with Horizontal(id="project-row"):
                    yield Static("Enter the link of the repo:", id="project-label")
                    yield Input(placeholder="GitHub repo", id="project-input")
                    yield Button("Clone", id="clone-button")
                yield Static("", id="status")
            yield Footer()

        def on_input_changed(self, event: Input.Changed) -> None:
            self.repo_name = event.value.strip()

        def on_button_pressed(self, event: Button.Pressed) -> None:
            if event.button.id == "clone-button" and self.repo_name:
                button = self.query_one("#clone-button", Button)
                button.add_class("button-pressed")
                self.set_timer(0.5, lambda: button.remove_class("button-pressed"))
                self.clone_repo(self.repo_name)

        def clone_repo(self, repo: str) -> None:
            status = self.query_one("#status", Static)

            branch = None
            if "/tree/" in repo:
                parts = repo.split("/tree/")
                repo = parts[0]
                branch = parts[1].split("/")[0]
                folder = repo.split("/")[-1] + "-" + branch


            url = f"{repo}.git"

            command = ["git", "clone"]
            if branch:
                command += ["--branch", branch, "--single-branch"]
            command.append(url)
            if folder:
                command.append(folder)

            try:
                result = subprocess.run(
                    command,
                    check=True,
                    capture_output=True,
                    text=True
                )
                status.update(
                    f"[green]✔ Cloned:[/] {url}"
                    + (f" [dim](branch: {branch})[/dim]" if branch else "")
                    + f"\n\n[dim]{result.stdout.strip()}[/dim]"
                )
            except subprocess.CalledProcessError as e:
                status.update(
                    f"[red]✖ Failed to clone:[/] {url}"
                    + (f" [dim](branch: {branch})[/dim]" if branch else "")
                    + f"\n\n[red]{e.stderr.strip()}[/red]"
                )

        def on_mount(self) -> None:
            try:
                label_widget = self.query_one("#clone-button", Button)
                self.set_focus(label_widget)
            except Exception:
                self.set_focus(None)

        def action_show_code(self) -> None:
            status_widget = self.query_one("#status", Static)
            
            if not status_widget.content:
                
                repo_url_part = self.repo_name if self.repo_name else "https://github.com/user/repo"
                full_clone_command = f"git clone {repo_url_part}.git"
                foldername = "examplefolder"
                branch = "branchname"
                full_clone_branch_command = f"git -b {branch} --single-branch clone {repo_url_part}.git repo-{branch}"
                
                status_widget.update(
                    "[bold cyan]This application uses the 'git clone' command, which is used as follows:[/bold cyan]\n\n"
                    f"For whole repos: [yellow]{full_clone_command}[/yellow]\n\n"
                    f"For a specific branch: [yellow]{full_clone_branch_command}[/yellow]\n\n"
                    "[dim]Press '?' again to hide this code.[/dim]"
                )
            else:
                status_widget.update("")

    if __name__ == "__main__":
        GitCloneApp().run()