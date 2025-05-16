# AI for Devs Course - Max

## Module 01 - Intro

- The course is all about using AI efficientyl as a dev

  - Copilot
  - Cursor
  - GPT (to some degree)

- Other example that Max dont find them efficient _yet_: v0, replit

- Tools Overview:

- Copilot
- Cursor

- Its a clone of Visual Studio Code empowered with AI

- Others
  Widnsurf - IDE
  CLine - AI assistant

## M02 - Leveraging Github COpilot

### AUtocompletion

- When autocompleting, we can hover over the suggestion, and the number of suggestions

- Also there's the _complete the word_

### nextEdisSuggestion

- Go to settings, turn it on, it will recomend a '2nd step suggestion'
  - E.g.: When I updated a variable name, it suggested to update it also in a comment and in a print message

### Mastering Prompts

- Remember I can write the prompt in a comment

- `cmd+i` opens the chat, and I ahve different options

### Configuring Copilot

- Among the settings, there are 2 Max finds to be particularly interesting:

  - **Use Instruction Files**

    - I can create a file with general guidelines

  - **Temporal Context**
    - Consider the last changes, may be usefiul fpor exampe qhen ccreating an util functions - so it can suggest the import and implementation

- So, the key point is to be aware that those settings exist, and check them sometimes, as they get updated frequently

### Code Actions (Good for asking for review / refactoring)

- Select the code, and the AI sparks will appear
  **Easy way to ask for a review**

### Sidebar for more complex tasks

- Side bar chat for answers besides simply code
  - Also consider the buttons options (apply, compare, etc)

### Adding Context

- Add FIles for context

  - It shows it has the opened files context, but also, we can add files for context
  - I can type # in the prompt

- Other stuff for context: @
  - @vscode - May ask about vscode setting for example

### Terminal Commands - @terminal

- Also theres terminal COpilot Chat

### Copilot Slash Commands

- /explain
- /fix
- /tests

### Edit and Agent Mode (Agent seems to be a better version)

- When I use the checkbox of Ask, Edit or Agent
  - Edit can generate multiple files edits

![alt text](1.png)

### Unit Tests

- /tests

- Its preety good for creating unit tests

### /new command - creating new projects

### Prompt Engineering Essentials

- Be spacific
- Add useful context (and nothing else)
- Add examples (if possible)
- Split complex tasks
- Iterate to improve the result (but remember to dont be 100% only on AI)

### Notes while Max show an Example:

- Remember to use the special chars / features (@, #, /)

- Split the tasks:

  - Eg, Max asked for a Backend for booking tables in a restaurant
    - So first he asked for the routes (without the logic)

- Remember to not forget we are developpers and should iterate the code ourselves

### Copilot Extensions

- Check install check extensions
  - We can add specific contexts
