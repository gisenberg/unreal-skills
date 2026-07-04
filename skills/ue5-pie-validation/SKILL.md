---
name: ue5-pie-validation
description: Use for live UE5 Play-In-Editor validation of gameplay, input, animation, UI, save/load, asset, map, and content changes. Covers editor focus, possession, runtime state proof, fresh log scanning, real input routing, Blueprint-vs-instance checks, and validation reporting.
---

# UE5 PIE Validation

Compile success is not proof that gameplay works. Use PIE to verify runtime
state in the editor world.

## Preflight

1. Start or focus the editor.
2. Record the editor log byte offset.
3. Start PIE on the intended map.
4. Verify the active world, pawn, controller, and possession state.
5. Exercise the behavior through the same path the player or runtime uses.

## Evidence

- Input: send real focused input when bridge/MCP events do not hold axes.
- Animation: check gameplay state and visual/AnimInstance state separately.
- UI: verify widget construction, viewport presence, and live text/value state.
- Save/load: verify slot, file timestamp/size, and state after restart/travel.
- Map/content: inspect placed PIE instances, not just Blueprint CDOs.
- Combat/projectiles: count/spawn actors and verify class, transform, owner, or
  hit state.

## Logs

Scan only the fresh segment from the validation run. Old errors and failed
probe warnings should not be mixed into the verdict.

Use `scripts/scan_log.py` with `--offset` when a project does not already have a
log scan helper.
