# UE5 Agent Operating Model

UE5 agent work should be treated as a live-system workflow, not a text-only
patch workflow.

## Principles

- Read the project-local agent guidance before choosing a workflow.
- Open files in source control before editing, and keep binary assets in named,
  narrow changes.
- Prefer project-local gameplay code or wrapper code over engine edits.
- Use editor automation to read and write editor state, not ad hoc binary file
  manipulation.
- Prefer a thin project-local editor wrapper for start/restart/focus/smoke/log
  chores. Keep project paths, target names, endpoints, and source-control
  commands in project guidance rather than reusable skills.
- Verify player-visible behavior in PIE or a packaged runtime. Commandlet
  compile success is not enough.
- Record fresh log offsets before validation runs and scan only the new segment.
- Distinguish Blueprint defaults, placed map instances, and live PIE instances.
- Read back submitted source-control state with file revisions and changelist
  numbers before declaring work complete.

## Common Failure Modes

- Default changelists silently accumulate unrelated assets after editor work.
- Binary asset edits cannot be merged safely without coordination.
- Editor focus affects ticking, input, physics, and timing-sensitive validation.
- MCP or bridge key events may prove discrete input but fail to hold continuous
  axes.
- Missing module dialogs are often solved by closing the editor and rebuilding
  the editor target, not clicking through the modal.
- Shader worker version mismatches require rebuilding `ShaderCompileWorker`.
- Blueprint CDOs can be correct while placed level instances retain stale
  overrides.

## Source-Derived Findings To Preserve

- UGS-style workspace discovery may depend on engine source code paths such as
  `OpenProjectInfo.cs` and `Engine/Build/Build.version`. Before changing the
  engine/project directory shape, verify how the local UE tooling discovers the
  engine.
- UE MCP/editor automation can be router based rather than a flat tool list.
  Discover concrete toolsets first, then call tools through the active router
  envelope; do not assume toolset umbrella names or generic save calls exist.
- Shader worker output-version errors usually point at a stale
  `ShaderCompileWorker` binary/version file. Rebuild the worker before treating
  the problem as generic cache corruption.
- Missing UE support binaries may be GitDeps-managed. Check
  `Engine/Build/Commit.gitdeps.xml` before manually sourcing binaries.
- Zen/shared DDC behavior is controlled by engine config and runtime logs.
  Distinguish healthy local Zen startup from optional shared-cache
  infrastructure.
