# Contributing to Terminal-Planet-Collision-Sim

Welcome! 👋 Thanks for wanting to help build a planet-smashing simulator that runs in a terminal.

You don't need any open source experience to contribute here. This guide takes you through the whole process from the start, and then walks through a real example: adding a new planet preset.

If you get stuck at any point, that's normal. Open an issue or ask in the society chat. Asking questions counts as contributing too.

---

## The big picture

Contributing to a project on GitHub almost always follows the same five steps:

1. **Fork**: make your own copy of the project on GitHub.
2. **Clone**: download your copy to your computer.
3. **Branch**: make a separate workspace for your change.
4. **Change & commit**: edit the code and save a snapshot of your work.
5. **Pull request (PR)**: ask the project to pull your change into the main project.

Here's how the pieces connect:

```
  Open-Source-Society-UoM/Terminal-Planet-Collision-Sim   ← "upstream" (the real project)
                    │                         ▲
               fork │                         │ pull request
                    ▼                         │
       YOUR-USERNAME/Terminal-Planet-Collision-Sim        ← "origin" (your copy on GitHub)
                    │                         ▲
              clone │                         │ push
                    ▼                         │
                 your computer  ──────────────┘
```

You never edit the real project directly. You work on your copy, then *propose* your change through a PR. Nothing you do can break the main project, so feel free to experiment.

---

## One-time setup

You only need to do this once.

### 1. Install the tools

- **Git**: <https://git-scm.com/downloads>. Check it works with `git --version`.
- **Python 3.10 or newer**: <https://www.python.org/downloads/>. Check with `python --version`.
- **A GitHub account**: <https://github.com/signup>.

The first time you use Git, tell it who you are (use the email linked to your GitHub account):

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

### 2. Fork the repository

1. Go to <https://github.com/Open-Source-Society-UoM/Terminal-Planet-Collision-Sim>.
2. Click the **Fork** button near the top right.
3. Keep the default settings and click **Create fork**.

You now have your own copy at `https://github.com/YOUR-USERNAME/Terminal-Planet-Collision-Sim`.

### 3. Clone your fork

This downloads your fork to your computer. Replace `YOUR-USERNAME` with your GitHub username:

```bash
git clone https://github.com/YOUR-USERNAME/Terminal-Planet-Collision-Sim.git
cd Terminal-Planet-Collision-Sim
```

### 4. Connect to the original project

Your copy won't update itself when other people's changes get merged. Add the original project as a second "remote" called `upstream` so you can pull in their changes:

```bash
git remote add upstream https://github.com/Open-Source-Society-UoM/Terminal-Planet-Collision-Sim.git
git remote -v
```

You should see both `origin` (your fork) and `upstream` (the original).

### 5. Install the dependencies

```bash
pip install -r requirements.txt
```

This installs `numpy`, plus `windows-curses` if you're on Windows.

> 💡 **Optional:** to keep this project's packages separate from everything else on your machine, create a virtual environment first with `python -m venv .venv`, then activate it (`source .venv/bin/activate` on macOS/Linux, `.venv\Scripts\activate` on Windows).

---

## Making a change (every time)

### 1. Start from an up-to-date `main`

```bash
git checkout main
git pull upstream main
```

This makes sure you're building on the latest version of the project.

### 2. Create a branch

A branch is a separate workspace for one change. Give it a short name that describes the change:

```bash
git checkout -b feat/sun-jupiter-preset
```

We use these prefixes:

| Prefix   | Use it for                        | Example                      |
|----------|-----------------------------------|------------------------------|
| `feat/`  | New features                      | `feat/sun-jupiter-preset`    |
| `fix/`   | Bug fixes                         | `fix/collision-radius`       |
| `docs/`  | Documentation                     | `docs/contributing-guide`    |
| `chore/` | Setup, tooling, tidying up        | `chore/add-gitignore`        |

### 3. Make your change

Edit the files in your favourite editor. Keep each PR to **one** thing. Small PRs get reviewed and merged much faster than big ones.

### 4. Check it works

Run your code before you commit it. (See the worked example below for how to try out a preset.)

### 5. Commit

A commit is a saved snapshot of your work, with a message explaining what changed.

```bash
git status                 # see which files you changed
git add src/presets.py     # choose the files to include
git commit -m "feat: add Sun + Jupiter preset"
```

Start your commit message with the same prefix as your branch (`feat:`, `fix:`, `docs:`, `chore:`), then a short description in the present tense.

### 6. Push to your fork

```bash
git push -u origin feat/sun-jupiter-preset
```

This uploads your branch to *your* fork on GitHub.

### 7. Open a pull request

1. Go to your fork on GitHub. You'll usually see a yellow banner saying your branch had recent pushes. Click **Compare & pull request**.
2. Check that the **base repository** is `Open-Source-Society-UoM/Terminal-Planet-Collision-Sim` and the **base** branch is `main`.
3. Give it a clear title (your commit message is usually fine).
4. In the description, say:
   - **What** you changed
   - **Why** (link the issue if there is one, e.g. `Closes #12`)
   - **How you tested it**
5. Click **Create pull request**. 🎉

### 8. Respond to review

A maintainer will look over your PR and may leave comments or ask for changes. That's a normal part of the process and doesn't mean you did something wrong. To update your PR, make the changes on the same branch, then commit and push again:

```bash
git add src/presets.py
git commit -m "fix: correct Jupiter orbital velocity"
git push
```

