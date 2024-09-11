### ⚙️ Options and Parameters

The CLI has global parameters and options that can be used to customize its behavior.


```bash
Usage: pilot [OPTIONS] COMMAND [ARGS]...

  PR Pilot CLI - https://docs.pr-pilot.ai

  Delegate routine work to AI with confidence and predictability.

Options:
  --wait / --no-wait        Wait for PR Pilot to finish the task.
  --repo TEXT               Github repository in the format owner/repo.
  --spinner / --no-spinner  Display a loading indicator.
  --verbose                 Display status messages
  -m, --model TEXT          GPT model to use.
  -b, --branch TEXT         Run the task on a specific branch.
  --sync / --no-sync        Run task on your current branch and pull PR Pilots
                            changes when done.
  --debug                   Display debug information.
  --help                    Show this message and exit.

Commands:
  chat     💬 Chat with PR Pilot.
  config   🔧 Customize PR Pilots behavior.
  edit     ✍️ Let PR Pilot edit a file for you.
  grab     🤲 Grab commands, prompts and plans from other repositories.
  history  📜 Access recent tasks.
  plan     📋 Let PR Pilot execute a plan for you.
  run      🚀 Run a saved command.
  task     ➕ Create a new task for PR Pilot.
  upgrade  ⬆️ Upgrade pr-pilot-cli to the latest version.
```
