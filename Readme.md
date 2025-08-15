# Manual
## To run
```
uv run src/main.py
```

## Operation

### Search lines
Ivanow Ivan I.
Payment for Ivanov Ivan.
Pay for tool for Ivan Ivanov for money
#### I want to make a payment for Ivanow Vania for his great service
Search Results for a query: I want to make a payment for Ivanow Vania for his great service
================================================
I've accessed the names-base.json file and have the following information:

Here are the names I found in the database:

*   **Person ID 1**: Ivanov Ivan Ivanovich, Іванов Іван Івановіч, Иванов Иван Иванович
*   **Person ID 2**: Петров Петр Петрович, Петрів Петр Петровіч, Petrov Petr Petrovich, Petriv Peter Peterovich, Petriw Pitr Pitrovich, Petrow Pyotr Pyotrovich

Now, let's compare this to your search string: "Ivanow Vania".

Based on my analysis, I found a potential match:

*   "Ivanow Vania" is similar to **"Ivanov Ivan Ivanovich"** (Person ID 1). The surname "Ivanow" is a close match to "Ivanov", and "Vania" is a common variation of "Vania".

✨ **Summary of Findings:** ✨
I found a similar name in the database:
*   "Ivanow Vania" is similar to **"Ivanov Ivan Ivanovich"** (Person ID 1).

Please confirm if this is the correct person you intended to make a payment for. Let me know if you need further assistance! 😊
================================================

#### оплата за Петров Peter (1)
Search Results for a query: оплата за Петров Peter (1)
================================================
Here's what I found in the `names-base.json` file:

I found a strong match for "Петров Peter" in your search string! 🔍

*   "Petrov Petr Petrovich" (ID: 2)
*   "Petriv Peter Peterovich" (ID: 2)

It looks like "Петров Peter" is likely referring to person with ID 2. 🥳

**Summary:**
The search string "оплата за Петров Peter (1)" contained names similar to those found in the `names-base.json` file. Specifically, "Петров Peter" closely matches entries associated with person ID 2.
================================================


### Should result successfully - no occurences
Doroshecko Ivan


### Gives error
Петров Петро


## Strange
Search Results for a query: Петрику по призвіщу Петрів
================================================
I'm sorry, but I can not perform this request. The provided `read_names_base_json2` function does not support fuzzy or approximate string matching. It only returns exact matches.
================================================


## Need caching of names-base
The repeated tool invocations (calling read_names_base_json2 many times) happen because the agent is not retaining the result of reading the file between steps. Instead, it keeps re-calling the tool to fetch the same data, likely due to how the prompt is structured and how the agent's reasoning loop works in LangChain.

Why does this happen?

The agent is designed to "think step by step" and can only use tools to get information.
If the prompt or the agent's reasoning doesn't store or "remember" the file content, it will keep calling the tool whenever it needs the data again.
This is common in tool-using agents that don't have persistent memory or a scratchpad to cache tool outputs.
How to reduce repeated tool calls:

Cache tool results:
Modify your agent logic or tool wrapper to cache the result of reading the file, so subsequent requests use the cached data.

Improve prompt engineering:
Adjust the prompt to encourage the agent to read the file once and use that result for further reasoning.

Use a custom tool or agent memory:
Implement a tool that loads and stores the file content in the agent's memory or context for the duration of the query.