The PR updates automatically. When it's approved, a maintainer will merge it, and you'll officially be a contributor!

---

## Worked example: adding a Sun + Jupiter preset

Let's put that all together with a real change. The README lists five presets for v1, and only **Earth + Mars** exists so far. We'll add **Sun + Jupiter**.

### Step 1: Get set up

```bash
git checkout main
git pull upstream main
git checkout -b feat/sun-jupiter-preset
```

### Step 2: Understand the existing code

Two files matter here.

[`src/body.py`](../src/body.py) defines a `Body`, which is a single object in space:

```python
@dataclass
class Body:
    name: str
    mass: float            # kilograms
    radius: float          # metres
    position: np.ndarray   # [x, y, z] in metres
    velocity: np.ndarray   # [vx, vy, vz] in metres per second
    shape: str = "sphere"
```

[`src/presets.py`](../src/presets.py) holds the presets. Each preset is a function that returns a list of two `Body` objects. Here's the existing one:

```python
def earth_mars():
    earth = Body(
        name="Earth",
        mass=5.972e24,
        radius=6.371e6,
        position=np.array([0.0, 0.0, 0.0]),
        velocity=np.array([0.0, 500.0, 0.0]),
    )
    mars = Body(
        name="Mars",
        mass=6.39e23,
        radius=3.389e6,
        position=np.array([2.0e8, 0.0, 0.0]),
        velocity=np.array([-800.0, 0.0, 0.0]),
    )
    return [earth, mars]
```

> 💡 `5.972e24` is Python's way of writing 5.972 × 10²⁴. All values are in SI units: kilograms, metres, and metres per second.

### Step 3: Write the new preset

Add this function to the bottom of `src/presets.py`:

```python
def sun_jupiter():
    sun = Body(
        name="Sun",
        mass=1.989e30,
        radius=6.957e8,
        position=np.array([0.0, 0.0, 0.0]),
        velocity=np.array([0.0, 0.0, 0.0]),
    )
    jupiter = Body(
        name="Jupiter",
        mass=1.898e27,
        radius=6.9911e7,
        position=np.array([7.785e11, 0.0, 0.0]),
        velocity=np.array([0.0, 1.307e4, 0.0]),
    )
    return [sun, jupiter]
```

What we chose and why:

- The **Sun** sits still at the centre (the origin).
- **Jupiter** starts about 778.5 million km away along the x-axis. That's its average distance from the Sun.
- Jupiter moves at about 13 km/s along the y-axis, which is at right angles to the line joining it to the Sun. That sideways speed is what puts it into orbit instead of falling straight in.

Real-world values like these are easy to find on [NASA's planetary fact sheets](https://nssdc.gsfc.nasa.gov/planetary/factsheet/). Mention your source in the PR description so reviewers can check your numbers.

### Step 4: Try it out

From the `src` folder, import your preset and print it:

```bash
cd src
python -c "from presets import sun_jupiter; print(sun_jupiter())"
cd ..
```

You should see two `Body(...)` entries printed, one for the Sun and one for Jupiter. If you see an error instead, read the last line of it. It usually tells you exactly what's wrong, such as a typo or a missing comma.

### Step 5: Commit, push, and open the PR

```bash
git add src/presets.py
git commit -m "feat: add Sun + Jupiter preset"
git push -u origin feat/sun-jupiter-preset
```

Then open a PR on GitHub (see [step 7](#7-open-a-pull-request) above) with a description like:

> **What:** Adds a `sun_jupiter()` preset to `src/presets.py`.
>
> **Why:** Sun + Jupiter is one of the v1 presets listed in the README.
>
> **Testing:** Ran `python -c "from presets import sun_jupiter; print(sun_jupiter())"` from `src/`, and both bodies print correctly.
>
> **Source for values:** NASA planetary fact sheets.

That's it. You've made an open source contribution. 🪐

> Once Sun + Jupiter is merged, the remaining presets (Rogue asteroid + Earth, Neutron star + gas giant, Binary star system) are great first contributions too.

---

## Keeping your fork up to date

Other people's PRs get merged while you work. Before starting something new, sync your `main`:

```bash
git checkout main
git pull upstream main
git push origin main
```

If your PR branch falls behind and GitHub reports a conflict, ask for help in your PR. A maintainer can walk you through fixing it.

---

## Tips and etiquette

- **Look for an issue first.** If you want to work on something, comment on its issue so others know it's taken. If there's no issue, open one to talk through the idea before writing lots of code.
- **One change per PR.** Splitting work into small PRs makes review quick and painless.
- **Never commit directly to `main`.** Always use a branch, even on your own fork.
- **Be kind.** Everyone here is learning. Review comments are about the code, not about you.
- **Ask questions.** If something in this guide is unclear, that's a bug in the guide. Tell us, or open a PR to fix it!

---

## Git cheat sheet

| Command                            | What it does                                   |
|------------------------------------|------------------------------------------------|
| `git status`                       | Show what's changed and what's staged          |
| `git checkout -b <name>`           | Create and switch to a new branch              |
| `git checkout <name>`              | Switch to an existing branch                   |
| `git add <file>`                   | Stage a file for the next commit               |
| `git commit -m "<message>"`        | Save a snapshot with a message                 |
| `git push -u origin <branch>`      | Upload a new branch to your fork               |
| `git pull upstream main`           | Pull the latest changes from the main project  |
| `git log --oneline`                | Show recent commits                            |
| `git diff`                         | Show line-by-line changes you haven't staged   |

Happy hacking! 🚀
