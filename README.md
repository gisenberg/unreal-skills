# Unreal Skills

Reusable Codex skills and context for UE5 work. These are intentionally
project-agnostic: copy or install the relevant folders under `skills/` into a
repo-local `.agents/skills` directory or a user Codex skills directory, then add
project-specific paths and commands in that project's own guidance.
Keep project-specific course runners, lecture TODOs, map names, depot paths, and
client details in the target project's local guidance instead of this repo.

## Skills

- `ue5-angelscript`: AngelScript gameplay implementation in Hazelight-style UE
  forks.
- `ue5-build`: UE editor target, generated project file, module, ShaderCompileWorker,
  cook, and packaging workflows.
- `ue5-editor-automation`: Editor lifecycle and MCP/automation routing.
- `ue5-perforce`: Perforce hygiene for UE projects with binary assets.
- `ue5-pie-validation`: Live PIE validation for gameplay, input, UI, animation,
  save/load, and map behavior.

## Context

`context/ue5-agent-operating-model.md` summarizes the operating rules these
skills assume.
