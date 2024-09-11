## 🛠️ Usage

In your repository, use the `pilot` command:

```bash
pilot task "Tell me about this project!"
# 📝 Ask PR Pilot to edit a local file for you:
pilot edit cli/cli.py "Make sure all functions and classes have docstrings."
# ⚡ Generate code quickly and save it as a file:
pilot task -o test_utils.py --code "Write some unit tests for the utils.py file."
# 🔍 Capture part of your screen and add it to a prompt:
pilot task -o component.html --code --snap "Write a Bootstrap5 component that looks like this."
# 📊 Get an organized view of your Github issues:
pilot task "Find all open Github issues labeled as 'bug', categorize and prioritize them"
# 📝 Ask PR Pilot to analyze your test results using prompt templates:
pilot task -f prompts/analyze-test-results.md.jinja2
```

For more detailed examples, please visit our **[demo repository](https://github.com/PR-Pilot-AI/demo/tree/main)**.


### ⬇️ Grab commands from other repositories

Once saved in a repository, commands can be grabbed from anywhere:

```bash
➜  code pilot grab commands pr-pilot-ai/core

       pr-pilot-ai/core
       haiku             Writes a Haiku about your project
       test-analysis     Run unit tests, analyze the output & provide suggestions
       daily-report      Assemble a comprehensive daily report & send it to Slack
       pr-description    Generate PR Title & Description
       house-keeping     Organize & clean up cfg files (package.json, pom.xml, etc)
       readme-badges     Generate badges for your README file

[?] Grab:
   [ ] haiku
   [X] test-analysis
   [ ] daily-report
 > [X] pr-description
   [ ] house-keeping
   [ ] readme-badges


You can now use the following commands:

  pilot run test-analysis   Run unit tests, analyze the output & provide suggestions
  pilot run pr-description  Generate PR Title & Description
```

Our **[core repository](https://github.com/PR-Pilot-AI/core)** contains an ever-growing, curated list of commands
that we tested and handcrafted for you. You can grab them and use them in your own repositories.

### 📝 Advanced Usage: Execute a step-by-step plan

Break down more complex tasks into smaller steps with a plan:

```yaml
# add_page.yaml

name: Add a TODO Page
prompt: |
  We are adding a TODO page to the application.
  Users should be able to:
  - See a list of their TODOs
  - Cross of TODO items / mark them as done
  - Add new TODO items

steps:
  - name: Create HTML template
    prompt: |
      1. Look at templates/users.html to understand the basic structure
      2. Create templates/todo.html based on the example
  - name: Create view controller
    prompt: |
      The controller should handle all actions/calls from the UI.
      1. Look at views/users.py to understand the basic structure
      2. Create views/todo.py based on the example
  - name: Integrate the page
    prompt: |
      Integrate the new page into the application:
      1. Add a new route in urls.py, referencing the new view controller
      2. Add a new tab to the navigation in templates/base.html
  - name: Generate PR description
    template: prompts/generate-pr-description.md.jinja2
```
You can run this plan with:
```bash
pilot plan add_page.yaml
```

PR Pilot will then autonomously:
* Create a new branch and open a PR
* Implement the HTML template and view controller
* Integrate the new page into the navigation
* Look at all changes and create a PR description based on your preferences defined in `prompts/generate-pr-description.md.jinja2`

Save this as part of your code base. Next time you need a new page, simply adjust the plan and run it again.
If you don't like the result, simply close the PR and delete the branch.

You can iterate on the plan until you are satisfied with the result.
