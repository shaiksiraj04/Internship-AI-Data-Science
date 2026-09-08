# AI Registration Assistant

## Day 1 — Research & Planning

**Task ID:** AI-SS-001
**Domain:** Student Support & Internship Management
**Technology:** Python, NLP, Chatbot, Machine Learning

---

# 1. Project Objective

The objective of this project is to build an AI Registration Assistant that can guide students through the internship registration process.

The chatbot should be able to understand user messages, identify the user's intention, collect important information, validate the information, and complete the registration process.

---

# 2. What is a Chatbot?

✍️ Write in your own words:

- What is a chatbot?
- How does a chatbot communicate with a user?
- What is the difference between a simple rule-based chatbot and an AI/NLP chatbot?

---

# 3. What is NLP?

✍️ Write in your own words:

- What does NLP stand for?
- What is Natural Language Processing?
- Why do we need NLP in our registration assistant?
- Give 2–3 examples of NLP being used in real-world applications.

---

# 4. What is an Intent?

✍️ Write in your own words:

An intent represents **************\_\_\_\_**************.

### Examples

| User Message                         | Intent   |
| ------------------------------------ | -------- |
| "Hi"                                 | greeting |
| "Hello there"                        | greeting |
| "I want to register"                 | register |
| "I want to apply for the internship" | register |

### My own examples

| User Message | Intent |
| ------------ | ------ |
|              |        |
|              |        |
|              |        |

---

# 5. What is an Entity?

✍️ Write in your own words:

An entity is ********************\_\_********************.

### Examples

| User Message                                            | Entity                                            |
| ------------------------------------------------------- | ------------------------------------------------- |
| "My name is Rahul"                                      | name = Rahul                                      |
| "My email is [rahul@gmail.com](mailto:rahul@gmail.com)" | email = [rahul@gmail.com](mailto:rahul@gmail.com) |
| "I study Computer Science"                              | field = Computer Science                          |

### My own examples

| User Message | Entity |
| ------------ | ------ |
|              |        |
|              |        |
|              |        |

---

# 6. Intent vs Entity

✍️ Explain the difference between an intent and an entity.

### Example

User message:

> "I want to register for the internship."

Intent:

> ---

Entity:

> ---

Another example:

User message:

> "My name is Rahul."

Intent:

> ---

Entity:

> ---

---

# 7. Initial Intents for Our Chatbot

The initial chatbot will contain the following intents:

1. greeting
2. register
3. name
4. email
5. field
6. experience
7. help
8. thank_you
9. unknown

✍️ Explain what each intent should represent.

| Intent     | What does it mean? |
| ---------- | ------------------ |
| greeting   |                    |
| register   |                    |
| name       |                    |
| email      |                    |
| field      |                    |
| experience |                    |
| help       |                    |
| thank_you  |                    |
| unknown    |                    |

---

# 8. Entities We Need to Collect

The registration assistant needs to collect information from the student.

Initial entities:

1. Name
2. Email
3. Field of Study
4. Programming Experience

### Entity Plan

| Entity     | Example                                   | Why do we need it? |
| ---------- | ----------------------------------------- | ------------------ |
| name       | Rahul Kumar                               |                    |
| email      | [rahul@gmail.com](mailto:rahul@gmail.com) |                    |
| field      | Computer Science                          |                    |
| experience | Beginner                                  |                    |

---

# 9. Conversation Flow

The basic registration conversation should follow this flow:

```text
START
  ↓
Greeting
  ↓
Registration Request
  ↓
Collect Name
  ↓
Collect Email
  ↓
Collect Field of Study
  ↓
Collect Programming Experience
  ↓
Validate Information
  ↓
Registration Confirmation
  ↓
END
```

✍️ Explain this flow in your own words.

---

# 10. Example Conversation

Create your own complete conversation.

The conversation should include:

- Greeting
- Registration request
- Name
- Email
- Field of study
- Programming experience
- Confirmation

Example structure:

```text
User:
...

Assistant:
...

User:
...

Assistant:
...

User:
...

Assistant:
...
```

✍️ Write the complete conversation yourself.

---

# 11. Possible User Problems / Edge Cases

Think about situations where the chatbot may receive unexpected input.

### Example

1. User enters an invalid email address.

### My edge cases

2. ***

3. ***

4. ***

5. ***

6. ***

---

# 12. Expected Responses

Create possible responses for each intent.

| Intent     | Example Response |
| ---------- | ---------------- |
| greeting   |                  |
| register   |                  |
| name       |                  |
| email      |                  |
| field      |                  |
| experience |                  |
| help       |                  |
| thank_you  |                  |
| unknown    |                  |

---

# 13. Technologies

The project will use technologies such as:

- Python
- NLTK / spaCy
- Scikit-learn
- Rasa / ChatterBot (if required)
- JSON / Python dictionaries

Optional advanced technologies include:

- Transformers
- BERT
- LangChain

✍️ For each technology that you understand, write one or two lines explaining what you think it will do in this project.

---

# 14. Planned System Architecture

Our initial system architecture is:

```text
User
  ↓
User Message
  ↓
Text Preprocessing
  ↓
Intent Recognition
  ↓
Entity Extraction
  ↓
Dialog Management
  ↓
Validation
  ↓
Registration Data
  ↓
Response Generation
  ↓
User
```

✍️ Explain what you think happens at each stage.

---

# 15. Data Storage Plan

The project does not require a database.

We can initially use:

- Python dictionaries
- JSON files

✍️ Explain why JSON or dictionaries can be useful for this project.

---

# 16. Project Features

## Core Features

- Greeting and Introduction
- User Information Collection
- Intent Recognition
- Entity Extraction
- Validation Checks
- Registration Confirmation

## Possible Bonus Features

- Multi-language Support
- Sentiment Analysis
- FAQ Handling
- Admin Dashboard
- Analytics & Logging
- Web Interface

✍️ Select the bonus features you would like to attempt after completing the core project.

My selected bonus features:

1. ***
2. ***
3. ***

---

# 17. Day 1 Learning Summary

✍️ Answer these questions without looking at the previous sections:

### 1. What is NLP?

Answer:

---

### 2. What is an intent?

Answer:

---

### 3. What is an entity?

Answer:

---

### 4. What is the difference between intent and entity?

Answer:

---

### 5. What is the main purpose of our chatbot?

Answer:

---

---

# 18. Day 1 Completion Checklist

- [ ] I understand what a chatbot is.
- [ ] I understand the basic idea of NLP.
- [ ] I understand intent.
- [ ] I understand entity.
- [ ] I understand the difference between intent and entity.
- [ ] I designed the basic conversation flow.
- [ ] I identified the initial intents.
- [ ] I identified the entities we need.
- [ ] I thought about possible edge cases.
- [ ] I understand the basic project architecture.

---

# 19. Questions I Still Have

Write down anything you don't understand.

1. ***

2. ***

3. ***

4. ***
