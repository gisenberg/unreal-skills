---
name: ue5-course-runner
description: Use for progressing UE5 course, tutorial, lecture, or TODO-driven implementation work from local task files. Covers finding the next task, classifying no-code items, implementation loops, map expectations, validation evidence, task-list updates, and source-control readbacks.
---

# UE5 Course Runner

Use this for course-style work where each item should end with implemented
behavior, validation evidence, and an updated task list.

## Loop

1. Read the task list.
2. If no item is specified, run `scripts/next_lecture.py` or find the first
   unchecked item manually.
3. Read the linked lecture/plan/handoff file.
4. Classify the item as actionable or no-code.
5. Create or reuse a named source-control change.
6. Implement using project conventions.
7. Validate in editor, PIE, packaged runtime, or commandlets as appropriate.
8. Update the task list with evidence.
9. Read back source-control state before submitting or reporting completion.

## No-Code Items

Mark no-code only when the source plan explicitly says the item is conceptual,
workflow-only, reference-only, promotional, or has nothing to implement. Include
that reason in the task list.

## Map Rule

If a lecture adds mechanics that need level placement or live exercise, decide
explicitly whether the main validation map should change. Do not use an
unrelated open map as a reason to skip validation. Either coordinate the map
change, create an alternate live validation path, or state why no map edit is
required.

## Validation Standard

Prefer:

- asset/config readback;
- Blueprint compile/readback for content classes;
- live PIE state for relevant actors, components, widgets, or subsystems;
- real input routing for input changes;
- fresh log slice scans;
- submitted changelist and file revision readbacks.

Use direct function calls only as narrow wiring smoke.
