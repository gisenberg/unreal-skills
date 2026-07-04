---
name: ue5-editor-automation
description: Use for Unreal Editor automation setup and routing, including editor lifecycle wrappers, MCP server startup, bridge fallback choice, toolset discovery, focus handling, logs, and recovery from missing-module or modal startup blockers.
---

# UE5 Editor Automation

Use a project-local editor wrapper when one exists. The wrapper should make the
editor state explicit before automation starts.

## Preflight

1. Check whether the project provides a wrapper for start, restart, focus,
   logs, and smoke checks.
2. Start the editor with logs enabled and the intended automation endpoint.
3. Verify the automation port/tool namespace before calling editor tools.
4. Focus the editor before timing-sensitive validation.
5. If a modal blocks startup, stop the failed process and relaunch cleanly.

## MCP Routing

Prefer the native UE MCP/editor toolset route for generic editor operations
once the endpoint is healthy. Use bridge-specific automation only for project
contracts or when the native route is unavailable.

Do not assume tool names. Discover concrete toolsets and invoke tools through
the active router envelope. Avoid large schema dumps; inspect local plugin
source or request one narrow schema at a time.

## Recovery

- Missing modules: close editor, build the editor target, restart.
- Automation endpoint unavailable: restart with the endpoint flags, then smoke.
- Wrapper smoke bug but port is open: verify with a direct initialize call and
  report the wrapper issue separately.
- Experimental plugin blocks startup: temporarily disable the plugin only when
  recovery-first editor access is the immediate goal.
