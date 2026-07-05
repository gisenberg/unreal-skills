---
name: ue5-editor-automation
description: Use for Unreal Editor automation setup and routing, including editor lifecycle wrappers, MCP server startup, bridge fallback choice, toolset discovery, focus handling, logs, and recovery from missing-module or modal startup blockers.
---

# UE5 Editor Automation

Use a project-local editor wrapper when one exists. The wrapper should make the
editor state explicit before automation starts.

## Wrapper Pattern

A `ue-cli`-style wrapper is useful across UE projects when it stays thin,
project-local, and config-driven. It should standardize lifecycle and evidence:

- `doctor`: report project, editor PID, enabled automation plugins, ports, and
  endpoint config;
- `start` / `restart` / `stop`: launch the editor with logs and the intended
  automation flags;
- `focus`: foreground the editor before PIE or input-sensitive validation;
- `mcp smoke` / `bridge smoke`: prove endpoint health before editor calls;
- `logs`: return bounded recent log slices;
- source-control sanity checks such as default-changelist inspection.

Do not put project gameplay semantics or hard-coded sample paths in a reusable
wrapper. Keep those in the target project's local guidance.

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

Do not assume MCP exposes a flat tool list. UE 5.8-style MCP may expose only
router tools first:

- `list_toolsets`
- `describe_toolset`
- `call_tool`

Discover concrete toolset names before calling tools. Names can be specific
module paths, for example `EditorToolset.EditorAppToolset`,
`editor_toolset.toolsets.asset.AssetTools`, or
`editor_toolset.toolsets.blueprint.BlueprintTools`; do not guess umbrella names
such as `EditorToolset`.

Invoke tools through the router envelope used by the active server:

```json
{
  "toolset_name": "editor_toolset.toolsets.asset.AssetTools",
  "tool_name": "exists",
  "arguments": { "path": "/Game/Example" }
}
```

Avoid large schema dumps; inspect local plugin source first or request one
specific toolset/tool schema at a time. If an agent runtime does not initially
show native MCP tools, verify endpoint config and port health, then use the
runtime's tool-discovery mechanism before falling back to raw JSON-RPC. Treat
raw JSON-RPC as transport only; editor operations should still go through UE
toolsets.

For asset work, discover the actual save tool. In EditorToolset-style servers,
asset saves may be `AssetTools.save_assets`, not a generic save call or a scene
actor save call. After MCP or bridge asset moves/renames, inspect source
control for default-changelist fallout before submitting.

## Recovery

- Missing modules: close editor, build the editor target, restart.
- Automation endpoint unavailable: restart with the endpoint flags, then smoke.
- Wrapper smoke bug but port is open: verify with a direct initialize call and
  report the wrapper issue separately.
- Experimental plugin blocks startup: temporarily disable the plugin only when
  recovery-first editor access is the immediate goal.
