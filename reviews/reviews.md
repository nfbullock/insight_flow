- looks at stats from "yesterday"
- aggregation integration with Insight API, Todoist & Obsidian
- queries LLM for content
- outputs metadata from review context for higher level reviews
Here's a suggestion of how the `review` module could function:

1. **Yesterday's Review:** This can include completed tasks, calories consumed/burned (if you're tracking that), time spent on different activities, moods, highlights, and lows of the day.

2. **Weekly Review:** This could provide an overview of the past week, including major achievements, areas of improvement, patterns in mood or productivity, significant events, and so on. It could also show how the week compared to previous weeks in terms of productivity, health, mood, etc.

3. **Monthly Review:** This could give a broader perspective, focusing more on significant accomplishments, trends, areas of growth, and overall wellbeing. This could also include a comparison with previous months.

For the "Today" aspect, you might want to consider a separate `planner` or `agenda` module that can handle present and future-tense tasks, appointments, meal plans, exercise routines, etc.

Dividing these into separate modules will help you to maintain a clean and clear separation of concerns in your software, making it easier to manage and modify as needed. Additionally, it will help the user differentiate between reviewing past activities and planning future ones.