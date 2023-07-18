As a module this is responsible for simply organizing tasks, generating encouragement for challenging areas.


- prompt generated from yesterday's review metadata.
- goals integration, how tasks fit into those goals and a short statement on how today's tasks in the association get me closer to my goal.
	- if a goal doesn't pertain to an existing goal, create an inquiry question to determine why I'm doing a thing and how to get at first principles or at least my goal machine/template.
- Incorporation of the theme into prompt and content generation.
- 

# Prompts
## Prompt 1 - Task Alignment

As an analytical and strategic partner, use today's tasks {{today's_tasks}}, and my list of alignments to identify how each task corresponds to my principles and aspirations. For each task, provide a brief explanation about its alignment, expressing how its completion contributes to the fulfillment of the respective principle or goal.

If a task does not seem to correspond with any existing principle or goal, pose a series of insightful Socratic questions. The aim is to provoke thoughtful reflection, leading either to the suggestion of creating a new principle or goal or to a reconsideration of the task's importance. Remember, the objective here is depth, not breadth. The intent is not to exhaustively categorize each task but to illuminate hidden patterns and bring about a more conscious awareness of my actions.

Below is a JSON formatted list of my alignments:
{{alignments}}

## Prompt 2 - Motivation and Review

Switching gears, let's focus on the tasks marked with high priority and a long overdue date. Generate thoughtful and compelling motivational statements for these tasks. Allow the day's theme {{theme_of_the_day}} and yesterday's review metadata to subtly shape these statements.

Bear in mind that the goal here is not mere positivist rhetoric. Rather, let these statements be imbued with a depth of understanding, aligning with my values and principles, and echoing the wisdom of thinkers like Alan Watts, Jordan B. Peterson, and Ray Dalio. The aim is to challenge me, invigorate my sense of purpose, and reaffirm my commitment to my principles and goals.

BEGIN REVIEW JOURNAL
{{yesterday's_review_metadata}} 
END REVIEW JOURNAL
